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

def calcular_porcentajes(problema: str):
    """Calcula porcentajes"""
    problema_lower = problema.lower()
    match = re.search(r"(\d+)\s*%\s*de\s*(\d+)", problema_lower)
    if match:
        porcentaje = int(match.group(1))
        cantidad = int(match.group(2))
        resultado = (cantidad * porcentaje) / 100
        return {
            "tipo": "porcentaje",
            "solucion": f"El {porcentaje}% de {cantidad} es {resultado}",
            "pasos": [
                f"Fórmula: (cantidad × porcentaje) / 100",
                f"Sustitución: ({cantidad} × {porcentaje}) / 100",
                f"Cálculo: {resultado}"
            ]
        }

    numeros = [int(n) for n in re.findall(r'\d+', problema)]
    if not numeros:
        return None

    if len(numeros) >= 2:
        if "%" in problema_lower:
            porcentaje, cantidad = numeros[0], numeros[1]
        else:
            cantidad, porcentaje = numeros[0], numeros[1]

        resultado = (cantidad * porcentaje) / 100
        return {
            "tipo": "porcentaje",
            "solucion": f"El {porcentaje}% de {cantidad} es {resultado}",
            "pasos": [
                f"Fórmula: (cantidad × porcentaje) / 100",
                f"Sustitución: ({cantidad} × {porcentaje}) / 100",
                f"Cálculo: {resultado}"
            ]
        }
    
    return None
