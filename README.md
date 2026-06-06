# CareApp

Reproductive health AI assistant for Sub-Saharan Africa — multilingual chat, contraceptive recommendations, myth-busting, and programme monitoring insights. Built with FastAPI and React.

## Features

- **Health chat** — streaming responses via Google Gemini or Groq (KB fallback without API keys)
- **Recommendations** — rule-based contraceptive matching with regional data
- **Myth buster** — evidence-based fact checks from a structured knowledge base
- **Multilingual** — English, Kiswahili, Amharic, French, Somali (UI + AI)
- **Programme data** — optional Western Kenya monitoring CSV integration

## Tech stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.11+, FastAPI, SQLAlchemy, Alembic |
| Database | PostgreSQL 15 / SQLite (local) |
| AI | Gemini (default) or Groq |
| Frontend | React 18, TypeScript, Vite, Tailwind, Zustand |

## Prerequisites

- **Python** 3.11–3.13
- **Node.js** 18+ (20 recommended)
- **Docker** (optional, for PostgreSQL)
- **API keys** (optional): [Google AI Studio](https://aistudio.google.com/) and/or [Groq](https://console.groq.com/)

## Project structure

```
CareAiApp/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── requirements.txt          # → backend/requirements.txt
├── docker-compose.yml
├── backend/                  # FastAPI API
│   ├── requirements.txt
│   ├── .env.example
│   └── app/
├── frontend/                 # React SPA
│   ├── package.json
│   └── .env.example
└── docs/                     # HASH submission deliverables (markdown)
```

## Setup

### 1. Clone and configure

```bash
git clone https://github.com/mrdahir/CareAi.git
cd CareAi
```

### 2. Backend

```bash
# Create virtual environment (from repo root or backend/)
python -m venv backend/venv
# Windows:
backend\venv\Scripts\activate
# macOS/Linux:
# source backend/venv/bin/activate

pip install -r requirements.txt
copy backend\.env.example backend\.env   # Windows
# cp backend/.env.example backend/.env   # macOS/Linux
```

Edit `backend/.env`:

```env
DATABASE_URL=sqlite+aiosqlite:///./care_app.db
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key_here
# GROQ_API_KEY=your_key_here
# LLM_PROVIDER=groq
CORS_ORIGINS=["http://localhost:5173"]
```

Initialize data and start the API:

```bash
cd backend
python scripts/gen_kb.py
python scripts/data_processing/run_pipeline.py
python scripts/load_knowledge_base.py
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- API: http://localhost:8000  
- Swagger: http://localhost:8000/docs  

### 3. Frontend

In a second terminal:

```bash
cd frontend
npm install
copy .env.example .env.local   # Windows
# cp .env.example .env.local   # macOS/Linux
npm run dev
```

- App: http://localhost:5173  

### 4. Docker (optional)

```bash
docker-compose up -d postgres
docker-compose up backend
```

Ensure `backend/.env` contains your LLM keys. The backend container mounts programme data when the Western Kenya CSV folder is present.

## Environment variables

| Location | Key variables |
|----------|----------------|
| `backend/.env` | `DATABASE_URL`, `LLM_PROVIDER`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `CORS_ORIGINS` |
| `frontend/.env.local` | `VITE_API_URL`, `VITE_APP_NAME` |

See `backend/.env.example` and `frontend/.env.example` for full lists.

## Programme monitoring data (optional)

Raw DASSA CSV files are **not stored in this repository** (download from the challenge platform locally). The repo includes processed aggregates at `backend/data/processed/western_kenya_stats.json` so programme APIs work without the raw folder.

To refresh stats from your own copy of the CSVs, place exports in:

`reversing-the-stall-in-fertility-decline-in-western-kenya-programme-monitoring-data-All-2026-05-19_1703/`

Then process:

```bash
cd backend
python scripts/data_processing/western_kenya_pipeline.py
```

- `GET /api/programme/summary`  
- `GET /api/programme/stats?county=Busia`  

## Tests

```bash
# Backend
cd backend
pytest -v

# Frontend
cd frontend
npm run test:run
npm run build
```

## API overview

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/chat` | AI chat |
| POST | `/api/chat/stream` | Streaming chat |
| POST | `/api/recommend` | Contraceptive recommendations |
| POST | `/api/myth-check` | Myth verification |
| POST | `/api/faq` | FAQ answers |
| GET | `/api/contraceptives` | List methods |
| GET | `/api/programme/summary` | Programme stats (if data loaded) |

More: interactive API docs at `http://localhost:8000/docs` when the backend is running.

## Documentation

| Document | Description |
|----------|-------------|
| [docs/SUBMISSION_CHECKLIST.md](docs/SUBMISSION_CHECKLIST.md) | HASH submission checklist (all 7 deliverables) |
| [docs/REPRODUCIBILITY_PACKAGE.md](docs/REPRODUCIBILITY_PACKAGE.md) | How reviewers run and verify the prototype |
| [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | How to use the app |
| [docs/TECHNICAL_REPORT.md](docs/TECHNICAL_REPORT.md) | Technical report (HASH submission) |
| [docs/DATA_USE_DOCUMENTATION.md](docs/DATA_USE_DOCUMENTATION.md) | Data use documentation |
| [docs/TEAM_CONTRIBUTION_STATEMENT.md](docs/TEAM_CONTRIBUTION_STATEMENT.md) | Team contribution statement |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |

**Repository:** https://github.com/mrdahir/CareAi/

## Medical disclaimer

CareApp provides **general health education only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for personal medical decisions.

## License

[MIT License](LICENSE) — Copyright (c) 2026 CareApp contributors.

Health content should be reviewed by qualified professionals before production use.
