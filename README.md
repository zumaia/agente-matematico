# 🎯 Agente Matemático Inteligente ESO+

> **Agente AI especializado en matemáticas de ESO/Bachillerato con arquitectura híbrida**  
> *Preparado para AgentX Competition 2025-2026 - Purple Agent Category*

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![AgentX Ready](https://img.shields.io/badge/AgentX-Competition-purple.svg)](https://agentx.ai)
[![Version](https://img.shields.io/badge/Version-4.0.0-orange.svg)](https://github.com/zumaia/agente-matematico)

## Capturas (demo)

A continuación se muestran capturas de la interfaz incluidas en `demo/`:

![Purple UI — Interfaz principal](demo/screenshot_purple_ui.png)

![Green UI — Evaluador](demo/screenshot_green_ui.png)

Si quieres reemplazarlas por otras, agrega archivos PNG con los mismos nombres en la carpeta `demo/` y el README se actualizará automáticamente al mostrar las nuevas imágenes.

## 🌟 Descripción

**Agente Matemático Inteligente ESO+** es un sistema avanzado de resolución de problemas matemáticos que combina algoritmos tradicionales con inteligencia artificial para ofrecer soluciones precisas y explicaciones paso a paso. Diseñado específicamente para estudiantes de ESO y Bachillerato.

### 🏆 Preparado para AgentX Competition
Este proyecto está optimizado para participar como **Purple Agent** en la competencia AgentX 2025-2026, implementando los estándares A2A para evaluación de agentes AI.

## 🚀 Características Principales

### 🧠 **Arquitectura Híbrida Inteligente**
| Módulo | Función | Ventaja |
|--------|---------|---------|
| **🔢 Algoritmos Matemáticos** | Resolución precisa con métodos tradicionales | Máxima precisión |
| **🤖 IA Groq Integration** | Problemas complejos y explicaciones naturales | Flexibilidad y adaptabilidad |
| **⚡ Cache Inteligente** | Almacenamiento de soluciones recurrentes | Respuestas ultra-rápidas (<500ms) |
| **🎯 Detección de Intención** | Análisis semántico de problemas | Priorización automática de resolutores |

### 📚 **Dominio Matemático Completo**
- **🔤 Álgebra**: Ecuaciones lineales, sistemas de ecuaciones, expresiones algebraicas
- **📐 Geometría**: Áreas, volúmenes, teorema de Pitágoras, perímetros
- **🔢 Aritmética**: Fracciones, porcentajes, operaciones combinadas, potencias
- **📊 Estadística**: Media, mediana, moda, rango, probabilidad básica
- **🔄 Patrones**: Secuencias numéricas, detección de regularidades

### 🌐 **Interfaz Completa**
- **🖥️ Interfaz Web Moderna** - Diseño responsive y intuitivo
- **🔌 API REST Completa** - Para integraciones programáticas
- **📚 Documentación Automática** - Swagger/OpenAPI incluido
- **🎨 Templates Profesionales** - Experiencia de usuario mejorada

## 🛠️ Instalación Rápida

# 🎯 Math Agent (ESO / High School)

English • Español • Demo

- English (current): `README.md`
- Español: `README_es.md`
- Demo & screenshots: `demo/README.md`

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
Visita: http://localhost:8000

Para arrancar también el servicio Green localmente (si no usas Docker), en otra terminal:

```bash
python green_app.py
# o: uvicorn green_app:app --host 0.0.0.0 --port 8001 --reload
```

---

## Uso con Docker Compose (recomendado para demo/entrega)

1) Asegúrate de tener Docker y docker-compose instalados.
2) Crea un `.env` con la variable (opcional):

```bash
echo "GROQ_API_KEY=tu_api_key_aqui" > .env
```

3) Arranca los servicios:

```bash
docker-compose up --build
```

Esto levanta dos servicios:
- Purple (app) en http://localhost:8000
- Green (evaluador) en http://localhost:8001

Para detenerlos:

```bash
docker-compose down
```

Notas: en entorno Docker, Green está configurado para comunicarse con Purple usando el nombre de servicio `http://app:8000` dentro de la red de Compose.

---

## Evaluación automática

Usa `scripts/run_local_eval.py` para ejecutar una evaluación rápida (usa el servicio Green contra Purple).

Ejemplo local (si ambos servidores están corriendo):

```bash
# desde la raíz del repo
python scripts/run_local_eval.py
```

También puedes ejecutar el runner dentro del contenedor Green:

```bash
docker-compose exec -T green python3 scripts/run_local_eval.py
```

---

## Endpoints importantes

- `/` (GET) — interfaz web
- `/resolver` (POST) — resolver problema en JSON
- `/resolver-web` (POST) — form submit desde la web
- `/api` (GET) — info básica y health
- `/health` (GET, en Green) — healthcheck evaluador
- `/cache/estado` (GET) — estado del cache
- `/cache/limpiar` (DELETE) — limpiar cache

---

## Buenas prácticas y seguridad

- Nunca comites claves en `.env`. Asegúrate de que `.gitignore` incluye `.env`, `venv/`, `__pycache__/` y `*.pyc`.
- Si crees que una clave fue expuesta, rótala inmediatamente.
- Para CI, usa secretos del repositorio y no incluyas claves en los workflows.

---

## Contribuir

1. Fork del proyecto
2. Crear rama: `git checkout -b feature/mi-cambio`
3. Commit y push
4. Abrir Pull Request

Revisa `demo/README.md` para guías rápidas de demo y capturas.

---

## Autor y licencia

Oscar Rojo — https://github.com/zumaia

Licencia: MIT (ver `LICENSE`)

---

