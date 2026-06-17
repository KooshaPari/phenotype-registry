import { defineConfig } from "vitepress";

export default defineConfig({
  title: "Phenotype Registry",
  description: "Master index for Phenotype specs, patterns, templates, and library research.",
  base: process.env.GITHUB_PAGES === "true" ? "/phenotype-registry/" : "/",
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    nav: [
      { text: "Overview", link: "/" },
      { text: "Registries", link: "/registries" },
      { text: "Library Research", link: "/library-research" },
      { text: "GitHub", link: "https://github.com/KooshaPari/phenotype-registry" },
    ],
    sidebar: [
      {
        text: "Phenotype Registry",
        items: [
          { text: "Overview", link: "/" },
          { text: "Registry Reference", link: "/registries" },
          { text: "Library Research", link: "/library-research" },
        ],
      },
      {
        text: "Rationalization",
        items: [
          { text: "Zero-Loop Plan", link: "/rationalization/ZERO_LOOP_ECOSYSTEM_PLAN" },
          { text: "Ecosystem DAG", link: "/rationalization/ECOSYSTEM_DAG" },
          { text: "Session Protocol", link: "/rationalization/SESSION_ARTIFACT_PROTOCOL" },
          { text: "ADR-004 Staging", link: "/adr/ADR-004-absorption-staging-vs-canonical" },
          { text: "ADR-005 AgilePlus", link: "/adr/ADR-005-agileplus-governance-boundary" },
          { text: "ADR-006 Zero-Loop", link: "/adr/ADR-006-zero-loop-agent-session" },
        ],
      },
    ],
    socialLinks: [{ icon: "github", link: "https://github.com/KooshaPari/phenotype-registry" }],
    search: {
      provider: "local",
    },
  },
});
