#!/usr/bin/env python3
"""
phenotype-registry prompt + plan + response scraper.

Usage:
    python3 scripts/scrape.py --device mac --out <out-dir> [--incremental] [--source <src>]
    python3 scripts/scrape.py --device win --out <out-dir> [--incremental] [--source <src>]

Sources: claude-code, codex, cursor-agent, forge, droid, aider, other

Mechanical filter (per docs/intent/README.md § 4):
  - slash-command-only
  - single-word-confirm
  - empty-or-null
  - duplicate-continue within same session

Semantic tags (assigned by cheap keyword classifier — no LLM call):
  - repo-defining     (creates new repo/crate/module)
  - policy-setting    (sets rule, ADR, governance, deny, allow)
  - idea              (brainstorm, explore, what if, imagine, riff)
  - bugfix            (fix this, error, broken, failing, debug)
  - implementation    (build, implement, add, write, create, scaffold)
  - narrative         (summarized completed work)

Binding to a repo: project-folder substring match against ECOSYSTEM_MAP
repo list. Unbound → _orphan/.

This script is idempotent: --incremental skips records whose id already
exists in <out>/_seen.txt.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator


# --------------------------------------------------------------------------- #
# Source-specific extractors
# --------------------------------------------------------------------------- #

@dataclass
class Record:
    """A raw record pulled from a source."""
    id: str               # stable hash
    source: str           # claude-code | codex | cursor-agent | forge | droid | aider | other
    timestamp: str        # ISO 8601
    text: str             # the prompt or response text
    project: str | None   # absolute project path, if known
    session_id: str | None
    kind: str             # prompt | plan | response | spec | idea | design-doc
    extra: dict = field(default_factory=dict)


# Trash filter regexes (per docs/intent/README.md § 4)
RE_SLASH_CMD = re.compile(r"^/[a-z][a-z0-9_-]*\s*$", re.IGNORECASE)
RE_SINGLE_WORD = re.compile(
    r"^(yes|y|ok|no|n|thanks|thx|thx!|👍|k|sure|continue|next|go on|resume|ship it|do it|approved|lgtm|go|do next|next one|yep|yeah|yup|nope|nah)\s*[.!]?\s*$",
    re.IGNORECASE,
)
RE_EMPTY = re.compile(r"^\s*$")
RE_DUP_CONTINUE = re.compile(r"^(go on|continue|next|resume|keep going|carry on)\s*[.!]?\s*$", re.IGNORECASE)


# Keyword-based tag inference (cheap; no LLM call needed for first pass)
TAG_RULES = [
    ("repo-defining",  re.compile(r"\b(new repo|new crate|new module|new project|scaffold|create a (new |the )?(repo|crate|module|service|app|package)|monorepo|new (phenotype|pheno)|greenfield|bootstrap)\b", re.IGNORECASE)),
    ("policy-setting", re.compile(r"\b(ADR|adr|policy|policies|deny|allow[- ]?list|governance|rule|standard|convention|adopt|retire|archive|merge|supersede|rationaliz)\b", re.IGNORECASE)),
    ("idea",           re.compile(r"\b(brainstorm|what if|imagine|riff|explore|ideate|spark|seed|dream|consider|possibility|maybe we could|what about|wild idea)\b", re.IGNORECASE)),
    ("bugfix",         re.compile(r"\b(fix (this|that|the|these)|error|broken|failing|debug|stack[- ]?trace|panic|crash|null[- ]?pointer|segfault|undefined|cannot|can't|won't|wont|fails?|doesn't work|doesnt work|issue with)\b", re.IGNORECASE)),
    ("implementation", re.compile(r"\b(build|implement|add|write|create|scaffold|wire|hook up|set up|stand up|ship|integrate|port|migrate|generate|render|expose|pump|route|dispatch|connect|install|deploy|publish|release)\b", re.IGNORECASE)),
    ("narrative",      re.compile(r"\b(done|finished|completed|shipped|merged|closed|resolved|narrative|summary|recap|update|changelog|status)\b", re.IGNORECASE)),
]


def infer_tag(text: str) -> str:
    """Return the highest-priority tag for the given text. Falls back to 'narrative'."""
    for tag, rx in TAG_RULES:
        if rx.search(text):
            return tag
    return "narrative"


# --------------------------------------------------------------------------- #
# Repo binding
# --------------------------------------------------------------------------- #

# Canonical repo names, with the path substrings that bind a project folder to them.
# Populated from phenotype-registry/ECOSYSTEM_MAP.md role classification.
# The order matters: longer / more specific substrings first.
REPO_BINDINGS: list[tuple[str, str]] = [
    # Top-level monorepo
    ("phenotype-registry",   "phenotype-registry"),
    ("phenotype-registry",   "repos/phenotype-registry"),
    # The bare "repos/" dir IS the monorepo — bind to phenotype-registry
    ("phenotype-registry",   "repos/"),
    ("phenotype-registry",   "Phenotype/repos"),
    ("phenotype-registry",   "Phenotype/cursor"),
    # Cluster A — LLM routing
    ("OmniRoute",            "OmniRoute"),
    ("OmniRoute",            "repos/OmniRoute"),
    ("Tokn",                 "Tokn"),
    ("Tokn",                 "repos/Tokn"),
    ("phenoAI",              "phenoAI"),
    ("phenoAI",              "repos/phenoAI"),
    ("phenoRouterMonitor",   "phenoRouterMonitor"),
    ("phenoRouterMonitor",   "repos/phenoRouterMonitor"),
    ("bifrost",              "bifrost"),
    ("cliproxyapi-plusplus", "cliproxyapi-plusplus"),
    ("helios-cli",           "helios-cli"),
    ("helioscope",           "helioscope"),
    ("heliosApp",            "heliosApp"),
    ("heliosBench",          "heliosBench"),
    ("helios-router",        "helios-router"),
    # Cluster B — Agent runtimes
    ("Agentora",             "Agentora"),
    ("Agentora",             "repos/Agentora"),
    ("thegent",              "thegent"),
    ("thegent",              "repos/thegent"),
    ("PhenoAgent",           "PhenoAgent"),
    ("PhenoAgent",           "repos/PhenoAgent"),
    # Cluster C — Resilience
    ("phenotype-resilience", "phenotype-resilience"),
    ("phenotype-resilience", "repos/phenotype-resilience"),
    ("ResilienceKit",        "ResilienceKit"),
    ("Stashly",              "Stashly"),
    ("phenotype-dep-guard",  "phenotype-dep-guard"),
    # Cluster D — Observability
    ("phenoObservability",   "phenoObservability"),
    ("phenoObservability",   "repos/phenoObservability"),
    ("phenotype-observability", "phenotype-observability"),
    ("ObservabilityKit",     "ObservabilityKit"),
    ("Metron",               "Metron"),
    ("Traceon",              "Traceon"),
    # Cluster E — Auth
    ("Authvault",            "Authvault"),
    ("AuthKit",              "AuthKit"),
    ("phenotype-auth-ts",    "phenotype-auth-ts"),
    # Cluster F — Shared crate monorepos
    ("HexaKit",              "HexaKit"),
    ("HexaKit",              "repos/HexaKit"),
    ("pheno",                "/pheno/"),
    ("pheno",                "repos/pheno/"),
    ("phenoShared",          "phenoShared"),
    ("PhenoProc",            "PhenoProc"),
    # Cluster G — Spec / Docs
    ("PhenoSpecs",           "PhenoSpecs"),
    ("PhenoSpecs",           "repos/PhenoSpecs"),
    ("PhenoHandbook",        "PhenoHandbook"),
    ("phenoXdd",             "phenoXdd"),
    ("phenoDesign",          "phenoDesign"),
    ("phenodocs",            "phenodocs"),
    # Cluster H — Config
    ("Settly",               "Settly"),
    ("Conft",                "Conft"),
    # Cluster I — *Kit SDKs
    ("DataKit",              "DataKit"),
    ("McpKit",               "McpKit"),
    ("TestingKit",           "TestingKit"),
    ("PlatformKit",          "PlatformKit"),
    ("PhenoKits",            "PhenoKits"),
    # Cluster J — Helios
    ("HeliosLab",            "HeliosLab"),
    # Cluster K — Landing
    ("phenotype-landing",    "phenotype-landing"),
    # App / product
    ("Tracera",              "Tracera"),
    ("Tracera",              "repos/Tracera"),
    ("AgilePlus",            "AgilePlus"),
    ("AgilePlus",            "repos/AgilePlus"),
    ("hwLedger",             "hwLedger"),
    ("hwLedger",             "repos/hwLedger"),
    ("eyetracker",           "eyetracker"),
    ("PlayCua",              "PlayCua"),
    ("PlayCua",              "repos/PlayCua"),
    ("Dino",                 "Dino"),
    ("Dino",                 "repos/Dino"),
    ("DINOForge-UnityDoorstop", "DINOForge-UnityDoorstop"),
    ("dinoforge-packs",      "dinoforge-packs"),
    ("phenotype-voxel",      "phenotype-voxel"),
    ("phenotype-postfx",     "phenotype-postfx"),
    ("WorldSphereMod",       "WorldSphereMod"),
    # Apps
    ("Agentora",             "Agentora-"),
    ("Agentora",             "repos/Agentora-"),
    # Tools / infra
    ("phenotype-tooling",    "phenotype-tooling"),
    ("phenotype-infra",      "phenotype-infra"),
    ("PhenoDevOps",          "PhenoDevOps"),
    ("BytePort",             "BytePort"),
    ("BytePort",             "repos/BytePort"),
    ("nanovms",              "nanovms"),
    ("nanovms",              "repos/nanovms"),
    ("FocalPoint",           "FocalPoint"),
    ("FocalPoint",           "repos/FocalPoint"),
    ("Civis",                "Civis"),
    ("Civis",                "repos/Civis"),
    ("PhenoVCS",             "PhenoVCS"),
    ("PhenoVCS",             "repos/PhenoVCS"),
    ("KWatch",               "KWatch"),
    ("KodeVibe",             "KodeVibe"),
    ("KlipDot",              "KlipDot"),
    ("Tasken",               "Tasken"),
    ("Tracely",              "Tracely"),
    ("Pyron",                "Pyron"),
    ("NetScript",            "NetScript"),
    ("PhenoProc",            "PhenoProc"),
    ("Eidolon",              "Eidolon"),
    ("Eidolon",              "repos/Eidolon"),
    ("Eventra",              "Eventra"),
    ("PhenotypeMCP",         "PhenoMCP"),
    ("PhenotypeMCP",         "repos/PhenoMCP"),
    ("PhenoMCP-cheap",       "PhenoMCP-cheap"),
    ("PhenoMCP-1st",         "PhenoMCP-1st"),
    # phenos
    ("phenoAgents",          "pheno-agents-md"),
    ("phenoConfig",          "pheno-config"),
    ("phenoContext",         "pheno-context"),
    ("phenoErrors",          "pheno-errors"),
    ("phenoFlags",           "pheno-flags"),
    ("phenoCliBase",         "pheno-cli-base"),
    ("phenoPortAdapter",     "pheno-port-adapter"),
    ("phenoOtel",            "pheno-otel"),
    ("phenoTracing",         "pheno-tracing"),
    ("phenoCargoTemplate",   "pheno-cargo-template"),
    ("phenoFastapiBase",     "pheno-fastapi-base"),
    ("phenoCostCard",        "pheno-cost-card"),
    ("phenoLlmsTxt",         "pheno-llms-txt"),
    ("phenoMcpRouter",       "pheno-mcp-router"),
    ("phenoPromptTest",      "pheno-prompt-test"),
    ("phenoPydanticModels",  "pheno-pydantic-models"),
    ("phenoScaffoldKit",     "pheno-scaffold-kit"),
    ("phenoVibecodingGuard", "pheno-vibecoding-guard"),
    ("phenoWorklogSchema",   "pheno-worklog-schema"),
    ("phenoGoCtxkit",        "pheno-go-ctxkit"),
    ("phenoZodSchemas",      "pheno-zod-schemas"),
    ("phenoWtrees",          "pheno-wtrees"),
    ("phenoData",            "phenoData"),
    # Worktrees / scm
    ("pheno-contracts",      "phenotype-contracts"),
    ("pheno-contracts",      "PhenoContracts"),
    ("phenotype-bus",        "phenotype-bus"),
    ("phenotype-hub",        "phenotype-hub"),
    ("phenotype-journeys",   "phenotype-journeys"),
    ("phenotype-omlx",       "phenotype-omlx"),
    ("phenotype-ops-mcp",    "phenotype-ops-mcp"),
    ("phenotype-org-audits", "phenotype-org-audits"),
    ("phenotype-registry",   "phenotype-registry"),
    ("phenotype-registry",   "repos/phenotype-registry"),
    ("phenotype-otel",       "phenotype-otel"),
    ("phenotype-errors",     "phenotype-errors"),
    ("phenotype-go-sdk",     "phenotype-go-sdk"),
    ("phenotype-python-sdk", "phenotype-python-sdk"),
    ("phenotype-zod-schemas", "phenotype-zod-schemas"),
    ("phenotype-water",      "phenotype-water"),
    ("phenotype-terrain",    "phenotype-terrain"),
    ("phenotype-voxel",      "phenotype-voxel"),
    ("phenotype-postfx",     "phenotype-postfx"),
    ("phenotype-teamcomm",   "phenotype-teamcomm"),
    ("phenotype-tooling",    "phenotype-tooling"),
    ("phenotype-e2e-base",   "phenotype-e2e-base"),
    ("phenotype-landing",    "phenotype-landing"),
    ("phenotype-journeys",   "phenotype-journeys"),
    ("phenotype-journeys",   "repos/phenotype-journeys"),
    ("phenotype-auth-ts",    "phenotype-auth-ts"),
    ("phenotype-ts-utils",   "phenotype-ts-utils"),
    ("phenotype-vessel",     "phenotype-vessel"),
    ("phenotype-water",      "phenotype-water"),
    ("phenotype-rs-utils",   "phenotype-py-utils"),
    ("phenotype-py-extras",  "phenotype-py-extras"),
    # Apps / single-purpose
    ("Civis",                "Civis"),
    ("Civis",                "repos/Civis"),
    ("Conft",                "Conft"),
    ("Conft",                "repos/Conft"),
    ("Apisync",              "Apisync"),
    ("Apisync",              "repos/Apisync"),
    ("AppGen",               "AppGen"),
    ("AppGen",               "repos/AppGen"),
    ("AgentMCP",             "AgentMCP"),
    ("AgentMCP",             "repos/AgentMCP"),
    ("Benchora",             "Benchora"),
    ("Benchora",             "repos/Benchora"),
    ("DevHex",               "DevHex"),
    ("DevHex",               "repos/DevHex"),
    ("DataKit",              "DataKit"),
    ("GDK",                  "GDK"),
    ("KaskMan",              "KaskMan"),
    ("MCPForge",             "MCPForge"),
    ("McpKit",               "McpKit"),
    ("PlatformKit",          "PlatformKit"),
    ("Planify",              "Planify"),
    ("PolicyStack",          "PolicyStack"),
    ("portage",              "portage"),
    ("quadsgm",              "QuadSGM"),
    ("Tracely",              "Tracely"),
    ("vibeproxy",            "vibeproxy"),
    ("phenoVibeproxy",       "vibeproxy-monitoring-unified"),
    ("worldsphere",          "WorldSphereMod"),
    ("unified-review",       "unified-review"),
    ("unified_review_surface", "unified_review_surface"),
    ("testingkit",           "TestingKit"),
    ("tokn",                 "Tokn"),
    ("Tokn",                 "repos/Tokn"),
    ("thegent",              "thegent"),
    ("thegent",              "repos/thegent"),
    ("sidekick",             "Sidekick"),
    ("tracera",              "Tracera"),
    ("tracera",              "repos/Tracera"),
    ("phenotype-org",        "phenotype-org"),
    ("PhenoProject",         "PhenoProject"),
    ("PhenoPlugins",         "PhenoPlugins"),
    ("phenoEvents",          "phenoEvents"),
    ("pheno-otel",           "pheno-otel"),
    ("phenoAgents",          "pheno-agents-md"),
    ("phenoShared",          "phenoShared"),
    ("phenoUtils",           "phenoUtils"),
    ("phenoXdd",             "phenoXdd"),
    ("phenoXddLib",          "phenoXddLib"),
    ("phenoAI",              "phenoAI"),
    ("phenoData",            "phenoData"),
    ("phenoDesign",          "phenoDesign"),
    ("phenoDesign",          "phenoDesign-"),
    ("phenoForge",           "phenoForge"),
    ("phenoMCP",             "phenoMCP"),
    ("phenoPlugins",         "phenoPlugins"),
    ("phenoProc",            "phenoProc"),
    ("phenoProc",            "PhenoProc"),
    ("phenoResearch",        "phenoResearchEngine"),
    ("phenoRuntime",         "phenoRuntime"),
    ("phenoSchema",          "phenoSchema"),
    ("phenoSpecs",           "phenoSpecs"),
    ("phenoVCS",             "phenoVCS"),
    ("phenoDesign",          "phenoDesign"),
    ("phenoVibeProxy",       "vibeproxy"),
    # Single repos
    ("focalpoint",           "focalpoint"),
    ("agileplus",            "agileplus"),
    ("byteport",             "byteport"),
    ("hwledger",             "hwledger"),
    ("phenokits",            "phenokits"),
    ("thegent-landing",      "thegent-landing"),
    ("odin-landing",         "odin-landing"),
    # pheno-plans
    ("pheno-wtrees",         "pheno-wtrees"),
    ("pheno-wtrees",         "phenotype-wtrees"),
    ("phenotype-wtrees",     "phenotype-wtrees"),
    ("registry-wtrees",      "registry-wtrees"),
    ("phenotype-wtrees",     "phenotype-registry-wtrees"),
    # Single-purpose tools
    ("HeliosCLI",            "HeliosCLI"),
    ("HeliosCLI",            "repos/HeliosCLI"),
    ("HeliosLab",            "HeliosLab"),
    ("HeliosLab",            "repos/HeliosLab"),
]


def bind_repo(project: str | None, text: str | None = None) -> str | None:
    """Return the canonical repo name bound to this record, or None."""
    if project:
        # Sort by length of substring descending so longer / more specific wins
        for repo, needle in sorted(REPO_BINDINGS, key=lambda x: -len(x[1])):
            if needle in project:
                return repo
        # Case-insensitive fallback
        p_lower = project.lower()
        for repo, needle in sorted(REPO_BINDINGS, key=lambda x: -len(x[1])):
            if needle.lower() in p_lower:
                return repo
    if text:
        for repo, needle in sorted(REPO_BINDINGS, key=lambda x: -len(x[1])):
            if needle in text:
                return repo
    return None


# --------------------------------------------------------------------------- #
# Mechanical filter
# --------------------------------------------------------------------------- #

def is_trash(text: str) -> str | None:
    """Return the trash reason if the text is trash, else None."""
    if not text or RE_EMPTY.match(text):
        return "empty-or-null"
    if RE_SLASH_CMD.match(text):
        return "slash-command-only"
    if RE_SINGLE_WORD.match(text):
        return "single-word-confirm"
    return None


# --------------------------------------------------------------------------- #
# Per-source extractors
# --------------------------------------------------------------------------- #

def stable_id(*parts: str) -> str:
    h = hashlib.sha1()
    for p in parts:
        h.update(p.encode("utf-8", "ignore"))
        h.update(b"\x1f")
    return h.hexdigest()[:16]


def iso_from_ms(ms: int | float) -> str:
    try:
        return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat()
    except Exception:
        return ""


def iso_from_s(s: int | float) -> str:
    try:
        return datetime.fromtimestamp(s, tz=timezone.utc).isoformat()
    except Exception:
        return ""


def extract_claude_code(home: Path) -> Iterator[Record]:
    """~/.claude/{history.jsonl, projects/*, plans/*, idea-seeds/*, memory/*, agents/*, skills/*}"""
    # 1. history.jsonl
    p = home / ".claude" / "history.jsonl"
    if p.exists():
        with p.open(encoding='utf-8', errors='replace') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                disp = (obj.get("display") or "").strip()
                pasted = obj.get("pastedContents") or {}
                ts = obj.get("timestamp")
                project = obj.get("project")
                if pasted and not disp:
                    # Use the pasted content as the text
                    disp = "[pasted content: " + ", ".join(pasted.keys()) + "]"
                if not disp:
                    continue
                yield Record(
                    id=stable_id("claude-history", str(ts), disp[:200]),
                    source="claude-code",
                    timestamp=iso_from_ms(ts) if ts else "",
                    text=disp,
                    project=project,
                    session_id=None,
                    kind="prompt",
                    extra={"sub_source": "history.jsonl"},
                )
    # 2. plans/*.md
    plans = home / ".claude" / "plans"
    if plans.is_dir():
        for f in sorted(plans.glob("*.md")):
            try:
                text = f.read_text()
            except Exception:
                continue
            yield Record(
                id=stable_id("claude-plan", f.name, text[:200]),
                source="claude-code",
                timestamp=iso_from_s(f.stat().st_mtime),
                text=text,
                project=None,
                session_id=None,
                kind="plan",
                extra={"sub_source": "plans/", "filename": f.name},
            )
    # 3. idea-seeds/*.md
    seeds = home / ".claude" / "idea-seeds"
    if seeds.is_dir():
        for f in sorted(seeds.glob("*.md")):
            try:
                text = f.read_text()
            except Exception:
                continue
            # First YAML-ish block at top
            front = text[:600]
            sess = None
            proj = None
            src = None
            for ln in front.splitlines():
                if ln.startswith("session_id:"):
                    sess = ln.split(":", 1)[1].strip()
                elif ln.startswith("project_folder:"):
                    proj = ln.split(":", 1)[1].strip()
                elif ln.startswith("source:"):
                    src = ln.split(":", 1)[1].strip()
            yield Record(
                id=stable_id("claude-ideaseed", f.name, text[:200]),
                source="cursor-agent",   # idea-seeds are from Cursor Agent transcripts
                timestamp=iso_from_s(f.stat().st_mtime),
                text=text,
                project=("/" + proj.replace("-", "/")) if proj else None,
                session_id=sess,
                kind="prompt",
                extra={"sub_source": "idea-seeds/", "filename": f.name, "original_source": src or "cursor_agent_transcript"},
            )
    # 4. memory/*.md
    mem = home / ".claude" / "memory"
    if mem.is_dir():
        for f in sorted(mem.glob("*.md")):
            try:
                text = f.read_text()
            except Exception:
                continue
            yield Record(
                id=stable_id("claude-memory", f.name, text[:200]),
                source="claude-code",
                timestamp=iso_from_s(f.stat().st_mtime),
                text=text,
                project=None,
                session_id=None,
                kind="plan",  # memory entries are "plan-ish"
                extra={"sub_source": "memory/", "filename": f.name},
            )
    # 5. projects/<encoded>/<uuid>.jsonl — extract user-message prompts from full session log
    proj_root = home / ".claude" / "projects"
    if proj_root.is_dir():
        for proj_dir in proj_root.iterdir():
            if not proj_dir.is_dir():
                continue
            for f in proj_dir.glob("*.jsonl"):
                # We DON'T process subagents/*.jsonl in this sweep — that's a follow-up pass.
                sess_id = f.stem
                # Project path is encoded in dir name: -Users-kooshapari-CodeProjects-Phenotype-repos-Foo → /Users/kooshapari/CodeProjects/Phenotype/repos/Foo
                proj_path = "/" + proj_dir.name.lstrip("-").replace("-", "/")
                try:
                    with f.open(encoding='utf-8', errors='replace') as fh:
                        for line in fh:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                obj = json.loads(line)
                            except Exception:
                                continue
                            if obj.get("type") not in ("user",):
                                continue
                            msg = obj.get("message", {})
                            content = msg.get("content")
                            if isinstance(content, str):
                                txt = content
                            elif isinstance(content, list):
                                # Concatenate all text parts
                                parts = []
                                for c in content:
                                    if isinstance(c, dict) and c.get("type") == "text":
                                        parts.append(c.get("text", ""))
                                    elif isinstance(c, dict) and c.get("type") == "tool_use":
                                        pass
                                    elif isinstance(c, dict) and c.get("type") == "tool_result":
                                        pass
                                txt = "\n".join(p for p in parts if p)
                            else:
                                continue
                            if not txt:
                                continue
                            ts = obj.get("timestamp")
                            yield Record(
                                id=stable_id("claude-project", sess_id, str(obj.get("uuid","")), txt[:200]),
                                source="claude-code",
                                timestamp=iso_from_ms(ts) if ts else iso_from_s(f.stat().st_mtime),
                                text=txt,
                                project=proj_path,
                                session_id=sess_id,
                                kind="prompt",
                                extra={"sub_source": f"projects/{proj_dir.name}/"},
                            )
                except (OSError, PermissionError):
                    continue


def extract_codex(home: Path) -> Iterator[Record]:
    """~/.codex/{history.jsonl, sessions/**/rollout-*.jsonl, memories/, prompts/, skills/}"""
    # 1. history.jsonl
    p = home / ".codex" / "history.jsonl"
    if p.exists():
        with p.open(encoding='utf-8', errors='replace') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                text = (obj.get("text") or "").strip()
                if not text:
                    continue
                ts = obj.get("ts")
                sess = obj.get("session_id")
                yield Record(
                    id=stable_id("codex-history", str(ts), sess or "", text[:200]),
                    source="codex",
                    timestamp=iso_from_s(ts) if ts else "",
                    text=text,
                    project=None,
                    session_id=sess,
                    kind="prompt",
                    extra={"sub_source": "history.jsonl"},
                )
    # 2. sessions/YYYY/MM/DD/rollout-*.jsonl — extract user messages
    sess_root = home / ".codex" / "sessions"
    if sess_root.is_dir():
        for f in sess_root.rglob("rollout-*.jsonl"):
            try:
                with f.open(encoding='utf-8', errors='replace') as fh:
                    for line in fh:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                        except Exception:
                            continue
                        if obj.get("type") not in ("user_message", "user", "message"):
                            continue
                        # Different codex versions have different shapes — try a few
                        msg = obj.get("message") or obj
                        content = msg.get("content") if isinstance(msg, dict) else None
                        if isinstance(content, str):
                            txt = content
                        elif isinstance(content, list):
                            parts = []
                            for c in content:
                                if isinstance(c, dict) and c.get("type") in ("text", "input_text"):
                                    parts.append(c.get("text", ""))
                                elif isinstance(c, dict) and c.get("type") in ("input_image", "image"):
                                    parts.append("[image]")
                            txt = "\n".join(p for p in parts if p)
                        else:
                            continue
                        if not txt:
                            continue
                        ts = obj.get("timestamp") or obj.get("ts")
                        sess = obj.get("session_id") or obj.get("id") or f.stem
                        # Codex rollouts often have cwd/payload.cwd
                        cwd = obj.get("cwd") or (obj.get("payload") or {}).get("cwd") if isinstance(obj.get("payload"), dict) else None
                        yield Record(
                            id=stable_id("codex-rollout", f.name, str(obj.get("id", "")), txt[:200]),
                            source="codex",
                            timestamp=iso_from_ms(ts) if ts and ts > 10_000_000_000 else iso_from_s(ts) if ts else iso_from_s(f.stat().st_mtime),
                            text=txt,
                            project=cwd,
                            session_id=sess,
                            kind="prompt",
                            extra={"sub_source": "rollout", "file": f.name},
                        )
            except (OSError, PermissionError):
                continue
    # 3. memories/MEMORY.md and raw_memories.md — codex-curated agent reflections
    mem_dir = home / ".codex" / "memories"
    if mem_dir.is_dir():
        for fname in ("MEMORY.md", "raw_memories.md", "memory_summary.md"):
            f = mem_dir / fname
            if not f.exists():
                continue
            try:
                text = f.read_text()
            except Exception:
                continue
            yield Record(
                id=stable_id("codex-mem", fname, text[:200]),
                source="codex",
                timestamp=iso_from_s(f.stat().st_mtime),
                text=text,
                project=None,
                session_id=None,
                kind="response",  # these are LLM-generated reflection / memory
                extra={"sub_source": f"memories/{fname}"},
            )
    # 4. memories/extensions/ad_hoc/instructions.md and per-task .md files
    if mem_dir.is_dir():
        for f in mem_dir.rglob("*.md"):
            if f.name in ("MEMORY.md", "raw_memories.md", "memory_summary.md"):
                continue
            if "/.git/" in str(f):
                continue
            try:
                text = f.read_text()
            except Exception:
                continue
            yield Record(
                id=stable_id("codex-memfile", f.name, text[:200]),
                source="codex",
                timestamp=iso_from_s(f.stat().st_mtime),
                text=text,
                project=None,
                session_id=None,
                kind="plan" if "skill" in str(f).lower() else "response",
                extra={"sub_source": f"memories/{f.relative_to(mem_dir)}"},
            )
    # 5. prompts/*.md (codex prompt templates)
    prompts_dir = home / ".codex" / "prompts"
    if prompts_dir.is_dir():
        for f in sorted(prompts_dir.glob("*.md")):
            try:
                text = f.read_text()
            except Exception:
                continue
            yield Record(
                id=stable_id("codex-prompt", f.name, text[:200]),
                source="codex",
                timestamp=iso_from_s(f.stat().st_mtime),
                text=text,
                project=None,
                session_id=None,
                kind="spec",
                extra={"sub_source": f"prompts/{f.name}"},
            )
    # 6. external_agent_session_imports.json — bridges codex threads ↔ claude project paths
    ext = home / ".codex" / "external_agent_session_imports.json"
    if ext.exists():
        try:
            data = json.loads(ext.read_text())
        except Exception:
            data = {}
        records = data.get("records", []) if isinstance(data, dict) else []
        for i, rec in enumerate(records):
            if not isinstance(rec, dict):
                continue
            sp = rec.get("source_path", "")
            yield Record(
                id=stable_id("codex-import", str(rec.get("imported_thread_id", i)), sp),
                source="codex",
                timestamp=iso_from_s(rec.get("imported_at")) if rec.get("imported_at") else "",
                text=json.dumps(rec, indent=2),
                project=sp,  # this binds the import to a real project path
                session_id=rec.get("imported_thread_id"),
                kind="response",
                extra={"sub_source": "external_agent_session_imports.json", "source_path": sp},
            )


def extract_cursor(home: Path) -> Iterator[Record]:
    """~/.cursor/{prompt_history.json, projects/*/agent-transcripts/*, ai-tracking/ai-code-tracking.db, plans/*}"""
    # 1. prompt_history.json
    p = home / ".cursor" / "prompt_history.json"
    if p.exists():
        try:
            data = json.loads(p.read_text())
        except Exception:
            data = []
        if isinstance(data, list):
            for i, item in enumerate(data):
                if not isinstance(item, str):
                    continue
                # prompt_history contains terminal-output-bleed. Try to extract just the user prompt.
                txt = item.strip()
                if not txt:
                    continue
                yield Record(
                    id=stable_id("cursor-history", str(i), txt[:200]),
                    source="cursor-agent",
                    timestamp="",
                    text=txt,
                    project=None,
                    session_id=None,
                    kind="prompt",
                    extra={"sub_source": "prompt_history.json", "index": i},
                )
    # 2. projects/agent-transcripts/*.jsonl
    at = home / ".cursor" / "projects" / "agent-transcripts"
    if at.is_dir():
        for f in sorted(at.glob("*.jsonl")):
            try:
                with f.open(encoding='utf-8', errors='replace') as fh:
                    for line in fh:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                        except Exception:
                            continue
                        role = obj.get("role") or obj.get("type")
                        if role not in ("user", "user_message", "human"):
                            continue
                        content = obj.get("content")
                        if isinstance(content, str):
                            txt = content
                        elif isinstance(content, list):
                            parts = [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") in ("text", "input_text")]
                            txt = "\n".join(p for p in parts if p)
                        else:
                            continue
                        if not txt:
                            continue
                        ts = obj.get("ts") or obj.get("timestamp") or obj.get("created_at")
                        yield Record(
                            id=stable_id("cursor-at", f.name, str(ts), txt[:200]),
                            source="cursor-agent",
                            timestamp=iso_from_s(ts) if ts else iso_from_s(f.stat().st_mtime),
                            text=txt,
                            project=None,
                            session_id=None,
                            kind="prompt",
                            extra={"sub_source": "agent-transcripts/", "file": f.name},
                        )
            except (OSError, PermissionError):
                continue
    # 3. ai-tracking/ai-code-tracking.db
    db = home / ".cursor" / "ai-tracking" / "ai-code-tracking.db"
    if db.exists():
        try:
            con = sqlite3.connect(str(db))
            cur = con.cursor()
            try:
                for row in cur.execute("SELECT conversationId, title, tldr, overview, summaryBullets, model, mode, updatedAt FROM conversation_summaries WHERE tldr IS NOT NULL OR overview IS NOT NULL OR summaryBullets IS NOT NULL ORDER BY updatedAt"):
                    cid, title, tldr, overview, bullets, model, mode, upd = row
                    text_parts = []
                    if title:
                        text_parts.append(f"# {title}")
                    if tldr:
                        text_parts.append(f"## TLDR\n{tldr}")
                    if overview:
                        text_parts.append(f"## Overview\n{overview}")
                    if bullets:
                        text_parts.append(f"## Bullets\n{bullets}")
                    text = "\n\n".join(text_parts)
                    if not text.strip():
                        continue
                    yield Record(
                        id=stable_id("cursor-aitrack", cid, text[:200]),
                        source="cursor-agent",
                        timestamp=iso_from_ms(upd) if upd else "",
                        text=text,
                        project=None,
                        session_id=cid,
                        kind="response",  # these are LLM-generated summaries
                        extra={"sub_source": "ai-tracking.db/conversation_summaries", "model": model, "mode": mode, "title": title},
                    )
            except sqlite3.OperationalError:
                pass
            con.close()
        except Exception:
            pass
    # 4. plans/*.plan.md
    plans = home / ".cursor" / "plans"
    if plans.is_dir():
        for f in sorted(plans.glob("*.plan.md")):
            try:
                text = f.read_text()
            except Exception:
                continue
            yield Record(
                id=stable_id("cursor-plan", f.name, text[:200]),
                source="cursor-agent",
                timestamp=iso_from_s(f.stat().st_mtime),
                text=text,
                project=None,
                session_id=None,
                kind="plan",
                extra={"sub_source": "plans/", "filename": f.name},
            )


def _extract_forge_text(obj: dict) -> str:
    """Drill into forge's nested message structure.

    Real forge shape (verified 2026-06-17 against local install):
      {"kind":"message","message":{
        "id":"...","content":{
          "user":      {"content":[{"text":"..."}]}                # user prompt
          "assistant": {"content":{"text":"..."},                # assistant reply
                        "reasoning_details":[...],               # CoT (sometimes)
                        "tool_calls":[...], "tool_results":[...]}
        },
        "timestamp": 1781751381
      }}
    Older builds may use:
      {"kind":"user_message","content":"..."}
      {"kind":"agent_message","content":"..."}
    """
    msg = obj.get("message")
    if not isinstance(msg, dict):
        return ""
    content = msg.get("content")
    if not isinstance(content, dict):
        # Older flat shape
        if isinstance(content, str):
            return content
        return ""

    # Prefer "user" if present, else "assistant", else "system", else "tool"
    for role in ("user", "assistant", "system", "tool"):
        blob = content.get(role)
        if not isinstance(blob, dict):
            continue
        inner = blob.get("content")
        if isinstance(inner, str):
            return inner
        if isinstance(inner, list):
            # User-style: [{"text": "..."}]
            parts = []
            for c in inner:
                if isinstance(c, dict):
                    if "text" in c and isinstance(c["text"], str):
                        parts.append(c["text"])
                    elif c.get("type") in ("text", "input_text", "output_text") and isinstance(c.get("text"), str):
                        parts.append(c["text"])
            if parts:
                return "\n".join(p for p in parts if p)
        if isinstance(inner, dict):
            # Assistant-style: {"text":"..."} (single string) or {"reasoning":...}
            txt = inner.get("text")
            if isinstance(txt, str) and txt:
                return txt
    # Reasoning details fallback (CoT content)
    rd = content.get("assistant", {}).get("reasoning_details") if isinstance(content.get("assistant"), dict) else None
    if isinstance(rd, list):
        for r in rd:
            if isinstance(r, dict) and r.get("text"):
                return r["text"]
    return ""


def extract_forge(home: Path) -> Iterator[Record]:
    """~/Library/Application Support/forge/conversations/*.jsonl (Mac), %APPDATA%/forge/... (Win)"""
    # Mac: ~/Library/Application Support/forge
    mac_dir = home / "Library" / "Application Support" / "forge"
    win_dir = home / "AppData" / "Roaming" / "forge"
    candidates = [mac_dir, win_dir]
    for base in candidates:
        if not base.is_dir():
            continue
        for f in sorted(base.glob("conversations/*.jsonl")):
            sess = f.stem
            try:
                with f.open(encoding='utf-8', errors='replace') as fh:
                    for line in fh:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                        except Exception:
                            continue
                        kind = obj.get("kind", "")
                        ts = obj.get("ts") or obj.get("created_at") or 0
                        if kind in ("agent_message", "assistant"):
                            txt = _extract_forge_text(obj)
                            if not txt:
                                continue
                            yield Record(
                                id=stable_id("forge-agent", sess, str(ts), txt[:200]),
                                source="forge",
                                timestamp=iso_from_s(ts) or iso_from_s(f.stat().st_mtime),
                                text=txt,
                                project=None,
                                session_id=sess,
                                kind="response",
                                extra={"sub_source": f"conversations/{f.name}", "forge_kind": kind},
                            )
                        elif kind in ("user_message", "user"):
                            txt = _extract_forge_text(obj)
                            if not txt:
                                continue
                            yield Record(
                                id=stable_id("forge-user", sess, str(ts), txt[:200]),
                                source="forge",
                                timestamp=iso_from_s(ts) or iso_from_s(f.stat().st_mtime),
                                text=txt,
                                project=None,
                                session_id=sess,
                                kind="prompt",
                                extra={"sub_source": f"conversations/{f.name}", "forge_kind": kind},
                            )
                        elif kind == "message":
                            # Newer shape: ONE line with both user and assistant sides.
                            # We can only emit user prompts (assistant text is duplicative
                            # of claude-code history which we already captured).
                            msg = obj.get("message", {})
                            content = msg.get("content", {}) if isinstance(msg, dict) else {}
                            if not isinstance(content, dict):
                                continue
                            user_blob = content.get("user")
                            if isinstance(user_blob, dict):
                                inner = user_blob.get("content")
                                if isinstance(inner, list):
                                    parts = [c.get("text", "") for c in inner if isinstance(c, dict) and isinstance(c.get("text"), str)]
                                    txt = "\n".join(p for p in parts if p)
                                else:
                                    txt = ""
                                if not txt:
                                    continue
                                yield Record(
                                    id=stable_id("forge-user", sess, str(ts), txt[:200]),
                                    source="forge",
                                    timestamp=iso_from_s(ts) or iso_from_s(f.stat().st_mtime),
                                    text=txt,
                                    project=None,
                                    session_id=sess,
                                    kind="prompt",
                                    extra={"sub_source": f"conversations/{f.name}", "forge_kind": "message.user"},
                                )
                        elif kind in ("plan", "plan_response"):
                            txt = _extract_forge_text(obj) or json.dumps(obj.get("content", {}))
                            if not txt:
                                continue
                            yield Record(
                                id=stable_id("forge-plan", sess, str(ts), txt[:200]),
                                source="forge",
                                timestamp=iso_from_s(ts) or iso_from_s(f.stat().st_mtime),
                                text=txt,
                                project=None,
                                session_id=sess,
                                kind="plan",
                                extra={"sub_source": f"conversations/{f.name}", "forge_kind": kind},
                            )
            except (OSError, PermissionError):
                continue


def extract_droid(home: Path) -> Iterator[Record]:
    """~/.droid (Factory Droid CLI) — sessions live in chat-history/ or per-repo subdirs.

    Locations probed (in order):
        ~/.droid/sessions/**/*.jsonl
        ~/.droid/chat-history/*.jsonl
        ~/.droid/history.jsonl
        ~/.local/share/droid/**/*.jsonl
    """
    bases = [
        home / ".droid",
        home / "AppData" / "Roaming" / "droid",  # Windows
        home / ".local" / "share" / "droid",
    ]
    for base in bases:
        if not base.is_dir():
            continue
        # history.jsonl (similar to claude/codex)
        hp = base / "history.jsonl"
        if hp.exists():
            with hp.open(encoding='utf-8', errors='replace') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                    except Exception:
                        continue
                    txt = (obj.get("text") or obj.get("display") or "").strip()
                    if not txt:
                        continue
                    yield Record(
                        id=stable_id("droid-history", str(obj.get("ts", "")), txt[:200]),
                        source="droid",
                        timestamp=iso_from_s(obj.get("ts")) if obj.get("ts") else "",
                        text=txt,
                        project=obj.get("project"),
                        session_id=obj.get("session_id"),
                        kind="prompt",
                        extra={"sub_source": "history.jsonl"},
                    )
        # rollouts / chat
        for pat in ("sessions/**/*.jsonl", "chat-history/*.jsonl", "**/rollout-*.jsonl", "**/*.jsonl"):
            for f in sorted(base.glob(pat)):
                # Skip history.jsonl (already handled)
                if f.name == "history.jsonl":
                    continue
                try:
                    with f.open(encoding='utf-8', errors='replace') as fh:
                        for line in fh:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                obj = json.loads(line)
                            except Exception:
                                continue
                            role = obj.get("role") or obj.get("type")
                            if role not in ("user", "user_message", "human"):
                                continue
                            content = obj.get("content") or obj.get("message", {}).get("content")
                            if isinstance(content, str):
                                txt = content
                            elif isinstance(content, list):
                                parts = [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") in ("text", "input_text")]
                                txt = "\n".join(p for p in parts if p)
                            else:
                                continue
                            if not txt:
                                continue
                            ts = obj.get("ts") or obj.get("timestamp") or obj.get("created_at")
                            yield Record(
                                id=stable_id("droid-rollout", f.name, str(ts), txt[:200]),
                                source="droid",
                                timestamp=iso_from_s(ts) if ts else iso_from_s(f.stat().st_mtime),
                                text=txt,
                                project=None,
                                session_id=obj.get("session_id") or f.stem,
                                kind="prompt",
                                extra={"sub_source": f"droid/{f.name}"},
                            )
                except (OSError, PermissionError):
                    continue


def extract_aider(home: Path) -> Iterator[Record]:
    """~/.aider/{analytics.json, .aider.chat.history.md, ...}"""
    base = home / ".aider"
    if not base.is_dir():
        return
    # .aider.chat.history.md is the canonical Aider chat log when configured
    chat = home / ".aider.chat.history.md"
    if chat.exists():
        try:
            text = chat.read_text()
        except Exception:
            text = ""
        if text.strip():
            yield Record(
                id=stable_id("aider-history", text[:200]),
                source="aider",
                timestamp=iso_from_s(chat.stat().st_mtime),
                text=text,
                project=None,
                session_id=None,
                kind="prompt",
                extra={"sub_source": ".aider.chat.history.md"},
            )
    # analytics.json
    analytics = base / "analytics.json"
    if analytics.exists():
        try:
            data = json.loads(analytics.read_text())
        except Exception:
            data = {}
        # analytics can have prompts in 'chat_messages' or similar
        if isinstance(data, dict):
            for k, v in data.items():
                if "prompt" in k.lower() and isinstance(v, list):
                    for i, item in enumerate(v):
                        if isinstance(item, str) and item.strip():
                            yield Record(
                                id=stable_id("aider-analytics", k, str(i), item[:200]),
                                source="aider",
                                timestamp="",
                                text=item,
                                project=None,
                                session_id=None,
                                kind="prompt",
                                extra={"sub_source": f"analytics.json/{k}", "index": i},
                            )


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

EXTRACTORS = {
    "claude-code":  extract_claude_code,
    "codex":        extract_codex,
    "cursor-agent": extract_cursor,
    "forge":        extract_forge,
    "droid":        extract_droid,
    "aider":        extract_aider,
    # other: not yet implemented (iMessage/Notes — defer)
}


def apply_filters_and_tag(records: Iterable[Record]) -> tuple[list[Record], Counter, Counter]:
    seen_dup_per_session: dict[str, set[str]] = defaultdict(set)
    keep: list[Record] = []
    drop_counts: Counter = Counter()
    tag_counts: Counter = Counter()
    for r in records:
        reason = is_trash(r.text)
        if reason:
            drop_counts[reason] += 1
            continue
        # duplicate-continue check (per session)
        norm = RE_DUP_CONTINUE.match(r.text)
        if norm:
            key = "continue"
            if r.session_id and key in seen_dup_per_session.get(r.session_id, set()):
                drop_counts["duplicate-continue"] += 1
                continue
            seen_dup_per_session.setdefault(r.session_id or "_", set()).add(key)
        # bind repo
        repo = bind_repo(r.project, r.text)
        if repo:
            r.extra["bound_repo"] = repo
        # tag
        tag = infer_tag(r.text)
        r.extra["tag"] = tag
        tag_counts[tag] += 1
        keep.append(r)
    return keep, drop_counts, tag_counts


def render_markdown(r: Record, registry_root: Path) -> Path:
    """Render a Record to a .md file under docs/curated-<kind>/<source>/<YYYY-MM>/<id>.md"""
    if r.timestamp:
        try:
            dt = datetime.fromisoformat(r.timestamp.replace("Z", "+00:00"))
            yyyy_mm = dt.strftime("%Y-%m")
        except Exception:
            yyyy_mm = "unknown"
    else:
        yyyy_mm = "unknown"
    kind_dir = {
        "prompt":   "curated-prompts",
        "plan":     "curated-plans",
        "response": "curated-responses",
        "spec":     "curated-responses",
        "idea":     "curated-responses",
        "design-doc": "curated-responses",
    }.get(r.kind, "curated-responses")
    out_dir = registry_root / "docs" / kind_dir / r.source / yyyy_mm
    # If the record binds to a repo, ALSO write a symlink-ish binding in a per-repo subdir
    repo = r.extra.get("bound_repo")
    if not repo:
        out_dir = out_dir / "_orphan"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{r.id}.md"
    # If file already exists, skip
    if out_path.exists():
        return out_path
    front = {
        "id": r.id,
        "source": r.source,
        "kind": r.kind,
        "timestamp": r.timestamp,
        "project": r.project,
        "session_id": r.session_id,
        "bound_repo": repo,
        "tag": r.extra.get("tag"),
        "sub_source": r.extra.get("sub_source"),
    }
    yaml_lines = ["---"]
    for k, v in front.items():
        if v is None or v == "":
            yaml_lines.append(f"{k}: null")
        else:
            # Quote
            s = str(v).replace('"', '\\"')
            yaml_lines.append(f'{k}: "{s}"')
    yaml_lines.append("---")
    yaml_lines.append("")
    body = "\n".join(yaml_lines) + f"# {r.kind} — {r.id}\n\n"
    body += f"**Source:** `{r.source}`\n"
    body += f"**Kind:** `{r.kind}`\n"
    body += f"**Timestamp:** {r.timestamp or 'unknown'}\n"
    if r.project:
        body += f"**Project:** `{r.project}`\n"
    if r.session_id:
        body += f"**Session:** `{r.session_id}`\n"
    if repo:
        body += f"**Bound repo:** [`{repo}`](../{('../../' * 4) if not out_path.parts[-4].startswith('curated') else ''}../intent/{repo}.md)\n"
    body += f"**Tag:** `{r.extra.get('tag')}`\n"
    body += f"**Sub-source:** `{r.extra.get('sub_source')}`\n"
    body += "\n---\n\n"
    body += r.text.strip() + "\n"
    out_path.write_text(body)
    return out_path


def render_per_repo_intent(records: list[Record], registry_root: Path) -> dict[str, dict]:
    """For each bound repo, aggregate bound prompts/plans/responses and render
    docs/intent/<repo>.md (only if the file doesn't already exist or is a stub)."""
    by_repo: dict[str, dict[str, list[Record]]] = defaultdict(lambda: defaultdict(list))
    for r in records:
        repo = r.extra.get("bound_repo")
        if not repo:
            continue
        by_repo[repo][r.kind].append(r)
    return by_repo


def aggregate_bindings_from_jsonl(out: Path) -> dict[str, dict]:
    """Re-derive the full binding index from _curated.jsonl.

    This is the authoritative source — even if a partial run overwrites
    _bindings.json, this rebuilds it from the cumulative curated corpus.
    """
    by_repo: dict[str, dict[str, list[str]]] = defaultdict(lambda: {"prompt": [], "plan": [], "response": []})
    jsonl = out / "_curated.jsonl"
    if not jsonl.exists():
        return {}
    seen_ids_per_repo: dict[str, set[str]] = defaultdict(lambda: {"prompt": set(), "plan": set(), "response": set()})
    with jsonl.open(encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            repo = obj.get("extra", {}).get("bound_repo")
            if not repo:
                continue
            kind = obj.get("kind", "response")
            if kind not in ("prompt", "plan", "response"):
                kind = "response"
            rid = obj.get("id")
            if rid in seen_ids_per_repo[repo][kind]:
                continue
            seen_ids_per_repo[repo][kind].add(rid)
            by_repo[repo][kind].append(rid)
    return by_repo


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--device", choices=("mac", "win", "linux"), required=True)
    ap.add_argument("--out", type=Path, required=True, help="registry worktree root (writes into docs/...)")
    ap.add_argument("--source", action="append", help="limit to specific source(s); can repeat")
    ap.add_argument("--incremental", action="store_true", help="skip records already in <out>/_seen.txt")
    ap.add_argument("--home", type=Path, default=Path.home(), help="device home dir; defaults to $HOME")
    args = ap.parse_args()

    if args.device == "win":
        # On Windows the home is usually %USERPROFILE% = C:/Users/<name>
        if str(args.home) == str(Path.home()):
            # Try the most common Windows profile locations
            for guess in [Path("C:/Users/koosh"), Path("C:/Users/kooshapari"), Path("/c/Users/koosh"), Path("/c/Users/kooshapari")]:
                if guess.is_dir():
                    args.home = guess
                    break
    if args.device == "mac" and not str(args.home).startswith("/Users"):
        # Sanity: if running on Mac but home isn't /Users/..., trust the user
        pass

    sources = args.source or list(EXTRACTORS.keys())
    print(f"[scrape] device={args.device} home={args.home} sources={sources} out={args.out}", file=sys.stderr)

    # Incremental: load seen ids
    seen_path = args.out / "_seen.txt"
    seen: set[str] = set()
    if args.incremental and seen_path.exists():
        seen = set(seen_path.read_text().splitlines())
        print(f"[scrape] incremental: {len(seen)} already seen", file=sys.stderr)

    out_jsonl = args.out / "_curated.jsonl"
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)

    total_raw = 0
    total_kept = 0
    all_records: list[Record] = []
    drop_counts_total: Counter = Counter()
    tag_counts_total: Counter = Counter()
    src_counts: Counter = Counter()

    with out_jsonl.open("a", encoding='utf-8', errors='replace') as fj:
        for source in sources:
            ext = EXTRACTORS.get(source)
            if not ext:
                print(f"[scrape] no extractor for source={source}", file=sys.stderr)
                continue
            print(f"[scrape] extracting source={source} ...", file=sys.stderr)
            t0 = time.time()
            raw_records = list(ext(args.home))
            print(f"[scrape]   extracted {len(raw_records)} raw records in {time.time()-t0:.1f}s", file=sys.stderr)
            total_raw += len(raw_records)
            kept, drops, tags = apply_filters_and_tag(raw_records)
            drop_counts_total.update(drops)
            tag_counts_total.update(tags)
            for r in kept:
                src_counts[source] += 1
                if r.id in seen:
                    continue
                seen.add(r.id)
                all_records.append(r)
                fj.write(json.dumps(asdict(r)) + "\n")
            print(f"[scrape]   kept {len(kept)} after filter; drops={dict(drops)} tags={dict(tags)}", file=sys.stderr)

    print(f"[scrape] TOTAL raw={total_raw} kept={len(all_records)} drops={dict(drop_counts_total)} tags={dict(tag_counts_total)}", file=sys.stderr)
    print(f"[scrape] per-source kept: {dict(src_counts)}", file=sys.stderr)

    # Render markdown files
    print(f"[scrape] rendering markdown ...", file=sys.stderr)
    rendered = 0
    for r in all_records:
        try:
            render_markdown(r, args.out)
            rendered += 1
        except Exception as e:
            print(f"[scrape] render failed for {r.id}: {e}", file=sys.stderr)
    print(f"[scrape] rendered {rendered} markdown files", file=sys.stderr)

    # Save seen set
    seen_path.write_text("\n".join(sorted(seen)))

    # Aggregate per-repo bindings from the FULL curated corpus (handles incremental runs)
    by_repo = aggregate_bindings_from_jsonl(args.out)
    binding_path = args.out / "_bindings.json"
    binding_path.write_text(json.dumps(
        {repo: {k: v for k, v in kinds.items() if v} for repo, kinds in by_repo.items() if any(kinds.values())},
        indent=2,
        sort_keys=True,
    ))
    print(f"[scrape] wrote binding index to {binding_path}", file=sys.stderr)
    total_bound = sum(len(v.get("prompt", [])) + len(v.get("plan", [])) + len(v.get("response", [])) for v in by_repo.values())
    print(f"[scrape] bound to {len(by_repo)} repos ({total_bound} records total)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
