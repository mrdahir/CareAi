# 🛠️ TECHNICAL REFERENCE & COMMAND CHEAT SHEET

---

## 📦 FINAL TECH STACK

### Backend Stack

```
Framework:        FastAPI 0.109.0 (Python web framework)
Runtime:          Python 3.11+
ORM:              SQLAlchemy 2.0+ (database)
Migrations:       Alembic 1.13+ (database versioning)
Database:         PostgreSQL 15+ with pgvector extension
Vector Search:    pgvector (for semantic search)
AI/LLM:           Claude 3.5 Sonnet (Anthropic API)
API Client:       Anthropic Python SDK
Validation:       Pydantic 2.0+
Async:            asyncio, aiohttp
Caching:          Redis (optional, nice-to-have)
Logging:          Python logging + structlog
Testing:          pytest, pytest-cov
Deployment:       Docker, Railway

Key Dependencies:
- anthropic==0.25.0 (Claude API)
- fastapi==0.109.0
- sqlalchemy==2.0.23
- asyncpg==0.29.0
- pydantic==2.5.0
- alembic==1.13.1
- python-dotenv==1.0.0
- pydantic-settings==2.1.0
- pytest==7.4.3
- pytest-cov==4.1.0
- black==23.12.0 (code formatting)
- mypy==1.7.1 (type checking)
- ruff==0.1.8 (linting)
```

### Frontend Stack

```
Framework:        React 18.2+
Language:         TypeScript 5.3+
Build Tool:       Vite 5.0+ (replaces Create React App)
CSS:              Tailwind CSS 3.4+
HTTP Client:      axios 1.6+
State:            Zustand 4.4+ (lightweight state management)
Routing:          React Router 6.20+
Forms:            React Hook Form 7.48+ + Zod 3.13+ (validation)
Components:       shadcn/ui (optional, nice-to-have)
Icons:            Lucide React
Testing:          Vitest, React Testing Library
E2E Testing:      Cypress 13.6+ or Playwright
Deployment:       Vercel
PWA:              PWA manifest, Service Worker

Key Dependencies:
- react==18.2.0
- react-dom==18.2.0
- typescript==5.3.3
- vite==5.0.0
- tailwindcss==3.4.0
- react-router-dom==6.20.0
- react-hook-form==7.48.0
- zod==3.13.0
- axios==1.6.0
- zustand==4.4.0
- lucide-react==0.383.0
```

---

## 📋 COMPLETE REQUIREMENTS.TXT (Backend)

```txt
# FastAPI & Web
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-multipart==0.0.6

# Database
sqlalchemy==2.0.23
alembic==1.13.1
asyncpg==0.29.0
psycopg2-binary==2.9.9
pgvector==0.2.4

# AI/LLM
anthropic==0.25.0

# Data Processing
pandas==2.1.3
numpy==1.24.3
pydantic==2.5.0
pydantic-settings==2.1.0

# Utilities
python-dotenv==1.0.0
python-slugify==8.0.1
requests==2.31.0
httpx==0.25.2

# Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
cryptography==41.0.7

# Async
aiohttp==3.9.1

# Logging & Monitoring
structlog==24.1.0
python-json-logger==2.0.7

# Development
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
pytest-mock==3.12.0
black==23.12.0
mypy==1.7.1
ruff==0.1.8
isort==5.13.2
pre-commit==3.6.0

# Deployment
gunicorn==21.2.0
```

---

## 📋 COMPLETE PACKAGE.JSON (Frontend)

```json
{
  "name": "health-ai-frontend",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:run": "vitest run",
    "test:coverage": "vitest run --coverage",
    "type-check": "tsc --noEmit",
    "format": "prettier --write \"src/**/*.{ts,tsx,css}\""
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.0",
    "zustand": "^4.4.0",
    "react-hook-form": "^7.48.0",
    "zod": "^3.13.0",
    "tailwindcss": "^3.4.0",
    "lucide-react": "^0.383.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.0.0",
    "typescript": "^5.3.3",
    "vitest": "^1.1.0",
    "@testing-library/react": "^14.1.2",
    "@testing-library/jest-dom": "^6.1.5",
    "cypress": "^13.6.0",
    "tailwindcss": "^3.4.0",
    "postcss": "^8.4.32",
    "autoprefixer": "^10.4.16",
    "prettier": "^3.1.1",
    "eslint": "^8.55.0",
    "@typescript-eslint/eslint-plugin": "^6.14.0",
    "@typescript-eslint/parser": "^6.14.0"
  }
}
```

---

## 🐳 DOCKER COMMANDS

### Build Backend Image

```bash
# From backend directory
docker build -t health-ai-backend:latest .

# Tag for registry
docker tag health-ai-backend:latest yourregistry/health-ai-backend:latest

# Push to registry
docker push yourregistry/health-ai-backend:latest
```

### Run with Docker Compose (Local Development)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# View specific service logs
docker-compose logs -f postgres
docker-compose logs -f backend
```

### Docker Compose File Structure

```yaml
version: '3.8'
services:
  postgres:
    image: postgres:15-alpine
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: health_user
      POSTGRES_PASSWORD: your_secure_password
      POSTGRES_DB: health_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U health_user"]
      interval: 10s
      timeout: 5s
      retries: 5

  pgadmin:
    image: dpage/pgadmin4:latest
    ports:
      - "5050:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@health.local
      PGADMIN_DEFAULT_PASSWORD: admin
    depends_on:
      - postgres

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql+asyncpg://health_user:password@postgres/health_db
      CLAUDE_API_KEY: your_api_key
      ENVIRONMENT: development
    depends_on:
      postgres:
        condition: service_healthy
    volumes:
      - ./backend:/app
    command: uvicorn app.main:app --host 0.0.0.0 --reload

volumes:
  postgres_data:
```

---

## 🔧 ENVIRONMENT VARIABLES

### .env.local (Backend)

```bash
# Environment
ENVIRONMENT=development

# Database
DATABASE_URL=postgresql+asyncpg://health_user:password@localhost/health_db
DATABASE_ECHO=true

# Claude API
CLAUDE_API_KEY=sk-ant-your-actual-key-here
CLAUDE_MODEL=claude-3-5-sonnet-20241022

# Server
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4

# CORS
CORS_ORIGINS=["http://localhost:3000", "http://localhost:5173"]
CORS_ALLOW_CREDENTIALS=true

# Logging
LOG_LEVEL=INFO

# Redis (optional)
REDIS_URL=redis://localhost:6379/0

# Rate Limiting
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_SECONDS=60
```

### .env.local (Frontend)

```bash
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME="Health AI Assistant"
VITE_VERSION=0.1.0
VITE_SUPPORTED_LANGUAGES=en,sw,am,fr,so
```

---

## 📲 PYTHON COMMANDS (Backend)

### Initial Setup

```bash
# Create virtual environment
python3.11 -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install -r requirements-dev.txt
```

### Database Management

```bash
# Create initial migration
cd backend
alembic revision --autogenerate -m "Initial schema"

# Run migrations
alembic upgrade head

# Check migration status
alembic current

# Downgrade migration
alembic downgrade -1
```

### Running Backend

```bash
# Development (with reload)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# With environment file
source .env.local
uvicorn app.main:app --reload
```

### Testing

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_recommendation_engine.py -v

# Run with markers
pytest -m "unit" -v  # Only unit tests
pytest -m "integration" -v  # Only integration tests

# Watch mode (auto-run on changes)
pytest-watch
```

### Code Quality

```bash
# Format code with Black
black app/

# Check code style
ruff check app/

# Fix style issues
ruff check app/ --fix

# Type checking
mypy app/ --ignore-missing-imports

# Sort imports
isort app/

# Run all checks
pre-commit run --all-files
```

### Data Processing

```bash
# Load APHRC data
python scripts/data_processing/load_data.py

# Clean data
python scripts/data_processing/clean_data.py

# Run full pipeline
python scripts/data_processing/run_pipeline.py

# Load knowledge base
python scripts/load_knowledge_base.py

# Generate embeddings
python scripts/generate_embeddings.py
```

---

## 📱 NPM COMMANDS (Frontend)

### Setup

```bash
# Create project with Vite
npm create vite@latest frontend -- --template react-ts
cd frontend

# Install dependencies
npm install

# Install Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Development

```bash
# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Type checking
npm run type-check

# Format code
npm run format

# Lint
npm run lint
```

### Testing

```bash
# Run tests
npm run test

# Run tests with UI
npm run test:ui

# Run tests once (CI)
npm run test:run

# Coverage report
npm run test:coverage

# E2E tests (Cypress)
npx cypress open

# E2E tests (headless)
npx cypress run
```

---

## 🚀 DEPLOYMENT COMMANDS

### Railway Backend Deployment

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Create new project
railway init

# Link to existing project
railway link

# Set environment variables
railway variables:set DATABASE_URL=...
railway variables:set CLAUDE_API_KEY=...

# Deploy
railway up

# View logs
railway logs

# SSH into production
railway shell
```

### Vercel Frontend Deployment

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Production deployment
vercel --prod

# Set environment variables
vercel env add VITE_API_URL

# View deployments
vercel list

# Check logs
vercel logs
```

### GitHub Actions CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r backend/requirements.txt
      - run: pytest backend/

  deploy-backend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: git push https://heroku:${{ secrets.HEROKU_API_KEY }}@git.heroku.com/health-ai-app.git main

  deploy-frontend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: vercel/action@main
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

---

## 🧪 API TESTING COMMANDS

### Using cURL

```bash
# Chat endpoint
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Is the pill safe while breastfeeding?",
    "language": "en"
  }'

# Recommendation endpoint
curl -X POST http://localhost:8000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "age": 28,
    "breastfeeding": false,
    "pregnancy_goals": "space_children",
    "health_conditions": [],
    "preferred_duration": "long_term",
    "region": "Kenya",
    "language": "sw"
  }'

# Myth check endpoint
curl -X POST http://localhost:8000/api/myth-check \
  -H "Content-Type: application/json" \
  -d '{
    "statement": "Contraception causes infertility",
    "language": "en"
  }'
```

### Using Python

```python
import requests

BASE_URL = "http://localhost:8000/api"

# Chat
response = requests.post(
    f"{BASE_URL}/chat",
    json={
        "message": "Tell me about IUD effectiveness",
        "language": "en"
    }
)
print(response.json())

# Recommendation
response = requests.post(
    f"{BASE_URL}/recommend",
    json={
        "age": 28,
        "breastfeeding": False,
        "pregnancy_goals": "space_children",
        "health_conditions": [],
        "preferred_duration": "long_term"
    }
)
print(response.json())
```

---

## 📊 MONITORING & DEBUGGING

### View Logs

**Backend:**
```bash
docker-compose logs -f backend
tail -f backend/logs/app.log
```

**Frontend:**
```bash
# Browser console (F12)
# Check Network tab
# Check Console for errors
```

### Database Queries

```bash
# Access PostgreSQL CLI
docker-compose exec postgres psql -U health_user -d health_db

# Common queries
\dt  # List tables
SELECT * FROM chatmessage LIMIT 5;  # View messages
SELECT COUNT(*) FROM contraceptivemethod;  # Count methods
```

### API Documentation

Once backend is running:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Performance Monitoring

```python
# In FastAPI middleware, add:
import time
from fastapi import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

---

## 🔐 SECURITY CHECKLIST

**Before Production:**
```bash
# ✅ Check for exposed secrets
git grep -i "password\|secret\|key" | grep -v ".env.example"

# ✅ Run security audit
pip audit

# ✅ CORS configuration
# Only allow frontend domain in CORS_ORIGINS

# ✅ Database backups
# Set up automated backups on Railway

# ✅ API rate limiting
# Enabled in config.py

# ✅ HTTPS enforced
# Railway auto-handles, Vercel auto-handles

# ✅ API keys not in code
# All in .env.local (not committed)

# ✅ SQL injection protection
# Using SQLAlchemy ORM (parametrized queries)

# ✅ XSS protection
# React auto-escapes, Tailwind safe
```

---

## 📈 SCALING REMINDERS

**If traffic increases:**

1. **Database:**
   - Enable connection pooling
   - Add indexes on frequent queries
   - Archive old messages

2. **Backend:**
   - Increase Gunicorn workers
   - Add Redis caching
   - Enable gzip compression

3. **Frontend:**
   - Enable code splitting
   - Add lazy loading
   - Optimize images

4. **Claude API:**
   - Implement response caching
   - Batch requests if possible
   - Monitor token usage

---

## 📚 QUICK REFERENCE

| Task | Command |
|------|---------|
| Start dev environment | `docker-compose up -d && cd backend && source venv/bin/activate && uvicorn app.main:app --reload` |
| Run tests | `pytest --cov=app` |
| Format code | `black app/ && isort app/` |
| Check types | `mypy app/` |
| Build Docker | `docker build -t health-app .` |
| Deploy | `git push main` (auto-deploys via CI/CD) |
| View logs | `docker-compose logs -f` |
| Database shell | `docker-compose exec postgres psql -U health_user -d health_db` |
| Frontend dev | `cd frontend && npm run dev` |
| Frontend build | `cd frontend && npm run build` |

---

## ✅ GO LIVE CHECKLIST

Before marking as "done":

- [ ] All endpoints returning 200/correct status
- [ ] Database migrations completed
- [ ] Knowledge base loaded and verified
- [ ] Tests passing (backend 80%+, frontend 70%+)
- [ ] No console errors in browser
- [ ] API documented at /docs
- [ ] Health check endpoint responding
- [ ] Environment variables configured
- [ ] Logging working
- [ ] Rate limiting enabled
- [ ] CORS configured
- [ ] Error handling tested
- [ ] Mobile layout responsive
- [ ] Offline mode tested
- [ ] Security scan passed
- [ ] Load time < 3 seconds
- [ ] All features working as described
- [ ] Demo script prepared

---

Good luck! 🚀
