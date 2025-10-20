from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse
import os
import json
from pydantic import BaseModel
import uvicorn
from matematica import algebra, geometria, aritmetica, estadistica, patrones, cache
from matematica.algebra import resolver_ecuacion_lineal, sistemas_ecuaciones
from matematica.geometria import calcular_area, teorema_pitagoras, calcular_volumen
from matematica.aritmetica import operaciones_fracciones, calcular_porcentajes
from matematica.estadistica import calcular_media, calcular_mediana, calcular_moda, calcular_rango, probabilidad_basica
from matematica.patrones import priorizar_resolutores, analizar_intencion
from matematica.ia import resolver_con_groq
from matematica.cache import cache_global
from matematica.utils import procesar_pasos_detallados

app = FastAPI(
    title="Agente Matemático Inteligente ESO+",
    description="Resuelve problemas de matemáticas con IA Gratuita",
    version="4.0.0"
)

# Crear carpeta static si no existe
os.makedirs("static", exist_ok=True)

# Configurar templates y archivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta para favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

class ProblemaRequest(BaseModel):
    problema: str

# INTERFAZ WEB - ÚNICA RUTA PRINCIPAL
@app.get("/", response_class=HTMLResponse)
async def interfaz_web(request: Request):
    """Página principal con interfaz web"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api")
def home():
    return {
        "mensaje": "¡Agente Matemático Mejorado! 🎯", 
        "version": "4.0.0",
        "arquitectura": "modular",
        "modulos": ["algebra", "geometria", "aritmetica", "estadistica", "patrones", "cache", "ia"],
        "mejoras": ["+5 funciones estadísticas", "detección de intención", "sistema de cache"]
    }

@app.post("/resolver-web")
async def resolver_problema_web(problema: str = Form(...), request: Request = None):
    """Endpoint web que devuelve HTML con la solución"""
    print(f"🔍 Problema recibido en resolver-web: '{problema}'")
    
    # PRIMERO: Verificar cache
    respuesta_cache = cache_global.obtener(problema)
    if respuesta_cache:
        resultado = {**respuesta_cache, "metodo": "cache", "estado": "resuelto"}
        # PROCESAR PASOS ANTES DE ENVIAR AL TEMPLATE
        if 'pasos_detallados' in resultado:
            resultado['pasos_detallados'] = procesar_pasos_detallados(resultado['pasos_detallados'])
        return templates.TemplateResponse("solucion.html", {"request": request, "resultado": resultado})
    
    # Lista completa de resolutores
    resolutores_base = [
        resolver_ecuacion_lineal,
        calcular_area,
        operaciones_fracciones, 
        calcular_porcentajes,
        teorema_pitagoras,
        calcular_volumen,
        sistemas_ecuaciones,
        calcular_media,
        calcular_mediana,
        calcular_moda,
        calcular_rango,
        probabilidad_basica
    ]
    
    # SEGUNDO: Priorizar resolutores basado en el problema
    resolutores_priorizados = priorizar_resolutores(problema, resolutores_base)
    
    print(f"🔧 Resolutores priorizados: {[r.__name__ for r in resolutores_priorizados]}")
    
    # TERCERO: Intentar con funciones matemáticas
    for resolutor in resolutores_priorizados:
        solucion = resolutor(problema)
        if solucion:
            print(f"✅ Resuelto con {resolutor.__name__}: {solucion['tipo']}")
            resultado = {
                "problema": problema,
                "solucion": solucion["solucion"],
                "tipo_problema": solucion["tipo"],
                "pasos_detallados": procesar_pasos_detallados(solucion["pasos"]),  # PROCESAR AQUÍ
                "metodo": "algoritmo_matematico",
                "estado": "resuelto"
            }
            # Guardar en cache
            cache_global.guardar(problema, resultado)
            return templates.TemplateResponse("solucion.html", {"request": request, "resultado": resultado})
    
    # CUARTO: Usar Groq para problemas complejos
    print("🔄 Usando Groq IA...")
    try:
        solucion_ia = resolver_con_groq(problema)
        
        if solucion_ia["exito"]:
            resultado = {
                "problema": problema,
                "solucion": solucion_ia["solucion"],
                "tipo_problema": solucion_ia["tipo"],
                "pasos_detallados": procesar_pasos_detallados(solucion_ia["pasos"]),  # PROCESAR AQUÍ
                "modelo_ia": solucion_ia["modelo"],
                "metodo": "ia_groq",
                "estado": "resuelto"
            }
            # Guardar respuesta de IA en cache
            cache_global.guardar(problema, resultado)
            return templates.TemplateResponse("solucion.html", {"request": request, "resultado": resultado})
        else:
            resultado = {
                "problema": problema,
                "solucion": solucion_ia["solucion"],
                "tipo_problema": solucion_ia["tipo"],
                "pasos_detallados": procesar_pasos_detallados(solucion_ia["pasos"]),  # PROCESAR AQUÍ
                "estado": "error"
            }
            return templates.TemplateResponse("solucion.html", {"request": request, "resultado": resultado})
            
    except Exception as e:
        print(f"❌ Error con Groq: {e}")
        resultado = {
            "problema": problema,
            "solucion": f"Error interno: {str(e)}",
            "tipo_problema": "error_interno",
            "pasos_detallados": ["Error en la función Groq"],
            "estado": "error"
        }
        return templates.TemplateResponse("solucion.html", {"request": request, "resultado": resultado})

@app.get("/cache/estado")
def estado_cache():
    """Endpoint para ver el estado del cache"""
    return {
        "total_entradas": len(cache_global.cache),
        "archivo": cache_global.archivo
    }

@app.delete("/cache/limpiar")
def limpiar_cache():
    """Endpoint para limpiar el cache"""
    cache_global.cache = {}
    cache_global.guardar_cache()
    return {"mensaje": "Cache limpiado correctamente"}

if __name__ == "__main__":
    print("🚀 Servidor iniciado - Agente Mejorado v4.0")
    print("📊 Nuevas capacidades: Estadística + Patrones + Cache")
    uvicorn.run(app, host="0.0.0.0", port=8000)