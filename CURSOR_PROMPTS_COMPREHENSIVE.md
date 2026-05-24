# 🚀 REPRODUCTIVE HEALTH AI ASSISTANT - CURSOR IDE PROMPTS
## Senior Engineer's Complete Implementation Guide

---

## EXECUTIVE DECISION: Python vs JavaScript

### **RECOMMENDATION: Python + React Hybrid** ✅
**Why Python for backend:**
- ⚡ **Faster AI integration** - Claude SDK native, seamless API calls
- 📊 **Data processing** - Pandas/NumPy for APHRC dataset analysis
- 🧠 **Knowledge base management** - Vector embeddings, semantic search built-in
- 🔧 **ML/recommendation engine** - scikit-learn, decision trees trivial to build
- 🏃 **Competition deadline** - 3-4 weeks? Python is 2x faster for AI projects

**JavaScript limitations:**
- Node.js Claude SDK works but less mature
- Data processing clunkier (no NumPy equivalent)
- Vector DB integrations less smooth
- Recommendation logic more verbose

### **Tech Stack (Final):**
```
Backend:      Python 3.11 + FastAPI + Pydantic
Frontend:     React 18 + TypeScript + Tailwind CSS
Database:     PostgreSQL + pgvector extension
Vector DB:    Pinecone (free tier) or local embeddings
AI Engine:    Claude 3.5 Sonnet (Anthropic API)
Deployment:   Railway (backend) + Vercel (frontend)
```

---

# 📋 PHASE 1: PROJECT SETUP & ARCHITECTURE

## PROMPT 1A: Initialize Project Structure

**Paste this into Cursor Composer / @Codebase:**

```
You are a senior Python engineer. Create a complete, production-ready project structure 
for a reproductive health AI assistant (competition app).

PROJECT REQUIREMENTS:
- Backend: FastAPI (Python 3.11+)
- Frontend: React with TypeScript
- MVP deadline: 30 days
- Target: Sub-Saharan Africa (multilingual, low-bandwidth)
- Core feature: Contraceptive recommendation chatbot + myth buster

SPECIFIC REQUIREMENTS:
1. Create full directory structure (backend + frontend separated)
2. Include environment configuration (.env template)
3. Create comprehensive .gitignore
4. Set up Docker configuration for local testing
5. Include requirements.txt with ALL dependencies pinned to versions
6. Create comprehensive README.md with setup instructions
7. Include database schema (PostgreSQL + pgvector)
8. Create configuration files for both frontend and backend

DIRECTORY STRUCTURE MUST INCLUDE:
Backend:
  /backend
    /app
      /api (routes)
      /models (Pydantic schemas)
      /services (business logic)
      /utils (helpers)
      /db (database)
      /middleware (auth, logging)
      main.py
    /data
      /raw (APHRC dataset)
      /processed (cleaned)
      /knowledge_base (FAQs, guidelines)
    /tests
      test_api.py
      test_services.py
    requirements.txt
    .env.example
    docker-compose.yml

Frontend:
  /frontend
    /src
      /components (UI)
      /pages
      /services (API calls)
      /hooks (custom React hooks)
      /types (TypeScript types)
      /utils
      /assets
    package.json
    tsconfig.json
    .env.example

GENERATE:
- Complete folder structure with comments
- Sample __init__.py files
- requirements.txt with exact versions
- .env.example showing all needed variables
- docker-compose.yml for local PostgreSQL + pgvector
- tsconfig.json optimized for production
- package.json with all scripts (dev, build, test)

OUTPUT: Create all files with proper structure. Include helpful comments in each file.
```

---

## PROMPT 1B: Architecture & API Design

**Paste into Cursor:**

```
As a senior architect, design the complete API structure for this reproductive health AI app.

CONTEXT:
- Single-page app (SPA) with React frontend
- Python FastAPI backend
- Supports multiple African languages (Swahili, Amharic, French, English)
- Core features: contraceptive chatbot + recommendations + myth-busting
- Must work on low-bandwidth connections

DESIGN REQUIREMENTS:
1. Create a comprehensive OpenAPI/Swagger spec showing all endpoints
2. Design REST API endpoints (not GraphQL - simpler for competition)
3. Include request/response schemas for each endpoint
4. Plan database models (SQLAlchemy ORM)
5. Design middleware stack (CORS, logging, error handling, auth)

API ENDPOINTS NEEDED:
├── POST /api/chat
│   ├── Input: {"message": "string", "user_id": "uuid", "language": "string"}
│   ├── Output: {"response": "string", "sources": ["urls"], "confidence": float}
│
├── POST /api/recommend
│   ├── Input: {"age": int, "breastfeeding": bool, "health_conditions": [...], "language": "string"}
│   ├── Output: {"recommendations": [{"method": "string", "match_score": float, "details": "string"}]}
│
├── GET /api/contraceptives
│   ├── Returns list of all contraceptive methods with details
│
├── POST /api/myth-check
│   ├── Input: {"statement": "string", "language": "string"}
│   ├── Output: {"is_myth": bool, "fact": "string", "evidence": "string", "sources": ["urls"]}
│
├── POST /api/faq
│   ├── Input: {"query": "string", "language": "string"}
│   ├── Output: {"answer": "string", "related_topics": [...], "sources": [...]}
│
├── GET /api/health
│   ├── Basic health check endpoint
│
└── POST /api/feedback
    ├── Input: {"message_id": "uuid", "rating": 1-5, "feedback": "string"}
    ├── Returns: {"status": "success"}

DATABASE MODELS:
1. User (id, created_at, language_preference, session_history)
2. ChatMessage (id, user_id, message, response, language, timestamp)
3. ContraceptiveMethod (id, name, description, effectiveness, side_effects, duration)
4. KnowledgeBase (id, category, content, source, embedding_vector, language)
5. Myth (id, myth_text, fact_text, evidence, sources, language)

GENERATE:
- Pydantic schemas for all requests/responses
- SQLAlchemy models for all database tables
- FastAPI route structure (separate routers for each feature)
- CORS, logging, error handling middleware
- Database connection pool configuration
- Session management strategy

DETAILS: Include type hints, docstrings, and production-ready error handling.
```

---

# 📊 PHASE 2: BACKEND SETUP - FASTAPI & DATABASE

## PROMPT 2A: Create FastAPI Main Application

**Paste into Cursor:**

```
You are a senior backend engineer. Create a production-ready FastAPI application structure.

REQUIREMENTS:
1. Create main.py with complete FastAPI application initialization
2. Include all middleware (CORS, logging, error handling, request validation)
3. Add comprehensive logging setup (structured JSON logs for production)
4. Include graceful shutdown handlers
5. Create startup/shutdown event handlers
6. Add request/response logging middleware
7. Create custom exception handlers
8. Add API versioning support

SPECIFIC REQUIREMENTS:
- Support CORS for React frontend (configurable by environment)
- Log all requests/responses (include user_id, language, response_time)
- Handle errors gracefully with proper HTTP status codes
- Support request ID tracking for debugging
- Include health check endpoint
- Create lifespan context manager for database connection management
- Add rate limiting placeholder (ready for production)

STRUCTURE:
app/
  __init__.py (export FastAPI instance)
  main.py (FastAPI initialization)
  config.py (environment config using Pydantic)
  logging_config.py (JSON logging setup)
  middleware/
    __init__.py
    logging.py (request/response logging)
    error_handler.py (global exception handling)
    cors.py (CORS configuration)

GENERATE:
1. main.py - Complete FastAPI app with middleware stack
2. config.py - Pydantic BaseSettings with environment variables
3. logging_config.py - Structured JSON logging configuration
4. middleware/logging.py - Request/response logging middleware
5. middleware/error_handler.py - Custom exception handlers
6. docker-compose.yml - PostgreSQL + pgvector for local development
7. sample .env.local file

INCLUDE:
- Type hints throughout
- Docstrings for all functions
- Production-ready error messages (no sensitive info in 500 errors)
- Request ID for correlation logging
- Response time tracking
- Proper HTTP status codes
```

---

## PROMPT 2B: Database Setup with SQLAlchemy & Alembic

**Paste into Cursor:**

```
You are a senior database engineer. Set up production-ready database layer.

CONTEXT:
- PostgreSQL 15+ with pgvector extension (for AI embeddings)
- Using SQLAlchemy ORM with async support
- Migration management with Alembic
- Connection pooling optimized for FastAPI

REQUIREMENTS:
1. Create SQLAlchemy base configuration
2. Create all database models (User, ChatMessage, ContraceptiveMethod, KnowledgeBase, Myth)
3. Set up async database session management
4. Initialize Alembic for migrations
5. Create database initialization script
6. Add connection pooling configuration
7. Include soft delete support (for compliance)

DATABASE MODELS NEEDED:

User:
  - id (UUID, primary key)
  - language (string: en, sw, am, fr, so)
  - created_at (timestamp)
  - last_active_at (timestamp)
  - deleted_at (soft delete)

ChatMessage:
  - id (UUID)
  - user_id (FK to User)
  - message_text (string, stored in original language)
  - ai_response (text, multilingual)
  - language_detected (string)
  - tokens_used (int, for API cost tracking)
  - response_quality_score (float, 0-1, from user feedback)
  - created_at (timestamp)
  - embedding_vector (pgvector, 1536 dims)

ContraceptiveMethod:
  - id (UUID)
  - name (string)
  - description (text, multilingual)
  - effectiveness_percentage (float)
  - duration (string: "permanent", "5-years", "3-months")
  - side_effects (JSONB array)
  - contraindications (JSONB array)
  - cost_level (string: low/medium/high)
  - accessibility (string: available_ota, prescription_needed)
  - embedding_vector (pgvector)
  - created_at (timestamp)

KnowledgeBase:
  - id (UUID)
  - category (string: faq, guideline, research, myth)
  - content (text, multilingual)
  - source_url (string)
  - source_authority (string: WHO, CDC, local_ministry)
  - language (string)
  - embedding_vector (pgvector)
  - verified_by (string, who verified this)
  - created_at (timestamp)

Myth:
  - id (UUID)
  - myth_text (text, original language)
  - fact_text (text, multilingual correction)
  - evidence (text, detailed explanation with sources)
  - sources (JSONB array of URLs)
  - severity (string: high, medium, low - based on health impact)
  - language (string)
  - embedding_vector (pgvector)
  - created_at (timestamp)

UserFeedback:
  - id (UUID)
  - user_id (FK to User)
  - message_id (FK to ChatMessage)
  - rating (int: 1-5)
  - feedback_text (text)
  - created_at (timestamp)

GENERATE:
1. app/db/base.py - SQLAlchemy declarative base
2. app/db/models.py - All database models with relationships
3. app/db/session.py - Async session factory and dependency injection
4. app/db/database.py - Database connection pool setup
5. app/db/init_db.py - Database initialization script
6. migrations/env.py - Alembic environment configuration
7. migrations/versions/001_initial_schema.py - Initial migration

INCLUDE:
- Proper indexes on frequently queried columns
- Foreign key relationships with cascade rules
- Indexes on embedding vectors for similarity search
- Soft delete support (deleted_at timestamp)
- Timestamp tracking (created_at, updated_at)
- JSONB for flexible schema (side effects, sources)
- Proper nullable constraints
- Production-grade comments explaining schema decisions

SPECIAL: Include pgvector configuration for semantic search of embeddings
```

---

# 🧠 PHASE 3: KNOWLEDGE BASE & DATA PIPELINE

## PROMPT 3A: Build Knowledge Base System

**Paste into Cursor:**

```
You are a senior data engineer. Create the knowledge base system for reproductive health info.

REQUIREMENTS:
1. Create structured knowledge base for contraceptive information
2. Build fact verification system with sources
3. Create myth detection and correction database
4. Set up multilingual support (English, Swahili, Amharic, French, Somali)
5. Create data loading pipeline from structured files
6. Generate embeddings for semantic search

KNOWLEDGE BASE STRUCTURE:

data/knowledge_base/
  contraceptive_methods.json
  faqs_by_category.json
  common_myths.json
  guidelines_references.json
  translations.json

CONTRACEPTIVE_METHODS.JSON FORMAT:
{
  "methods": [
    {
      "id": "implant",
      "names": {
        "en": "Contraceptive Implant",
        "sw": "Kipunguza Ufike",
        "am": "የእንጀራ መከላከያ",
        "fr": "Implant Contraceptif"
      },
      "effectiveness": 99.9,
      "duration": "3-5 years",
      "reversible": true,
      "side_effects": {
        "common": [
          {"en": "Irregular bleeding", "sw": "Kufa kwa njia isiyofanana", ...},
          ...
        ],
        "serious": [...]
      },
      "contraindications": ["pregnancy", "breast_cancer_history"],
      "accessibility": "clinic_only",
      "cost": "low",
      "best_for": ["breastfeeding_mothers", "long_term_spacing"],
      "sources": [
        "WHO_2022_contraceptive_methods",
        "CDC_guidelines"
      ]
    },
    ...
  ]
}

COMMON_MYTHS.JSON FORMAT:
{
  "myths": [
    {
      "id": "myth_001",
      "myth": {
        "en": "Family planning causes infertility",
        "sw": "Kupanga familia husababisha kutokuwa na watoto",
        ...
      },
      "fact": {
        "en": "Family planning is reversible. Fertility returns within 1-3 months of stopping.",
        ...
      },
      "evidence": "Detailed scientific explanation",
      "severity": "high",
      "sources": ["WHO_2020_fertility_study", "UNICEF_report"],
      "counter_arguments": [
        "Implants are removed instantly with full fertility return",
        "Pills stop working immediately when discontinued"
      ]
    }
  ]
}

GENERATE:
1. data/knowledge_base/contraceptive_methods.json - Complete methods database
2. data/knowledge_base/common_myths.json - 20+ myths with corrections
3. data/knowledge_base/faqs.json - 50+ FAQs organized by category
4. app/services/knowledge_base.py - Service to load and query knowledge base
5. app/utils/embeddings.py - Generate embeddings for semantic search
6. app/services/data_loader.py - Load JSON files into database
7. scripts/load_knowledge_base.py - Script to populate database

SPECIFIC CONTENT:
- Contraceptive methods: implant, IUD, pill, injectable, condom, emergency
- Include 20+ common myths specific to Sub-Saharan Africa
- FAQs by category: breastfeeding, side effects, effectiveness, privacy, cost
- Include multilingual translations for all content
- Add WHO and CDC sources for credibility

INCLUDE:
- Structured JSON files ready to parse
- Data validation schema (Pydantic)
- Error handling for missing translations
- Logging of loaded data
- Database population script with error recovery
- Embedding generation using Claude embeddings API

CRITICAL: Ensure all health information is evidence-based and sourced
```

---

## PROMPT 3B: Data Processing Pipeline

**Paste into Cursor:**

```
You are a senior data engineer. Build the APHRC dataset processing pipeline.

CONTEXT:
- APHRC (African Population & Health Research Center) dataset with reproductive health data
- Need to extract contraceptive usage patterns, switching behavior, demographics
- Will inform recommendation algorithm
- Must handle missing values, outliers, and data quality issues

REQUIREMENTS:
1. Create data cleaning pipeline (remove duplicates, handle missing values)
2. Extract feature engineering (age groups, regions, usage patterns)
3. Generate summary statistics for recommendations
4. Create data quality reports
5. Export clean dataset for use in recommendation engine

PROCESSING PIPELINE STEPS:

Step 1: Data Loading
  - Load APHRC CSV/Excel files
  - Validate schema and columns
  - Handle encoding issues
  - Log data shape and missing values

Step 2: Data Cleaning
  - Remove exact duplicates
  - Handle missing values (strategy: drop if >40% missing, forward fill if <10%)
  - Standardize column names (lowercase, snake_case)
  - Fix data type mismatches
  - Outlier detection (age >60, impossible values)

Step 3: Feature Engineering
  - Create age groups (15-19, 20-24, 25-34, 35-49)
  - Create region categories (East, West, Central, Southern Africa)
  - Extract contraceptive method categories
  - Create reason_for_switching categories
  - Create discontinuation reason categories

Step 4: Exploratory Analysis
  - Most used contraceptive methods (show %)
  - Discontinuation rates by method
  - Switching patterns (method A → method B)
  - Regional variations
  - Age-based preferences
  - Reasons for non-use

Step 5: Generate Summary Statistics
  - Aggregated by region, age group, method
  - Use these in recommendation algorithm

GENERATE:
1. scripts/data_processing/load_data.py - Load APHRC dataset
2. scripts/data_processing/clean_data.py - Data cleaning pipeline
3. scripts/data_processing/feature_engineering.py - Feature creation
4. scripts/data_processing/exploratory_analysis.py - EDA and statistics
5. scripts/data_processing/generate_insights.py - Create insights for recommendations
6. scripts/data_processing/run_pipeline.py - Orchestrate entire pipeline
7. data/processed/contraceptive_stats.json - Summary statistics for recommendations
8. data/processed/data_quality_report.html - HTML report of data quality

INCLUDE:
- Pandas dataframe operations
- Error handling and logging
- Data validation checks
- Summary statistics export as JSON
- Visualization code (matplotlib) for EDA
- CSV exports of cleaned data
- Comments explaining each transformation

OUTPUT: Create production-ready scripts with logging, error handling, and documentation
```

---

# 🤖 PHASE 4: AI ENGINE - CLAUDE API INTEGRATION

## PROMPT 4A: Claude API Service Layer

**Paste into Cursor:**

```
You are a senior AI/ML engineer. Create the Claude API service layer for the app.

CONTEXT:
- Using Anthropic Claude 3.5 Sonnet model
- Building system prompts for reproductive health expert
- Multi-language support (English, Swahili, Amharic, French, Somali)
- Must prevent hallucinations and ensure factual accuracy
- Need to track token usage for cost monitoring

REQUIREMENTS:
1. Create Claude API wrapper service
2. Build system prompts for different use cases (chatbot, recommender, myth-buster)
3. Implement safety guardrails and fact-checking
4. Add token tracking and cost monitoring
5. Create prompt templates for consistent behavior
6. Implement retry logic with exponential backoff
7. Add streaming response support for better UX

SYSTEM PROMPTS NEEDED:

PROMPT 1: Contraceptive Chatbot
  - Expert reproductive health advisor
  - Answers Q&A about contraceptive methods
  - Emphasizes: accurate info, privacy, no judgment
  - Includes: "I'm not a doctor" disclaimer
  - Must cite sources
  - Handles multiple languages

PROMPT 2: Myth Buster
  - Detects common myths/misconceptions
  - Provides evidence-based corrections
  - Includes scientific sources
  - Emphasizes cultural sensitivity
  - Avoids dismissive tone

PROMPT 3: Recommendation Assistant
  - Asks clarifying questions (age, pregnancy goals, medical conditions)
  - Recommends contraceptive methods based on user profile
  - Explains why each method fits
  - Includes effectiveness, duration, side effects
  - Emphasizes: discuss with healthcare provider

PROMPT 4: FAQ Answerer
  - Answers specific health questions
  - Provides detailed explanations
  - Includes relevant contraceptive info
  - Cites sources
  - Handles sensitive questions with care

GENERATE:
1. app/services/claude_service.py - Main Claude API wrapper
2. app/services/prompts.py - System prompts and templates
3. app/models/claude_models.py - Request/response models for Claude
4. app/services/token_tracker.py - Track token usage and costs
5. app/utils/safety_filters.py - Fact-checking and safety guardrails
6. app/services/response_formatter.py - Format Claude responses

SPECIFIC IMPLEMENTATION:
- Use Claude 3.5 Sonnet (best speed/quality for competition)
- Implement streaming for chat responses
- Add token counting (anthropic.messages.count_tokens)
- Create retry logic with exponential backoff (3 retries max)
- Add response caching for common questions (Redis)
- Log all API calls with user_id, tokens, response_time
- Implement cost tracking (tokens × rate)

SAFETY MEASURES:
- Parse response to check for disclaimer
- Verify response length (max 2000 chars for mobile)
- Check for forbidden medical claims
- Validate response addresses actual user question
- Filter out speculative information

INCLUDE:
- Type hints for all functions
- Comprehensive docstrings
- Error handling with proper logging
- Cost calculation and logging
- Token count validation
- Request/response validation
- Performance metrics (response time)

IMPORTANT: Build system prompts that are detailed enough to prevent hallucinations 
but not so long that they eat token budget. Include knowledge base references in prompts.
```

---

## PROMPT 4B: Recommendation Engine

**Paste into Cursor:**

```
You are a senior ML engineer. Build the contraceptive recommendation engine.

REQUIREMENTS:
1. Create decision tree-based recommendation algorithm
2. Handle user input (age, breastfeeding, health conditions, etc.)
3. Rank contraceptive methods by fit
4. Provide detailed reasoning for each recommendation
5. Incorporate APHRC dataset insights
6. Support personalization based on user preferences

ALGORITHM DESIGN:

INPUT PARAMETERS:
- age (int: 15-49)
- breastfeeding (bool)
- months_postpartum (int: 0-24)
- pregnancy_goals (string: space_children, prevent_pregnancy, flexible)
- health_conditions (list: anemia, hypertension, diabetes, etc.)
- side_effect_tolerance (list: bleeding_ok, hormones_preferred, etc.)
- preferred_duration (string: short_term, medium, long_term, permanent)
- cost_sensitive (bool)
- privacy_needed (bool)

DECISION LOGIC:

STEP 1: Filter by Safety
  - Remove contraindicated methods (e.g., avoid combined hormones if hypertension)
  - Remove methods unsafe during breastfeeding if applicable

STEP 2: Filter by Duration Preference
  - Short-term (weeks-months): pills, condoms, injectables
  - Medium (months-years): implants, IUD
  - Long-term (years): IUD, implants
  - Permanent: sterilization

STEP 3: Score by Fit
  For each remaining method, calculate score (0-100):
    - Effectiveness fit (does it match goals?): 0-30 points
    - Side effect alignment (tolerance match): 0-20 points
    - Ease of use: 0-15 points
    - Accessibility in region: 0-20 points
    - Cost alignment: 0-15 points

STEP 4: Incorporate APHRC Insights
  - Show popularity in user's region
  - Show discontinuation rates
  - Show common reasons for switching from this method

STEP 5: Rank & Return
  - Top 3 recommendations sorted by score
  - Include explanation for each

EXAMPLE OUTPUT:
{
  "recommendations": [
    {
      "rank": 1,
      "method": "Contraceptive Implant",
      "match_score": 92,
      "key_reasons": [
        "99.9% effective (exceeds your spacing goals)",
        "Safe while breastfeeding",
        "Works for 3-5 years (long-term spacing)",
        "Available at clinic near you"
      ],
      "side_effects": "Some irregular bleeding (usually improves)",
      "next_steps": "Visit clinic, discuss with provider",
      "popularity_in_region": "Used by 35% of women in your area"
    },
    ...
  ]
}

GENERATE:
1. app/services/recommendation_engine.py - Main recommendation logic
2. app/models/recommendation_models.py - Input/output schemas
3. app/utils/scoring_logic.py - Scoring functions
4. app/utils/safety_filters.py - Contraindication checking
5. data/processed/recommendation_rules.json - Decision rules as JSON
6. tests/test_recommendation_engine.py - Unit tests

INCLUDE:
- Type hints throughout
- Comprehensive logging
- Unit tests for each decision point
- Edge case handling
- Regional customization (different data by region)
- Performance optimization (execute in <500ms)
- Caching of calculated scores

SPECIAL: Make it explainable (why this recommendation?) for user trust
```

---

# 💬 PHASE 5: API ENDPOINTS - IMPLEMENT ALL ROUTES

## PROMPT 5A: Chat & Chatbot Endpoints

**Paste into Cursor:**

```
You are a senior backend engineer. Implement the chat API endpoints.

REQUIREMENTS:
1. Create POST /api/chat endpoint for conversational AI
2. Create POST /api/chat/stream for streaming responses
3. Create GET /api/chat/history for conversation history
4. Add message validation and filtering
5. Track conversation context across messages
6. Support all languages with detection
7. Generate embeddings for conversation analysis

ENDPOINT SPECIFICATIONS:

POST /api/chat
Request:
{
  "message": "Can I use contraceptive pills while breastfeeding?",
  "user_id": "uuid (optional, for returning users)",
  "language": "en|sw|am|fr|so (auto-detect if missing)",
  "context": {
    "age": 25,
    "breastfeeding": true
  }
}

Response (200 OK):
{
  "response_id": "uuid",
  "message": "AI response here with sources",
  "sources": ["WHO_2022_guidelines", "CDC_resources"],
  "confidence": 0.95,
  "follow_up_suggestions": [
    "Tell me about side effects",
    "Which is most effective?"
  ],
  "tokens_used": 245,
  "language_detected": "en"
}

Error Responses:
- 400: Invalid input
- 429: Rate limit exceeded
- 500: Server error

GET /api/chat/history
Query params:
  ?user_id=uuid
  ?limit=10
  ?offset=0

Response:
{
  "messages": [
    {
      "message_id": "uuid",
      "user_message": "...",
      "ai_response": "...",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "total_count": 25
}

GENERATE:
1. app/api/routes/chat.py - Chat endpoints
2. app/api/routes/chat_stream.py - Streaming endpoints
3. app/services/chat_service.py - Business logic
4. app/models/chat_models.py - Request/response schemas
5. app/utils/language_detection.py - Auto-detect language

INCLUDE:
- Input validation (message length, user_id format)
- Rate limiting (10 requests per minute per user)
- Session management
- Conversation context tracking
- Error handling
- Logging (message, response, tokens)
- Response caching for common questions
- Streaming support for real-time responses

SPECIAL REQUIREMENTS:
- Support conversation context (remember previous messages)
- Auto-detect language from message
- Translate responses if needed
- Track conversation quality (user ratings)
- Handle timeout gracefully (show status message)
```

---

## PROMPT 5B: Recommendation & Myth-Busting Endpoints

**Paste into Cursor:**

```
You are a senior backend engineer. Implement recommendation and myth-busting endpoints.

ENDPOINTS TO CREATE:

1. POST /api/recommend
Input:
{
  "user_id": "uuid (optional)",
  "age": 28,
  "breastfeeding": false,
  "months_postpartum": 0,
  "pregnancy_goals": "space_children",
  "health_conditions": [""],
  "side_effect_tolerance": ["minimal_bleeding"],
  "preferred_duration": "long_term",
  "region": "Kenya",
  "language": "sw"
}

Response (200 OK):
{
  "recommendations": [
    {
      "method": "Contraceptive Implant",
      "match_score": 92,
      "effectiveness": "99.9%",
      "duration": "3-5 years",
      "side_effects": "Irregular bleeding",
      "accessibility": "clinic_only",
      "cost": "low",
      "why_recommended": ["High effectiveness", "Long-term", "..."],
      "regional_popularity": "Used by 35% in your area",
      "provider_near_you": true,
      "learn_more_url": "/details/implant"
    }
  ],
  "survey_questions_answered": 6
}

2. POST /api/myth-check
Input:
{
  "statement": "Contraceptive pills make you infertile",
  "language": "en"
}

Response (200 OK):
{
  "is_myth": true,
  "severity": "high",
  "myth": "Contraceptive pills make you infertile",
  "fact": "Pills are reversible - fertility returns within 1-3 months",
  "evidence": "Multiple studies show immediate fertility return...",
  "sources": ["WHO_2022", "CDC_2023"],
  "similar_myths": ["Implants cause infertility", "...]
}

3. POST /api/faq
Input:
{
  "question": "Is it safe to use contraception while breastfeeding?",
  "language": "en",
  "category": "breastfeeding" (optional)
}

Response (200 OK):
{
  "question": "...",
  "answer": "...",
  "related_faqs": ["...", "..."],
  "sources": ["...", "..."],
  "find_clinic": "Click here to find clinic near you"
}

4. GET /api/contraceptives
Query params:
  ?language=en
  ?region=Kenya
  ?category=long_term

Response (200 OK):
{
  "methods": [
    {
      "id": "implant",
      "name": "Contraceptive Implant",
      "description": "...",
      "effectiveness": 99.9,
      "duration": "3-5 years",
      "side_effects": [...],
      "accessibility": "clinic_only"
    }
  ]
}

GENERATE:
1. app/api/routes/recommend.py - Recommendation endpoint
2. app/api/routes/myth_check.py - Myth-busting endpoint
3. app/api/routes/faq.py - FAQ endpoint
4. app/api/routes/contraceptives.py - Methods listing endpoint
5. app/services/recommend_service.py - Recommendation logic
6. app/services/myth_service.py - Myth detection
7. app/models/recommend_models.py - Request/response schemas
8. app/models/myth_models.py - Myth schemas

INCLUDE:
- Input validation with detailed error messages
- Paging support for large result sets
- Filtering and sorting
- Localization (translate to user's language)
- Regional customization
- Logging and error handling
- Response caching (Redis)
- Performance optimization (<500ms)

SPECIAL: Ensure myth detection is very accurate (no false positives)
```

---

# ⚛️ PHASE 6: FRONTEND - REACT APP

## PROMPT 6A: React Project Setup & Core Components

**Paste into Cursor:**

```
You are a senior frontend engineer. Create production-ready React application.

REQUIREMENTS:
1. Initialize React 18 + TypeScript project
2. Set up Vite as build tool (faster than Create React App)
3. Create core layout components
4. Set up routing with React Router v6
5. Create API client with axios
6. Set up state management (Zustand - lighter than Redux)
7. Style with Tailwind CSS
8. Add form validation (React Hook Form + Zod)

PROJECT STRUCTURE:
frontend/
  ├── src/
  │   ├── components/
  │   │   ├── Layout/
  │   │   │   ├── Header.tsx
  │   │   │   ├── Sidebar.tsx
  │   │   │   └── Layout.tsx
  │   │   ├── Chat/
  │   │   │   ├── ChatBox.tsx
  │   │   │   ├── MessageList.tsx
  │   │   │   ├── InputBox.tsx
  │   │   │   └── Chat.tsx
  │   │   ├── Recommendation/
  │   │   │   ├── Survey.tsx
  │   │   │   ├── RecommendationCard.tsx
  │   │   │   └── Recommendations.tsx
  │   │   ├── MythBuster/
  │   │   │   ├── MythInput.tsx
  │   │   │   ├── MythResult.tsx
  │   │   │   └── MythBuster.tsx
  │   │   ├── Common/
  │   │   │   ├── Button.tsx
  │   │   │   ├── Card.tsx
  │   │   │   ├── Loading.tsx
  │   │   │   └── ErrorMessage.tsx
  │   ├── pages/
  │   │   ├── Home.tsx
  │   │   ├── Chat.tsx
  │   │   ├── Recommend.tsx
  │   │   ├── MythBuster.tsx
  │   │   ├── About.tsx
  │   │   └── NotFound.tsx
  │   ├── services/
  │   │   ├── api.ts (axios instance)
  │   │   ├── chatService.ts
  │   │   ├── recommendService.ts
  │   │   └── mythService.ts
  │   ├── store/
  │   │   └── useAppStore.ts (Zustand)
  │   ├── types/
  │   │   ├── chat.ts
  │   │   ├── recommendation.ts
  │   │   └── common.ts
  │   ├── utils/
  │   │   ├── languageDetect.ts
  │   │   ├── formatDate.ts
  │   │   └── validation.ts
  │   ├── App.tsx
  │   ├── main.tsx
  │   └── index.css
  ├── public/
  ├── vite.config.ts
  ├── tsconfig.json
  ├── tailwind.config.js
  ├── postcss.config.js
  └── package.json

GENERATE:
1. Complete vite.config.ts
2. tsconfig.json optimized for production
3. tailwind.config.js with custom colors
4. package.json with all dependencies
5. src/App.tsx with routing setup
6. src/components/Layout/Layout.tsx
7. src/services/api.ts (axios instance)
8. src/store/useAppStore.ts (Zustand state)
9. src/types/ - all TypeScript types
10. src/index.css (Tailwind imports)

INCLUDE:
- TypeScript strict mode
- Environment variable setup
- API interceptors (auth headers, error handling)
- Global error handling
- Loading states
- Responsive design (mobile-first)
- Dark mode support (Tailwind)
- Accessibility (ARIA labels)

CRITICAL: Make it work offline or with minimal bandwidth (PWA support)
```

---

## PROMPT 6B: Chat Interface Component

**Paste into Cursor:**

```
You are a senior React engineer. Create the chat interface component.

REQUIREMENTS:
1. Create ChatBox component with message display
2. Implement real-time message streaming
3. Add typing indicator
4. Support message history
5. Add language selector
6. Implement rate limiting UI
7. Add accessibility features

COMPONENT STRUCTURE:

ChatBox.tsx
├── Header (language selector, clear history)
├── MessageList
│   ├── Message (user)
│   ├── Message (AI with sources)
│   └── TypingIndicator
├── InputBox
│   ├── TextInput with multiline
│   ├── Send button
│   └── Character counter
└── Footer (token usage, disclaimer)

FEATURES:
- Display user and AI messages with different styling
- Show sources as clickable links
- Streaming responses (word by word)
- Typing indicator while AI responds
- Message history pagination
- Clear conversation button
- Language selector (en, sw, am, fr, so)
- Copy message to clipboard
- Rate message quality (thumbs up/down)
- Show token usage and estimated cost

GENERATE:
1. src/components/Chat/ChatBox.tsx
2. src/components/Chat/MessageList.tsx
3. src/components/Chat/Message.tsx
4. src/components/Chat/InputBox.tsx
5. src/components/Chat/TypingIndicator.tsx
6. src/services/chatService.ts
7. src/hooks/useChat.ts (custom hook)
8. src/types/chat.ts

INCLUDE:
- TypeScript types for all data
- Error boundaries
- Loading states
- Error messages
- Accessibility (focus management, ARIA)
- Responsive design (mobile, tablet, desktop)
- Keyboard shortcuts (Enter to send, Esc to clear)
- Auto-scroll to latest message

STYLING:
- Use Tailwind CSS
- Mobile-first responsive design
- Dark mode support
- Professional, health-app aesthetic
- Good contrast for readability
```

---

## PROMPT 6C: Recommendation Engine UI

**Paste into Cursor:**

```
You are a senior React engineer. Create the recommendation survey and results UI.

REQUIREMENTS:
1. Create survey form for user profile
2. Implement step-by-step wizard UI
3. Show recommendation results with comparison
4. Add details/learn more for each method
5. Include provider locator
6. Add print/share recommendations

SURVEY STEPS:
1. Age selection
2. Pregnancy goals (space children, prevent, flexible)
3. Health conditions (checkboxes)
4. Side effect tolerance
5. Preferred duration
6. Region/location

RECOMMENDATION CARD SHOULD SHOW:
- Method name & icon
- Match score (0-100)
- Effectiveness percentage
- Duration
- Key benefits
- Possible side effects
- Accessibility
- Regional popularity
- "Learn more" link
- "Find clinic" button

GENERATE:
1. src/components/Recommendation/Survey.tsx (wizard form)
2. src/components/Recommendation/SurveyStep.tsx (reusable step)
3. src/components/Recommendation/Recommendations.tsx (results page)
4. src/components/Recommendation/RecommendationCard.tsx
5. src/components/Recommendation/MethodDetails.tsx (modal)
6. src/pages/Recommend.tsx
7. src/services/recommendService.ts
8. src/hooks/useRecommendation.ts

INCLUDE:
- Form validation (required fields)
- Progress bar showing survey completion
- Previous/Next navigation
- Results sorting/filtering
- Comparison mode (compare 2-3 methods side-by-side)
- Print recommendations button
- Share via WhatsApp/email
- Save recommendations to device

STYLING:
- Wizard UI with progress indicator
- Color-coded match scores (red/yellow/green)
- Icons for each contraceptive method
- Professional health app aesthetic
- Mobile responsive
```

---

# 🚀 PHASE 7: DEPLOYMENT & PRODUCTION

## PROMPT 7A: Docker & Deployment Configuration

**Paste into Cursor:**

```
You are a senior DevOps engineer. Create production-ready deployment configuration.

REQUIREMENTS:
1. Create Docker images for backend (Python/FastAPI)
2. Create Docker Compose for local development
3. Create GitHub Actions CI/CD pipeline
4. Prepare deployment to Railway (backend) and Vercel (frontend)
5. Set up environment-based configuration
6. Add health checks and monitoring

GENERATE:
1. backend/Dockerfile - Multi-stage build for Python app
2. backend/.dockerignore
3. docker-compose.yml - Local development setup
4. docker-compose.prod.yml - Production setup
5. .github/workflows/ci-cd.yml - GitHub Actions pipeline
6. Deployment guide (README)
7. Environment configuration examples

DOCKERFILE SHOULD:
- Use Python 3.11 slim image
- Install requirements in separate layer
- Run as non-root user
- Include health check
- Expose port 8000
- Support both development and production

CI/CD PIPELINE SHOULD:
- Run tests on every push
- Build and push Docker image
- Deploy to Railway on main branch
- Run linting and type checks
- Generate coverage reports

INCLUDE:
- Security best practices (no secrets in image)
- Optimized layer caching
- Health check endpoints
- Resource limits
- Proper logging
```

---

## PROMPT 7B: Production Deployment Checklist

**Paste into Cursor:**

```
As a senior engineer, create a comprehensive production deployment checklist and guide.

DEPLOYMENT CHECKLIST:

PRE-DEPLOYMENT:
☐ All tests passing (unit, integration)
☐ Code review completed
☐ Dependencies updated and compatible
☐ Environment variables configured
☐ Database migrations tested
☐ API documentation updated
☐ Rate limiting configured
☐ Error handling tested
☐ Logging configured
☐ Security scan passed

DATABASE SETUP:
☐ PostgreSQL with pgvector installed
☐ Database migrations run
☐ Knowledge base loaded
☐ Indexes created
☐ Backups configured
☐ Connection pooling tuned

BACKEND DEPLOYMENT (Railway):
☐ Dockerfile builds successfully
☐ Environment variables set in Railway
☐ Database URL configured
☐ Claude API key configured
☐ Health check endpoint responds
☐ Logs accessible
☐ Monitoring alerts set

FRONTEND DEPLOYMENT (Vercel):
☐ Build succeeds
☐ Environment variables set
☐ API endpoint URL configured
☐ PWA manifest configured
☐ Analytics configured
☐ Error tracking configured

SECURITY CHECKLIST:
☐ CORS properly configured
☐ Rate limiting enabled
☐ Input validation on all endpoints
☐ No sensitive data in logs
☐ API keys not exposed
☐ HTTPS enforced
☐ Database encryption enabled
☐ Backups encrypted
☐ Access logs monitored

MONITORING & ALERTS:
☐ Error tracking (Sentry)
☐ Performance monitoring
☐ API latency alerts
☐ Error rate alerts
☐ Cost tracking (Claude API)
☐ Database performance alerts
☐ Uptime monitoring

GENERATE:
1. DEPLOYMENT_GUIDE.md - Step-by-step deployment guide
2. PRODUCTION_CHECKLIST.md - Pre-deployment checklist
3. MONITORING_SETUP.md - How to set up monitoring
4. TROUBLESHOOTING.md - Common issues and solutions
5. SCALING_GUIDE.md - How to scale as users grow

INCLUDE:
- Railway deployment instructions
- Vercel deployment instructions
- Database setup guide
- Environment variable setup
- Monitoring configuration
- Backup strategy
- Disaster recovery plan
```

---

# 📝 PHASE 8: TESTING & QUALITY ASSURANCE

## PROMPT 8A: Backend Testing Suite

**Paste into Cursor:**

```
As a senior QA engineer, create comprehensive backend testing suite.

TESTING STRATEGY:
- Unit tests for services and utilities
- Integration tests for API endpoints
- Database tests
- API response validation
- Error handling tests
- Rate limiting tests

TEST STRUCTURE:
tests/
├── unit/
│   ├── test_recommendation_engine.py
│   ├── test_myth_detector.py
│   ├── test_knowledge_base.py
│   └── test_embeddings.py
├── integration/
│   ├── test_chat_api.py
│   ├── test_recommend_api.py
│   ├── test_myth_api.py
│   └── test_faq_api.py
├── conftest.py (pytest fixtures)
└── test_data/ (test datasets)

GENERATE:
1. tests/conftest.py - Pytest configuration and fixtures
2. tests/unit/test_recommendation_engine.py
3. tests/unit/test_knowledge_base.py
4. tests/integration/test_chat_api.py
5. tests/integration/test_recommend_api.py
6. tests/integration/test_myth_api.py
7. pytest.ini - Test configuration
8. .coveragerc - Coverage configuration

INCLUDE:
- Unit tests for all recommendation logic
- API endpoint tests with mocked Claude API
- Database transaction rollback between tests
- Fixtures for test data
- Parametrized tests for multiple scenarios
- Error case testing
- Mock external API calls
- Coverage > 80% goal

TESTING COMMANDS:
pytest                  # Run all tests
pytest --cov           # Run with coverage
pytest --cov=app       # Coverage by module
pytest -v              # Verbose output
```

---

## PROMPT 8B: Frontend Testing Suite

**Paste into Cursor:**

```
As a senior frontend engineer, create React component testing suite.

TESTING TOOLS:
- Vitest (fast unit tests)
- React Testing Library (component tests)
- Cypress (e2e tests)
- Playwright (alternative e2e)

TEST STRUCTURE:
src/components/__tests__/
├── Chat/
│   ├── ChatBox.test.tsx
│   ├── MessageList.test.tsx
│   └── InputBox.test.tsx
├── Recommendation/
│   ├── Survey.test.tsx
│   └── Recommendations.test.tsx
└── Common/
    ├── Button.test.tsx
    └── Card.test.tsx

e2e/
├── chat.spec.ts
├── recommendation.spec.ts
├── myth_buster.spec.ts
└── navigation.spec.ts

GENERATE:
1. vitest.config.ts - Vitest configuration
2. src/__tests__/setup.ts - Test environment setup
3. src/components/__tests__/Chat/ChatBox.test.tsx
4. src/components/__tests__/Recommendation/Survey.test.tsx
5. e2e/chat.spec.ts - Cypress e2e tests
6. e2e/recommendation.spec.ts
7. e2e/myth_buster.spec.ts

INCLUDE:
- Component render tests
- User interaction tests
- API call mocking
- Form submission tests
- Error state tests
- Loading state tests
- E2E happy path tests
- Mobile responsiveness tests

TEST COMMANDS:
npm run test            # Run unit tests
npm run test:coverage   # Coverage report
npm run test:e2e       # Run Cypress tests
npm run test:e2e:ui    # Cypress UI
```

---

# 📚 PHASE 9: DOCUMENTATION

## PROMPT 9A: Complete API Documentation

**Paste into Cursor:**

```
Create comprehensive API documentation with OpenAPI spec and examples.

GENERATE:
1. docs/API_DOCUMENTATION.md - Complete API guide
2. docs/ENDPOINTS.md - All endpoint specifications
3. docs/AUTHENTICATION.md - Auth strategy
4. docs/ERROR_CODES.md - Error code reference
5. docs/EXAMPLES.md - cURL and Python examples
6. openapi.yaml - OpenAPI 3.0 specification

DOCUMENTATION SHOULD INCLUDE:
- Base URL and versioning
- Authentication (if any)
- Rate limits
- Request/response examples for all endpoints
- Error codes and meanings
- Webhooks (if any)
- SDK examples (Python, JavaScript)
- Common use cases
- Troubleshooting guide

GENERATE: Complete, production-ready API docs
```

---

## PROMPT 9B: User Documentation

**Paste into Cursor:**

```
Create user-facing documentation and guides.

GENERATE:
1. docs/USER_GUIDE.md - How to use the app
2. docs/FAQ.md - Common user questions
3. docs/PRIVACY.md - Privacy policy
4. docs/DISCLAIMER.md - Medical disclaimer
5. docs/ACCESSIBILITY.md - Accessibility features
6. docs/TROUBLESHOOTING.md - How to fix issues

INCLUDE:
- Step-by-step guides for each feature
- Screenshots (placeholder references)
- Keyboard shortcuts
- Accessibility information
- Language support details
- Offline capabilities
- Data privacy and storage
- Contact support
```

---

# 🎯 EXECUTION SUMMARY

## How to Use These Prompts

**STEP 1: Start with Phase 1**
```
Copy PROMPT 1A into Cursor Composer
Hit @ to reference codebase
Cursor will generate complete project structure
```

**STEP 2: Follow Sequentially**
- Phase 1 (Project Setup) → 2 hours
- Phase 2 (FastAPI Backend) → 4 hours
- Phase 3 (Knowledge Base) → 3 hours
- Phase 4 (Claude AI Integration) → 4 hours
- Phase 5 (API Endpoints) → 4 hours
- Phase 6 (React Frontend) → 6 hours
- Phase 7 (Deployment) → 2 hours
- Phase 8 (Testing) → 4 hours
- Phase 9 (Documentation) → 2 hours

**TOTAL: ~31 hours of development**

## Quick Start Command (after Phase 1):

```bash
# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scripts/data_processing/run_pipeline.py
python scripts/load_knowledge_base.py
uvicorn app.main:app --reload

# Frontend setup (new terminal)
cd frontend
npm install
npm run dev
```

## Key Success Factors:

1. **Python for Backend** - Fastest AI development
2. **Claude API** - No training needed, instant setup
3. **Knowledge Base First** - Fact-check before coding
4. **MVP Focus** - One feature, polished
5. **Test as You Go** - 80% coverage minimum
6. **Deploy Early** - Get feedback quickly

---

## Cost Estimate (Claude API):

For 30-day competition:
- Testing & development: ~50,000 tokens → $0.30
- Demo day: ~10,000 tokens → $0.06
- **Total: ~$0.50**

---

## Competition Winning Formula:

✅ **Technical Excellence**: Clean code, proper error handling
✅ **User-Centric Design**: Mobile-first, accessible
✅ **Accurate Health Info**: Every claim verified and sourced
✅ **Cultural Sensitivity**: Multilingual, local context
✅ **Impact Story**: Show how this helps real people
✅ **Demo Quality**: 5-minute, compelling walkthrough

Good luck! 🚀
