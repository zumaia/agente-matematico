# green_agent/dataset_matematico.py
"""
Dataset de problemas matemáticos para evaluación ESO - FASE 2 COMPLETA
Basado en el expertise del Agente Matemático existente
"""

MATEMATICAS_DATASET = [
    # === ÁLGEBRA ===
    {
        "id": "alg_001",
        "problema": "Resolver la ecuación: 2x + 5 = 15",
        "solucion_esperada": "x = 5",
        "tipo": "ecuacion_lineal",
        "dificultad": "facil",
        "categoria": "algebra",
        "puntos": 10,
        "pasos_esperados": ["2x = 10", "x = 5"]
    },
    {
        "id": "alg_002",
        "problema": "Resolver el sistema: x + y = 10, 2x - y = 5",
        "solucion_esperada": "x = 5, y = 5",
        "tipo": "sistema_ecuaciones",
        "dificultad": "medio",
        "categoria": "algebra", 
        "puntos": 15,
        "pasos_esperados": ["3x = 15", "x = 5", "y = 5"]
    },
    {
        "id": "alg_003",
        "problema": "Factorizar: x² - 9",
        "solucion_esperada": "(x - 3)(x + 3)",
        "tipo": "factorizacion",
        "dificultad": "medio",
        "categoria": "algebra",
        "puntos": 12
    },
    
    # === GEOMETRÍA ===
    {
        "id": "geo_001",
        "problema": "Calcular el área de un triángulo con base 8 cm y altura 5 cm",
        "solucion_esperada": "20",
        "tipo": "area_triangulo",
        "dificultad": "facil",
        "categoria": "geometria",
        "puntos": 10,
        "unidades": "cm²"
    },
    {
        "id": "geo_002", 
        "problema": "Calcular el área de un círculo con radio 7 cm",
        "solucion_esperada": "153.94",
        "tolerancia": 0.1,
        "tipo": "area_circulo",
        "dificultad": "medio",
        "categoria": "geometria",
        "puntos": 12,
        "unidades": "cm²"
    },
    {
        "id": "geo_003",
        "problema": "Aplicar el teorema de Pitágoras: cateto a=3, cateto b=4, hallar hipotenusa",
        "solucion_esperada": "5",
        "tipo": "teorema_pitagoras", 
        "dificultad": "facil",
        "categoria": "geometria",
        "puntos": 10
    },
    
    # === ARITMÉTICA ===
    {
        "id": "arit_001",
        "problema": "Calcular 30% de 200",
        "solucion_esperada": "60",
        "tipo": "porcentaje",
        "dificultad": "facil", 
        "categoria": "aritmetica",
        "puntos": 8
    },
    {
        "id": "arit_002",
        "problema": "Sumar las fracciones: 1/2 + 1/3",
        "solucion_esperada": "5/6",
        "tipo": "fracciones",
        "dificultad": "facil",
        "categoria": "aritmetica",
        "puntos": 10
    },
    {
        "id": "arit_003",
        "problema": "Simplificar la expresión: (12 + 8) × 2 ÷ 4",
        "solucion_esperada": "10",
        "tipo": "operaciones_combinadas",
        "dificultad": "facil",
        "categoria": "aritmetica",
        "puntos": 8
    },
    
    # === ESTADÍSTICA ===
    {
        "id": "est_001",
        "problema": "Calcular la media de: 5, 7, 9, 11, 13",
        "solucion_esperada": "9",
        "tipo": "media_aritmetica",
        "dificultad": "facil",
        "categoria": "estadistica", 
        "puntos": 8
    },
    {
        "id": "est_002",
        "problema": "Encontrar la mediana de: 3, 1, 7, 5, 9",
        "solucion_esperada": "5",
        "tipo": "mediana",
        "dificultad": "medio",
        "categoria": "estadistica",
        "puntos": 10
    },
    {
        "id": "est_003",
        "problema": "Calcular la moda de: 2, 3, 3, 5, 7, 3, 8",
        "solucion_esperada": "3",
        "tipo": "moda",
        "dificultad": "facil",
        "categoria": "estadistica",
        "puntos": 8
    },
    
    # === GEOMETRÍA ANALÍTICA ===
    {
        "id": "ga_001",
        "problema": "Hallar la distancia entre los puntos A(2,3) y B(5,7)",
        "solucion_esperada": "5",
        "tipo": "distancia_puntos",
        "dificultad": "medio",
        "categoria": "geometria_analitica",
        "puntos": 12
    },
    {
        "id": "ga_002",
        "problema": "Encontrar el punto medio entre (1,2) y (5,8)",
        "solucion_esperada": "(3,5)",
        "tipo": "punto_medio",
        "dificultad": "medio",
        "categoria": "geometria_analitica",
        "puntos": 10
    },
    {
        "id": "ga_003",
        "problema": "Hallar la pendiente de la recta que pasa por (1,2) y (4,8)",
        "solucion_esperada": "2",
        "tipo": "pendiente_recta",
        "dificultad": "medio",
        "categoria": "geometria_analitica",
        "puntos": 10
    },
    
    # === TRIGONOMETRÍA ===
    {
        "id": "trig_001",
        "problema": "Calcular sen(30°)",
        "solucion_esperada": "0.5",
        "tolerancia": 0.01,
        "tipo": "trigonometria_basica",
        "dificultad": "facil",
        "categoria": "trigonometria",
        "puntos": 8
    },
    {
        "id": "trig_002",
        "problema": "Calcular cos(60°)",
        "solucion_esperada": "0.5",
        "tolerancia": 0.01,
        "tipo": "trigonometria_basica",
        "dificultad": "facil",
        "categoria": "trigonometria",
        "puntos": 8
    },
    {
        "id": "trig_003",
        "problema": "Resolver: tan(θ) = 1, encontrar θ en el primer cuadrante",
        "solucion_esperada": "45",
        "tipo": "resolver_angulo",
        "dificultad": "medio",
        "categoria": "trigonometria",
        "puntos": 12,
        "unidades": "°"
    },
    
    # === FUNCIONES ===
    {
        "id": "func_001",
        "problema": "Dada f(x) = 2x + 3, calcular f(5)",
        "solucion_esperada": "13",
        "tipo": "evaluar_funcion",
        "dificultad": "facil",
        "categoria": "funciones",
        "puntos": 8
    },
    {
        "id": "func_002",
        "problema": "Encontrar los ceros de f(x) = x² - 4",
        "solucion_esperada": "x = -2, x = 2",
        "tipo": "ceros_funcion",
        "dificultad": "medio",
        "categoria": "funciones",
        "puntos": 12
    },
    {
        "id": "func_003",
        "problema": "Dada f(x) = 3x - 1, encontrar f⁻¹(x)",
        "solucion_esperada": "f⁻¹(x) = (x + 1)/3",
        "tipo": "funcion_inversa",
        "dificultad": "medio",
        "categoria": "funciones",
        "puntos": 15
    },
    
    # === SUCESIONES ===
    {
        "id": "suc_001",
        "problema": "Encontrar el término 5 de la sucesión: 2, 5, 8, 11, ...",
        "solucion_esperada": "14",
        "tipo": "termino_sucesion",
        "dificultad": "facil",
        "categoria": "sucesiones",
        "puntos": 8
    },
    {
        "id": "suc_002",
        "problema": "Calcular la suma de los primeros 4 términos de: 1, 3, 5, 7, ...",
        "solucion_esperada": "16",
        "tipo": "suma_sucesion",
        "dificultad": "medio",
        "categoria": "sucesiones",
        "puntos": 12
    },
    {
        "id": "suc_003",
        "problema": "Encontrar la fórmula del término general de: 3, 6, 9, 12, ...",
        "solucion_esperada": "aₙ = 3n",
        "tipo": "formula_general",
        "dificultad": "medio",
        "categoria": "sucesiones",
        "puntos": 15
    },
    
    # === COMBINATORIA ===
    {
        "id": "comb_001",
        "problema": "Calcular las combinaciones de 3 elementos tomados de 5",
        "solucion_esperada": "10",
        "tipo": "combinaciones",
        "dificultad": "medio",
        "categoria": "combinatoria",
        "puntos": 12
    },
    {
        "id": "comb_002",
        "problema": "Calcular 5! (factorial de 5)",
        "solucion_esperada": "120",
        "tipo": "factorial",
        "dificultad": "facil",
        "categoria": "combinatoria",
        "puntos": 8
    },
    {
        "id": "comb_003",
        "problema": "¿De cuántas formas se pueden ordenar 3 libros en un estante?",
        "solucion_esperada": "6",
        "tipo": "permutaciones",
        "dificultad": "medio",
        "categoria": "combinatoria",
        "puntos": 10
    },
    
    # === PATRONES ===
    {
        "id": "pat_001",
        "problema": "Completar el patrón: 2, 4, 8, 16, ...",
        "solucion_esperada": "32",
        "tipo": "patron_geometrico",
        "dificultad": "facil",
        "categoria": "patrones",
        "puntos": 8
    },
    {
        "id": "pat_002",
        "problema": "Encontrar el siguiente número: 1, 1, 2, 3, 5, 8, ...",
        "solucion_esperada": "13",
        "tipo": "sucesion_fibonacci",
        "dificultad": "medio",
        "categoria": "patrones",
        "puntos": 10
    },
    {
        "id": "pat_003",
        "problema": "Completar: 3, 6, 9, 12, ...",
        "solucion_esperada": "15",
        "tipo": "patron_aritmetico",
        "dificultad": "facil",
        "categoria": "patrones",
        "puntos": 8
    },
    
    # === ÁLGEBRA LINEAL ===
    {
        "id": "la_001",
        "problema": "Sumar las matrices: [[1,2],[3,4]] + [[5,6],[7,8]]",
        "solucion_esperada": "[[6,8],[10,12]]",
        "tipo": "suma_matrices",
        "dificultad": "medio",
        "categoria": "algebra_lineal",
        "puntos": 12
    },
    {
        "id": "la_002",
        "problema": "Multiplicar el vector [2,3] por el escalar 4",
        "solucion_esperada": "[8,12]",
        "tipo": "producto_escalar",
        "dificultad": "facil",
        "categoria": "algebra_lineal",
        "puntos": 8
    },
    {
        "id": "la_003",
        "problema": "Calcular el determinante de [[1,2],[3,4]]",
        "solucion_esperada": "-2",
        "tipo": "determinante",
        "dificultad": "medio",
        "categoria": "algebra_lineal",
        "puntos": 15
    },
    
    # === GRÁFICOS ===
    {
        "id": "graf_001",
        "problema": "¿En qué cuadrante se encuentra el punto (-3, 4)?",
        "solucion_esperada": "II",
        "tipo": "cuadrantes",
        "dificultad": "facil",
        "categoria": "graficos",
        "puntos": 8
    },
    {
        "id": "graf_002",
        "problema": "Encontrar la intersección con el eje Y de y = 2x + 3",
        "solucion_esperada": "3",
        "tipo": "interseccion_y",
        "dificultad": "facil",
        "categoria": "graficos",
        "puntos": 8
    },
    {
        "id": "graf_003",
        "problema": "¿La función y = x² es par o impar?",
        "solucion_esperada": "par",
        "tipo": "paridad_funcion",
        "dificultad": "medio",
        "categoria": "graficos",
        "puntos": 10
    }
]

# Dataset por categorías para evaluaciones específicas
DATASET_POR_CATEGORIA = {
    "algebra": [p for p in MATEMATICAS_DATASET if p["categoria"] == "algebra"],
    "geometria": [p for p in MATEMATICAS_DATASET if p["categoria"] == "geometria"],
    "aritmetica": [p for p in MATEMATICAS_DATASET if p["categoria"] == "aritmetica"],
    "estadistica": [p for p in MATEMATICAS_DATASET if p["categoria"] == "estadistica"],
    "geometria_analitica": [p for p in MATEMATICAS_DATASET if p["categoria"] == "geometria_analitica"],
    "trigonometria": [p for p in MATEMATICAS_DATASET if p["categoria"] == "trigonometria"],
    "funciones": [p for p in MATEMATICAS_DATASET if p["categoria"] == "funciones"],
    "sucesiones": [p for p in MATEMATICAS_DATASET if p["categoria"] == "sucesiones"],
    "combinatoria": [p for p in MATEMATICAS_DATASET if p["categoria"] == "combinatoria"],
    "patrones": [p for p in MATEMATICAS_DATASET if p["categoria"] == "patrones"],
    "algebra_lineal": [p for p in MATEMATICAS_DATASET if p["categoria"] == "algebra_lineal"],
    "graficos": [p for p in MATEMATICAS_DATASET if p["categoria"] == "graficos"],
    "facil": [p for p in MATEMATICAS_DATASET if p["dificultad"] == "facil"],
    "medio": [p for p in MATEMATICAS_DATASET if p["dificultad"] == "medio"]
}

def obtener_problemas_aleatorios(n=5, categoria=None, dificultad=None):
    """Obtiene problemas aleatorios del dataset"""
    import random
    problemas = MATEMATICAS_DATASET.copy()
    
    if categoria:
        problemas = [p for p in problemas if p["categoria"] == categoria]
    if dificultad:
        problemas = [p for p in problemas if p["dificultad"] == dificultad]
        
    return random.sample(problemas, min(n, len(problemas)))