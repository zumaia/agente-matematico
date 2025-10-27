from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from datetime import datetime
import sys
import os
from fastapi.responses import FileResponse
from green_agent.evaluador import GreenAgentMatematico
from green_agent.dataset_matematico import obtener_problemas_aleatorios
from fastapi.templating import Jinja2Templates
from typing import Optional

"""
Servidor FastAPI para Green Agent matemático
Evaluador especializado en problemas de ESO/Bachillerato
"""



# Añadir el directorio actual al path para imports
sys.path.append(os.path.dirname(__file__))

app = FastAPI(
    title="MathESO Evaluator - Green Agent",
    description="Green Agent especializado en evaluación matemática para ESO/Bachillerato",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")
green_agent = GreenAgentMatematico()

class EvaluacionRequest(BaseModel):
    purple_agent_url: str
    num_problemas: int = 5
    categoria: Optional[str] = None
    dificultad: Optional[str] = None

# ========== ENDPOINTS PRINCIPALES ==========

@app.get("/", response_class=HTMLResponse)
async def interfaz_web(request: Request, lang: Optional[str] = None):
    """Interfaz web para el Green Agent.

    Se acepta parámetro de query `lang` para seleccionar idioma (ej. `?lang=en`).
    Por compatibilidad con la preferencia del proyecto, el idioma por defecto es inglés (`en`).
    """
    # Determinar URL por defecto para el Purple Agent. En entorno docker-compose se usará 'http://app:8000'
    default_purple = os.getenv('DEFAULT_PURPLE_AGENT_URL', 'http://localhost:8000')
    # Priorizar parámetro de query, luego variable de entorno DEFAULT_GREEN_LANG, finalmente 'en'
    lang = (lang or request.query_params.get('lang') or os.getenv('DEFAULT_GREEN_LANG') or 'en').lower()

    if lang.startswith('en'):
        template_name = "green_index_en.html"
    elif lang.startswith('eu'):
        # If Basque/Euskera template is added in the future, use it. Fallback to Spanish currently.
        template_name = "green_index.html"
    else:
        # default Spanish template kept as `green_index.html`
        template_name = "green_index.html"

    return templates.TemplateResponse(template_name, {"request": request, "default_purple_url": default_purple})

@app.get("/favicon.ico", include_in_schema=False)
async def favicon_green():
    return FileResponse("static/favicon.ico")

@app.get("/green-agent-card")
async def green_agent_card():
    """Agent Card específico para Green Agent - Estándar AgentBeats"""
    return {
        "a2a_version": "1.0",
        "name": "MathESO Evaluator",
        "version": "1.0.0",
        "description": "Green Agent specialized in secondary school mathematics evaluation (ESO/Bachillerato)",
        "author": "Oscar Rojo",
        "domain": "mathematics_education",
        "education_level": "secondary",
        # ACTUALIZAR CAPABILITIES
        "capabilities": [
            "algebra", "geometry", "arithmetic", "statistics",
            "analytic_geometry", "trigonometry", "functions", 
            "sequences", "combinatorics", "patterns",
            "linear_algebra", "graphics"
        ],
        "supported_languages": ["es", "en", "eu"],
        "a2a_role": "green_agent",
        "benchmark_type": "educational_math",
        "evaluation_metrics": ["accuracy", "response_time", "categorical_analysis"],
        "task_types": ["problem_solving", "calculation", "reasoning"],
        "difficulty_levels": ["easy", "medium"],
        "total_tasks": len(green_agent.dataset), 
        "assessment_interface": {
            "start_endpoint": "/evaluate",
            "reset_endpoint": "/reset", 
            "status_endpoint": "/health",
            "info_endpoint": "/green-agent-card"
        },
        "features": [
            "multi_domain_math",
            "educational_focus", 
            "auto_scoring",
            "performance_metrics",
            "multi_language_support"
        ],
        "timestamp": datetime.now().isoformat()
    }

@app.post("/evaluate")
async def evaluate_agent_english(request: EvaluacionRequest):
    """
    Endpoint ESTÁNDAR AgentBeats (en inglés)
    """
    try:
        problemas = obtener_problemas_aleatorios(
            n=request.num_problemas,
            categoria=request.categoria,
            dificultad=request.dificultad
        )
        
        resultados = green_agent.evaluar_purple_agent(
            request.purple_agent_url, 
            problemas
        )
        
        print("DEBUG - Resultados completos:", resultados)
        
        return {
            "assessment_id": f"math_eso_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "status": "completed",
            "results": {
                "overall_score": resultados["metricas_generales"]["accuracy_general"],
                "total_score": resultados["metricas_generales"]["puntuacion_total"],
                "max_score": resultados["metricas_generales"]["puntuacion_maxima"],
                "average_response_time": resultados["metricas_generales"]["tiempo_promedio_respuesta"],
                "tasks_completed": resultados["metricas_generales"]["problemas_correctos"],
                "total_tasks": resultados["metricas_generales"]["total_problemas"]
            },
            "detailed_results": resultados["resultados_detallados"],
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"ERROR en evaluate: {str(e)}")
        return {
            "status": "error", 
            "error_message": str(e),
            "timestamp": datetime.now().isoformat()
        }

@app.post("/evaluate-es")
async def evaluate_agent_spanish(request: EvaluacionRequest):
    """
    Endpoint en español para evaluación
    """
    try:
        problemas = obtener_problemas_aleatorios(
            n=request.num_problemas,
            categoria=request.categoria,
            dificultad=request.dificultad
        )
        
        resultados = green_agent.evaluar_purple_agent(
            request.purple_agent_url, 
            problemas
        )
        
        return {
            "evaluacion_id": f"math_eso_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "estado": "completado",
            "metricas": {
                "precision_general": resultados["metricas_generales"]["accuracy_general"],
                "puntuacion_total": resultados["metricas_generales"]["puntuacion_total"],
                "puntuacion_maxima": resultados["metricas_generales"]["puntuacion_maxima"],
                "tiempo_promedio": resultados["metricas_generales"]["tiempo_promedio_respuesta"],
                "problemas_correctos": resultados["metricas_generales"]["problemas_correctos"],
                "total_problemas": resultados["metricas_generales"]["total_problemas"]
            },
            "resultados_detallados": resultados["resultados_detallados"],
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "estado": "error", 
            "mensaje_error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@app.get("/problems")
async def listar_problemas(categoria: str = None, dificultad: str = None):
    """Lista los problemas disponibles para evaluación"""
    problemas = green_agent.dataset
    
    if categoria:
        problemas = [p for p in problemas if p["categoria"] == categoria]
    if dificultad:
        problemas = [p for p in problemas if p["dificultad"] == dificultad]
        
    return {
        "total_problems": len(problemas),
        "filters": {"categoria": categoria, "dificultad": dificultad},
        "problems": problemas
    }

@app.get("/health")
async def health_check():
    """Health check para AgentBeats"""
    return {
        "status": "healthy",
        "service": "MathESO Evaluator - Green Agent",
        "timestamp": datetime.now().isoformat(),
        "a2a_compliant": True
    }

@app.post("/reset")
async def reset_evaluation():
    """
    Endpoint A2A para resetear el estado de evaluación
    """
    return {
        "status": "success",
        "message": "Evaluation state reset successfully",
        "timestamp": datetime.now().isoformat(),
        "a2a_compliant": True
    }

if __name__ == "__main__":
    print("🟢 MathESO Evaluator - Green Agent iniciado")
    print("📚 Especializado en evaluación matemática ESO/Bachillerato")
    print("🌐 Endpoints disponibles:")
    print("   POST /evaluate     - Evaluación en inglés (AgentBeats)")
    print("   POST /evaluate-es  - Evaluación en español")
    print("   GET  /problems     - Listar problemas")
    print("   GET  /health       - Health check")
    print("   POST /reset        - Resetear evaluación")
    uvicorn.run(app, host="0.0.0.0", port=8001)