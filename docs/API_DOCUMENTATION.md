# CareApp API Documentation

Base URL: `http://localhost:8000/api` (development)

Interactive docs: http://localhost:8000/docs

## Authentication

None in MVP. Rate limiting applies per IP when `RATE_LIMIT_ENABLED=true`.

## LLM

Responses use **Google Gemini** (default) or **Groq** via `LLM_PROVIDER`. KB fallback when no API key.

## Endpoints

### Health

`GET /health` → `{ "status": "healthy", ... }`

### Chat

`POST /chat`

```json
{ "message": "Is the implant safe?", "language": "en", "user_id": null }
```

`POST /chat/stream` — plain-text streamed body

`GET /chat/history?user_id=<uuid>&limit=10`

`POST /chat/feedback` — `{ "user_id", "message_id", "rating", "feedback" }`

### Recommendations

`POST /recommend` — age, breastfeeding, pregnancy_goals, preferred_duration, region, language

### Myth check

`POST /myth-check` — `{ "statement", "language" }`

### FAQ

`POST /faq` — `{ "question", "language", "category" }`

### Contraceptives

`GET /contraceptives?language=en&category=`

## Errors

| Code | Meaning |
|------|---------|
| 400 | Validation error |
| 429 | Rate limit exceeded |
| 500 | Server error |

## Rate limits

Default: 100 requests / 60 seconds per IP. `/api/health` and `/docs` are exempt.

Configure: `RATE_LIMIT_REQUESTS`, `RATE_LIMIT_SECONDS`, `RATE_LIMIT_ENABLED`.
