# Reproducibility Package

**HASH Innovation Challenge — Prototype Submission**  
**Deliverable 5 of 7:** Reproducibility Package  
**Project:** CareApp  
**Source Code Repository:** https://github.com/mrdahir/CareAi/  
**Date:** June 2026

This document provides materials to run CareApp locally and verify the main prototype results.

---

## What can be reproduced

After following the steps below:

1. The backend and frontend start on a standard laptop  
2. The web app is available at http://localhost:5173  
3. Chat, contraceptive recommendations, and myth verification work as demonstrated  
4. Automated tests pass  
5. Programme summary statistics load from bundled aggregate data  

CareApp does **not** train custom machine-learning models. Reproducibility depends on the **source code**, **JSON knowledge base**, **rule engine**, and optionally **LLM API keys**.

---

## Quick start

### Prerequisites

- Python 3.11+  
- Node.js 18+  
- Git  

Clone the repository:

```bash
git clone https://github.com/mrdahir/CareAi.git
cd CareAi
```

### Step 1 — Backend

```bash
python -m venv backend/venv
backend\venv\Scripts\activate
pip install -r requirements.txt
copy backend\.env.example backend\.env
cd backend
python scripts/gen_kb.py
python scripts/data_processing/run_pipeline.py
python scripts/load_knowledge_base.py
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

On macOS/Linux, use `source backend/venv/bin/activate` and `cp backend/.env.example backend/.env`.

### Step 2 — Frontend (new terminal)

```bash
cd frontend
npm install
copy .env.example .env.local
npm run dev
```

On macOS/Linux, use `cp .env.example .env.local`.

### Step 3 — Verification

| Check | URL or action | Expected result |
|-------|----------------|-----------------|
| Health | http://localhost:8000/api/health | Status OK |
| API docs | http://localhost:8000/docs | Swagger UI loads |
| Web app | http://localhost:5173 | CareApp home page loads |
| Chat | `/chat` in the app | Response streams or returns text |
| Recommend | Survey at `/recommend` | Top 3 methods returned |
| Myth buster | `/myth-buster` | Myth corrected with sources |

Example myth statement: *Family planning causes permanent infertility*.

---

## Running without LLM API keys

Leave `GEMINI_API_KEY` and `GROQ_API_KEY` empty in `backend/.env`.

The app uses the **knowledge-base fallback** for chat, myths, and FAQs. All automated tests pass without API keys.

Optional LLM connectivity test:

```bash
python backend/scripts/test_llm_providers.py
```

---

## Scripts and notebooks

CareApp uses **Python scripts** (no Jupyter notebooks required):

| Script | Purpose |
|--------|---------|
| `backend/scripts/gen_kb.py` | Builds myth and FAQ JSON files |
| `backend/scripts/load_knowledge_base.py` | Loads KB into SQLite/PostgreSQL |
| `backend/scripts/translate_kb.py` | Translates KB strings (optional; uses Gemini) |
| `backend/scripts/data_processing/western_kenya_pipeline.py` | DASSA CSVs to programme stats JSON |
| `backend/scripts/data_processing/run_pipeline.py` | Pipeline with sample or real CSV data |
| `backend/scripts/test_llm_providers.py` | Gemini/Groq connectivity check |

---

## Model training workflow

**Not applicable.** CareApp uses:

1. **Pre-trained LLMs** (Gemini, Groq Llama) with retrieval-augmented prompts  
2. **Rule-based recommendation engine** (deterministic scoring)  
3. **Lexical myth matching** (Jaccard similarity)  

---

## Evaluation scripts

```bash
cd backend
pytest -v

cd frontend
npm run test:run
npm run build
```

| Command | Coverage |
|---------|----------|
| `pytest -v` | Recommendation engine, knowledge base, API routes, streaming |
| `npm run test:run` | React component tests |
| `npm run build` | TypeScript compilation |

Tests use SQLite and empty LLM keys by default.

---

## Sample inputs and outputs

### Recommendation (POST `/api/recommend`)

**Input:**

```json
{
  "age": 25,
  "breastfeeding": false,
  "pregnancy_goals": "space_children",
  "health_conditions": [],
  "preferred_duration": "long_term",
  "region": "Kenya",
  "language": "en"
}
```

**Output:** JSON with top 3 ranked contraceptive methods, scores, and rationale.

### Myth check (POST `/api/myth-check`)

**Input:**

```json
{
  "statement": "Family planning causes permanent infertility",
  "language": "en"
}
```

**Output:** `is_myth: true`, evidence text, and cited sources.

### Programme summary (GET `/api/programme/summary`)

**Output:** Total visits, counselling rate, and top methods when stats are available.  
Bundled aggregate file: `backend/data/processed/western_kenya_stats.json`

### Western Kenya pipeline (optional)

Raw DASSA CSV files are not stored in the repository. To regenerate stats from local CSV files, set `WESTERN_KENYA_DATA_DIR` or mount the data path in `docker-compose.yml`, then run:

```bash
cd backend
python scripts/data_processing/western_kenya_pipeline.py
```

Verify at http://localhost:8000/api/programme/summary

---

## Docker

Container deployment with PostgreSQL is documented in the repository README (`docker-compose up`).

---

*End of reproducibility package.*
