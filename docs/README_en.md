# 🎯 Math Agent (ESO / High School)

This file is a backup copy of the primary `README.md` (English). Keep it in `docs/` as a reference or for packaging.

## Quick start (same as root README)

- Purple server (main): `app.py` — port 8000
- Green evaluator: `green_app.py` — port 8001
- Automatic evaluation runner: `scripts/run_local_eval.py`

### Requirements & local install

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

Run the Green evaluator in a separate terminal:

```bash
python green_app.py
# or: uvicorn green_app:app --host 0.0.0.0 --port 8001 --reload
```

---

For the full, canonical documentation see the root `README.md` (English). If you need the Spanish translation, open `README_es.md` in the repository root.
