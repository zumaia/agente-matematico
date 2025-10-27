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


def resolver_determinante(problema: str):
    """Resuelve determinantes de matrices pequeñas escritas como [[a,b],[c,d]]"""
    m = re.search(r'\[\s*\[\s*([\d\-\.]+)\s*,\s*([\d\-\.]+)\s*\]\s*,\s*\[\s*([\d\-\.]+)\s*,\s*([\d\-\.]+)\s*\]\s*\]', problema)
    if m:
        a, b, c, d = [float(x) for x in m.groups()]
        det = a * d - b * c
        pasos = [f"Matriz: [[{a},{b}],[{c},{d}]]", f"Determinante: {a}×{d} - {b}×{c} = {det}"]
        return {
            "tipo": "determinante",
            "solucion": f"Determinante = {int(det) if det.is_integer() else det}",
            "pasos": pasos
        }
    return None


def resolver_suma_matrices(problema: str):
    """Suma matrices escritas como [[a,b],[c,d]] + [[e,f],[g,h]]"""
    m = re.search(r'\[\s*\[\s*([\d\-\.]+)\s*,\s*([\d\-\.]+)\s*\]\s*,\s*\[\s*([\d\-\.]+)\s*,\s*([\d\-\.]+)\s*\]\s*\]\s*\+\s*\[\s*\[\s*([\d\-\.]+)\s*,\s*([\d\-\.]+)\s*\]\s*,\s*\[\s*([\d\-\.]+)\s*,\s*([\d\-\.]+)\s*\]\s*\]', problema)
    if m:
        a,b,c,d,e,f,g,h = [float(x) for x in m.groups()]
        r1 = [a+e, b+f]
        r2 = [c+g, d+h]
        pasos = [f"Matriz A: [[{a},{b}],[{c},{d}]]", f"Matriz B: [[{e},{f}],[{g},{h}]]", f"Suma: [[{r1[0]},{r1[1]}],[{r2[0]},{r2[1]}]]"]
        # Formatear como enteros si corresponde
        def fmt(x):
            return int(x) if float(x).is_integer() else x
        solucion = f"[[{fmt(r1[0])},{fmt(r1[1])}],[{fmt(r2[0])},{fmt(r2[1])}]]"
        return {"tipo": "suma_matrices", "solucion": solucion, "pasos": pasos}
    return None


def resolver_producto_escalar(problema: str):
    """Multiplica un vector por un escalar. Detecta patrones como:
    'Multiplicar el vector [2,3] por el escalar 4' -> '[8,12]'
    Devuelve la solución con formato canónico sin espacios dentro de corchetes.
    """
    try:
        texto = problema.lower()
        # Buscar el primer vector entre corchetes
        vm = re.search(r'\[\s*([\-0-9\.,\s]+)\s*\]', texto)
        if not vm:
            return None

        vector_str = vm.group(1)
        # Extraer números del vector
        componentes = [c.strip() for c in re.split(r',', vector_str) if c.strip()]
        if not componentes:
            return None

        # Buscar el escalar: palabra 'escalar' seguida de un número, o 'por el' seguido de número
        esc_m = re.search(r'escalar\s*([\-+]?[0-9]*\.?[0-9]+)', texto)
        if not esc_m:
            esc_m = re.search(r'por\s+el\s+escalar\s*([\-+]?[0-9]*\.?[0-9]+)', texto)
        if not esc_m:
            # Intentar buscar un número cercano al final del enunciado
            esc_m = re.search(r'([\-+]?[0-9]*\.?[0-9]+)\s*$', texto)
        if not esc_m:
            return None

        escalar = float(esc_m.group(1))

        # Multiplicar componentes
        resultado = []
        for c in componentes:
            try:
                v = float(c)
            except ValueError:
                # Si no es numérico, abortar
                return None
            prod = v * escalar
            # Formatear como entero si corresponde
            if float(prod).is_integer():
                resultado.append(str(int(prod)))
            else:
                resultado.append(str(prod))

        solucion = '[' + ','.join(resultado) + ']'
        pasos = [f"Vector: [{', '.join(componentes)}]", f"Escalar: {escalar}", f"Producto componente a componente: [{', '.join(resultado)}]"]
        return {"tipo": "producto_escalar", "solucion": solucion, "pasos": pasos}

    except Exception:
        return None