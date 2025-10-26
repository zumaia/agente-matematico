#!/usr/bin/env bash
set -e
# Activar venv y ejecutar la evaluación del Green Agent contra el servidor local

if [ -f "venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source venv/bin/activate
else
  echo "Entorno virtual 'venv' no encontrado. Ejecuta: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
  exit 1
fi

python3 - <<'PY'
from green_agent.evaluador import GreenAgentMatematico
import json

g = GreenAgentMatematico()
res = g.evaluar_purple_agent('http://127.0.0.1:8000', None)
print(json.dumps(res, indent=2, ensure_ascii=False))
PY
