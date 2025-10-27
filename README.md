# 🎯 Agente Matemático Inteligente ESO+

> **Agente AI especializado en matemáticas de ESO/Bachillerato con arquitectura híbrida**  
> *Preparado para AgentX Competition 2025-2026 - Purple Agent Category*

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![AgentX Ready](https://img.shields.io/badge/AgentX-Competition-purple.svg)](https://agentx.ai)
[![Version](https://img.shields.io/badge/Version-4.0.0-orange.svg)](https://github.com/zumaia/agente-matematico)

![Agente Matemático Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=Agente+Matemático+ESO+Demo)

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

### Prerrequisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)

### 📥 Instalación Paso a Paso

```bash
# 1. Clonar el repositorio
git clone https://github.com/zumaia/agente-matematico.git
cd agente-matematico

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno (opcional)
cp .env.example .env
# Editar .env con tu API key de Groq si la tienes

# 5. Ejecutar servidor
python app.py


**¡Listo!** 🎉 Visita `http://localhost:8000` para usar la interfaz web.

## 📖 Uso

### 🌐 Interfaz Web (Recomendado para usuarios)

1. **Abre** `http://localhost:8000` en tu navegador
2. **Escribe** tu problema matemático en el campo de texto
3. **Haz clic** en "Resolver Problema"
4. **Obtén** solución paso a paso con explicaciones detalladas

### 🌐 **Soporte Multiidioma Completo**
- **🇪🇸 Español** - Idioma principal
- **🇬🇧 Inglés** - Cobertura internacional  
- **🇪🇺 Euskera** - Soporte regional
- **🔄 Cambio dinámico** - Interfaz adaptable en tiempo real

### 🎨 **Interfaz Mejorada**
- **📱 Diseño totalmente responsive** - Adaptable a móviles y tablets
- **🎯 21 ejemplos organizados** por categorías matemáticas
- **⚡ Selector de idioma intuitivo** - Cambio inmediato ES/EN/EU
- **📊 Gráficos integrados** para visualización matemática

### 📚 **Dominio Matemático Extendido** (7 categorías)
- **🧮 Álgebra**: Ecuaciones lineales, cuadráticas, sistemas de ecuaciones
- **📐 Geometría**: Áreas, volúmenes, Pitágoras, circunferencias
- **🔢 Aritmética**: Fracciones, porcentajes, operaciones combinadas
- **📊 Estadística**: Media, mediana, moda, probabilidad, rango
- **📈 Trigonometría**: Seno, coseno, tangente, funciones trigonométricas
- **🔄 Sucesiones**: Patrones numéricos, progresiones, términos generales
- **🎲 Combinatoria**: Permutaciones, combinaciones, principios de conteo
- **📏 Geometría Analítica**: Distancias, pendientes, ecuaciones de recta

### 🔌 API REST (Para desarrolladores)

```python
import requests

# Ejemplo de uso básico
response = requests.post(
    "<http://localhost:8000/resolver>",
    json={"problema": "resolver la ecuación 2x + 5 = 15"}
)

print(response.json())

```

**Respuesta esperada:**

```json
{
  "problema": "resolver la ecuación 2x + 5 = 15",
  "solucion": "x = 5",
  "tipo_problema": "ecuacion_lineal",
  "pasos_detallados": [
    "Restar 5 a ambos lados: 2x = 10",
    "Dividir ambos lados por 2: x = 5"
  ],
  "metodo": "algoritmo_matematico",
  "estado": "resuelto"
}

```
 # 🎯 Agente Matemático Inteligente (ESO / Bachillerato)

Proyecto híbrido para resolver problemas matemáticos combinando resolutores algorítmicos y un fallback de IA. Preparado para evaluación A2A (AgentX) y para uso local con Docker o en un entorno virtual Python.

Resumen rápido
- Servidor principal (Purple): `app.py` — puerto 8000
- Evaluador (Green): `green_app.py` — puerto 8001
- Evaluación automática: `scripts/run_local_eval.py`

Estado: rama `main`. Revisa la carpeta `demo/` para ejemplos de uso y capturas.

---

## Requisitos
- Python 3.10+ (recomendado 3.11)
- pip
- Docker & docker-compose (opcional, recomendado para reproducibilidad)

## Instalación y ejecución local (venv)

1) Clona el repo:

```bash
git clone https://github.com/zumaia/agente-matematico.git
cd agente-matematico
```

2) Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
# venv\Scripts\activate  # Windows (PowerShell)
```

3) Instala dependencias:

```bash
pip install -r requirements.txt
```

4) Opcional: copia el ejemplo de variables de entorno y añade tu clave si la tienes:

```bash
cp .env.example .env
# Edita .env para añadir GROQ_API_KEY si quieres usar el fallback de IA
```

5) Ejecuta el servidor Purple (interfaz web):

```bash
python app.py
# o: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
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

Si quieres que añada capturas de pantalla en la sección `demo/` o una versión en inglés, lo hago a continuación.
