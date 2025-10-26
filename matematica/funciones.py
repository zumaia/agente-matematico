import re
import math

def evaluar_funcion(problema: str):
    """Evalúa funciones matemáticas simples"""
    problema_lower = problema.lower()
    
    # Patrón: f(x) = 2x + 1 cuando x=3
    patron_funcion = r'f\(x\)\s*=\s*([^=]+?)\s+cuando\s+x\s*=\s*(\d+)'
    match = re.search(patron_funcion, problema_lower)
    
    if match:
        expresion = match.group(1).strip()
        x_valor = float(match.group(2))
        
        # Reemplazar x por el valor
        expresion_eval = expresion.replace('x', f'({x_valor})')
        
        try:
            # Evaluar expresión matemática (¡CUIDADO! En producción usar eval seguro)
            resultado = eval(expresion_eval, {"__builtins__": None}, {"math": math})
            
            return {
                "tipo": "evaluar_funcion",
                "solucion": f"f({x_valor}) = {resultado}",
                "pasos": [
                    f"Función: f(x) = {expresion}",
                    f"Sustituir x = {x_valor}: {expresion_eval}",
                    f"Resultado: {resultado}"
                ]
            }
        except:
            pass
    
    return None

def tabla_valores(problema: str):
    """Genera tabla de valores para una función"""
    problema_lower = problema.lower()
    
    if "tabla de valores" in problema_lower:
        # Extraer función del problema
        if "y =" in problema_lower:
            funcion_match = problema_lower.split("y =")[1].split()[0]
            # Generar tabla simple
            tabla = []
            for x in range(-2, 3):  # Valores de -2 a 2
                try:
                    y = eval(funcion_match.replace('x', str(x)), {"math": math})
                    tabla.append(f"x={x}, y={y}")
                except:
                    pass
            
            if tabla:
                return {
                    "tipo": "tabla_valores",
                    "solucion": f"Tabla generada con {len(tabla)} valores",
                    "pasos": [
                        f"Función: y = {funcion_match}",
                        "Valores:"
                    ] + tabla
                }
    
    return None


def ceros_funcion(problema: str):
    """Encuentra los ceros (raíces) de funciones polinómicas simples (grado <= 2)."""
    problema_lower = problema.lower().replace('^','**')
    if 'ceros' in problema_lower or 'encontrar los ceros' in problema_lower or 'encontrar los ceros de' in problema_lower:
        # Extraer la expresión después de 'f(x) ='
        m = re.search(r'f\(x\)\s*=\s*([^,;\n]+)', problema_lower)
        if not m:
            # Intentar buscar patrón 'f(x) = x2 - 4' (con carácteres especiales)
            m = re.search(r'f\(x\)\s*=\s*([^,;\n]+)', problema)
        if m:
            expr = m.group(1).strip()
            # Normalizar: permitir ² como ^2
            expr = expr.replace('²', '**2').replace('^2', '**2')
            # Intentar resolver polinomio de grado 2
            try:
                # Convertir a variable simbólica simple: asumir polinomio en x con coeficientes numéricos
                # Extraer coeficientes a*x**2 + b*x + c
                # Usar regex para coeficientes
                # Buscar términos
                a = b = c = 0.0
                # Termino x**2
                m2 = re.search(r'([+-]?\d*\.?\d*)\s*\*?\s*x\*\*2', expr)
                if m2:
                    a = float(m2.group(1)) if m2.group(1) not in ['', '+', '-'] else (1.0 if m2.group(1) in ['', '+'] else -1.0)
                else:
                    if 'x**2' in expr:
                        a = 1.0
                # Termino x
                m1 = re.search(r'([+-]?\d*\.?\d*)\s*\*?\s*x(?!\*\*)', expr)
                if m1:
                    b = float(m1.group(1)) if m1.group(1) not in ['', '+', '-'] else (1.0 if m1.group(1) in ['', '+'] else -1.0)
                # Termino independiente
                mc = re.search(r'([+-]?\d+\.?\d*)\s*(?:$|[^\d\.]?)', expr.replace(' ', ''))
                if mc:
                    # tomar el último número como c si no aparece en términos anteriores
                    nums = re.findall(r'[+-]?\d+\.?\d*', expr)
                    if nums:
                        # si el último número no fue parte de coeficientes detectados, asignarlo a c
                        c = float(nums[-1])

                # Si no detectamos a (no es cuadrático), intentar factorizar simple o resolver lineal
                if abs(a) > 1e-9:
                    disc = b*b - 4*a*c
                    if disc < 0:
                        solucion = "No hay raíces reales"
                        pasos = [f"Discriminante: {disc} < 0 → sin raíces reales"]
                    else:
                        r1 = (-b + disc**0.5) / (2*a)
                        r2 = (-b - disc**0.5) / (2*a)
                        solucion = f"x = {r1}, x = {r2}"
                        pasos = [f"Discriminante: {disc}", f"Raíces: {r1}, {r2}"]
                    return {"tipo": "ceros_funcion", "solucion": solucion, "pasos": pasos}
                else:
                    # lineal bx + c = 0 => x = -c/b
                    if abs(b) > 1e-9:
                        x = -c / b
                        return {"tipo": "ceros_funcion", "solucion": f"x = {x}", "pasos": [f"Resolver {b}x + {c} = 0 → x = {-c}/{b} = {x}"]}
            except Exception:
                pass
    return None