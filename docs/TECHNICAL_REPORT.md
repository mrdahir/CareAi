# Technical Report (Maximum 10 Pages)

**HASH Innovation Challenge — Prototype Submission**  
**Deliverable 2 of 7:** Technical Report (Maximum 10 Pages)

| Field | Value |
|-------|-------|
| **Project** | CareApp — Reproductive Health AI Assistant for Sub-Saharan Africa |
| **Track** | Reproductive and Sexual Health Artificial Intelligence |
| **Version** | 1.0.0 |
| **Date** | June 2026 |
| **Source Code Repository** | https://github.com/mrdahir/CareAi/ |

Related deliverables include the prototype web app, this repository, data use documentation, and team contribution statement. Additional HASH submission materials (reproducibility package, IP declaration, checklist) are kept locally for portal upload, not in this repository.

---

## Abstract

CareApp is a multilingual digital health platform for contraceptive education and decision support in Sub-Saharan Africa. The prototype combines a curated knowledge base, a rule-based recommendation engine, generative AI for open-ended questions, and optional programme monitoring data from Western Kenya. This report describes the problem, our solution, the technical design, ethical safeguards, and a path to scale. It is written to fit within the ten-page limit when exported to PDF at standard academic formatting (12 pt, normal margins).

---

## A. Problem Statement

### Challenge track selected

We are submitting CareApp under the **Reproductive and Sexual Health Artificial Intelligence** track. The platform targets a problem that programme managers and clinicians in East Africa describe often: people arrive at clinics already confused about methods, carrying myths from neighbours and social media, and counsellors have ten minutes—sometimes less—to fix that in a language the client actually speaks.

CareApp also touches two related challenge themes. First, **health misinformation**: our myth-buster module addresses false beliefs that keep women off modern methods or push them to stop early. Second, **programme visibility**: where we have permission to use aggregate service data, the home screen shows counselling rates and method mix from a Western Kenya family planning programme, so educational content is not entirely detached from what facilities in that region actually provide.

### Reproductive health problem being addressed

Sub-Saharan Africa still accounts for a large share of global unmet need for family planning. UNFPA estimates that roughly 218 million women of reproductive age who want to avoid pregnancy are not using a modern method. In Kenya, the Demographic and Health Survey puts modern contraceptive prevalence among married women near 58%, with unmet need around 14%. Progress has slowed in places—a “fertility stall” in parts of East Africa despite continued investment—and method mix often skews toward condoms and pills while long-acting reversible contraceptives stay underused relative to their effectiveness.

We break the problem into four areas where a digital tool can help without pretending to replace a clinician.

**Unmet need and method mix.** Adolescents, postpartum women, and rural clients face distance, cost, and stock-outs. In Western Kenya programme data that we process in CareApp, condoms account for about 40% of reported adoption, oral pills 24%, implants 16%, injectables 15%, and IUDs 2%. High contact with services is visible; so is room to improve informed choice toward longer-acting options when appropriate.

**Weak pre-decision counselling.** Choosing a method depends on pregnancy intention, breastfeeding status, blood pressure, side-effect tolerance, privacy, and cost. Community facilities rarely have time to walk through all of that. A structured survey plus explicit rules can standardise the *information* layer while referral language keeps clinical decisions at the facility.

**Misinformation.** Stories linking family planning to permanent infertility or cancer are common. Correcting them needs short, trusted answers in Kiswahili or Amharic—not a PDF in English on a clinic wall.

**Workforce and access gaps.** Task-shifting information to a phone does not fix stock-outs or transport, but it can extend reach when a CHW or a woman at home needs the same message a nurse would give on a good day.

Side-effect counselling deserves its own sentence because it drives discontinuation everywhere, not only in SSA: users who expect zero bleeding change on implants often stop at month two if nobody warned them. FAQs tagged “side effects” and chat prompts that normalise clinic follow-up aim at that gap without collecting sensitive clinical identifiers in the survey.

---

### Target users and beneficiaries

**Primary users** are women and adolescents aged 15–49. The recommendation survey enforces that age band. We pay particular attention to postpartum and breastfeeding clients—the engine excludes combined hormonal pills during lactation and boosts progestin-only and barrier methods—and to users who report hypertension, diabetes, or anaemia, which trigger contraindication filters aligned with common WHO Medical Eligibility Criteria concerns.

**Secondary users** are CHWs, peer educators, and facility counsellors who want consistent myth corrections and ranked method lists with plain-language rationale during household visits or group talks.

**Tertiary beneficiaries** are programme managers. Endpoints such as `GET /api/programme/summary` expose aggregates only: 216,539 client visits, 98% counselling coverage, county breakdowns for Siaya and Busia, and method-mix shares. No individual client records leave the programme pipeline.

The UI supports English, Kiswahili, Amharic, French, and Somali. Language choice persists in the browser; the backend detects language when helpful and instructs the LLM to reply in the user’s selection.

### Relevance to Sub-Saharan African contexts

SSA is mobile-first: smartphones reach places broadband does not. CareApp is a responsive web app with streaming chat so partial responses appear on slow links, answers capped around 400 words, and a knowledge-base fallback when LLM APIs fail.

Linguistic diversity is not a nice-to-have. Health equity literature consistently shows that information in a second language is harder to act on. Five languages in the prototype reflect East and Horn of Africa and Francophone reach, with English and Kiswahili as the best-reviewed content today.

Regional grounding matters. Generic chatbots recommend methods that may not be stocked locally. CareApp overlays regional popularity on recommendation cards and, on the non-streaming chat path, can inject Western Kenya statistics when the user mentions Kenya or programme counties. The survey lets users pick Kenya, Ethiopia, Tanzania, Uganda, or Nigeria for similar overlays from preset profiles where programme files are absent.

We position the tool as **education**, not diagnosis or prescribing—consistent with how ministries and ethics boards expect digital health to behave when a doctor is not in the loop.

Finally, the Western Kenya programme framing—*Reversing the Stall in Fertility Decline*—matches a policy conversation happening in several East African countries: contact with services is up, but mCPR curves have flattened. Tools that improve demand-side literacy and give managers a readable snapshot of method mix can sit alongside supply-side investments without duplicating EMR functions we are not ready to certify.

---

## B. Solution Overview

### Description of the proposed innovation

CareApp is a **functional prototype** spanning a web application, conversational chatbot, decision-support survey, and a programme summary widget on the home page. It is not production-certified; it demonstrates feasibility for the HASH jury and partners.

Architecturally we use three layers that reinforce each other:

1. **Curated evidence (deterministic).** JSON files describe six contraceptive methods, 22 verified myths, and 51 FAQs, with tags, contraindications, and source references (WHO, CDC). This layer works even when API keys are missing.

2. **Rule-based recommendations (algorithmic).** A scoring engine ranks methods with inspectable weights and filters. Outputs stay stable run to run—important if a clinical advisor needs to sign off before field deployment.

3. **Generative AI (adaptive).** Gemini or Groq handles questions the FAQ index does not cover, myth statements that do not match the catalogue, and multilingual phrasing. Retrieved KB snippets are prepended to each prompt; system instructions forbid diagnosis and require referral language for urgent symptoms.

We call this **structured core, generative periphery**. Pure chatbots hallucinate; pure pamphlets cannot answer “Can I start pills if my BP was high last visit?” CareApp tries to split the difference.

Implementation: **FastAPI** (Python 3.11+), **React 18** with TypeScript and Tailwind, optional **PostgreSQL** or SQLite, Docker-friendly layout. Western Kenya aggregates load from processed JSON after running the documented pipeline script—no live connection to a production EMR in this submission.

### Key functionalities

The table below separates what judges will see in the UI from what exists on the API only.

| Capability | UI route | API | Notes |
|------------|----------|-----|--------|
| Health chat | `/chat` | `POST /api/chat/stream`, `POST /api/chat` | UI uses stream first; fallback persists to DB |
| Recommendations | `/recommend` | `POST /api/recommend` | Six-step survey |
| Myth buster | `/myth-buster` | `POST /api/myth-check` | KB match then LLM |
| Programme summary | `/` (widget) | `GET /api/programme/summary`, `GET /api/programme/stats` | Widget on Home; county drill-down API-only |
| About | `/about` | — | Disclaimers, credits |
| FAQ | — | `POST /api/faq` | Ask via chat instead |
| Method catalogue | — | `GET /api/contraceptives` | |
| Chat history | — | `GET /api/chat/history` | |
| Feedback | — | `POST /api/chat/feedback` | |

**Chat.** The user types a question (up to 2,000 characters). The client opens a stream from `/api/chat/stream`: word chunks, KB context, LLM text. That path does **not** write to the database and does **not** add programme context. If streaming fails, the client posts to `/api/chat`, which returns JSON with sources, may persist an anonymous user UUID and messages, and can append programme stats when Kenya-related keywords appear. Local history lives in React state until refresh.

**Recommendations.** Six steps: age (15–49), pregnancy goals, breastfeeding yes/no, health conditions (hypertension, diabetes, anaemia), duration preference, region. Age is collected for eligibility framing but is **not** used in scoring today. The API also accepts `cost_sensitive`, `privacy_needed`, and `side_effect_tolerance`; the survey does **not** expose those yet—they default false or empty. The engine returns three ranked methods with scores, rationale, regional popularity strings, and a disclaimer. If everything is filtered out, a condom recommendation appears at 70% confidence.

**Myth buster.** User text is matched against 22 myths with Jaccard similarity ≥ 0.35 (confidence 0.95). Otherwise the LLM evaluates the claim (confidence 0.70). Severity and sources display in the UI.

**Safety.** Rate limiting (100 requests per minute per IP), no prescription logic, footer disclaimer on every page. Clinical review of KB content before live deployment is documented in CONTRIBUTING.md.

### User workflow

A typical session: land on Home, optionally read programme highlights, switch language in the header, then open Chat or Recommend. CHWs might skip straight to Myth buster during a group discussion. Programme staff can hit the summary API directly for county-level stats without logging into a separate dashboard—that dashboard is roadmap, not prototype. Request flow: React pages call FastAPI routes; chat and myths may invoke Gemini or Groq after KB retrieval; recommendations use the rule engine only.

### Expected health system benefits

For **clients**, the benefit is time and privacy: questions at night, myths checked before a clinic argument, method options rehearsed before a visit. For **providers**, repeated counselling scripts and myth corrections free minutes for exams and procedures. For **programmes**, aggregate chat themes (when logging is on) and existing visit statistics can sit beside DHIS2 indicators; we plan DHIS2 export but have not built it here.

Judges evaluating the prototype should expect a polished demo path—Home, Chat, Recommend, Myth buster, About—not a full analytics suite. The API surface is wider than the UI on purpose: partners can wire CHW tablets to myth-check and recommend endpoints while we finish consumer-facing FAQ and history screens.

---

## C. Technical Approach

### AI/ML methods used

We do **not** train custom models in this prototype. **Google Gemini** is the default generator; **Groq** (Llama 3.3 70B) is the fallback when configured. Both receive the same system prompt template: non-diagnostic scope, cite sources when possible, respond in the selected language, stay under the mobile word cap.

**Retrieval-augmented generation** is lightweight: keyword overlap and category tags pull FAQ entries, method blurbs, and myth text into the prompt. There is no vector database—acceptable for 51 FAQs and six methods, but a known ceiling for paraphrase-heavy queries.

**Recommendation and myth matching** stay non-ML. That is intentional. Facility advisors and ministry reviewers can read the Python and the JSON and understand why implant ranked above pill for a breastfeeding user without inspecting neural weights.

When an API key is present, the LLM layer adds paraphrase and tone—explaining in Kiswahili what “progestin-only injectable” means in plain terms. When absent, users still get structured FAQ answers and rule outputs. That degradation path matters in hackathon demos and in clinics that want to pilot rules first before enabling generative chat.

### Algorithms and models implemented

**Recommendation engine** (`recommendation_engine.py`). Each method starts from a base score in the KB. Adjustments include: contraindication filters (e.g. combined hormonal methods removed for hypertension or breastfeeding); effectiveness weighting by pregnancy goal; duration preference; accessibility tags; regional popularity bonus from programme JSON or country presets; breastfeeding bonus (+10 when `best_for` tags include breastfeeding-related labels; +8 for implant, IUD, condom, injectable after our v1.0.1 tag alignment fix). Top three methods by score are returned. If the best score falls below 70% of the normalised maximum, **condom** is injected as a dual-protection default.

**Myth buster.** Tokenise input and each myth statement, compute Jaccard index on word sets, take the best match above 0.35. Matched myths return stored rebuttals; unmatched text goes to the LLM myth prompt.

**Chat paths.** Operators should treat streaming and non-streaming as two modes until we unify them: persistence and programme context only on `/api/chat`; lower latency and simpler ops on `/api/chat/stream`.

### System architecture

Monolithic FastAPI app with routers for chat, recommend, myths, programme, FAQ, contraceptives. Services: `chat_service`, `recommendation_engine`, `myth_service`, `kb_loader`, `llm_client`. React calls REST and SSE. Config via environment: `GEMINI_API_KEY`, `GROQ_API_KEY`, `DATABASE_URL`, CORS origins. Alembic migrations define chat and feedback tables.

Security today: CORS allowlist, rate limits, no auth on the public demo (production would need facility tokens). Users should not enter names or national IDs in free text; the reproducibility package describes redaction if logs are exported for research. Backend entrypoint is `backend/app/main.py`; routers under `backend/app/api/`. Docker Compose and environment variables are documented in the README and [`REPRODUCIBILITY_PACKAGE.md`](REPRODUCIBILITY_PACKAGE.md).

### Data processing pipeline

Content authors edit JSON under `backend/app/data/` with per-language strings. On startup, `kb_loader` validates schemas and caches objects in memory. At request time, chat retrieval scans FAQs; recommendations read method objects directly; myths iterate the full list for similarity. Programme aggregates are produced offline by `western_kenya_pipeline.py` from challenge datasets and shipped as static JSON—no nightly ETL in the prototype.

Updates are git commits reviewed by the team, not automated scraping from the web. That keeps clinical accountability traceable.

### Model evaluation methods

**LLM outputs:** manual review checklist (accuracy, tone, language, refusal behaviour). No automated BLEU or clinical NLP benchmark in v1.0.

**Rules and API:** pytest unit tests for ranking, breastfeeding bonus, condom fallback, myth threshold; integration tests hit `/health` and core POST routes. Example: `test_breastfeeding_bonus_applied_to_lactation_compatible_methods` guards the tag-name fix.

**Known limits:** LLMs can still invent details if retrieval misses; Jaccard misses rephrased myths; scores are heuristic, not validated against continuation rates. Partner pilots with pre/post knowledge tests would be the next rigorous step.

---

## D. Ethical and Responsible AI Considerations

### Data privacy and security measures

Surveys collect categorical health flags, not identifiers. Chat persistence is optional and off on the default stream path. Where logs are kept, facility consent processes should apply. Aggregate programme stats never include names or phone numbers. API keys stay in `.env`, not the repository. Data minimisation extends to programme integration: only aggregates from the Western Kenya pipeline appear in the app; raw challenge dataset rows stay out of the repository.

### Bias and fairness considerations

Content was drafted for SSA contexts by a small team—we cannot represent every community. Amharic and Somali strings deserve native-speaker review before wide release. The engine must not be marketed as a substitute for physical exam or lab work where contraindications are unclear. We have not deployed community review boards in this challenge phase; a production roll-out should include them for myth phrasing and adolescent messaging.

### Transparency and explainability approaches

Recommendations include per-method rationale strings from rules, not post-hoc LLM excuses. Myth hits show which catalogue entry matched. Chat answers include source lists when the non-stream path returns them. We treat CareApp as counselling support, not autonomous care: every recommendation card and myth panel directs users to qualified providers for method initiation, contraindication screening, and STI testing.

### Alignment with local/regional legal and regulatory requirements

Where logs are kept, processes should align with the **Kenya Data Protection Act, 2019** and any partner IRB. Prompts exclude emergency diagnosis; users see referral language for severe symptoms. Adolescents receive the same clinical facts with confidentiality messaging on the About page. CONTRIBUTING.md requires clinical sign-off for KB changes. Team contribution and IP declarations accompany this submission as separate documents.

---

## E. Scalability and Sustainability

### Potential deployment strategy

API processes are stateless and can scale horizontally behind a load balancer. KB reload on deploy keeps instances consistent. Streaming helps perceived performance on 2G and 3G. Three tiers: (1) **Demo** — single VM, stream-only chat, no database; (2) **Facility** — PostgreSQL, `/api/chat` persistence, optional programme injection; (3) **Programme** — multi-tenant config, authenticated staff view, DHIS2 or EMR export (roadmap).

### Resource requirements

LLM calls dominate marginal cost. Caching answers to top FAQs, caps per IP, and smaller models for myth fallback keep a clinic pilot affordable. Hosting a FastAPI container and static frontend is modest compared to call charges at high volume. Embeddings over the FAQ corpus would be the first ML upgrade without changing the React shell.

### Integration with existing health systems

Aggregate chat themes (when logging is on) and visit statistics can sit beside DHIS2 indicators; DHIS2 export is planned, not shipped in this prototype. Ministries can fork the JSON knowledge base without retraining models. Integration with existing mHealth programmes (SMS reminders, CHW registers) is a more realistic long-term home than a standalone app-store product.

### Long-term maintenance considerations

Versioned data files, pytest in CI, Docker Compose for local parity, and [`REPRODUCIBILITY_PACKAGE.md`](REPRODUCIBILITY_PACKAGE.md) support handover to county IT teams. Near-term product work: expose `cost_sensitive` and `privacy_needed` in the survey; unify chat stream and persist paths; add FAQ and method browser pages. LLM chat remains optional—rules and myths work without API keys.

---

## References (selected)

- Kenya Demographic and Health Survey (KDHS), 2022.  
- UNFPA, *State of World Population*, 2022 (unmet need estimates).  
- WHO, *Family Planning Handbook*, 2022 (medical eligibility framework informing KB content).  
- FP2030 partnership reports on method discontinuation and counselling quality in LMICs.

---

## Document control

| Item | Detail |
|------|--------|
| Source Code Repository | https://github.com/mrdahir/CareAi/ |
| Reproducibility Package | `docs/REPRODUCIBILITY_PACKAGE.md` |
| Data use Documentation | `docs/DATA_USE_DOCUMENTATION.md` |
| Prototype version | 1.0.0 |

*End of report.*
