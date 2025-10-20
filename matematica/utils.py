import re

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