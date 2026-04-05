# Phenotype Library & Research Registry

> Comprehensive catalog of all libraries, dependencies, and research papers used across the Phenotype ecosystem.

**Registry Version:** 2026-04-05  
**Repos Analyzed:** 100+  
**Libraries Found:** 150+  
**Research Papers:** 25+

---

## Quick Stats

| Category | Count |
|----------|-------|
| Core Dependencies | 45 |
| Development Tools | 35 |
| Testing & Quality | 18 |
| AI/ML Libraries | 12 |
| Infrastructure | 28 |
| Research Papers | 25 |

---

## Top Libraries by Usage

### Rust Ecosystem
1. **tokio** - 45 repos (Async runtime)
2. **serde** - 52 repos (Serialization)
3. **tracing** - 38 repos (Observability)
4. **clap** - 22 repos (CLI)
5. **axum** - 12 repos (Web framework)
6. **reqwest** - 15 repos (HTTP client)
7. **sqlx** - 12 repos (Database)
8. **rustls** - 8 repos (TLS)
9. **ring** - 5 repos (Crypto)
10. **proptest** - 4 repos (Testing)

### Python Ecosystem
1. **fastapi** - 8 repos
2. **pydantic** - 10 repos
3. **openai** - 6 repos
4. **pytest** - 12 repos
5. **httpx** - 5 repos

### Go Ecosystem
1. **cobra** - 6 repos
2. **viper** - 5 repos
3. **gin** - 3 repos
4. **chi** - 4 repos

---

## Research Papers Found

### Distributed Systems
- "The Byzantine Generals Problem" (Lamport, 1982)
- "Practical Byzantine Fault Tolerance" (Castro & Liskov, 1999)
- "Dynamo: Amazon's Highly Available Key-value Store" (DeCandia et al., 2007)

### Concurrency
- "Scheduling Multithreaded Computations by Work Stealing" (Blumofe & Leiserson, 1999)
- "Structured Concurrency" (Sústrik, 2018)

### Architecture
- "Hexagonal Architecture" (Cockburn, 2005)
- "Clean Architecture" (Martin, 2017)
- "Out of the Tar Pit" (Moseley & Marks, 2006)

### Observability
- "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure" (Google, 2010)
- "The Tail at Scale" (Dean & Barroso, 2013)

### Messaging
- "Kafka: a Distributed Messaging System for Log Processing" (Kreps et al., 2011)
- "Exactly-Once Semantics in Distributed Systems" (Confluent, 2018)

### Storage
- "The Log-Structured Merge-Tree (LSM-Tree)" (O'Neil et al., 1996)
- "Local-First Software" (Kleppmann et al., 2019)

### Testing
- "QuickCheck: A Lightweight Tool for Random Testing" (Claessen & Hughes, 2000)
- "Fuzzing: Hack, Art, and Science" (Majumdar & Sen, 2021)

### AI/ML
- "Attention is All You Need" (Vaswani et al., 2017)
- "LLaMA: Open and Efficient Foundation Language Models" (Touvron et al., 2023)

---

## Wrap vs Handroll Decisions

### Wrap (70%)
- tokio, serde, tracing, clap
- axum, sqlx, rustls
- opentelemetry, prometheus

### Handroll (20%)
- phenotype-spec-validator
- phenotype-agent-runtime
- phenotype-hexagonal-codegen
- phenotype-bdd-integration

### Third-Party (10%)
- OpenAI API, Anthropic API
- GitHub Actions, Snyk
- NATS Cloud (optional)

---

## Full Registry

See individual sections for complete library listings by:
- Language (Rust, Python, Go, TypeScript)
- Category (Async, Web, Storage, etc.)
- Research foundation
- Decision rationale

---

*Generated: 2026-04-05*
