# Infrastructure Cost & ROI Estimation Guide

Typical monthly infrastructure footprint when running self-hosted AI automation stacks on client-owned cloud accounts:

| Workload Tier | Recommended Cloud Spec | Monthly Infra Cost | Typical Use Case |
| :--- | :--- | :--- | :--- |
| **Starter / MVP** | 2 vCPU · 4 GB RAM VPS + Managed Supabase Free/Pro | **\$12 – \$45 / mo** | Early-stage SaaS MVP, 1–2 n8n/WhatsApp bots |
| **Growth Agency / SMB** | 4–8 vCPU · 16 GB RAM VPS | **\$40 – \$96 / mo** | Unlimited n8n workflows, WAHA, Postgres, Redis, Qdrant RAG |
| **Dedicated 2-Node Cluster** | Dedicated Core Node (16 GB) + High-Perf Worker Node (16 GB) | **\$180 – \$220 / mo** | Zero-downtime WhatsApp/CRM + heavy Claude Code / Remotion / multi-agent workers |

### Direct API vs. Multi-Provider Gateway Routing
Routing non-critical background triage through lightweight models (`gemini-3.8-flash-low` / open models) while reserving frontier reasoning (`claude-opus-4-6-thinking` / `claude-sonnet-4-6`) strictly for complex builds reduces monthly LLM spend by **50–75%** without degrading client-facing quality.
