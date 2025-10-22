import re
import math

def resolver_sucesiones(problema: str) -> dict:
    """
    Resuelve problemas de sucesiones y progresiones para ESO
    """
    problema = problema.lower().strip()
    
    if any(palabra in problema for palabra in ['progresión aritmética', 'sucesión aritmética', 'pa', 'diferencia constante']):
        return resolver_progresion_aritmetica(problema)
    elif any(palabra in problema for palabra in ['progresión geométrica', 'sucesión geométrica', 'pg', 'razón constante']):
        return resolver_progresion_geometrica(problema)
    elif any(palabra in problema for palabra in ['término general', 'término n-ésimo', 'sucesión', 'progresión']):
        return resolver_termino_general(problema)
    else:
        return None

def resolver_progresion_aritmetica(problema: str) -> dict:
    """
    Resuelve progresiones aritméticas: an = a1 + (n-1)*d
    """
    try:
        # Extraer números del problema
        numeros = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', problema)]
        
        if len(numeros) >= 3:
            # Suponer: primer término, diferencia, posición
            a1, d, n = numeros[0], numeros[1], numeros[2]
            termino_n = a1 + (n - 1) * d
            suma_n = n * (a1 + termino_n) / 2
            
            pasos = [
                f"1. Primer término (a₁) = {a1}",
                f"2. Diferencia (d) = {d}",
                f"3. Término en posición n = {n}",
                f"4. Fórmula: aₙ = a₁ + (n-1)×d",
                f"5. aₙ = {a1} + ({n}-1)×{d} = {a1} + {n-1}×{d} = {termino_n}",
                f"6. Suma de los primeros {n} términos: Sₙ = n×(a₁+aₙ)/2 = {n}×({a1}+{termino_n})/2 = {suma_n}"
            ]
            
            return {
                "tipo": "progresion_aritmetica",
                "solucion": f"Término aₙ = {termino_n}, Suma Sₙ = {suma_n}",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

def resolver_progresion_geometrica(problema: str) -> dict:
    """
    Resuelve progresiones geométricas: an = a1 * r^(n-1)
    """
    try:
        numeros = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', problema)]
        
        if len(numeros) >= 3:
            a1, r, n = numeros[0], numeros[1], numeros[2]
            termino_n = a1 * (r ** (n - 1))
            
            if r != 1:
                suma_n = a1 * (1 - r**n) / (1 - r)
            else:
                suma_n = a1 * n
            
            pasos = [
                f"1. Primer término (a₁) = {a1}",
                f"2. Razón (r) = {r}",
                f"3. Término en posición n = {n}",
                f"4. Fórmula: aₙ = a₁ × r^(n-1)",
                f"5. aₙ = {a1} × {r}^({n}-1) = {a1} × {r}^{n-1} = {termino_n}",
                f"6. Suma de los primeros {n} términos: Sₙ = {suma_n}"
            ]
            
            return {
                "tipo": "progresion_geometrica",
                "solucion": f"Término aₙ = {termino_n}, Suma Sₙ = {suma_n}",
                "pasos": pasos
            }
    except Exception as e:
        return None
    
    return None

def resolver_termino_general(problema: str) -> dict:
    """
    Encuentra el término general de una sucesión
    """
    try:
        numeros = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', problema)]
        
        if len(numeros) >= 3:
            # Detectar si es aritmética o geométrica
            a1, a2, a3 = numeros[0], numeros[1], numeros[2]
            
            # Verificar si es aritmética
            if a2 - a1 == a3 - a2:
                d = a2 - a1
                formula = f"aₙ = {a1} + (n-1)×{d}"
                pasos = [
                    f"1. Términos: {a1}, {a2}, {a3}",
                    f"2. Diferencia constante: {a2} - {a1} = {a3} - {a2} = {d}",
                    f"3. Es una progresión aritmética",
                    f"4. Término general: aₙ = a₁ + (n-1)×d",
                    f"5. Fórmula: {formula}"
                ]
                return {
                    "tipo": "termino_general_aritmetico",
                    "solucion": f"Término general: {formula}",
                    "pasos": pasos
                }
            
            # Verificar si es geométrica
            elif a2/a1 == a3/a2:
                r = a2 / a1
                formula = f"aₙ = {a1} × {r}^(n-1)"
                pasos = [
                    f"1. Términos: {a1}, {a2}, {a3}",
                    f"2. Razón constante: {a2}/{a1} = {a3}/{a2} = {r}",
                    f"3. Es una progresión geométrica",
                    f"4. Término general: aₙ = a₁ × r^(n-1)",
                    f"5. Fórmula: {formula}"
                ]
                return {
                    "tipo": "termino_general_geometrico",
                    "solucion": f"Término general: {formula}",
                    "pasos": pasos
                }
    except Exception as e:
        return None
    
    return None

# Funciones auxiliares
def encontrar_termino_aritmetica(primer_termino: float, diferencia: float, posicion: int) -> float:
    return primer_termino + (posicion - 1) * diferencia

def encontrar_termino_geometrica(primer_termino: float, razon: float, posicion: int) -> float:
    return primer_termino * (razon ** (posicion - 1))