def analizar_intencion(problema: str):
    """Detecta la intención del problema para mejor routing"""
    problema_lower = problema.lower()
    
    intenciones = {
        'explicacion': ['explica', 'cómo', 'como', 'qué es', 'que es', 'defin', 'significa'],
        'calculo': ['calcula', 'resuelve', 'cuánto es', 'cuanto es', '=', 'resultado'],
        'comparar': ['mayor', 'menor', 'mejor', 'peor', 'compar', 'diferenci'],
        'convertir': ['convertir', 'pasar a', 'transformar', 'expresa en'],
        'graficar': ['gráfica', 'grafica', 'dibuja', 'representa'],
        'estadistica': ['media', 'mediana', 'moda', 'promedio', 'rango', 'probabilidad'],
        'verificar': ['correcto', 'incorrecto', 'verdad', 'falso', 'comprueba']
    }
    
    for intencion, palabras in intenciones.items():
        if any(palabra in problema_lower for palabra in palabras):
            return intencion
    
    return 'desconocido'

def detectar_tipo_problema(problema: str):
    """Detecta el tipo específico de problema matemático"""
    problema_lower = problema.lower()
    
    patrones = {
        'ecuacion_lineal': ['x +', 'x -', 'x =', 'ecuación', 'ecuacion'],
        'sistema_ecuaciones': ['sistema', 'x e y', 'x y y'],
        'area': ['área', 'area', 'superficie'],
        'volumen': ['volumen', 'cubo', 'esfera'],
        'fracciones': ['fracción', 'fraccion', '/', 'mitad', 'tercio'],
        'porcentaje': ['porcentaje', '%', 'por ciento'],
        'pitagoras': ['pitágoras', 'pitagoras', 'hipotenusa'],
        'estadistica': ['media', 'mediana', 'moda', 'promedio'],
        'probabilidad': ['probabilidad', 'probable']
    }
    
    tipos_detectados = []
    for tipo, palabras in patrones.items():
        if any(palabra in problema_lower for palabra in palabras):
            tipos_detectados.append(tipo)
    
    return tipos_detectados

def priorizar_resolutores(problema: str, resolutores_disponibles: list):
    """Reordena los resolutores basado en la intención detectada"""
    intencion = analizar_intencion(problema)
    tipos = detectar_tipo_problema(problema)
    
    # Mapeo de tipos a funciones específicas
    tipo_a_resolutor = {
        'media': 'calcular_media',
        'mediana': 'calcular_mediana', 
        'moda': 'calcular_moda',
        'rango': 'calcular_rango',
        'probabilidad': 'probabilidad_basica'
    }
    
    # Reordenar resolutores basado en detección
    resolutores_priorizados = []
    
    # Primero los que coinciden con el tipo detectado
    for resolutor in resolutores_disponibles:
        if any(tipo in resolutor.__name__ for tipo in tipos):
            resolutores_priorizados.append(resolutor)
    
    # Luego el resto
    for resolutor in resolutores_disponibles:
        if resolutor not in resolutores_priorizados:
            resolutores_priorizados.append(resolutor)
    
    return resolutores_priorizados