"""
Configuración de emergencia para problemas de extracción
"""

EMERGENCY_PATTERNS = {
    "html_indicators": [
        "<div", "<span", "<style", "language-switcher",
        "practice_title", "Ver solución", "Volver al Inicio"
    ],
    "generic_answers": [
        "x = 5", "x = 5.0", "x = 5.00", "x=5",
        "= 12", "Área = 12"
    ],
    "error_indicators": [
        "🏠", "Powered by FastAPI", "Groq AI",
        "Agente Matemático ESO+", "cache problema"
    ]
}

def is_html_response(text: str) -> bool:
    """Detecta si la respuesta es HTML completo"""
    return any(indicator in text for indicator in EMERGENCY_PATTERNS["html_indicators"])

def is_generic_answer(answer: str, correct_answer: str) -> bool:
    """Detecta si la respuesta es genérica e incorrecta"""
    clean_answer = answer.strip().lower()
    clean_correct = correct_answer.strip().lower()
    
    return (clean_answer in [g.lower() for g in EMERGENCY_PATTERNS["generic_answers"]] 
            and clean_answer != clean_correct)