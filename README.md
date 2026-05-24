<div align="center">

# 🗄️ MiMoDB

**AI-Powered Database Explorer — Powered by Xiaomi MiMo V2.5**

[![Made with MiMo](https://img.shields.io/badge/Made_with-Xiaomi_MiMo_V2.5-ff6900?style=for-the-badge)](https://mimo.money)
[![GitHub Pages](https://img.shields.io/badge/Live-GitHub_Pages-222?style=for-the-badge&logo=github)](https://gyoomei.github.io/mimodb/)
[![Zero Backend](https://img.shields.io/badge/Backend-Zero-10b981?style=for-the-badge)](#)
[![Single HTML](https://img.shields.io/badge/File-Single_HTML-6366f1?style=for-the-badge)](#)

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=flat-square)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000&style=flat-square)](#)
[![MiMo AI](https://img.shields.io/badge/AI-Xiaomi_MiMo_V2.5-ff6900?style=flat-square)](#)
[![NoSQL](https://img.shields.io/badge/DB-NoSQL_Documents-06b6d4?style=flat-square)](#)

</div>

---

**MiMoDB** is a visual JSON document explorer with AI-powered query generation. Browse collections, filter documents, build aggregation pipelines — or just describe what you want in plain English and let MiMo generate the query.

## The Problem

NoSQL databases are powerful but hard to explore. You either use clunky CLI tools, pay for cloud dashboards, or write raw queries from memory. There's no free, zero-setup tool that lets you visually browse documents AND generate queries with natural language.

## How It Works

1. **Browse** 6 sample collections (users, products, orders, analytics, sessions, notifications) with real document data
2. **Filter** with JSON syntax — `{ "status": "active", "age": { "$gte": 25 } }`
3. **Ask MiMo** — click AI Query, describe what you want in plain English, get a working query
4. **View** results in JSON tree, table, or aggregation pipeline visualization
5. **Chat** with MiMo for deeper exploration — explain data, suggest aggregations, debug queries

## Features

- **6 Collections with Real Data** — Users, products, orders, analytics, sessions, notifications with realistic schemas and documents
- **JSON Syntax Highlighting** — Color-coded keys, strings, numbers, booleans, nulls with hover effects
- **3 View Modes** — JSON tree, table view, pipeline visualization
- **AI Query Generator** — Plain English → MongoDB-style JSON filter (MiMo V2.5)
- **Chat with MiMo** — Sidebar AI assistant for query help, data explanation, aggregation suggestions
- **Schema Viewer** — Auto-detected field types per collection
- **Document Browser** — Click any `_id` to view individual documents
- **Dark/Light Theme** — CSS variables, animated mesh gradient, floating particles
- **Zero Backend** — Single HTML file, Pollinations.ai free API, no install

## Architecture

```
┌──────────────────────────────────────────────────┐
│                    index.html                     │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │ Sidebar  │  │ Query    │  │ Results Panel  │  │
│  │ Colls    │  │ Bar      │  │ JSON | Table   │  │
│  │ Docs     │  │ Filter   │  │ Pipeline Viz   │  │
│  │ Schema   │  │ Aggregate│  │                │  │
│  └──────────┘  │ Raw      │  └───────────────┘  │
│                └────┬─────┘                      │
│                     │                            │
│  ┌──────────────────┴───────────────────────┐    │
│  │  Pollinations.ai → MiMo V2.5             │    │
│  │  AI Query Generator + Chat Assistant     │    │
│  └──────────────────────────────────────────┘    │
│  ┌──────────────────────────────────────────┐    │
│  │  In-Memory Document Store (6 collections)│    │
│  │  Filter engine + JSON renderer           │    │
│  └──────────────────────────────────────────┘    │
└──────────────────────────────────────────────────┘
```

## Performance

| Metric | Value |
|--------|-------|
| File size | 35 KB (single HTML) |
| Collections | 6 |
| Documents | 47 |
| View modes | 3 (JSON, Table, Pipeline) |
| Query time | < 20ms (client-side) |
| External deps | 0 (CDN only) |
| Backend | None |

## Security

- **All data client-side** — Documents live in browser memory, nothing sent to external DB
- **AI queries text-only** — Only the user's natural language prompt is sent to MiMo API
- **No credentials** — No database connections, no API keys, no auth tokens
- **No persistence** — Data resets on page reload (demo mode)

## What's Different

| Tool | AI Query | Free | Visual | Zero Setup |
|------|----------|------|--------|------------|
| **MiMoDB** | ✅ MiMo | ✅ | ✅ JSON+Table+Pipeline | ✅ |
| MongoDB Compass | ❌ | ✅ | ✅ | ❌ (needs DB) |
| Studio 3T | ❌ | Limited | ✅ | ❌ (needs DB) |
| NoSQL Booster | ❌ | Limited | ✅ | ❌ (needs DB) |
| ChatGPT + Mongo | ✅ GPT | ❌ | ❌ | ❌ |

MiMoDB is the only zero-setup NoSQL explorer with built-in AI query generation — no database connection required.

## Getting Started

### Use Online

Visit: **[gyoomei.github.io/mimodb](https://gyoomei.github.io/mimodb/)**

### Run Locally

```bash
git clone https://github.com/gyoomei/mimodb.git
cd mimodb
open index.html
```

No install, no build, no dependencies.

## License

MIT

---

<div align="center">

**Built for the [Xiaomi MiMo 100T Creator Program](https://mimo.money)**

</div>
