# Entrega — Agente Matemático (Fase 1: Green Agent)

Este repositorio contiene el Agente Matemático (Purple) y el evaluador (Green) preparado para la Fase 1 del concurso AgentBeats / AgentX.

Contenido clave
- `app.py`: Purple Agent (interfaz web y endpoints A2A `/api`, `/agent-card`, `/resolver-web`, `/reset`).
- `green_app.py`: Green Agent (evaluador) con endpoints `/evaluate`, `/evaluate-es`, `/health`, `/green-agent-card`.
- `green_agent/`: implementación del evaluador, dataset de problemas y métricas.
- `matematica/`: resolutores algorítmicos por dominio.
- `scripts/run_local_eval.py`: runner de evaluación local usado para pruebas automáticas.
- `docker-compose.yml` + `Dockerfile`: configuración para levantar ambos servicios en desarrollo y pruebas.

Objetivo de esta entrega
- Proveer un artefacto reproducible que permita a los jueces ejecutar la Fase 1 (Green Agent) contra el Purple Agent localmente o en su entorno de evaluación.

Requisitos para ejecutar
- Docker & Docker Compose (recomendado para la evaluación reproducible). Alternativamente, usar un virtualenv con `requirements.txt`.
- Variables sensibles: `GROQ_API_KEY` (si se quiere habilitar fallback IA). NO subir la clave al repositorio. Usar `.env` local o secretos de CI.

Cómo ejecutar (modo desarrollo)
1. Copia `.env.example` a `.env` y ajusta variables (si usas GROQ, pega la clave localmente).
2. Construir y levantar con Docker Compose (monta el código para desarrollo):

```bash
docker-compose up --build -d
docker-compose logs -f
```

3. Acceder a:
- Purple Agent (UI): http://localhost:8000
- Green Agent (UI y evaluación): http://localhost:8001

Ejecutar evaluación automática (opcional)
- Para ejecutar el runner de evaluación desde el contenedor Green:

```bash
# desde la raíz del repo
docker-compose exec -T green python3 scripts/run_local_eval.py
```

Recomendaciones de seguridad
- Rotar `GROQ_API_KEY` si alguna vez fue subida.
- No incluir `.env` en commits. Si accidentalmente se subió, rotar claves y limpiar historial.

Entrega y verificación (qué deben hacer los jueces)
1. Clonar el repo.
2. Ejecutar `docker-compose up --build -d`.
3. Visitar `http://localhost:8001` y lanzar una evaluación; comprobar que las llamadas entre Green y Purple funcionan (Green usará por defecto `http://app:8000` en Compose).
4. (Opcional) Ejecutar `scripts/run_local_eval.py` y revisar `results/` si se genera.

Notas finales
- Entregaremos además un `docker-compose.prod.yml` (opcional) y un pequeño demo con capturas de pantalla si es necesario.
