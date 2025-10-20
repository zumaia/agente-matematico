import re
import math

def resolver_ecuacion_lineal(problema: str):
    """Resuelve ecuaciones de primer grado simples"""
    patron = r'(\d+)x\s*\+\s*(\d+)\s*=\s*(\d+)'
    match = re.search(patron, problema)
    
    if match:
        a, b, c = int(match.group(1)), int(match.group(2)), int(match.group(3))
        solucion = (c - b) / a
        return {
            "tipo": "ecuacion_lineal",
            "solucion": f"x = {solucion}",
            "pasos": [
                f"Ecuación: {a}x + {b} = {c}",
                f"Restar {b} en ambos lados: {a}x = {c - b}",
                f"Dividir entre {a}: x = {solucion}"
            ]
        }
    return None

def sistemas_ecuaciones(problema: str):
    """Resuelve sistemas de ecuaciones simples 2x2"""
    problema_lower = problema.lower()
    
    patron_ecuaciones = r'(\d*)x\s*([+-])\s*(\d*)y\s*=\s*(\d+)\s*,\s*(\d*)x\s*([+-])\s*(\d*)y\s*=\s*(\d+)'
    match = re.search(patron_ecuaciones, problema_lower.replace(' ', ''))
    
    if match:
        a1 = int(match.group(1)) if match.group(1) else 1
        signo1 = -1 if match.group(2) == '-' else 1
        b1 = signo1 * (int(match.group(3)) if match.group(3) else 1)
        c1 = int(match.group(4))
        
        a2 = int(match.group(5)) if match.group(5) else 1
        signo2 = -1 if match.group(6) == '-' else 1  
        b2 = signo2 * (int(match.group(7)) if match.group(7) else 1)
        c2 = int(match.group(8))
        
        det = a1 * b2 - a2 * b1
        if det != 0:
            x = (c1 * b2 - c2 * b1) / det
            y = (a1 * c2 - a2 * c1) / det
            
            return {
                "tipo": "sistema_ecuaciones",
                "solucion": f"x = {x:.2f}, y = {y:.2f}",
                "pasos": [
                    f"Sistema: {a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}",
                    f"Determinante: {a1}×{b2} - {a2}×{b1} = {det}",
                    f"x = ({c1}×{b2} - {c2}×{b1}) / {det} = {x:.2f}",
                    f"y = ({a1}×{c2} - {a2}×{c1}) / {det} = {y:.2f}"
                ]
            }
    
    return None