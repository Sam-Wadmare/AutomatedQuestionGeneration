# Project Map: AutomatedQuestionGeneration

## Purpose
This project is a small Flask web app that generates aptitude questions by combining:
- a local CSV dataset of question/option/answer rows,
- a Hugging Face T5 question-generation model,
- and a very simple browser UI.

## Scope of the Current Project
What this project *currently is*:
- A proof-of-concept/demo web app for AI-assisted aptitude question generation.
- Single-service Flask application with in-process model inference.
- Read-only question source from one local CSV file.
- Basic frontend for displaying one generated question at a time.

What this project is *not yet*:
- A production-grade exam engine with robust validation, analytics, and scale.
- A secured multi-user platform with authentication/authorization.
- A full-featured content pipeline (difficulty control, quality filtering, moderation).

## Top-Level Files and Folders

### `app.py`
Main Flask application.
- Initializes Flask app.
- Loads a T5 pipeline once at startup (`valhalla/t5-small-qg-prepend`).
- Loads `clean_general_aptitude_dataset.csv` with semicolon separator.
- Serves the homepage route (`/`) and the generation API (`/generate`).
- `/generate` picks a random source row, generates a new question text from that row's `Question`, and returns original options + answer as JSON.

### `templates/index.html`
Single-page HTML UI.
- Contains title, heading, question display container, option list container, and "Next Question" button.
- Includes client script from `/static/script.js`.

### `static/script.js`
Frontend behavior.
- Adds click handler on "Next Question" button.
- Calls `/generate` via `fetch`.
- Renders returned question and list of options in the DOM.
- Auto-loads first question on page load.

### `clean_general_aptitude_dataset.csv`
Data source used by backend.
- Semicolon-delimited file.
- Expected columns used by code:
  - `Question`
  - `Option A`
  - `Option B`
  - `Option C`
  - `Option D`
  - `Answer`

### `README.md`
Project readme and feature/stack overview.
- Mentions Flask + Transformers + Pandas pipeline.
- Contains setup section but appears truncated in current repository snapshot.

### `static/new.txt` and `templates/new.txt`
Empty placeholder files with no runtime effect in current code.

## Request/Response Flow
1. Browser loads `/`.
2. Flask returns `templates/index.html`.
3. Script runs and calls `/generate`.
4. Backend samples one row from CSV.
5. Backend generates a question with T5 from sampled context.
6. Backend returns JSON with `question`, `options`, `answer`.
7. Frontend updates page with question/options.

## Where It Lacks (Current Gaps)

### Runtime/Architecture
- Model inference runs in request path with no caching, queueing, or fallback.
- No API versioning or error contract.

### Reliability/Quality
- Basic automated tests now exist for route health, response shape, and CSV column presence.
- Data validation is currently limited to test-time checks (not enforced at runtime startup).
- No quality checks on generated question consistency vs options/answer.

### UX/Product
- UI does not display or validate the correct answer.
- No scoring, categories, difficulty, timer, or session history.
- Loading/error states are now included in the frontend.

### Security/Operations
- Runs in debug mode in main entrypoint.
- No dependency lock file, containerization, or deployment configuration.
- No rate-limiting, auth, logging standards, or monitoring.

## Improvement Roadmap

### Phase 1 Status
- ✅ Template folder aligned with Flask defaults (`templates/`).
- ✅ Added `requirements.txt` and completed README setup/run/test instructions.
- ✅ Added basic tests for route health, `/generate` response shape, and CSV columns.
- ✅ Added frontend loading/error states.

### Phase 2 (Quality and product readiness)
1. Add generation quality guards:
   - reject too-short/duplicate outputs
   - optional answer-option consistency checks
2. Add quiz UX features:
   - show/hide answer
   - score tracking
   - difficulty/category filtering
3. Introduce structured logging and better API errors.

### Phase 3 (Production readiness)
1. Move model loading/inference behind a dedicated service or background worker.
2. Add authentication, rate limiting, and telemetry.
3. Add CI/CD, containerization, and environment-based config.

## Should You Leave It or Continue?
- **Continue** if your goal is: learning NLP + Flask, building a portfolio prototype, or validating user interest quickly.
- **Pause/leave** if your goal is: immediate production deployment without investing in tests, architecture, and operations.

Practical recommendation:
- Keep it and do Phase 1. It is a manageable effort with high payoff and will clarify whether deeper investment is worth it.

## Important Notes
- Templates are stored in `templates/`, aligned with Flask defaults.
- The returned answer is included in API response but currently not shown in UI.
- Model loading happens lazily on first generation request and may be slow the first time `/generate` is called.
