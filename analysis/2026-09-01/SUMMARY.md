# Platform/API exhaust × AI — MCP registry probe, 2026-09-01 (frontier 4)

## Top find — MCP (Model Context Protocol) server registries
The tool/capability layer of the AI-agent economy. Canonical registry
(registry.modelcontextprotocol.io — Anthropic/GitHub/PulseMCP/Microsoft) + marketplaces
(Glama ~37k, mcp.so ~20,222, PulseMCP ~11,840 growing 1,000+/mo, Smithery ~7,000).
Independent May-2026 pull of the official API: **9,652 latest servers / 28,959 server-version
records**; 15,926 GitHub repos carry the `mcp-server` topic.

**Live probe today (official API, `/v0/servers`, paginable):** pulled a bounded **500-server
sample** — **every record carries a version field** (server × version = a real longitudinal
panel), reverse-DNS namespaces with heavy publisher concentration (ai.bowmark = 191 servers in
just the alphabetical "a" slice; ai.bluenexus 27, ai.ankimcp 25). Capability metadata shows what
agents get wired to (browser/web, filesystem, Slack, Google, payments…). **Caveat:** the 500 sample
is alphabetically ordered (early namespaces only), so counts aren't registry-representative;
raw sample in `mcp_registry_sample_500.jsonl`.
**Unclaimed (c≈3):** security/measurement papers exist (arXiv 2503.23278, 2506.13538, 2509.25292
"MCPCrawler"); the registry as a *governance/longitudinal capability* panel is under-built.

## Runner-up — AI Agent Marketplace Index (DeepNLP, Hugging Face)
Metadata for AI agents — name, website, description + monthly web-performance metrics
(Google/Bing rankings, GitHub stars, arXiv references). HF-hosted, probe-able; the agent-economy panel.

## Runner-up — AI-provider Usage-Policy / AUP change tracking
How AI companies change permissible use over time (Anthropic AUP→"Usage Policy" updates with new
high-risk-use requirements; OpenAI's 2024 removal of its military-use ban). Governance of AI self-
regulation, incl. political/military uses. No clean public diff-tracker exists — assemblable from
Wayback (a ledger seed) + providers' policy pages.
