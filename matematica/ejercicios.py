import random
from typing import List, Dict

def generar_ejercicios_basicos(tipo_problema: str) -> List[Dict]:
    """Ejercicios para 1º-2º ESO"""
    if "ecuacion" in tipo_problema.lower():
        return [
            {
                "problema": "Resuelve: x + 5 = 12",
                "solucion": "x = 7",
                "dificultad": "básica",
                "nivel": "1º ESO"
            },
            {
                "problema": "Resuelve: 2x = 16", 
                "solucion": "x = 8",
                "dificultad": "básica",
                "nivel": "1º ESO"
            }
        ]

def generar_ejercicios_similares(tipo_problema: str, problema_original: str) -> List[Dict]:
    """
    Genera ejercicios similares para practicar
    """
    ejercicios = []
    
    if "ecuacion" in tipo_problema.lower():
        ejercicios = generar_ecuaciones_similares()
    elif "area" in tipo_problema.lower():
        ejercicios = generar_areas_similares()
    elif "trigonometria" in tipo_problema.lower() or "seno" in tipo_problema.lower() or "coseno" in tipo_problema.lower():
        ejercicios = generar_trigonometria_similar()
    elif "porcentaje" in tipo_problema.lower():
        ejercicios = generar_porcentajes_similares()
    elif "fraccion" in tipo_problema.lower():
        ejercicios = generar_fracciones_similares()
    elif "estadistica" in tipo_problema.lower() or "media" in tipo_problema.lower():
        ejercicios = generar_estadistica_similar()
    else:
        ejercicios = generar_ejercicios_generales()
    
    return ejercicios

def generar_ecuaciones_similares() -> List[Dict]:
    ejercicios = []
    for i in range(3):
        a, b = random.randint(1, 10), random.randint(1, 20)
        ejercicio = {
            "problema": f"Resuelve la ecuación: {a}x + {b} = {a*2 + b}",
            "solucion": f"x = 2",
            "dificultad": "media"
        }
        ejercicios.append(ejercicio)
    return ejercicios

def generar_areas_similares() -> List[Dict]:
    figuras = ["círculo", "triángulo", "rectángulo", "cuadrado"]
    ejercicios = []
    for i in range(3):
        figura = random.choice(figuras)
        if figura == "círculo":
            radio = random.randint(1, 10)
            ejercicio = {
                "problema": f"Calcula el área de un {figura} con radio {radio} cm",
                "solucion": f"Área = π × {radio}² ≈ {3.1416 * radio**2:.2f} cm²",
                "dificultad": "media"
            }
        elif figura == "triángulo":
            base, altura = random.randint(1, 10), random.randint(1, 10)
            ejercicio = {
                "problema": f"Calcula el área de un {figura} con base {base} cm y altura {altura} cm",
                "solucion": f"Área = ({base} × {altura}) / 2 = {base * altura / 2} cm²",
                "dificultad": "básica"
            }
        ejercicios.append(ejercicio)
    return ejercicios

def generar_trigonometria_similar() -> List[Dict]:
    ejercicios = []
    angulos = [30, 45, 60, 90]
    funciones = ["seno", "coseno", "tangente"]
    
    for i in range(3):
        angulo = random.choice(angulos)
        funcion = random.choice(funciones)
        ejercicio = {
            "problema": f"Calcula el {funcion} de {angulo} grados",
            "solucion": f"{funcion.capitalize()}({angulo}°) = ... (usa calculadora)",
            "dificultad": "media"
        }
        ejercicios.append(ejercicio)
    return ejercicios

def generar_porcentajes_similares() -> List[Dict]:
    ejercicios = []
    for i in range(3):
        numero = random.randint(10, 100)
        porcentaje = random.randint(5, 50)
        ejercicio = {
            "problema": f"Calcula el {porcentaje}% de {numero}",
            "solucion": f"{porcentaje}% de {numero} = {numero * porcentaje / 100}",
            "dificultad": "básica"
        }
        ejercicios.append(ejercicio)
    return ejercicios

def generar_fracciones_similares() -> List[Dict]:
    ejercicios = []
    for i in range(3):
        a, b = random.randint(1, 10), random.randint(1, 10)
        c, d = random.randint(1, 10), random.randint(1, 10)
        ejercicio = {
            "problema": f"Suma las fracciones: {a}/{b} + {c}/{d}",
            "solucion": f"Resultado = {(a*d + c*b)}/{(b*d)}",
            "dificultad": "media"
        }
        ejercicios.append(ejercicio)
    return ejercicios

def generar_estadistica_similar() -> List[Dict]:
    ejercicios = []
    conjuntos = [
        [2, 4, 6, 8, 10],
        [5, 10, 15, 20],
        [1, 3, 5, 7, 9, 11]
    ]
    
    for i in range(3):
        datos = random.choice(conjuntos)
        ejercicio = {
            "problema": f"Calcula la media del conjunto: {datos}",
            "solucion": f"Media = {sum(datos) / len(datos)}",
            "dificultad": "básica"
        }
        ejercicios.append(ejercicio)
    return ejercicios

def generar_ejercicios_generales() -> List[Dict]:
    return [
        {
            "problema": "Resuelve: 2x + 5 = 15",
            "solucion": "x = 5",
            "dificultad": "básica"
        },
        {
            "problema": "Calcula el área de un cuadrado de lado 4 cm",
            "solucion": "Área = 16 cm²",
            "dificultad": "básica"
        },
        {
            "problema": "¿Cuál es el 20% de 80?",
            "solucion": "16",
            "dificultad": "básica"
        }
    ]


def generar_ejercicios_por_nivel(tipo_problema: str, nivel_eso: str) -> List[Dict]:
    """
    Genera ejercicios ESPECÍFICOS para cada nivel ESO
    """
    if "1º" in nivel_eso:
        return generar_ejercicios_1eso(tipo_problema)
    elif "2º" in nivel_eso:
        return generar_ejercicios_2eso(tipo_problema)
    elif "3º" in nivel_eso:
        return generar_ejercicios_3eso(tipo_problema)
    elif "4º" in nivel_eso:
        return generar_ejercicios_4eso(tipo_problema)
    else:
        return generar_ejercicios_generales(tipo_problema)

# ==================== 1º ESO ====================
def generar_ejercicios_1eso(tipo_problema: str) -> List[Dict]:
    """Ejercicios para 1º ESO - Operaciones básicas, geometría simple"""
    if "ecuacion" in tipo_problema.lower():
        return [
            {
                "problema": "Resuelve: x + 8 = 15",
                "solucion": "x = 7",
                "dificultad": "básica",
                "nivel": "1º ESO"
            },
            {
                "problema": "Encuentra x: 3x = 21",
                "solucion": "x = 7", 
                "dificultad": "básica",
                "nivel": "1º ESO"
            }
        ]
    
    elif "area" in tipo_problema.lower():
        return [
            {
                "problema": "Calcula el área de un cuadrado de lado 5 cm",
                "solucion": "Área = 25 cm²",
                "dificultad": "básica",
                "nivel": "1º ESO"
            },
            {
                "problema": "Un rectángulo mide 6 cm de base y 4 cm de altura. ¿Cuál es su área?",
                "solucion": "Área = 24 cm²",
                "dificultad": "básica", 
                "nivel": "1º ESO"
            }
        ]
    
    elif "porcentaje" in tipo_problema.lower():
        return [
            {
                "problema": "Calcula el 25% de 80",
                "solucion": "20",
                "dificultad": "básica",
                "nivel": "1º ESO"
            },
            {
                "problema": "Si un libro cuesta 20€ y tiene 10% de descuento, ¿cuánto pagas?",
                "solucion": "18€",
                "dificultad": "básica",
                "nivel": "1º ESO"
            }
        ]
    
    # Ejercicios generales 1º ESO
    return [
        {
            "problema": "Calcula: 125 + 68",
            "solucion": "193",
            "dificultad": "básica",
            "nivel": "1º ESO"
        },
        {
            "problema": "¿Cuál es el perímetro de un cuadrado de lado 7 cm?",
            "solucion": "28 cm",
            "dificultad": "básica",
            "nivel": "1º ESO"
        }
    ]

# ==================== 2º ESO ====================
def generar_ejercicios_2eso(tipo_problema: str) -> List[Dict]:
    """Ejercicios para 2º ESO - Ecuaciones, geometría, estadística básica"""
    if "ecuacion" in tipo_problema.lower():
        return [
            {
                "problema": "Resuelve: 2x - 5 = 3x + 1",
                "solucion": "x = -6",
                "dificultad": "media",
                "nivel": "2º ESO"
            },
            {
                "problema": "Resuelve el sistema: x + y = 10, x - y = 2",
                "solucion": "x = 6, y = 4",
                "dificultad": "media",
                "nivel": "2º ESO"
            }
        ]
    
    elif "pitagoras" in tipo_problema.lower():
        return [
            {
                "problema": "Un triángulo rectángulo tiene catetos 3 cm y 4 cm. ¿Cuánto mide la hipotenusa?",
                "solucion": "5 cm",
                "dificultad": "media", 
                "nivel": "2º ESO"
            },
            {
                "problema": "La hipotenusa mide 13 cm y un cateto 5 cm. ¿Cuánto mide el otro cateto?",
                "solucion": "12 cm",
                "dificultad": "media",
                "nivel": "2º ESO"
            }
        ]
    
    elif "estadistica" in tipo_problema.lower():
        return [
            {
                "problema": "Calcula la media de: 5, 7, 9, 11, 13",
                "solucion": "Media = 9",
                "dificultad": "media",
                "nivel": "2º ESO"
            },
            {
                "problema": "Encuentra la mediana de: 2, 4, 6, 8, 10",
                "solucion": "Mediana = 6", 
                "dificultad": "media",
                "nivel": "2º ESO"
            }
        ]
    
    # Ejercicios generales 2º ESO
    return [
        {
            "problema": "Calcula el volumen de un cubo de arista 3 cm",
            "solucion": "Volumen = 27 cm³",
            "dificultad": "media",
            "nivel": "2º ESO"
        },
        {
            "problema": "¿Cuál es el 15% de 200?",
            "solucion": "30",
            "dificultad": "media",
            "nivel": "2º ESO"
        }
    ]

# ==================== 3º ESO ====================
def generar_ejercicios_3eso(tipo_problema: str) -> List[Dict]:
    """Ejercicios para 3º ESO - Álgebra, trigonometría, funciones"""
    if "trigonometria" in tipo_problema.lower():
        return [
            {
                "problema": "Calcula el seno de 30 grados",
                "solucion": "sen(30°) = 0.5",
                "dificultad": "media",
                "nivel": "3º ESO"
            },
            {
                "problema": "Un triángulo tiene ángulo 60° y lado opuesto 8 cm. ¿Cuánto mide la hipotenusa?",
                "solucion": "Hipotenusa ≈ 9.24 cm",
                "dificultad": "avanzada",
                "nivel": "3º ESO"
            }
        ]
    
    elif "sistema" in tipo_problema.lower():
        return [
            {
                "problema": "Resuelve: 2x + 3y = 12, x - y = 1",
                "solucion": "x = 3, y = 2",
                "dificultad": "media",
                "nivel": "3º ESO"
            },
            {
                "problema": "Resuelve: 3x - 2y = 7, x + 4y = 10",
                "solucion": "x = 3, y = 1.75",
                "dificultad": "avanzada",
                "nivel": "3º ESO"
            }
        ]
    
    elif "funcion" in tipo_problema.lower():
        return [
            {
                "problema": "Grafica la función y = 2x + 1",
                "solucion": "Recta con pendiente 2 que pasa por (0,1)",
                "dificultad": "media",
                "nivel": "3º ESO"
            },
            {
                "problema": "Encuentra el vértice de y = x² - 4x + 3",
                "solucion": "Vértice en (2, -1)",
                "dificultad": "avanzada",
                "nivel": "3º ESO"
            }
        ]
    
    # Ejercicios generales 3º ESO
    return [
        {
            "problema": "Resuelve: x² - 5x + 6 = 0",
            "solucion": "x = 2, x = 3",
            "dificultad": "media",
            "nivel": "3º ESO"
        },
        {
            "problema": "Calcula la distancia entre (1,2) y (4,6)",
            "solucion": "Distancia = 5 unidades",
            "dificultad": "media",
            "nivel": "3º ESO"
        }
    ]

# ==================== 4º ESO ====================
def generar_ejercicios_4eso(tipo_problema: str) -> List[Dict]:
    """Ejercicios para 4º ESO - Análisis, combinatoria, geometría analítica"""
    if "combinatoria" in tipo_problema.lower():
        return [
            {
                "problema": "Calcula las permutaciones de 4 elementos",
                "solucion": "P(4) = 24",
                "dificultad": "media",
                "nivel": "4º ESO"
            },
            {
                "problema": "¿Cuántas combinaciones de 3 elementos hay en un conjunto de 6?",
                "solucion": "C(6,3) = 20",
                "dificultad": "avanzada",
                "nivel": "4º ESO"
            }
        ]
    
    elif "sucesion" in tipo_problema.lower():
        return [
            {
                "problema": "Encuentra el término general de: 2, 5, 8, 11, 14",
                "solucion": "aₙ = 3n - 1",
                "dificultad": "media",
                "nivel": "4º ESO"
            },
            {
                "problema": "Calcula la suma de los 10 primeros términos de: 1, 2, 4, 8, 16...",
                "solucion": "S₁₀ = 1023",
                "dificultad": "avanzada",
                "nivel": "4º ESO"
            }
        ]
    
    elif "geometria_analitica" in tipo_problema.lower():
        return [
            {
                "problema": "Encuentra la ecuación de la recta que pasa por (2,3) y (5,7)",
                "solucion": "y = (4/3)x + 1/3",
                "dificultad": "avanzada",
                "nivel": "4º ESO"
            },
            {
                "problema": "Calcula el punto medio entre (-1,4) y (3,-2)",
                "solucion": "Punto medio = (1, 1)",
                "dificultad": "media",
                "nivel": "4º ESO"
            }
        ]
    
    # Ejercicios generales 4º ESO
    return [
        {
            "problema": "Resuelve: log₂(x) = 3",
            "solucion": "x = 8",
            "dificultad": "avanzada",
            "nivel": "4º ESO"
        },
        {
            "problema": "Calcula el límite de (x² - 1)/(x - 1) cuando x tiende a 1",
            "solucion": "Límite = 2",
            "dificultad": "avanzada",
            "nivel": "4º ESO"
        }
    ]

def generar_ejercicios_generales(tipo_problema: str) -> List[Dict]:
    """Ejercicios generales cuando no se detecta nivel específico"""
    return [
        {
            "problema": "Resuelve: 2x + 5 = 15",
            "solucion": "x = 5",
            "dificultad": "básica",
            "nivel": "ESO General"
        },
        {
            "problema": "Calcula el área de un triángulo de base 6 y altura 4",
            "solucion": "Área = 12",
            "dificultad": "básica",
            "nivel": "ESO General"
        }
    ]

# Función de compatibilidad (mantener para no romper código existente)
def generar_ejercicios_similares(tipo_problema: str, problema_original: str) -> List[Dict]:
    """
    Función legacy - usa la nueva por nivel con ESO General por defecto
    """
    return generar_ejercicios_por_nivel(tipo_problema, "ESO General")