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