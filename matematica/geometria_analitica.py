import re
import math

def resolver_geometria_analitica(problema: str) -> dict:
    """
    Resuelve problemas de geometría analítica para ESO
    """
    problema = problema.lower().strip()
    
    if any(palabra in problema for palabra in ['distancia', 'puntos', 'coordenadas']):
        return resolver_distancia_entre_puntos(problema)
    elif any(palabra in problema for palabra in ['ecuación de la recta', 'ecuacion de la recta', 'pendiente']):
        return resolver_ecuacion_recta(problema)
    elif any(palabra in problema for palabra in ['punto medio', 'mitad']):
        return resolver_punto_medio(problema)
    else:
        return None

def resolver_distancia_entre_puntos(problema: str) -> dict:
    """
    Resuelve distancia entre dos puntos: d = √((x2-x1)² + (y2-y1)²)
    """
    try:
        numeros = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', problema)]
        
        if len(numeros) >= 4:
            x1, y1, x2, y2 = numeros[0], numeros[1], numeros[2], numeros[3]
            distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            
            pasos = [
                f"1. Punto A: ({x1}, {y1})",
                f"2. Punto B: ({x2}, {y2})",
                f"3. Fórmula: d = √[(x₂-x₁)² + (y₂-y₁)²]",
                f"4. d = √[({x2}-{x1})² + ({y2}-{y1})²]",
                f"5. d = √[({x2-x1})² + ({y2-y1})²]",
                f"6. d = √[{((x2-x1)**2)} + {((y2-y1)**2)}]",
                f"7. d = √{((x2-x1)**2 + (y2-y1)**2)} = {distancia:.2f}"
            ]
            
            return {
                "tipo": "distancia_entre_puntos",
                "solucion": f"Distancia = {distancia:.2f}",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

def resolver_ecuacion_recta(problema: str) -> dict:
    """
    Resuelve ecuación de la recta: y = mx + b
    """
    try:
        numeros = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', problema)]
        
        if len(numeros) >= 4:
            x1, y1, x2, y2 = numeros[0], numeros[1], numeros[2], numeros[3]
            
            # Calcular pendiente
            if x2 - x1 != 0:
                m = (y2 - y1) / (x2 - x1)
                # Calcular término independiente
                b = y1 - m * x1
                
                # Formatear ecuación
                if b >= 0:
                    ecuacion = f"y = {m:.2f}x + {b:.2f}"
                else:
                    ecuacion = f"y = {m:.2f}x - {abs(b):.2f}"
                
                pasos = [
                    f"1. Punto A: ({x1}, {y1})",
                    f"2. Punto B: ({x2}, {y2})",
                    f"3. Pendiente: m = (y₂-y₁)/(x₂-x₁) = ({y2}-{y1})/({x2}-{x1}) = {m:.2f}",
                    f"4. Ecuación punto-pendiente: y - y₁ = m(x - x₁)",
                    f"5. y - {y1} = {m:.2f}(x - {x1})",
                    f"6. y = {m:.2f}x + {b:.2f}",
                    f"7. Ecuación: {ecuacion}"
                ]
                
                return {
                    "tipo": "ecuacion_recta",
                    "solucion": f"Ecuación: {ecuacion}",
                    "pasos": pasos
                }
            else:
                return {
                    "tipo": "recta_vertical",
                    "solucion": f"Recta vertical: x = {x1}",
                    "pasos": ["Los puntos tienen la misma coordenada x", f"La recta es vertical: x = {x1}"]
                }
    except Exception as e:
        return None
    
    return None

def resolver_punto_medio(problema: str) -> dict:
    """
    Resuelve punto medio entre dos puntos: M = ((x1+x2)/2, (y1+y2)/2)
    """
    try:
        numeros = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', problema)]
        
        if len(numeros) >= 4:
            x1, y1, x2, y2 = numeros[0], numeros[1], numeros[2], numeros[3]
            xm = (x1 + x2) / 2
            ym = (y1 + y2) / 2
            
            pasos = [
                f"1. Punto A: ({x1}, {y1})",
                f"2. Punto B: ({x2}, {y2})",
                f"3. Fórmula: M = ((x₁+x₂)/2, (y₁+y₂)/2)",
                f"4. M = (({x1}+{x2})/2, ({y1}+{y2})/2)",
                f"5. M = ({x1+x2}/2, {y1+y2}/2)",
                f"6. M = ({xm}, {ym})"
            ]
            
            return {
                "tipo": "punto_medio",
                "solucion": f"Punto medio: ({xm}, {ym})",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

# Funciones auxiliares
def calcular_distancia(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calcular_pendiente(x1: float, y1: float, x2: float, y2: float) -> float:
    if x2 - x1 == 0:
        return float('inf')  # Recta vertical
    return (y2 - y1) / (x2 - x1)

def calcular_punto_medio(x1: float, y1: float, x2: float, y2: float) -> tuple:
    return ((x1 + x2) / 2, (y1 + y2) / 2)