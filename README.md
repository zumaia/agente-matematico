## 🎯 Math Agent (ESO / High School)

English • Español • Demo

- English (current): `README.md` (this file) — start here for usage and deployment
- Español: `README_es.md` — full Spanish translation
- Demo & screenshots: `demo/README.md`

This repository contains a hybrid math problem-solving agent for middle/high-school level math. It combines algorithmic solvers with an AI fallback for problems that require natural-language explanations or fuzzy reasoning. The repo includes both the Purple (UI/API) and Green (evaluator) services, Docker compose files and an automated local evaluation runner.

Table of contents

- [Quick summary](#quick-summary)
- [Requirements & local install](#requirements--local-install)
- [Docker Compose (recommended)](#docker-compose--recommended)
- [Automatic evaluation](#automatic-evaluation)
- [Important endpoints](#important-endpoints)
- [Security notes](#security-notes)
- [Contributing & license](#contributing--license)

## Quick summary

- Purple server (main): `app.py` — port 8000
- Green evaluator: `green_app.py` — port 8001
- Automatic evaluation runner: `scripts/run_local_eval.py`

## Requirements & local install

- Python 3.10+ (3.11 recommended)
- pip
- Docker & docker-compose (optional, recommended for reproducibility)

Local install (venv)

```bash
git clone https://github.com/zumaia/agente-matematico.git
cd agente-matematico
python -m venv venv
source venv/bin/activate  # Linux / macOS
pip install -r requirements.txt
cp .env.example .env  # optional: add GROQ_API_KEY for AI fallback
python app.py
# or: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Open http://localhost:8000

Run Green evaluator locally (separate terminal):

```bash
python green_app.py
# or: uvicorn green_app:app --host 0.0.0.0 --port 8001 --reload
```

## Docker Compose (recommended)

Create a `.env` with the optional Groq API key (if you use AI fallback):

```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

Start the services:

```bash
docker-compose up --build
```

Services started:
- Purple (app) → http://localhost:8000
- Green (evaluator) → http://localhost:8001

To stop:

```bash
docker-compose down
```

Note: inside Docker Compose the Green service contacts Purple via the internal network address `http://app:8000` (service name `app`).

## Automatic evaluation

Use `scripts/run_local_eval.py` to run a quick evaluation (Green evaluates Purple).

Local example (with both servers running):

```bash
# from repo root
python scripts/run_local_eval.py
```

Run the runner inside the Green container:

```bash
docker-compose exec -T green python3 scripts/run_local_eval.py
```

## Important endpoints

- `/` (GET) — web UI
- `/resolver` (POST) — resolve problem (JSON)
- `/resolver-web` (POST) — form submit from UI
- `/api` (GET) — basic info / health
- `/health` (GET, on Green) — evaluator health
- `/cache/estado` (GET) — cache status
- `/cache/limpiar` (DELETE) — clear cache

## Security notes

- Never commit secrets (`.env`) to the repository. Ensure `.gitignore` includes `.env`, `venv/`, `__pycache__/` and `*.pyc`.
- If a key may have been exposed, rotate it immediately.
- For CI, use repo secrets and avoid embedding keys in workflows.

## Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-change`
3. Commit and push
4. Open a Pull Request

See `demo/README.md` for demo instructions and screenshots.

## Author and license

Oscar Rojo — https://github.com/zumaia

License: MIT (see `LICENSE`)


