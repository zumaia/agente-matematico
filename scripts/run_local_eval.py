#!/usr/bin/env python3
"""Script de prueba: Ejecuta 5 problemas del dataset usando los resolutores locales.
Muestra la solución encontrada y si la heurística plausible_solution permitiría cachearla.
"""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_module_from_path(name, rel_path):
    path = os.path.join(ROOT, rel_path)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# Cargar módulos directamente por ruta (evita problemas si falta __init__.py)
algebra = load_module_from_path('matematica.algebra', 'matematica/algebra.py')
geometria = load_module_from_path('matematica.geometria', 'matematica/geometria.py')
aritmetica = load_module_from_path('matematica.aritmetica', 'matematica/aritmetica.py')
estadistica = load_module_from_path('matematica.estadistica', 'matematica/estadistica.py')
trigonometria = load_module_from_path('matematica.trigonometria', 'matematica/trigonometria.py')
sucesiones = load_module_from_path('matematica.sucesiones', 'matematica/sucesiones.py')
combinatoria = load_module_from_path('matematica.combinatoria', 'matematica/combinatoria.py')
geo_analitica = load_module_from_path('matematica.geometria_analitica', 'matematica/geometria_analitica.py')
dataset_mod = load_module_from_path('green_agent.dataset_matematico', 'green_agent/dataset_matematico.py')

# Importar funciones
resolver_ecuacion_lineal = algebra.resolver_ecuacion_lineal
sistemas_ecuaciones = algebra.sistemas_ecuaciones
calcular_area = geometria.calcular_area
teorema_pitagoras = geometria.teorema_pitagoras
calcular_volumen = geometria.calcular_volumen
operaciones_fracciones = aritmetica.operaciones_fracciones
calcular_porcentajes = aritmetica.calcular_porcentajes
calcular_media = estadistica.calcular_media
calcular_mediana = estadistica.calcular_mediana
calcular_moda = estadistica.calcular_moda
calcular_rango = estadistica.calcular_rango
probabilidad_basica = estadistica.probabilidad_basica
resolver_trigonometria = trigonometria.resolver_trigonometria
resolver_sucesiones = sucesiones.resolver_sucesiones
resolver_combinatoria = combinatoria.resolver_combinatoria
resolver_geometria_analitica = geo_analitica.resolver_geometria_analitica
obtener_problemas_aleatorios = dataset_mod.obtener_problemas_aleatorios

def plausible_solution(tipo_problema: str, problema: str, solucion_valor) -> bool:
    """
    Heurística local (copia ligera de la función en app.py) para evitar cachear soluciones no plausibles.
    """
    import re
    try:
        tipo = (tipo_problema or '').lower()
        s = str(solucion_valor).lower()

        if s.startswith('error') or 'no se pudo' in s:
            return False

        if 'ecuacion' in tipo or 'ecuación' in tipo or tipo == 'ecuacion_lineal':
            return 'x' in s or re.search(r'[-+]?[0-9]+\.?[0-9]*', s) is not None

        if 'trig' in tipo or 'seno' in problema.lower() or 'sen(' in problema.lower() or 'cos(' in problema.lower():
            nums = re.findall(r'[-+]?[0-9]*\.?[0-9]+', s)
            if nums:
                try:
                    v = float(nums[0])
                    return -1.0 - 1e-6 <= v <= 1.0 + 1e-6
                except ValueError:
                    return False
            return False

        if 'porcentaje' in tipo or 'aritm' in tipo or 'porcentaje' in problema.lower():
            return re.search(r'[-+]?[0-9]+\.?[0-9]*', s) is not None

        if any(k in tipo for k in ['area', 'volumen', 'teorema_pitagoras', 'distancia', 'punto_medio', 'pendiente']):
            nums = re.findall(r'[-+]?[0-9]*\.?[0-9]+', s)
            if nums:
                try:
                    v = float(nums[0])
                    return v >= 0 or '(' in s or '[' in s
                except ValueError:
                    return False
            return False

        return re.search(r'[xX]|[-+]?[0-9]+\.?[0-9]*', s) is not None
    except Exception:
        return False

def main():
    # Tomar 5 problemas aleatorios del dataset
    problemas = obtener_problemas_aleatorios(5)

    resolutores = [
        resolver_ecuacion_lineal,
        calcular_area,
        operaciones_fracciones,
        calcular_porcentajes,
        teorema_pitagoras,
        calcular_volumen,
        sistemas_ecuaciones,
        calcular_media,
        calcular_mediana,
        calcular_moda,
        calcular_rango,
        probabilidad_basica,
        resolver_trigonometria,
        resolver_sucesiones,
        resolver_combinatoria,
        resolver_geometria_analitica
    ]

    for p in problemas:
        text = p['problema']
        print('\n' + '='*80)
        print(f"ID: {p['id']} | Tipo esperado: {p.get('tipo','-')} | Problema: {text}")

        solucion = None
        for r in resolutores:
            try:
                out = r(text)
            except Exception as e:
                out = None
            if out:
                solucion = out
                print(f"Resuelto por: {r.__name__}")
                break

        if solucion:
            valor = solucion.get('solucion') if isinstance(solucion, dict) else str(solucion)
            pasos = solucion.get('pasos') if isinstance(solucion, dict) else None
            print(f"Solución encontrada: {valor}")
            if pasos:
                print("Pasos:")
                for step in pasos:
                    print(f"  - {step}")
            plausible = plausible_solution(solucion.get('tipo') if isinstance(solucion, dict) else '', text, valor)
            print(f"¿Plausible para cache? {'Sí' if plausible else 'No'}")
        else:
            print("No resuelto por los resolutores locales. Se usaría IA o extracción.")

if __name__ == '__main__':
    main()
