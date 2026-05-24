# 🏃 QUICK EXECUTION GUIDE - 30 DAY SPRINT
## Reproductive Health AI App - Competition Edition

---

## ⚡ WHY PYTHON + FASTAPI + REACT

| Factor | Python | JavaScript |
|--------|--------|-----------|
| **AI Integration** | ⭐⭐⭐⭐⭐ Native Claude SDK | ⭐⭐⭐ Node.js slower |
| **Data Processing** | ⭐⭐⭐⭐⭐ Pandas/NumPy | ⭐⭐ Clunky |
| **Speed to Market** | 3-4 weeks | 5-6 weeks |
| **Recommendation Engine** | Easy (decision trees) | Complex |
| **Knowledge Base** | Perfect for embeddings | Awkward |
| **Team Productivity** | High | Medium |

**VERDICT: Python for backend (AI logic) + React for frontend (beautiful UI)**

---

# 📅 30-DAY SPRINT BREAKDOWN

## WEEK 1: Foundation (Hours 0-40)

### Day 1-2: Project Setup (8 hours)

**Morning (4 hours):**
1. Open Cursor IDE
2. Copy **PROMPT 1A** (Project Setup) from the comprehensive guide
3. Paste into Cursor Composer
4. Let Cursor generate complete file structure
5. Review generated files
6. Copy all files to your project folder

**Afternoon (4 hours):**
1. Copy **PROMPT 1B** (Architecture & API Design)
2. Get API spec and database schema
3. Review and understand the data model
4. Commit to git

**Git Commands:**
```bash
git init
git add .
git commit -m "feat: initial project structure"
```

### Day 3-4: Backend Setup (8 hours)

**Morning (4 hours):**
1. Copy **PROMPT 2A** (FastAPI Main App)
2. Get main.py, config.py, logging_config.py
3. Set up Python environment:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or: venv\Scripts\activate  # Windows
   ```
4. Create requirements.txt from prompt
5. Install: `pip install -r requirements.txt`

**Afternoon (4 hours):**
1. Copy **PROMPT 2B** (Database Setup)
2. Get SQLAlchemy models and database config
3. Install: `pip install sqlalchemy alembic psycopg2-binary`
4. Set up PostgreSQL (use Docker):
   ```bash
   docker-compose up -d postgres pgadmin
   ```
5. Run migrations (Alembic)
6. Test database connection

**Test Locally:**
```bash
cd backend
uvicorn app.main:app --reload
# Visit: http://localhost:8000/docs (Swagger UI)
```

### Day 5: Knowledge Base (8 hours)

**All Day:**
1. Copy **PROMPT 3A** (Knowledge Base)
2. Get JSON files with contraceptive methods and myths
3. Review content for accuracy (CRITICAL!)
4. Organize by language (en, sw, am, fr, so)
5. Create sample data for testing
6. Commit changes

**Files Created:**
- `data/knowledge_base/contraceptive_methods.json`
- `data/knowledge_base/common_myths.json`
- `data/knowledge_base/faqs.json`

### Day 6: Data Pipeline (8 hours)

**Morning (4 hours):**
1. Copy **PROMPT 3B** (Data Processing)
2. Get data cleaning scripts
3. Download APHRC dataset (or use sample)
4. Run data pipeline:
   ```bash
   python scripts/data_processing/run_pipeline.py
   ```
5. Review data quality report

**Afternoon (4 hours):**
1. Load knowledge base into database:
   ```bash
   python scripts/load_knowledge_base.py
   ```
2. Verify data in database
3. Create test queries
4. Commit

### Day 7: Claude API Setup (8 hours)

**All Day:**
1. Sign up for Anthropic Claude API
2. Get API key from console.anthropic.com
3. Copy **PROMPT 4A** (Claude Service)
4. Get claude_service.py and prompts.py
5. Test Claude API calls:
   ```bash
   python -c "from app.services.claude_service import ChatService; ChatService.test()"
   ```
6. Verify token counting works
7. Commit

**By End of Week 1:**
✅ Project structure complete
✅ Database running locally
✅ FastAPI server running
✅ Claude API working
✅ Knowledge base loaded

---

## WEEK 2: Core Features (Hours 40-80)

### Day 8-9: Recommendation Engine (8 hours)

**Morning (4 hours):**
1. Copy **PROMPT 4B** (Recommendation Engine)
2. Get recommendation_engine.py
3. Understand decision logic (5 steps)
4. Create test cases

**Afternoon (4 hours):**
1. Test recommendation engine:
   ```python
   # Test input
   user_profile = {
       "age": 28,
       "breastfeeding": False,
       "pregnancy_goals": "space_children",
       "health_conditions": [],
       "preferred_duration": "long_term"
   }
   recommendations = RecommendationEngine.recommend(user_profile)
   print(recommendations)
   ```
2. Verify output makes sense
3. Adjust scoring weights
4. Commit

### Day 10-11: API Endpoints (8 hours)

**Morning (4 hours):**
1. Copy **PROMPT 5A** (Chat Endpoints)
2. Get chat.py, chat_service.py
3. Implement `/api/chat` endpoint
4. Test with Swagger UI

**Afternoon (4 hours):**
1. Copy **PROMPT 5B** (Recommend & Myth Endpoints)
2. Get all endpoint implementations
3. Implement `/api/recommend`, `/api/myth-check`, `/api/faq`
4. Test all endpoints

**Quick Test:**
```bash
# Terminal 1
cd backend && uvicorn app.main:app --reload

# Terminal 2
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Is the pill safe while breastfeeding?","language":"en"}'
```

### Day 12: Testing (4 hours)

**All Day:**
1. Copy **PROMPT 8A** (Backend Testing)
2. Create test files
3. Run tests:
   ```bash
   pytest tests/ -v --cov=app
   ```
4. Aim for 80%+ coverage
5. Fix failing tests

### Day 13-14: Frontend Setup (8 hours)

**Morning (4 hours):**
1. Copy **PROMPT 6A** (React Setup)
2. Create React project:
   ```bash
   npm create vite@latest frontend -- --template react-ts
   cd frontend
   npm install
   ```
3. Copy Tailwind config from prompt
4. Install: `npm install tailwindcss postcss autoprefixer`
5. Set up routing and state management

**Afternoon (4 hours):**
1. Copy **PROMPT 6B** (Chat Component)
2. Create Chat.tsx, MessageList.tsx, InputBox.tsx
3. Create API service (api.ts)
4. Connect to backend
5. Test locally: `npm run dev`

**By End of Week 2:**
✅ All API endpoints working
✅ React app running locally
✅ Chat interface working with backend
✅ Backend tests passing (80%+ coverage)
✅ Recommendation engine tested

---

## WEEK 3: Polish & Integration (Hours 80-120)

### Day 15-16: Complete Frontend (8 hours)

**Morning (4 hours):**
1. Copy **PROMPT 6C** (Recommendation UI)
2. Create Survey.tsx, Recommendations.tsx
3. Create UI for recommendation flow
4. Add form validation

**Afternoon (4 hours):**
1. Create MythBuster component
2. Implement myth checking flow
3. Style with Tailwind
4. Test responsiveness (mobile-first)

### Day 17: Frontend Testing (4 hours)

**All Day:**
1. Copy **PROMPT 8B** (Frontend Testing)
2. Create component tests
3. Run: `npm run test`
4. Aim for 70%+ coverage

### Day 18-19: Deployment Setup (8 hours)

**Morning (4 hours):**
1. Copy **PROMPT 7A** (Docker & Deployment)
2. Create Dockerfile for backend
3. Test locally:
   ```bash
   docker build -t health-app-backend .
   docker run -p 8000:8000 health-app-backend
   ```

**Afternoon (4 hours):**
1. Create docker-compose.prod.yml
2. Set up GitHub Actions CI/CD pipeline
3. Create Vercel config for frontend
4. Test full deployment locally

### Day 20-21: Deploy to Production (8 hours)

**Morning (4 hours):**
1. Create Railway account (backend)
2. Deploy backend:
   - Connect GitHub repo
   - Set environment variables
   - Deploy
3. Verify backend is live

**Afternoon (4 hours):**
1. Create Vercel account (frontend)
2. Update frontend .env with live backend URL
3. Deploy frontend
4. Verify full app works
5. Test all features end-to-end

**By End of Week 3:**
✅ Full app deployed (live URL)
✅ Database running in production
✅ Claude API integrated
✅ All tests passing
✅ Ready for demo

---

## WEEK 4: Demo & Competition (Hours 120-160)

### Day 22-23: Demo Preparation (8 hours)

**Morning (4 hours):**
1. Record demo video (5-10 minutes):
   - Show chat interface
   - Ask a real question
   - Show recommendation flow
   - Show myth-busting
   - Highlight multilingual support
2. Edit video professionally
3. Upload to YouTube (unlisted)

**Afternoon (4 hours):**
1. Prepare pitch deck (5 slides):
   - Problem statement
   - Solution
   - Key features
   - Impact
   - Team
2. Practice presentation (3 minutes)

### Day 24-25: Final Polish (8 hours)

**Morning (4 hours):**
1. Copy **PROMPT 9A & 9B** (Documentation)
2. Create final documentation
3. Update README
4. Clean up code

**Afternoon (4 hours):**
1. Final testing
2. Check for bugs
3. Optimize performance
4. Final commit

### Day 26-27: Buffer & Troubleshooting (4 hours)

**If needed:**
- Fix any production issues
- Improve UI/UX based on feedback
- Optimize API response times
- Add missing features

### Day 28-30: COMPETITION! 🏆

**Day 28:** Presentation day
**Day 29-30:** Results & celebration

---

# 🎯 CRITICAL SUCCESS FACTORS

## Code Quality Checklist

- [ ] All endpoints tested
- [ ] Database migrations working
- [ ] Error handling on all endpoints
- [ ] Logging configured
- [ ] Rate limiting enabled
- [ ] CORS properly set
- [ ] Environment variables secure
- [ ] No API keys in code
- [ ] All tests passing
- [ ] 80%+ test coverage

## Health Info Accuracy Checklist

- [ ] Every contraceptive fact verified
- [ ] Sources cited (WHO, CDC, local health ministry)
- [ ] Medical disclaimer shown
- [ ] No unauthorized medical claims
- [ ] Reviewed by someone with health background
- [ ] Myths based on research
- [ ] Culturally sensitive content
- [ ] Multiple language translations checked

## UX Checklist

- [ ] Works on mobile (primary use case)
- [ ] Works with slow internet
- [ ] Clear, simple interface
- [ ] No jargon
- [ ] Accessible (WCAG compliance)
- [ ] Load time < 3 seconds
- [ ] No confusing navigation
- [ ] Professional appearance

## Competition Checklist

- [ ] Demo video professional quality
- [ ] Pitch deck compelling
- [ ] Team roles clear
- [ ] Impact metrics shown
- [ ] Live URL working
- [ ] App doesn't crash
- [ ] Features working as described
- [ ] Health info accurate

---

# 💰 BUDGET

**Hosting (30 days):**
- Railway (backend): $5-20
- Vercel (frontend): Free
- PostgreSQL: $5-15
- pgvector: Included

**APIs:**
- Claude API: ~$0.50 (light usage during competition)
- Custom domain: $10 (optional)

**TOTAL: ~$20-45 for competition**

---

# 🆘 TROUBLESHOOTING QUICK LINKS

| Issue | Solution |
|-------|----------|
| PostgreSQL won't connect | Check `docker-compose.yml`, run `docker-compose logs db` |
| Claude API errors | Check API key, verify credit, check rate limits |
| Frontend won't connect to backend | Check CORS config, verify backend URL in .env |
| Tests failing | Run `pytest -v` to see detailed errors, check mocks |
| Deployment fails | Check environment variables, review logs on Railway |
| Mobile layout broken | Use browser DevTools (F12), check Tailwind config |

---

# 📞 WHEN TO ASK FOR HELP

**Use Cursor Composer @Codebase for:**
- Code generation
- Bug fixes
- Performance optimization
- Architecture questions

**Use Claude directly for:**
- Explanations
- Best practices
- Design decisions
- Documentation

**Do NOT:**
- Hardcode API keys
- Store passwords in code
- Skip error handling
- Ignore security warnings
- Deploy without testing

---

# 🚀 GO TIME!

**Start with PROMPT 1A → PROMPT 1B → PROMPT 2A → ...**

Each prompt is designed to be:
- ✅ Standalone (works independently)
- ✅ Copy-paste ready
- ✅ Production quality
- ✅ Well-commented
- ✅ Tested

**YOU GOT THIS! 💪**

Questions? Each prompt has detailed explanations. Read first, then ask.

Good luck at the competition! 🏆
