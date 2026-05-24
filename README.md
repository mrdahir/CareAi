# CareApp

**CareApp** is a reproductive health AI assistant for Sub-Saharan Africa — multilingual chat, contraceptive recommendations, and myth-busting backed by WHO/CDC-aligned knowledge.

## Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.11+, FastAPI, SQLAlchemy, Alembic |
| Database | PostgreSQL 15 + pgvector (SQLite for local/tests) |
| AI | **Google Gemini** (default) or **Groq** — KB fallback without keys |
| Frontend | React 18, TypeScript, Vite, Tailwind CSS, Zustand |

## Project structure

```
CareAiApp/
├── backend/          # FastAPI API
├── frontend/         # React SPA (careapp-frontend)
├── docker-compose.yml
├── docker-compose.prod.yml
└── docs/             # API + deployment guides
```

## Quick start

### 1. Database (optional Docker)

```bash
docker-compose up -d postgres
```

### 2. Backend

**Recommended:** Python **3.11–3.13**.

```bash
cd backend
py -3.13 -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env`:

```env
DATABASE_URL=sqlite+aiosqlite:///./care_app.db
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_key
# GROQ_API_KEY=your_groq_key
# LLM_PROVIDER=groq
```

```bash
python scripts\gen_kb.py
python scripts\data_processing\run_pipeline.py
python scripts\load_knowledge_base.py
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs

**Docker backend** (uses `backend/.env` for Gemini/Groq keys):

```bash
docker-compose up -d postgres
docker-compose up backend
```

**PostgreSQL migrations:**

```bash
alembic upgrade head
```

### 3. Frontend

```bash
cd frontend
npm install
copy .env.example .env.local
npm run dev
```

App: http://localhost:5173 — chat uses **streaming** (`/api/chat/stream`) with fallback to `/api/chat`.

### Western Kenya programme data

Place monitoring CSVs in  
`reversing-the-stall-in-fertility-decline-in-western-kenya-programme-monitoring-data-All-2026-05-19_1703/`  
(or set `WESTERN_KENYA_DATA_DIR`), then:

```bash
cd backend
python scripts/data_processing/western_kenya_pipeline.py
# or: python scripts/data_processing/run_pipeline.py
```

API: `GET /api/programme/summary`, `GET /api/programme/stats?county=Busia`  
Home page shows a live stats card when data is loaded.

- UI: English, Kiswahili, Amharic, French, Somali (header language selector)
- AI: Gemini/Groq respond in the selected language; KB uses translated JSON fields

Fill missing KB translations with Gemini (free tier — runs slowly, ~4s between calls):

```bash
cd backend
python scripts/translate_kb.py --lang sw
python scripts/load_knowledge_base.py
```

## Environment variables

### Backend (`backend/.env`)

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL or SQLite async URL |
| `LLM_PROVIDER` | `gemini` (default) or `groq` |
| `GEMINI_API_KEY` | Google AI Studio key |
| `GROQ_API_KEY` | Groq console key |
| `RATE_LIMIT_ENABLED` | `true` / `false` |
| `CORS_ORIGINS` | JSON array |

### Frontend (`frontend/.env.local`)

- `VITE_API_URL=http://localhost:8000/api`
- `VITE_APP_NAME=CareApp`

## Tests

```bash
cd backend
pytest -v
pytest --cov=app --cov-report=term-missing

cd ../frontend
npm run test:run
npm run build
```

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/chat` | AI chat |
| POST | `/api/chat/stream` | Streaming chat |
| GET | `/api/chat/history` | Message history |
| POST | `/api/recommend` | Contraceptive recommendations |
| POST | `/api/myth-check` | Myth verification |
| POST | `/api/faq` | FAQ answers |
| GET | `/api/contraceptives` | List methods |

See [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) and [docs/DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md).

## Medical disclaimer

CareApp provides general health education only. It is not a substitute for professional medical advice, diagnosis, or treatment. See [docs/DISCLAIMER.md](docs/DISCLAIMER.md).

## License

Competition / educational use — verify health content with qualified reviewers before production deployment.
