# CareApp Deployment Guide

## LLM providers (Gemini / Groq)

Set in backend environment (never commit real keys):

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key
GEMINI_MODEL=gemini-flash-latest

# Or Groq:
LLM_PROVIDER=groq
GROQ_API_KEY=your_key
GROQ_MODEL=llama-3.3-70b-versatile
```

Without keys, CareApp uses the knowledge-base fallback (still functional for demos).

## Local (Docker)

```bash
# From repo root — ensure backend/.env has GEMINI_API_KEY or GROQ_API_KEY
docker-compose up -d postgres
docker-compose up backend
```

Frontend separately:

```bash
cd frontend && npm run dev
```

## Production (Docker Compose)

```bash
export POSTGRES_PASSWORD=strong_password
export GEMINI_API_KEY=your_key
export LLM_PROVIDER=gemini
export CORS_ORIGINS='["https://your-app.vercel.app"]'

docker-compose -f docker-compose.prod.yml up -d
```

## Database migrations (PostgreSQL)

```bash
cd backend
alembic upgrade head
python scripts/load_knowledge_base.py
```

Development SQLite can still use `init_db()` on startup.

## Railway (backend)

1. Connect GitHub repo, root: `backend/`
2. Set env: `DATABASE_URL`, `LLM_PROVIDER`, `GEMINI_API_KEY` or `GROQ_API_KEY`, `CORS_ORIGINS`
3. Start command: `gunicorn app.main:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT -w 2`

## Vercel (frontend)

1. Root: `frontend/`
2. Build: `npm run build`
3. Output: `dist`
4. Env: `VITE_API_URL=https://your-api.railway.app/api`

## Health check

`GET /api/health` — use for load balancers and uptime monitors.
