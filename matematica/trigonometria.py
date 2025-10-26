import math
import re

def resolver_trigonometria(problema: str) -> dict:
    """
    Resuelve problemas de trigonometría básica para ESO
    """
    problema = problema.lower().strip()
    
    # Detectar tipo de problema trigonométrico
    if any(palabra in problema for palabra in ['seno', 'sin ', 'coseno', 'cos ', 'tangente', 'tan ']):
        return resolver_razones_trigonometricas(problema)
    elif any(palabra in problema for palabra in ['triángulo', 'triangulo', 'ángulo', 'angulo', 'hipotenusa', 'cateto']):
        return resolver_triangulo_rectangulo(problema)
    elif any(palabra in problema for palabra in ['teorema del seno', 'teorema del coseno', 'ley de senos', 'ley de cosenos']):
        return resolver_teorema_seno_coseno(problema)
    else:
        return None

def resolver_razones_trigonometricas(problema: str) -> dict:
    """
    Resuelve problemas de razones trigonométricas
    """
    try:
        # Patrón para encontrar ángulos y valores
        angulo_match = re.search(r'(\d+(?:\.\d+)?)\s*grados', problema)
        valor_match = re.search(r'(seno|coseno|tangente)\s*(?:de|of)?\s*(\d+(?:\.\d+)?)', problema)
        
        if angulo_match and valor_match:
            angulo = float(angulo_match.group(1))
            funcion = valor_match.group(1)
            angulo_rad = math.radians(angulo)
            
            if funcion == 'seno':
                resultado = math.sin(angulo_rad)
            elif funcion == 'coseno':
                resultado = math.cos(angulo_rad)
            elif funcion == 'tangente':
                resultado = math.tan(angulo_rad)
            else:
                return None
            
            pasos = [
                f"1. Convertir {angulo}° a radianes: {angulo}° × π/180 = {angulo_rad:.4f} rad",
                f"2. Calcular {funcion}({angulo_rad:.4f})",
                f"3. Resultado: {funcion}({angulo}°) = {resultado:.4f}"
            ]
            
            # Devolver la solución en formato canónico: solo el valor numérico (p.ej. 0.5)
            val = ('{:.4f}'.format(resultado)).rstrip('0').rstrip('.')
            return {
                "tipo": "razones_trigonometricas",
                "solucion": f"{val}",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

def resolver_triangulo_rectangulo(problema: str) -> dict:
    """
    Resuelve problemas de triángulos rectángulos usando trigonometría
    """
    try:
        # Extraer valores numéricos del problema
        numeros = [float(x) for x in re.findall(r'(\d+(?:\.\d+)?)', problema)]
        
        if len(numeros) >= 2:
            # Suponer que son cateto opuesto y adyacente
            co, ca = numeros[0], numeros[1]
            hipotenusa = math.sqrt(co**2 + ca**2)
            
            # Calcular ángulos
            angulo_alpha = math.degrees(math.atan(co/ca))
            angulo_beta = 90 - angulo_alpha
            
            pasos = [
                f"1. Calcular hipotenusa: √({co}² + {ca}²) = √{co**2 + ca**2} = {hipotenusa:.2f}",
                f"2. Ángulo α = arctan({co}/{ca}) = {angulo_alpha:.1f}°",
                f"3. Ángulo β = 90° - {angulo_alpha:.1f}° = {angulo_beta:.1f}°",
                f"4. Verificación: {angulo_alpha:.1f}° + {angulo_beta:.1f}° + 90° = 180°"
            ]
            
            return {
                "tipo": "triangulo_rectangulo",
                "solucion": f"Triángulo rectángulo: Hipotenusa = {hipotenusa:.2f}, Ángulos = {angulo_alpha:.1f}° y {angulo_beta:.1f}°",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

def resolver_teorema_seno_coseno(problema: str) -> dict:
    """
    Resuelve problemas usando teorema del seno o coseno
    """
    try:
        numeros = [float(x) for x in re.findall(r'(\d+(?:\.\d+)?)', problema)]
        
        if len(numeros) >= 3:
            a, b, c = numeros[0], numeros[1], numeros[2]
            
            # Teorema del coseno para encontrar un ángulo
            cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
            angulo_A = math.degrees(math.acos(cos_A))
            
            pasos = [
                f"1. Aplicar teorema del coseno: cos(A) = (b² + c² - a²) / (2bc)",
                f"2. cos(A) = ({b}² + {c}² - {a}²) / (2×{b}×{c})",
                f"3. cos(A) = ({b**2} + {c**2} - {a**2}) / {2*b*c} = {cos_A:.4f}",
                f"4. Ángulo A = arccos({cos_A:.4f}) = {angulo_A:.1f}°"
            ]
            
            return {
                "tipo": "teorema_coseno",
                "solucion": f"Ángulo A = {angulo_A:.1f}° (usando teorema del coseno)",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

# Funciones adicionales para cálculos específicos
def calcular_seno(angulo_grados: float) -> float:
    return math.sin(math.radians(angulo_grados))

def calcular_coseno(angulo_grados: float) -> float:
    return math.cos(math.radians(angulo_grados))

def calcular_tangente(angulo_grados: float) -> float:
    return math.tan(math.radians(angulo_grados))

def calcular_hipotenusa(cateto1: float, cateto2: float) -> float:
    return math.sqrt(cateto1**2 + cateto2**2)