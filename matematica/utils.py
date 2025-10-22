import re
from typing import List, Dict 

def procesar_pasos_detallados(pasos_texto):
    """
    Convierte el texto largo de pasos en una lista estructurada
    Elimina markdown y divide en pasos lógicos
    """
    if isinstance(pasos_texto, list):
        # Si ya es una lista, limpiar cada elemento
        return [limpiar_paso(paso) for paso in pasos_texto if paso and str(paso).strip()]
    
    texto = str(pasos_texto)
    
    # Si el texto es muy corto, devolver como lista de un elemento
    if len(texto) < 50:
        return [limpiar_paso(texto)]
    
    # Dividir por patrones comunes de pasos
    patrones = [
        r'\*\*Paso \d+:\*\*',
        r'\*\*Paso \d+\.\*\*', 
        r'Paso \d+:',
        r'Paso \d+\.',
        r'\d+\.\s',
        r'\*\*\d+\.\*\*\s',
        r'**Paso \d+**',
        r'Paso \d+\s*[-:]\s*'
    ]
    
    # Unir todos los patrones
    patron = '|'.join(patrones)
    
    # Dividir el texto usando los patrones
    partes = re.split(patron, texto)
    
    # Filtrar partes vacías y limpiar
    pasos_limpios = []
    for parte in partes:
        if parte and parte.strip():
            paso_limpio = limpiar_paso(parte)
            if paso_limpio:
                pasos_limpios.append(paso_limpio)
    
    # Si no se pudo dividir, dividir por párrafos largos
    if len(pasos_limpios) <= 1:
        pasos_limpios = dividir_por_parrafos(texto)
    
    return pasos_limpios

def limpiar_paso(texto):
    """Limpia un paso individual removiendo markdown y espacios extras"""
    if not texto or not str(texto).strip():
        return None
    
    texto_limpio = str(texto).strip()
    
    # Remover markdown básico
    texto_limpio = re.sub(r'\*\*(.*?)\*\*', r'\1', texto_limpio)  # **texto** → texto
    texto_limpio = re.sub(r'\*(.*?)\*', r'\1', texto_limpio)      # *texto* → texto
    texto_limpio = re.sub(r'`(.*?)`', r'\1', texto_limpio)        # `texto` → texto
    
    # Remover espacios múltiples
    texto_limpio = re.sub(r'\s+', ' ', texto_limpio)
    
    # Capitalizar primera letra
    if texto_limpio and len(texto_limpio) > 1:
        texto_limpio = texto_limpio[0].upper() + texto_limpio[1:]
    
    return texto_limpio.strip()

def dividir_por_parrafos(texto):
    """Divide texto largo en párrafos lógicos"""
    # Dividir por puntos seguidos de espacio y mayúscula
    partes = re.split(r'\.\s+(?=[A-Z])', texto)
    
    pasos = []
    for parte in partes:
        parte_limpia = limpiar_paso(parte)
        if parte_limpia and len(parte_limpia) > 10:  # Mínimo 10 caracteres
            # Asegurar que termina con punto
            if not parte_limpia.endswith('.'):
                parte_limpia += '.'
            pasos.append(parte_limpia)
    
    return pasos if pasos else [limpiar_paso(texto)]


def determinar_nivel_eso(problema: str) -> str:
    """
    Determina el nivel ESO aproximado basado en palabras clave del problema
    """
    problema = problema.lower()
    
    # Palabras clave por nivel de dificultad
    nivel_1_2 = [
        'suma', 'resta', 'multiplicación', 'división', 'fracción', 
        'porcentaje', 'área', 'perímetro', 'número natural', 'decimal',
        'operación básica', 'calcular', 'cuánto es'
    ]
    
    nivel_2_3 = [
        'ecuación', 'sistema', 'álgebra', 'polinomio', 'teorema', 
        'pitágoras', 'volumen', 'geometría', 'estadística', 'media',
        'mediana', 'moda', 'probabilidad básica'
    ]
    
    nivel_3_4 = [
        'trigonometría', 'seno', 'coseno', 'tangente', 'función',
        'gráfica', 'derivada', 'integral', 'límite', 'logaritmo',
        'combinatoria', 'permutación', 'variación', 'sucesión',
        'progresión', 'análisis', 'geometría analítica', 'distancia',
        'pendiente', 'coordenadas'
    ]
    
    # Contar ocurrencias por nivel
    count_1_2 = sum(1 for palabra in nivel_1_2 if palabra in problema)
    count_2_3 = sum(1 for palabra in nivel_2_3 if palabra in problema)  
    count_3_4 = sum(1 for palabra in nivel_3_4 if palabra in problema)
    
    # Determinar nivel basado en las palabras clave
    if count_3_4 > 0:
        return "3º-4º ESO"
    elif count_2_3 > 0:
        return "2º-3º ESO" 
    elif count_1_2 > 0:
        return "1º-2º ESO"
    else:
        return "ESO General"

def resaltar_con_emojis(texto: str) -> str:
    """
    Añade emojis relevantes al texto para hacerlo más atractivo
    """
    emoji_map = {
        'ecuación': '📊',
        'solución': '✅', 
        'resultado': '🎯',
        'calcular': '🧮',
        'área': '🔷',
        'volumen': '📦',
        'ángulo': '📐',
        'distancia': '📏',
        'probabilidad': '🎲',
        'estadística': '📈',
        'función': '📈',
        'gráfico': '📊',
        'teorema': '📚',
        'demostración': '🔍',
        'verificar': '✅',
        'error': '❌',
        'correcto': '✅'
    }
    
    texto_con_emojis = texto
    for palabra, emoji in emoji_map.items():
        if palabra in texto.lower():
            # Añadir emoji al principio si no hay ya uno
            if not any(e in texto for e in ['🧮', '📊', '🎯', '✅', '❌', '📈', '📐']):
                texto_con_emojis = f"{emoji} {texto_con_emojis}"
            break
    
    return texto_con_emojis

def formatear_ecuaciones(texto: str) -> str:
    """
    Mejora la visualización de ecuaciones en texto
    """
    sustituciones = {
        r'(\d+)x': r'\1x',           # 2x → 2x
        r'x\^2': 'x²',               # x^2 → x²  
        r'x\^3': 'x³',               # x^3 → x³
        r'(\d+)\^2': r'\1²',         # 3^2 → 3²
        r'(\d+)\^3': r'\1³',         # 2^3 → 2³
        r'sqrt\(([^)]+)\)': r'√\1',  # sqrt(4) → √4
        r'pi': 'π',                  # pi → π
        r'->': '→',                  # -> → →
        r'<=>': '⇔',                 # <=> → ⇔
        r'<=': '≤',                  # <= → ≤
        r'>=': '≥'                   # >= → ≥
    }
    
    texto_formateado = texto
    for patron, reemplazo in sustituciones.items():
        texto_formateado = re.sub(patron, reemplazo, texto_formateado)
    
    return texto_formateado

def mejorar_explicacion_pasos(pasos: List[str]) -> List[str]:
    """
    Aplica todas las mejoras a una lista de pasos
    """
    pasos_mejorados = []
    
    for i, paso in enumerate(pasos, 1):
        paso_mejorado = paso
        
        # Aplicar mejoras en orden
        paso_mejorado = formatear_ecuaciones(paso_mejorado)
        paso_mejorado = resaltar_con_emojis(paso_mejorado)
        
        # Numerar el paso
        paso_mejorado = f"{i}. {paso_mejorado}"
        
        pasos_mejorados.append(paso_mejorado)
    
    return pasos_mejorados

# Función de compatibilidad para usar en app.py
def procesar_y_mejorar_pasos(pasos_input) -> List[str]:
    """
    Función principal que usa tu procesamiento existente + nuevas mejoras
    """
    # Primero usa tu función existente para procesar
    pasos_procesados = procesar_pasos_detallados(pasos_input)
    
    # Luego aplica las mejoras educativas
    pasos_mejorados = mejorar_explicacion_pasos(pasos_procesados)
    
    return pasos_mejorados


def determinar_nivel_eso_preciso(problema: str, tipo_problema: str) -> str:
    """
    Detección MÁS PRECISA usando problema + tipo de problema
    """
    problema = problema.lower()
    tipo_problema = tipo_problema.lower()
    
    # PALABRAS CLAVE ESPECÍFICAS POR CURSO (basado en temario LOMLOE)
    nivel_1_eso = [
        'suma', 'resta', 'multiplicación', 'división', 'fracción simple', 
        'porcentaje básico', 'número natural', 'decimal básico', 'metro',
        'kilogramo', 'litro', 'perímetro', 'área básica', 'recta', 'ángulo',
        'polígono simple', 'gráfica simple', 'media simple', 'calcular cuánto es'
    ]
    
    nivel_2_eso = [
        'potencia', 'raíz cuadrada', 'ecuación primer grado', 'sistema simple',
        'proporcionalidad', 'teorema pitágoras', 'volumen', 'cuerpo geométrico',
        'polígono regular', 'estadística básica', 'probabilidad simple',
        'coordenadas cartesianas', 'porcentaje compuesto'
    ]
    
    nivel_3_eso = [
        'número racional', 'irracional', 'polinomio', 'ecuación segundo grado',
        'sistema ecuaciones', 'función lineal', 'cuadrática', 'geometría analítica',
        'trigonometría', 'seno', 'coseno', 'tangente', 'estadística avanzada',
        'probabilidad compuesta', 'gráfica función', 'análisis datos'
    ]
    
    nivel_4_eso = [
        'número real', 'notación científica', 'sucesión', 'progresión',
        'ecuación compleja', 'función exponencial', 'logarítmica', 'análisis función',
        'dominio', 'recorrido', 'límite', 'derivada', 'integral', 'combinatoria',
        'permutación', 'variación', 'estadística inferencial', 'optimización'
    ]
    
    # Contar ocurrencias por nivel
    puntuaciones = {
        "1º ESO": 0,
        "2º ESO": 0, 
        "3º ESO": 0,
        "4º ESO": 0
    }
    
    # Ponderar por palabras en el problema
    for palabra in nivel_1_eso:
        if palabra in problema:
            puntuaciones["1º ESO"] += 2
    
    for palabra in nivel_2_eso:
        if palabra in problema:
            puntuaciones["2º ESO"] += 2
            
    for palabra in nivel_3_eso:
        if palabra in problema:
            puntuaciones["3º ESO"] += 2
            
    for palabra in nivel_4_eso:
        if palabra in problema:
            puntuaciones["4º ESO"] += 2
    
    # Ponderar por tipo de problema
    tipos_1_2_eso = ['operaciones_fracciones', 'calcular_porcentajes', 'calcular_area', 'teorema_pitagoras']
    tipos_3_eso = ['sistemas_ecuaciones', 'trigonometria', 'estadistica']
    tipos_4_eso = ['sucesiones', 'combinatoria', 'geometria_analitica']
    
    if tipo_problema in tipos_1_2_eso:
        puntuaciones["1º ESO"] += 1
        puntuaciones["2º ESO"] += 1
    elif tipo_problema in tipos_3_eso:
        puntuaciones["3º ESO"] += 3
    elif tipo_problema in tipos_4_eso:
        puntuaciones["4º ESO"] += 3
    
    # Determinar nivel ganador
    nivel_ganador = max(puntuaciones, key=puntuaciones.get)
    
    # Si hay empate o puntuación muy baja, usar general
    if puntuaciones[nivel_ganador] == 0:
        return "ESO General"
    
    return nivel_ganador

# ==================== ADAPTACIÓN POR NIVEL ESO ====================

def adaptar_explicacion_por_nivel(pasos: List[str], nivel_eso: str, tipo_problema: str) -> List[str]:
    """
    Adapta las explicaciones al nivel ESO detectado
    """
    if not pasos:
        return pasos
    
    if "1º" in nivel_eso:
        return adaptar_para_1eso(pasos, tipo_problema)
    elif "2º" in nivel_eso:
        return adaptar_para_2eso(pasos, tipo_problema)
    elif "3º" in nivel_eso:
        return adaptar_para_3eso(pasos, tipo_problema)
    elif "4º" in nivel_eso:
        return adaptar_para_4eso(pasos, tipo_problema)
    else:
        return pasos  # Sin adaptación para ESO General

def adaptar_para_1eso(pasos: List[str], tipo_problema: str) -> List[str]:
    """Adapta para 1º ESO - Lenguaje simple"""
    pasos_adaptados = []
    for paso in pasos:
        paso_adaptado = paso
        # Simplificar lenguaje
        paso_adaptado = paso_adaptado.replace("ecuación", "operación")
        paso_adaptado = paso_adaptado.replace("variable", "número desconocido")
        if "=" in paso and "x" in paso:
            paso_adaptado += " (recuerda: lo que haces a un lado, lo haces al otro)"
        pasos_adaptados.append(paso_adaptado)
    
    if pasos_adaptados:
        pasos_adaptados.insert(0, "Vamos a resolverlo paso a paso:")
    return pasos_adaptados

def adaptar_para_2eso(pasos: List[str], tipo_problema: str) -> List[str]:
    """Adapta para 2º ESO - Introduce conceptos formales"""
    pasos_adaptados = []
    for paso in pasos:
        paso_adaptado = paso
        if "número desconocido" in paso_adaptado:
            paso_adaptado = paso_adaptado.replace("número desconocido", "variable x")
        if "operación" in paso_adaptado and "=" in paso_adaptado:
            paso_adaptado = paso_adaptado.replace("operación", "ecuación")
        pasos_adaptados.append(paso_adaptado)
    return pasos_adaptados

def adaptar_para_3eso(pasos: List[str], tipo_problema: str) -> List[str]:
    """Adapta para 3º ESO - Lenguaje técnico"""
    pasos_adaptados = []
    for paso in pasos:
        paso_adaptado = paso
        paso_adaptado = paso_adaptado.replace("al cuadrado", "²")
        paso_adaptado = paso_adaptado.replace("al cubo", "³")
        paso_adaptado = paso_adaptado.replace("raíz cuadrada", "√")
        pasos_adaptados.append(paso_adaptado)
    return pasos_adaptados

def adaptar_para_4eso(pasos: List[str], tipo_problema: str) -> List[str]:
    """Adapta para 4º ESO - Enfoque analítico"""
    pasos_adaptados = []
    for paso in pasos:
        paso_adaptado = paso
        paso_adaptado = paso_adaptado.replace("grados", "°")
        paso_adaptado = paso_adaptado.replace("pi", "π")
        pasos_adaptados.append(paso_adaptado)
    return pasos_adaptados