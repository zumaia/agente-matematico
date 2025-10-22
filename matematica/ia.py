from groq import Groq
import os
from dotenv import load_dotenv
from .procesador_groq import procesar_respuesta_groq

# Cargar variables del archivo .env
load_dotenv()

# Ahora puedes usar las variables de entorno
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Tu código sigue igual...
client = Groq(api_key=GROQ_API_KEY)

def resolver_con_groq(problema: str):
    """Usa Groq para resolver problemas complejos con IA"""
    try:
        print(f"🤖 Intentando resolver con Groq: {problema}")
        
        # Prompt mejorado para obtener respuestas más estructuradas
        prompt_mejorado = f"""
Resuelve el siguiente problema matemático paso a paso. 

**Formato requerido:**
1. Primero da la solución final claramente
2. Luego explica los pasos detallados numerados
3. Usa lenguaje claro y educativo
4. Sé conciso pero completo

**Problema:** {problema}

**Resolución:**
"""
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system", 
                    "content": "Eres un tutor de matemáticas experto en ESO. Resuelve problemas paso a paso de forma clara y educativa. Siempre estructura tu respuesta con: 1) Solución final clara, 2) Pasos numerados detallados."
                },
                {
                    "role": "user", 
                    "content": prompt_mejorado
                }
            ],
            temperature=0.3,
            max_tokens=1024
        )
        
        respuesta = response.choices[0].message.content
        
        # PROCESAR la respuesta de Groq para darle formato estructurado
        resultado_procesado = procesar_respuesta_groq(respuesta, problema)
        
        return {
            "tipo": resultado_procesado["tipo"],
            "solucion": resultado_procesado["solucion"],
            "pasos": resultado_procesado["pasos"],
            "modelo": "llama3-8b-8192",
            "exito": True
        }
        
    except Exception as e:
        print(f"❌ Error con Groq: {e}")
        return {
            "tipo": "error_groq",
            "solucion": f"Error: {str(e)}",
            "pasos": ["No se pudo conectar con el servicio de IA"],
            "exito": False
        }