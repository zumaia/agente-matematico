from groq import Groq

# Configuración de Groq
client = Groq(api_key="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")  # 🔑 Reemplaza con tu key

def resolver_con_groq(problema: str):
    """Usa Groq para resolver problemas complejos con IA"""
    try:
        print(f"🤖 Intentando resolver con Groq: {problema}")
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system", 
                    "content": "Eres un tutor de matemáticas experto en ESO. Resuelve problemas paso a paso de forma clara y educativa."
                },
                {
                    "role": "user", 
                    "content": f"Resuelve este problema matemático de ESO paso a paso: {problema}"
                }
            ],
            temperature=0.3,
            max_tokens=1024
        )
        
        respuesta = response.choices[0].message.content
        
        return {
            "tipo": "ia_groq",
            "solucion": "Resuelto con IA Groq",
            "pasos": [respuesta],
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