# green_agent/config_urgencia.py
"""
Configuración de emergencia para corregir el problema de extracción
"""

CONFIG_EXTRACCION_URGENTE = {
    "patrones_excluir": [
        "Problema 2",
        "Volver al Inicio", 
        "Powered by FastAPI",
        "Groq AI",
        "Ver solución",
        "Media Calcula",
        "área de un triángulo"
    ],
    "longitud_maxima_respuesta": 50,  # Caracteres máximos para una respuesta válida
    "numeros_excluir": ['5', '6', '4', '12']  # Números del problema ejemplo
}

def es_respuesta_valida(respuesta: str) -> bool:
    """Verifica si una respuesta parece ser válida (no una página de error)"""
    if not respuesta or respuesta == "No se pudo extraer solución":
        return False
    
    # Excluir respuestas que contengan texto de error
    for patron in CONFIG_EXTRACCION_URGENTE["patrones_excluir"]:
        if patron in respuesta:
            return False
    
    # Excluir respuestas demasiado largas (probablemente páginas completas)
    if len(respuesta) > CONFIG_EXTRACCION_URGENTE["longitud_maxima_respuesta"]:
        return False
    
    return True