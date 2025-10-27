# 🎯 Math Agent (ESO / High School)

Hybrid project to solve math problems using algorithmic solvers with an AI fallback. Ready for A2A evaluation (AgentX) and for local use via Docker or a Python virtual environment.

Quick summary
- Purple server (main): `app.py` — port 8000
- Green evaluator: `green_app.py` — port 8001
- Automatic evaluation runner: `scripts/run_local_eval.py`

Requirements
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

Docker Compose (recommended)

```bash
echo "GROQ_API_KEY=your_api_key_here" > .env  # optional
docker-compose up --build
```

Services:
- Purple: http://localhost:8000
- Green: http://localhost:8001

To stop:

```bash
docker-compose down
```

Automatic evaluation

Run the local evaluation runner (requires both services running):

```bash
python scripts/run_local_eval.py
```

Or inside the Green container:

```bash
docker-compose exec -T green python3 scripts/run_local_eval.py
```

Important endpoints

- `/` (GET) — web UI
- `/resolver` (POST) — solve problem (JSON)
- `/resolver-web` (POST) — form submit
- `/api` (GET) — basic info / health
- `/health` (GET, on Green) — evaluator health
- `/cache/estado` (GET) — cache status
- `/cache/limpiar` (DELETE) — clear cache

Security & best practices

- Do not commit secrets in `.env`. Ensure `.gitignore` includes `.env`, `venv/`, `__pycache__/` and `*.pyc`.
- Rotate any key that may have been exposed.
- Use repository secrets for CI.

Contributing

1. Fork
2. Create a branch: `git checkout -b feature/xxx`
3. Commit and push
4. Open a Pull Request

See `demo/README.md` for demo steps and screenshots.

Author & license

Oscar Rojo — https://github.com/zumaia

License: MIT
