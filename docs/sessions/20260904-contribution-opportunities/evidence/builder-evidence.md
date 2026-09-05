# Builder / agent-tools audit redo

Snapshot: 2026-09-05 03:08-03:25 UTC (2026-09-04 evening Pacific). Live GitHub REST via gh. Read-only. 18 distinct candidates. No historical star-growth measurement: rising is UNKNOWN. Followers are current public reach, not skill or accessibility. Repo ownership type User does not prove solo company, amateur status, agency background, or fork origin. All first 16 report GitHub fork:false; PiDeck README explicitly says wrapper, not fork.

|Repository|Stars|Owner followers|Disposition|Evidence / fit|
|---|---:|---:|---|---|
|[ayuayue/PiDeck](https://github.com/ayuayue/PiDeck)|752|20|START|Session history, Codex/Claude imports; outside feature #176 17h29m, #171 46h41m.|
|[Javis603/token-monitor](https://github.com/Javis603/token-monitor)|1945|25|START|Usage/cost telemetry; outside Unsloth integration #606 84m; owner polishes PR himself.|
|[openwong2kim/wmux](https://github.com/openwong2kim/wmux)|367|13|START|Terminal/worktree orchestration; outside remote-pane feature #1141 8h50m; CodeRabbit 1 inline comment.|
|[fujibee/agmsg](https://github.com/fujibee/agmsg)|1488|87|START|Cross-agent messaging; outside fix #899 13h10m; owner pushes minor fix preserving contributor credit.|
|[aqua5230/usage](https://github.com/aqua5230/usage)|308|11|CONDITIONAL|Quota UI; external Windows locale #64 1h; explicit Codex review on closed #95, portions later landed with credit.|
|[VasiHemanth/tokentelemetry](https://github.com/VasiHemanth/tokentelemetry)|342|10|CONDITIONAL|Local telemetry; external NONE author Windows fix #324 18h45m, no comments/reviews; substantive feature evidence not checked.|
|[777genius/agent-teams-ai](https://github.com/777genius/agent-teams-ai)|2062|658|CONDITIONAL|Multi-agent desktop; external Cursor MCP integration #567 10h03m, CodeRabbit rounds and Codex quota warning.|
|[erha19/ping-island](https://github.com/erha19/ping-island)|1090|205|CONDITIONAL|macOS agent UI; external OMP hooks #300 33h49m, six commits; owner publicly Alibaba/OpenSumi, less Diego biography fit.|
|[RizRiyz/luvus](https://github.com/RizRiyz/luvus)|702|UNKNOWN|DEFER LOW-FRICTION|Agent terminal; accepts external features, #238 required repeated CodeRabbit and human fixes/screenshots; #268 4h13m.|
|[Sma1lboy/rove](https://github.com/Sma1lboy/rove)|116|92|WATCH|Agent multiplexer; apparent non-owner fast merges sampled are COLLABORATOR; newcomer acceptance remains UNKNOWN.|
|[jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp)|2654|372|CONDITIONAL|Code retrieval; external Racket reader #564 9h52m, 30files/+2841, but substantial explicit review/workflows.|
|[peters/horizon](https://github.com/peters/horizon)|700|226|WATCH|GPU terminal canvas; only 2 non-owner merged search hits; macOS package #100 10h28m March; recent outsider flow sparse.|
|[he-yufeng/CoreCoder](https://github.com/he-yufeng/CoreCoder)|1701|529|WATCH|Tiny coding agent; outside LiteLLM provider #10 10d19h, other fixes weeks; owner Moonshot researcher, not target analogy.|
|[ucsandman/DashClaw](https://github.com/ucsandman/DashClaw)|297|45|WATCH|Agent approval policies; outside attribution #85 ~22days, repeated review of stale description; timing friction.|
|[saltbo/agent-kanban](https://github.com/saltbo/agent-kanban)|468|UNKNOWN|UNPROVEN|Latest15 closed merges realmroot bot; 0 non-owner/nonexcluded-bot merged search hits.|
|[aofp/yume](https://github.com/aofp/yume)|149|UNKNOWN|UNPROVEN|Native Tauri Claude UI; zero merged outside PR search hits.|
|[slopus/happy](https://github.com/slopus/happy)|23637|ORG|DEPRIORITIZE|Popular mobile coding client; organization-owner search cannot distinguish maintainers, outsider evidence UNKNOWN.|
|[winfunc/opcode](https://github.com/winfunc/opcode)|22394|ORG|EXCLUDE INACTIVE|Last pushed 2025-10-16 despite current 2026-09 snapshot; old outside merges do not prove current availability.|

## Best four: exact evidence and business judgments

### ayuayue/PiDeck
Owner [caoayu](https://github.com/ayuayue), 20 followers; company unset. Profile does not establish employment or agency background. [Contribution guide](https://github.com/ayuayue/PiDeck/blob/main/CONTRIBUTING.md) is short: typecheck/build, typed IPC, keep pi responsible for agent internals, avoid mutating native session JSONL.
- [#176](https://github.com/ayuayue/PiDeck/pull/176): session pinning by r0y1z2, association CONTRIBUTOR. Created Sep 1 10:53:35Z, merged Sep 2 04:22:42Z. 1 commit, +293/-10, 13 files; 0 issue comments/inline comments/public reviews.
- [#171](https://github.com/ayuayue/PiDeck/pull/171): session/subagent/todo/file-change cards and shared aggregation. User c834292137, type User, association CONTRIBUTOR, fork head owner c834292137; not owner or bot. Created Aug 28 06:23:26Z; merged Aug 30 05:04:15Z. 16 commits, +3916/-1699, 116 files, zero public review/comments. Demonstrates broad outsider changes land, but large diff plus absent public review is a quality/dogfood risk, not proof of project quality. Private review unknown.
- Counterexample [#137](https://github.com/ayuayue/PiDeck/pull/137): pinning feature closed Aug13. Owner said current tabs sufficiently met need, major refactor divergence, invite adjusting PR against new version. Later #176 acceptance shows fit/timing matter. [#177 voice transcription](https://github.com/ayuayue/PiDeck/pull/177) still open Sep1 onward.
Similarity: strong low-profile owner + useful wrapper + broad feature acceptance. Business: directly useful to SessionLedger/agent workstation, share import/recovery fixtures. Resume: Electron IPC, lifecycle, history interoperability; measurable data preservation better than trivial UI. Proposed lane: isolated importer edge-case/regression or session resume UX, preserving source transcripts.

### Javis603/token-monitor
Owner [Javis](https://github.com/Javis603),25followers, company/bio unset, links javis-ai.com. README explicitly welcomes PRs and uses AGENTS.md as contributor guide.
- [#606](https://github.com/Javis603/token-monitor/pull/606): external CONTRIBUTOR The-Minion-oOo, Unsloth Studio integration. Sep4 06:07:50Z ->07:32:09Z (84m19s). +265/-30,30files,5commits,0inline reviews,1owner comment. Maintainer pushed artwork cleanup himself and thanked source detection, watching, WSL, UI/docs/tests. Meaningful feature entry, not docs-only.
- [#609](https://github.com/Javis603/token-monitor/pull/609): CONTRIBUTOR qwertlooker settings repaint fix, Sep4 06:39:32Z ->09:37:27Z. 2commits,1inline cubic bot comment,1owner follow-up that changed behavior to preserve overlay while rendering beneath it. Bot presence did not cause long cycle.
- Counterexample [#581](https://github.com/Javis603/token-monitor/pull/581): bundled pricing rejected after owner reproduced upstream pricing working; did not want duplicate pricing source. [#389](https://github.com/Javis603/token-monitor/pull/389) weekly quota estimate open since Aug12; [#446](https://github.com/Javis603/token-monitor/pull/446) taskbar feature open since Aug18.
Similarity: strong small public footprint, pragmatic feature intake; explicitly not accepts-anything. Business: direct OmniRoute/Tracera cost visibility and source adapters. Resume: bounded IO, SQLite/watchers, cross-platform instrumentation. Propose real source parser/health compatibility instead of duplicating price catalogs.

### openwong2kim/wmux
Owner [wong2kim](https://github.com/openwong2kim),13followers, no bio/company. [Guide](https://github.com/openwong2kim/wmux/blob/main/CONTRIBUTING.md) focused PR, TS check, tests, npm11/Node22, Windows runtime setup; README invites PRs/localization.
- [#1141](https://github.com/openwong2kim/wmux/pull/1141): CONTRIBUTOR p-poppe remote split-pane feature, Aug31 13:43:28Z ->22:33:29Z; +163/-11,8files,3commits,1CodeRabbit inline comment,2issue comments including owner triage. No repeated rejection shown in this sample.
- [#1100](https://github.com/openwong2kim/wmux/pull/1100) same contributor remote terminal as ordinary Surface also merged (timestamps not drilled).
- Latest30 closed sample had zero unmerged closures; oldest-open first5 consisted owner/bot PRs. This is bounded sample, not universal acceptance. 129 non-owner/nonexcluded-bot merged search hits may include collaborators, so not outside-acceptance rate.
Similarity: strong low-profile functional product, feature PR evidence; no verified agency background. Business: matches worktree fanout, shell/session preservation, cross-agent coordination. Resume: PTYs, process lifecycle, remote surfaces, atomic patch application. Mac developer can help portability but Windows reproduction is needed for ConPTY work.

### fujibee/agmsg
Owner [fujibee](https://github.com/fujibee),87followers, public bio Serial Entrepreneur | AI | VR | web3. This is verified self-description, not proof of agency size or enterprise clientele.
- [#899](https://github.com/fujibee/agmsg/pull/899): CONTRIBUTOR joelmitz SQL-on-stdin fix, Aug19 15:05:33Z ->Aug20 04:15:25Z;2commits,1file,+41/-11,0inline reviews,3issue comments. Owner explicitly pushed minor comment correction himself to avoid roundtrip while preserving authorship.
- [#212](https://github.com/fujibee/agmsg/pull/212): CONTRIBUTOR Eotel initial prompt for spawned agent; Jun24 03:36:58Z ->Jun27 10:10:14Z,3commits,5files,+109,1comment,0inline comments.
- Latest15closed merges mostly owner; recent feature acceptance slower/older than PiDeck and token-monitor. Open/rejected counterexamples not deeply checked: UNKNOWN. 48 filtered merged search hits not an acceptance rate.
Similarity: entrepreneurship bio + small reach + pragmatic maintainer follow-up, product directly relevant. Business: cross-CLI messaging and reliable delivery; possible dogfood for coordinator workflows. Resume: IPC/storage correctness, SQL/ARG_MAX, durable messaging. Suggested lane: reproduced interop/delivery fix in real multiagent sessions.

## Important downgrade evidence
- [aqua5230/usage #64](https://github.com/aqua5230/usage/pull/64) Windows language detection merged Jul15 10:31:11Z->11:31:34Z,7commits,8files,0comments/reviews. But [#95](https://github.com/aqua5230/usage/pull/95) contains owner-posted Automated review (Codex), four concrete findings, conflict warning; owner eventually landed selected pieces with attribution and closed. Strong small builder but not no-AI-scrutiny.
- [luvus #238](https://github.com/RizRiyz/luvus/pull/238): substantive dock resize accepted, but repeated CodeRabbit/human rounds, regression tests, video request and multiple correctness fixes. Not first choice under low-churn requirement despite 702stars.
- [agent-teams-ai #567](https://github.com/777genius/agent-teams-ai/pull/567) Cursor MCP integration 10h03m,+636/12files,8commits,3inline comments; CodeRabbit and Codex bot present. Contributor successfully declined irrelevant lint nit with evidence. Moderate scrutiny, not automatic exclusion.
- [jcodemunch #564](https://github.com/jgravelle/jcodemunch-mcp/pull/564) external Racket reader +2841/30files merged Aug30 03:47:28Z->13:39:22Z; owner review found Windows oracle newline behavior. Automated health radar present. Current inbound automation appears elaborate: needs narrow issue selection.
- [DashClaw #85](https://github.com/ucsandman/DashClaw/pull/85) Apr14->May6: feature accepted but stale-description review repeated; owner acknowledged mistake. 45followers does not guarantee fast review.
- [CoreCoder #10](https://github.com/he-yufeng/CoreCoder/pull/10) Apr23->May4; real integration acceptance but owner publicly Moonshot AI researcher with contest credentials, unlike target biography.
- [rove #847](https://github.com/Sma1lboy/rove/pull/847) 17m17s but ZHallen122 is COLLABORATOR; #743 NarwhalChen also COLLABORATOR and merged own PR. Do not count as newcomer openness.

## Method caveats
Filtered search query was repo:OWNER/REPO is:pr is:merged -author:OWNER -author:app/dependabot -author:app/realmroot, sample3 sorted updated; excludes two common bot authors but not all bots/collaborators. Pulled explicit PR association on best cases. No denominator or random sample, so no acceptance percentages. Times are wall-clock creation-to-merge, not hours of review labor. Public zero review comments does not establish zero review elsewhere. Current stars are snapshots, not demonstrated growth. No outreach.
