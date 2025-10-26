#!/usr/bin/env bash
set -e
# Activar el entorno virtual del proyecto y arrancar el servidor

if [ -f "venv/bin/activate" ]; then
  echo "Activando venv..."
  # shellcheck disable=SC1091
  source venv/bin/activate
else
  echo "Entorno virtual 'venv' no encontrado. Creando uno y instalando dependencias..."
  python3 -m venv venv
  # shellcheck disable=SC1091
  source venv/bin/activate
  pip install -r requirements.txt
fi

echo "Arrancando servidor (app.py)..."
python3 app.py
