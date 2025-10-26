import re
import math

def _format_num(x: float) -> str:
    """Formatea números para devolver enteros sin .0 cuando corresponda."""
    try:
        if abs(x - int(x)) < 1e-9:
            return str(int(x))
        return str(x)
    except Exception:
        return str(x)


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

        # detectar si piden "siguiente" término
        pide_siguiente = any(p in problema for p in ['siguiente', 'próximo', 'próxima', 'qué sigue', '¿siguiente', '¿próximo'])

        # intentar detectar un n explícito en el texto (posición n)
        m_n = re.search(r'posición\s*(?:n\s*)?[:=]?\s*(\d+)|n\s*=?\s*(\d+)', problema)
        n_en_texto = None
        if m_n:
            n_en_texto = int(m_n.group(1) or m_n.group(2))

        if len(numeros) >= 2:
            # si tenemos al menos dos términos, deducimos la diferencia
            a1 = numeros[0]
            # si los números parecen ser una lista de términos (ej: 2,4,6,...)
            if len(numeros) >= 2:
                d = numeros[1] - numeros[0]
            else:
                d = 0

            # si piden siguiente, calculamos el siguiente a partir del último término provisto
            if pide_siguiente or n_en_texto is None and len(numeros) > 2 and 'siguiente' in problema:
                ultimo = numeros[-1]
                siguiente = ultimo + d
                pasos = [
                    f"1. Términos conocidos: {', '.join(_format_num(x) for x in numeros)}",
                    f"2. Diferencia (d) estimada = {d}",
                    f"3. Siguiente término = {ultimo} + {d} = {siguiente}"
                ]
                return {
                    "tipo": "progresion_aritmetica",
                    "solucion": _format_num(siguiente),
                    "pasos": pasos
                }

            # si hay un n explícito, calcular a_n y la suma
            if n_en_texto is not None:
                a1 = numeros[0]
                n = n_en_texto
                termino_n = a1 + (n - 1) * d
                suma_n = n * (a1 + termino_n) / 2
                pasos = [
                    f"1. Primer término (a₁) = {a1}",
                    f"2. Diferencia (d) = {d}",
                    f"3. Término en posición n = {n}",
                    f"4. Fórmula: aₙ = a₁ + (n-1)×d",
                    f"5. aₙ = {a1} + ({n}-1)×{d} = {termino_n}",
                    f"6. Suma de los primeros {n} términos: Sₙ = n×(a₁+aₙ)/2 = {suma_n}"
                ]
                return {
                    "tipo": "progresion_aritmetica",
                    "solucion": _format_num(termino_n),
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

        pide_siguiente = any(p in problema for p in ['siguiente', 'próximo', 'próxima', 'qué sigue', '¿siguiente', '¿próximo'])
        m_n = re.search(r'posición\s*(?:n\s*)?[:=]?\s*(\d+)|n\s*=?\s*(\d+)', problema)
        n_en_texto = None
        if m_n:
            n_en_texto = int(m_n.group(1) or m_n.group(2))

        if len(numeros) >= 2:
            a1 = numeros[0]
            # deducir razón si es posible
            if len(numeros) >= 2 and numeros[0] != 0:
                r = numeros[1] / numeros[0]
            else:
                r = 1

            # siguiente término si se pide
            if pide_siguiente or (n_en_texto is None and len(numeros) > 2 and 'siguiente' in problema):
                ultimo = numeros[-1]
                siguiente = ultimo * r
                pasos = [
                    f"1. Términos conocidos: {', '.join(_format_num(x) for x in numeros)}",
                    f"2. Razón (r) estimada = {r}",
                    f"3. Siguiente término = {ultimo} × {r} = {siguiente}"
                ]
                return {
                    "tipo": "progresion_geometrica",
                    "solucion": _format_num(siguiente),
                    "pasos": pasos
                }

            if n_en_texto is not None:
                n = n_en_texto
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
                    f"5. aₙ = {a1} × {r}^({n}-1) = {termino_n}",
                    f"6. Suma de los primeros {n} términos: Sₙ = {suma_n}"
                ]
                return {
                    "tipo": "progresion_geometrica",
                    "solucion": _format_num(termino_n),
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
                # Si piden el siguiente término, devolver el valor numérico
                if any(p in problema for p in ['siguiente', 'próximo', 'próxima', 'qué sigue', '¿siguiente']):
                    ultimo = numeros[-1]
                    siguiente = ultimo + d
                    return {
                        "tipo": "termino_general_aritmetico",
                        "solucion": _format_num(siguiente),
                        "pasos": pasos + [f"6. Siguiente término = {ultimo} + {d} = {siguiente}"]
                    }

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
                if any(p in problema for p in ['siguiente', 'próximo', 'próxima', 'qué sigue', '¿siguiente']):
                    ultimo = numeros[-1]
                    siguiente = ultimo * r
                    return {
                        "tipo": "termino_general_geometrico",
                        "solucion": _format_num(siguiente),
                        "pasos": pasos + [f"6. Siguiente término = {ultimo} × {r} = {siguiente}"]
                    }

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