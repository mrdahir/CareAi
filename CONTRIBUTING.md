# Contributing to CareApp

Thank you for your interest in contributing. CareApp is an open-source reproductive health education assistant for Sub-Saharan Africa.

## Getting started

1. Fork the repository and clone your fork.
2. Follow setup in [README.md](README.md).
3. Create a branch: `git checkout -b feature/your-change`.

## Development

| Area | Commands |
|------|----------|
| Backend | `cd backend && pytest -v` |
| Frontend | `cd frontend && npm run test:run && npm run build` |
| Lint (frontend) | `cd frontend && npm run lint` |

Use Python **3.11–3.13** for the backend. Do not commit `.env` files or API keys.

## Pull requests

- Keep changes focused and well described.
- Ensure tests pass before opening a PR.
- Update README or `docs/` if you change setup, APIs, or env vars.
- Health-related content changes should cite WHO/CDC or peer-reviewed sources.

## Medical content

CareApp provides **education only**, not medical advice. New myths, FAQs, or clinical claims require review by a qualified health professional before merge to production branches.

## Code of conduct

Be respectful and inclusive. We welcome contributors from all backgrounds working to improve access to reproductive health information.

## Questions

Open a GitHub issue for bugs, feature requests, or setup problems.
