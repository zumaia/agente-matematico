#!/usr/bin/env python3
"""Test script: Runs 5 problems from the dataset using local solvers.
Shows the found solution and whether the plausible_solution heuristic would allow caching it.
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

# Load modules directly by path (avoids issues if __init__.py is missing)
algebra = load_module_from_path('matematica.algebra', 'matematica/algebra.py')
geometria = load_module_from_path('matematica.geometria', 'matematica/geometria.py')
aritmetica = load_module_from_path('matematica.aritmetica', 'matematica/aritmetica.py')
estadistica = load_module_from_path('matematica.estadistica', 'matematica/estadistica.py')
trigonometria = load_module_from_path('matematica.trigonometria', 'matematica/trigonometria.py')
sucesiones = load_module_from_path('matematica.sucesiones', 'matematica/sucesiones.py')
combinatoria = load_module_from_path('matematica.combinatoria', 'matematica/combinatoria.py')
geo_analitica = load_module_from_path('matematica.geometria_analitica', 'matematica/geometria_analitica.py')
dataset_mod = load_module_from_path('green_agent.dataset_matematico', 'green_agent/dataset_matematico.py')

# Import functions
resolver_ecuacion_lineal = algebra.resolver_ecuacion_lineal
sistemas_ecuaciones = algebra.sistemas_ecuaciones
resolver_producto_escalar = algebra.resolver_producto_escalar
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

def plausible_solution(problem_type: str, problem: str, solution_value) -> bool:
    """
    Local heuristic (light copy of function in app.py) to avoid caching non-plausible solutions.
    """
    import re
    try:
        problem_type = (problem_type or '').lower()
        s = str(solution_value).lower()

        if s.startswith('error') or 'could not' in s or 'no se pudo' in s:
            return False

        if 'equation' in problem_type or 'ecuacion' in problem_type or 'ecuación' in problem_type or problem_type == 'ecuacion_lineal':
            return 'x' in s or re.search(r'[-+]?[0-9]+\.?[0-9]*', s) is not None

        if 'trig' in problem_type or 'sine' in problem.lower() or 'sin(' in problem.lower() or 'cos(' in problem.lower() or 'seno' in problem.lower() or 'sen(' in problem.lower():
            nums = re.findall(r'[-+]?[0-9]*\.?[0-9]+', s)
            if nums:
                try:
                    v = float(nums[0])
                    return -1.0 - 1e-6 <= v <= 1.0 + 1e-6
                except ValueError:
                    return False
            return False

        if 'percentage' in problem_type or 'arithmetic' in problem_type or 'porcentaje' in problem_type or 'percentage' in problem.lower() or 'porcentaje' in problem.lower():
            return re.search(r'[-+]?[0-9]+\.?[0-9]*', s) is not None

        if any(k in problem_type for k in ['area', 'volume', 'volume', 'pythagorean_theorem', 'distance', 'midpoint', 'slope']):
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
    # Take 5 random problems from the dataset
    problems = obtener_problemas_aleatorios(5)

    solvers = [
        resolver_ecuacion_lineal,
        calcular_area,
        operaciones_fracciones,
        calcular_porcentajes,
        teorema_pitagoras,
        calcular_volumen,
        sistemas_ecuaciones,
        resolver_producto_escalar,
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

    for p in problems:
        text = p['problema']
        print('\n' + '='*80)
        print(f"ID: {p['id']} | Expected type: {p.get('tipo','-')} | Problem: {text}")

        solution = None
        for solver in solvers:
            try:
                out = solver(text)
            except Exception as e:
                out = None
            if out:
                solution = out
                print(f"Solved by: {solver.__name__}")
                break

        if solution:
            value = solution.get('solucion') if isinstance(solution, dict) else str(solution)
            steps = solution.get('pasos') if isinstance(solution, dict) else None
            print(f"Solution found: {value}")
            if steps:
                print("Steps:")
                for step in steps:
                    print(f"  - {step}")
            plausible = plausible_solution(solution.get('tipo') if isinstance(solution, dict) else '', text, value)
            print(f"Plausible for cache? {'Yes' if plausible else 'No'}")
        else:
            print("Not solved by local solvers. Would use AI or extraction.")

if __name__ == '__main__':
    main()