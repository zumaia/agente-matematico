import re
import math

def calcular_area(problema: str):
    """Calcula áreas de figuras geométricas básicas"""
    problema_lower = problema.lower()
    numeros = [int(n) for n in re.findall(r'\d+', problema)]
    
    if not numeros:
        return None
        
    if "rectángulo" in problema_lower or "rectangulo" in problema_lower:
        if len(numeros) >= 2:
            base, altura = numeros[0], numeros[1]
            area = base * altura
            return {
                "tipo": "area_rectangulo",
                "solucion": f"Área = {area} unidades cuadradas",
                "pasos": [f"Fórmula: Área = base × altura", f"Sustitución: {base} × {altura}", f"Cálculo: {area}"]
            }
    
    elif "triángulo" in problema_lower or "triangulo" in problema_lower:
        if len(numeros) >= 2:
            base, altura = numeros[0], numeros[1]
            area = (base * altura) / 2
            return {
                "tipo": "area_triangulo", 
                "solucion": f"Área = {area} unidades cuadradas",
                "pasos": [f"Fórmula: Área = (base × altura) / 2", f"Sustitución: ({base} × {altura}) / 2", f"Cálculo: {area}"]
            }
    
    elif "círculo" in problema_lower or "circulo" in problema_lower:
        if len(numeros) >= 1:
            radio = numeros[0]
            area = math.pi * radio ** 2
            return {
                "tipo": "area_circulo",
                "solucion": f"Área ≈ {area:.2f} unidades cuadradas",
                "pasos": [f"Fórmula: Área = π × radio²", f"Sustitución: π × {radio}²", f"Cálculo: {area:.2f}"]
            }
    
    return None

def calcular_volumen(problema: str):
    """Calcula volúmenes de cuerpos geométricos"""
    problema_lower = problema.lower()
    numeros = [int(n) for n in re.findall(r'\d+', problema)]
    
    if not numeros:
        return None
    
    if "cubo" in problema_lower:
        if len(numeros) >= 1:
            lado = numeros[0]
            volumen = lado ** 3
            return {
                "tipo": "volumen_cubo",
                "solucion": f"Volumen = {volumen} unidades cúbicas",
                "pasos": [f"Fórmula: V = lado³", f"Sustitución: {lado}³", f"Cálculo: {volumen}"]
            }
    
    elif "esfera" in problema_lower:
        if len(numeros) >= 1:
            radio = numeros[0]
            volumen = (4/3) * math.pi * radio ** 3
            return {
                "tipo": "volumen_esfera",
                "solucion": f"Volumen ≈ {volumen:.2f} unidades cúbicas",
                "pasos": [f"Fórmula: V = (4/3)πr³", f"Sustitución: (4/3)π{radio}³", f"Cálculo: {volumen:.2f}"]
            }
    
    return None

def teorema_pitagoras(problema: str):
    """Aplica el teorema de Pitágoras"""
    problema_lower = problema.lower()
    
    if "pitágoras" in problema_lower or "pitagoras" in problema_lower:
        numeros = [int(n) for n in re.findall(r'\d+', problema)]
        
        if len(numeros) == 2:
            a, b = numeros[0], numeros[1]
            hipotenusa = math.sqrt(a**2 + b**2)
            return {
                "tipo": "teorema_pitagoras_hipotenusa",
                "solucion": f"Hipotenusa = {hipotenusa:.2f}",
                "pasos": [
                    f"Teorema: h² = a² + b²",
                    f"Sustitución: h² = {a}² + {b}²",
                    f"Cálculo: h² = {a**2} + {b**2} = {a**2 + b**2}",
                    f"h = √{a**2 + b**2} = {hipotenusa:.2f}"
                ]
            }
    
    return None