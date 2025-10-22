import re
from math import gcd

def operaciones_fracciones(problema: str):
    """Realiza operaciones con fracciones"""
    problema_lower = problema.lower()
    
    # Suma de fracciones: 1/2 + 1/3
    patron_suma = r'(\d+)/(\d+)\s*\+\s*(\d+)/(\d+)'
    match_suma = re.search(patron_suma, problema)
    
    if match_suma:
        a, b, c, d = int(match_suma.group(1)), int(match_suma.group(2)), int(match_suma.group(3)), int(match_suma.group(4))
        mcm = (b * d) // gcd(b, d)
        numerador = (a * (mcm // b)) + (c * (mcm // d))
        gcd_result = gcd(numerador, mcm)
        numerador_simpl = numerador // gcd_result
        denominador_simpl = mcm // gcd_result

        return {
            "tipo": "suma_fracciones",
            "solucion": f"Resultado: {numerador_simpl}/{denominador_simpl}",
            "pasos": [
                f"Fracciones: {a}/{b} + {c}/{d}",
                f"Mínimo común múltiplo: {mcm}",
                f"Numerador común: ({a}×{mcm//b}) + ({c}×{mcm//d}) = {numerador}",
                f"Fracción antes de simplificar: {numerador}/{mcm}",
                f"Fracción simplificada: {numerador_simpl}/{denominador_simpl}"
            ]
        }
    
    # Multiplicación de fracciones: 2/3 * 4/5
    patron_mult = r'(\d+)/(\d+)\s*\*\s*(\d+)/(\d+)'
    match_mult = re.search(patron_mult, problema)
    
    if match_mult:
        a, b, c, d = int(match_mult.group(1)), int(match_mult.group(2)), int(match_mult.group(3)), int(match_mult.group(4))
        numerador = a * c
        denominador = b * d
        return {
            "tipo": "multiplicacion_fracciones",
            "solucion": f"Resultado: {numerador}/{denominador}",
            "pasos": [
                f"Fracciones: {a}/{b} × {c}/{d}",
                f"Numeradores: {a} × {c} = {numerador}",
                f"Denominadores: {b} × {d} = {denominador}",
                f"Resultado: {numerador}/{denominador}"
            ]
        }
    
    return None

def calcular_porcentajes(problema):
    """
    Calcula porcentajes - VERSIÓN CORREGIDA
    """
    problema_limpio = problema.lower()
    
    # PRIMERO: Buscar patrones de descuento específicos
    patron_descuento = r'(\d+)\s*euros?\s*(?:con|de|tiene)\s*(\d+)%?\s*descuento'
    match_descuento = re.search(patron_descuento, problema_limpio)
    
    if match_descuento:
        precio_original = float(match_descuento.group(1))
        porcentaje_descuento = float(match_descuento.group(2))
        
        descuento = (porcentaje_descuento * precio_original) / 100
        precio_final = precio_original - descuento
        
        return {
            "solucion": f"Precio final: {precio_final} euros (descuento de {descuento} euros)",
            "tipo": "porcentaje_descuento",
            "pasos": [
                f"Precio original: {precio_original} euros",
                f"Porcentaje de descuento: {porcentaje_descuento}%",
                f"Descuento = ({porcentaje_descuento} × {precio_original}) / 100 = {descuento} euros",
                f"Precio final = {precio_original} - {descuento} = {precio_final} euros"
            ]
        }
    
    # SEGUNDO: Buscar patrones de aumento
    patron_aumento = r'(\d+)\s*euros?\s*(?:con|de|tiene)\s*(\d+)%?\s*(?:aumento|incremento)'
    match_aumento = re.search(patron_aumento, problema_limpio)
    
    if match_aumento:
        precio_original = float(match_aumento.group(1))
        porcentaje_aumento = float(match_aumento.group(2))
        
        aumento = (porcentaje_aumento * precio_original) / 100
        precio_final = precio_original + aumento
        
        return {
            "solucion": f"Precio final: {precio_final} euros (aumento de {aumento} euros)",
            "tipo": "porcentaje_aumento",
            "pasos": [
                f"Precio original: {precio_original} euros",
                f"Porcentaje de aumento: {porcentaje_aumento}%",
                f"Aumento = ({porcentaje_aumento} × {precio_original}) / 100 = {aumento} euros",
                f"Precio final = {precio_original} + {aumento} = {precio_final} euros"
            ]
        }
    
    # TERCERO: Búsqueda general de porcentajes
    patron_general = r'(\d+)%?\s*de\s*(\d+)'
    match_general = re.search(patron_general, problema_limpio)
    
    if match_general:
        porcentaje = float(match_general.group(1))
        cantidad = float(match_general.group(2))
        
        resultado = (porcentaje * cantidad) / 100
        
        return {
            "solucion": f"El {porcentaje}% de {cantidad} es {resultado}",
            "tipo": "porcentaje_simple",
            "pasos": [
                f"Fórmula: (porcentaje × cantidad) / 100",
                f"Sustitución: ({porcentaje} × {cantidad}) / 100",
                f"Cálculo: {resultado}"
            ]
        }
    
    return None