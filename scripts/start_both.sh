#!/usr/bin/env bash
# Lanzador sencillo que ejecuta el script Python que arranca ambos servicios
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$HERE/start_both.py"
