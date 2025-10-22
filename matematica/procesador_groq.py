# matematica/procesador_groq.py
import re
from typing import Dict, List

def procesar_respuesta_groq(texto_respuesta: str, problema: str) -> Dict:
    """
    Convierte la respuesta de texto de Groq en el formato estructurado
    que usan nuestras funciones matemáticas
    """
    
    # Limpiar y estandarizar el texto
    texto_limpio = texto_respuesta.strip()
    
    # Extraer la solución principal (primera línea o párrafo)
    solucion_principal = extraer_solucion_principal(texto_limpio)
    
    # Extraer pasos detallados
    pasos_detallados = extraer_pasos_detallados(texto_limpio)
    
    # Determinar tipo de problema
    tipo_problema = determinar_tipo_problema(problema, texto_limpio)
    
    return {
        "solucion": solucion_principal,
        "tipo": tipo_problema,
        "pasos": pasos_detallados,
        "exito": True,
        "modelo": "groq-procesado"
    }

def extraer_solucion_principal(texto: str) -> str:
    """Extrae la solución principal del texto"""
    # Buscar patrones comunes de respuestas
    patrones = [
        r'respuesta[:\s]*([^\n\.]+)',
        r'solución[:\s]*([^\n\.]+)', 
        r'resultado[:\s]*([^\n\.]+)',
        r'=?\s*([0-9\.\,\-\+\/\*\(\)\s]+)$',
        r'^([^\.\n]+?)(?:\.|\n|$)'
    ]
    
    for patron in patrones:
        match = re.search(patron, texto, re.IGNORECASE)
        if match:
            solucion = match.group(1).strip()
            if len(solucion) > 5:  # Evitar soluciones muy cortas
                return solucion.capitalize()
    
    # Si no encuentra patrón, tomar las primeras 100 caracteres
    return texto[:100].strip() + "..."

def extraer_pasos_detallados(texto: str) -> List[str]:
    """Extrae y formatea los pasos detallados"""
    pasos = []
    
    # Dividir por números de paso (1., 2., Paso 1, etc.)
    patrones_divisor = [
        r'\n\s*(\d+\.)\s*',
        r'\n\s*Paso\s*(\d+)[:\-]?\s*',
        r'\n\s*•\s*',
        r'\n\s*-\s*',
        r'\n\s*\*\s*'
    ]
    
    texto_dividido = texto
    for patron in patrones_divisor:
        texto_dividido = re.sub(patron, '||PASO||', texto_dividido)
    
    # Dividir y limpiar pasos
    partes = texto_dividido.split('||PASO||')
    for parte in partes[1:]:  # Saltar la primera parte (solución principal)
        paso_limpio = limpiar_paso(parte.strip())
        if paso_limpio and len(paso_limpio) > 10:  # Mínimo 10 caracteres
            pasos.append(paso_limpio)
    
    # Si no se pudieron dividir los pasos, dividir por oraciones
    if not pasos:
        oraciones = re.split(r'[\.!?]\s+', texto)
        for oracion in oraciones[1:3]:  # Tomar primeras 2-3 oraciones como pasos
            oracion_limpia = limpiar_paso(oracion.strip())
            if oracion_limpia and len(oracion_limpia) > 10:
                pasos.append(oracion_limpia)
    
    return pasos if pasos else ["Proceso de resolución detallado en la explicación completa."]

def limpiar_paso(texto: str) -> str:
    """Limpia un paso individual"""
    if not texto:
        return ""
    
    # Remover markdown básico
    texto = re.sub(r'\*\*(.*?)\*\*', r'\1', texto)
    texto = re.sub(r'\*(.*?)\*', r'\1', texto)
    texto = re.sub(r'`(.*?)`', r'\1', texto)
    
    # Remover espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)
    
    # Capitalizar primera letra
    if texto and len(texto) > 1:
        texto = texto[0].upper() + texto[1:]
    
    return texto.strip()

def determinar_tipo_problema(problema: str, respuesta: str) -> str:
    """Determina el tipo de problema basado en palabras clave"""
    problema = problema.lower()
    respuesta = respuesta.lower()
    
    tipos = {
        "algebra": ["ecuación", "x", "y", "variable", "despejar", "polinomio"],
        "geometria": ["área", "perímetro", "volumen", "triángulo", "círculo", "radio", "diámetro"],
        "aritmetica": ["fracción", "porcentaje", "suma", "resta", "multiplicación", "división"],
        "estadistica": ["media", "mediana", "moda", "probabilidad", "estadística", "promedio"],
        "trigonometria": ["seno", "coseno", "tangente", "ángulo", "triángulo", "grados"],
        "sucesiones": ["sucesión", "patrón", "secuencia", "término"],
        "combinatoria": ["combinación", "permutación", "variación", "combinatoria"]
    }
    
    for tipo, palabras_clave in tipos.items():
        for palabra in palabras_clave:
            if palabra in problema or palabra in respuesta:
                return tipo
    
    return "general"