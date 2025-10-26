import re
import math

def resolver_combinatoria(problema: str) -> dict:
    """
    Resuelve problemas de combinatoria para ESO
    """
    problema = problema.lower().strip()
    
    # Detección ampliada: frases del tipo "ordenar 3 libros" deben mapear a permutaciones
    if any(palabra in problema for palabra in ['permutación', 'permutacion', 'factorial', '!']) \
       or 'ordenar' in problema and 'libro' in problema:
        return resolver_permutaciones(problema)
    elif any(palabra in problema for palabra in ['combinación', 'combinacion', 'combinaciones']):
        return resolver_combinaciones(problema)
    elif any(palabra in problema for palabra in ['variación', 'variacion', 'variaciones']):
        return resolver_variaciones(problema)
    else:
        return None

def resolver_permutaciones(problema: str) -> dict:
    """
    Resuelve permutaciones: P(n) = n!
    """
    try:
        numeros = [int(float(x)) for x in re.findall(r'\d+', problema)]
        
        if numeros:
            n = numeros[0]
            resultado = math.factorial(n)
            
            pasos = [f"1. Número de elementos: n = {n}"]
            
            # Mostrar desarrollo del factorial
            desarrollo = " × ".join(str(i) for i in range(1, n+1))
            if n > 5:  # Para números grandes, mostrar primeros y últimos
                desarrollo = "1 × 2 × 3 × ... × " + str(n)
            
            pasos.extend([
                f"2. Fórmula: P(n) = n! = {desarrollo}",
                f"3. Resultado: {n}! = {resultado}"
            ])
            
            return {
                "tipo": "permutaciones",
                "solucion": f"P({n}) = {resultado}",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

def resolver_combinaciones(problema: str) -> dict:
    """
    Resuelve combinaciones: C(n,k) = n! / (k!(n-k)!)
    """
    try:
        numeros = [int(float(x)) for x in re.findall(r'\d+', problema)]
        
        if len(numeros) >= 2:
            n, k = numeros[0], numeros[1]
            
            if k > n:
                return {
                    "tipo": "combinaciones_error",
                    "solucion": f"Error: k ({k}) no puede ser mayor que n ({n})",
                    "pasos": ["k debe ser menor o igual que n"]
                }
            
            resultado = math.comb(n, k)
            
            pasos = [
                f"1. Número total de elementos: n = {n}",
                f"2. Número de elementos a elegir: k = {k}",
                f"3. Fórmula: C(n,k) = n! / (k! × (n-k)!)",
                f"4. C({n},{k}) = {n}! / ({k}! × {n-k}!)",
                f"5. Resultado: C({n},{k}) = {resultado}"
            ]
            
            return {
                "tipo": "combinaciones",
                "solucion": f"C({n},{k}) = {resultado}",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

def resolver_variaciones(problema: str) -> dict:
    """
    Resuelve variaciones: V(n,k) = n! / (n-k)!
    """
    try:
        numeros = [int(float(x)) for x in re.findall(r'\d+', problema)]
        
        if len(numeros) >= 2:
            n, k = numeros[0], numeros[1]
            
            if k > n:
                return {
                    "tipo": "variaciones_error",
                    "solucion": f"Error: k ({k}) no puede ser mayor que n ({n})",
                    "pasos": ["k debe ser menor o igual que n"]
                }
            
            resultado = math.perm(n, k)
            
            pasos = [
                f"1. Número total de elementos: n = {n}",
                f"2. Número de elementos a elegir: k = {k}",
                f"3. Fórmula: V(n,k) = n! / (n-k)!",
                f"4. V({n},{k}) = {n}! / {n-k}!",
                f"5. Resultado: V({n},{k}) = {resultado}"
            ]
            
            return {
                "tipo": "variaciones",
                "solucion": f"V({n},{k}) = {resultado}",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

# Funciones auxiliares
def factorial(n: int) -> int:
    return math.factorial(n)

def combinaciones(n: int, k: int) -> int:
    return math.comb(n, k)

def variaciones(n: int, k: int) -> int:
    return math.perm(n, k)