# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within phenotype-org-governance, please report it responsibly.

### How to Report

1. **Do not** open a public GitHub issue for security vulnerabilities.
2. Send a detailed description of the vulnerability to the maintainers via:
   - A private vulnerability report on GitHub (preferred)
   - Direct email to the repository maintainers
3. Include the following in your report:
   - Type of vulnerability
   - Full paths of source file(s) related to the vulnerability
   - Location of the affected source code (tag/branch/commit)
   - Step-by-step instructions to reproduce the issue
   - Proof-of-concept or exploit code (if possible)
   - Impact assessment of the vulnerability

### What to Expect

- Acknowledgment of your report within 48 hours
- Regular updates on the progress toward a fix
- Credit for the discovery (unless you prefer to remain anonymous)
- Public disclosure after a fix has been released

### Scope

This policy covers all code in this repository. Third-party dependencies are covered by their respective security policies.

### MCP-specific guidance

For Model Context Protocol (MCP) server, client, and gateway boundaries — including transport selection (stdio vs SSE/HTTP), schema validation, authentication tiers, and framework/runtime splits — see [`docs/security/mcp-boundary.md`](docs/security/mcp-boundary.md). That document is authoritative for MCP surfaces in the Phenotype fleet.
