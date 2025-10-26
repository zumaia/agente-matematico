# green_agent/metricas.py
"""
Sistema de métricas y scoring para evaluación de Purple Agents - VERSIÓN MEJORADA
Con detección avanzada de respuestas genéricas y HTML
"""

import re
import math
from typing import Dict, Any

class EvaluadorMetricas:
    def __init__(self):
        self.metricas_globales = {}
        # PATRONES DE DETECCIÓN MEJORADOS
        self.patrones_error_genericos = [
            'x = 5', 'x = 5.0', 'x = 5.00', 'x=5', 'x=5.0', 'x=5.00',
            '= 12', 'área = 12', 'área=12',
            '🏠', 'volver al inicio', 'fastapi', 'groq ai',
            'language switcher',
            'problema 1:', 'problema 2:', 'problema 3:',
            'ver solución', 'practice_title', 'cache problema'
        ]
    
    def normalizar_respuesta(self, respuesta: str) -> str:
        """Normaliza una respuesta para comparación - VERSIÓN MEJORADA"""
        if not respuesta or respuesta == "No se pudo extraer solución":
            return ""
        
        print(f"🔄 Normalizando: '{respuesta}'")
        
        # Convertir a minúsculas y limpiar
        respuesta = respuesta.lower().strip()
        
        # DETECCIÓN TEMPRANA: Si es HTML completo, extraer solo contenido matemático
        if self._es_respuesta_html(respuesta):
            print("⚠️  Detectado HTML - extrayendo contenido matemático")
            respuesta = self._extraer_contenido_matematico(respuesta)
        
        # Remover texto no matemático específico
        texto_no_matematico = [
            'agente matemático eso+', 'cache problema', 'información adicional',
            'language switcher', 'solución resultado:', '🏠', 'volver al inicio',
            'powered by fastapi', 'groq ai', 'problema 1', 'problema 2', 'problema 3',
            'ver solución', 'practice_title', '💪', '🔍', '📊', '📋'
        ]
        
        for texto in texto_no_matematico:
            respuesta = respuesta.replace(texto, '')
        
        # REMOVER SOLO caracteres realmente no matemáticos
        respuesta = re.sub(r'[^\w\d\s\/\.=,\-\+\[\]\(\)\{\}]', '', respuesta)
        
        # Normalizar espacios
        respuesta = ' '.join(respuesta.split())
        
        print(f"🔄 Normalizado a: '{respuesta}'")
        return respuesta.strip()

    def _es_respuesta_html(self, respuesta: str) -> bool:
        """Detecta si la respuesta contiene HTML/estructura de página completa"""
        indicadores_html = [
            '<div', '<span', '<style', 'language-switcher',
            'practice_title', 'ver solución', 'volver al inicio',
            'powered by', 'groq ai', 'cache problema'
        ]
        return any(ind in respuesta.lower() for ind in indicadores_html)

    def _extraer_contenido_matematico(self, html_completo: str) -> str:
        """Extrae solo el contenido matemático de respuestas HTML"""
        # Buscar bloques que contengan soluciones
        patrones_solucion = [
            r'solución\s*[:\-]\s*([^<\.]+)',
            r'resultado\s*[:\-]\s*([^<\.]+)', 
            r'respuesta\s*[:\-]\s*([^<\.]+)',
            r'>\s*([xy]\s*=\s*[^<]+)<',
            r'>\s*([\d\.\-\+]+)\s*<'
        ]
        
        for patron in patrones_solucion:
            matches = re.findall(patron, html_completo, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0]
                if match and self._es_respuesta_valida_post_html(match):
                    return match
        
        return html_completo  # Fallback a la respuesta original

    def _es_respuesta_valida_post_html(self, respuesta: str) -> bool:
        """Valida respuestas después de extracción HTML"""
        if not respuesta or len(respuesta) < 1:
            return False
        
        # Excluir respuestas genéricas
        resp_lower = respuesta.lower().strip()
        generic_answers = ['x = 5', 'x = 5.0', 'x = 5.00', '= 12']
        
        if resp_lower in generic_answers:
            return False
        
        # Debe contener contenido matemático
        return any(char in respuesta for char in '0123456789x[](),/-+=')

    def comparar_respuestas(self, respuesta_agente: str, respuesta_correcta: str, tolerancia=0.01) -> float:
        """Compara respuestas con DETECCIÓN AVANZADA de respuestas genéricas"""
        
        resp_agente_str = str(respuesta_agente)
        
        # DETECCIÓN CRÍTICA MEJORADA: Respuestas genéricas inválidas
        if self._es_respuesta_generica_invalida(resp_agente_str, respuesta_correcta):
            print("❌ RESPUESTA GENÉRICA INVÁLIDA DETECTADA")
            return 0.0
        
        # DETECCIÓN: Respuesta contiene múltiples problemas (HTML completo)
        if self._es_respuesta_multiple_problemas(resp_agente_str):
            print("⚠️  RESPUESTA CON MÚLTIPLES PROBLEMAS - BUSCANDO COINCIDENCIA...")
            return self._buscar_coincidencia_en_html(resp_agente_str, respuesta_correcta, tolerancia)

        # COMPARACIÓN NORMAL
        resp_agente = self.normalizar_respuesta(resp_agente_str)
        resp_correcta = self.normalizar_respuesta(str(respuesta_correcta))
        
        print(f"🔍 Comparando: '{resp_agente}' vs '{resp_correcta}'")
        
        # 1. COINCIDENCIA EXACTA (máxima prioridad)
        if resp_agente == resp_correcta:
            print("✅ Coincidencia exacta")
            return 1.0
        
        # 2. COMPARACIÓN NUMÉRICA ESTRICTA
        try:
            nums_agente = re.findall(r'[\-]?[\d\.]+', resp_agente)
            nums_correctos = re.findall(r'[\-]?[\d\.]+', resp_correcta)
            
            if nums_agente and nums_correctos:
                nums_agente_float = [float(n) for n in nums_agente]
                nums_correctos_float = [float(n) for n in nums_correctos]
                
                if (len(nums_agente_float) == len(nums_correctos_float) and
                    all(abs(a - c) <= tolerancia for a, c in zip(nums_agente_float, nums_correctos_float))):
                    print("✅ Coincidencia numérica exacta")
                    return 1.0
                    
        except (ValueError, IndexError):
            pass
        
        # 3. COMPARACIÓN PARA ECUACIONES
        if '=' in resp_agente and '=' in resp_correcta:
            score = self._comparar_ecuaciones(resp_agente, resp_correcta, tolerancia)
            if score > 0:
                return score
        
        # 4. COMPARACIÓN PARA SISTEMAS DE ECUACIONES
        if ',' in resp_agente and ',' in resp_correcta:
            score = self._comparar_sistemas_ecuaciones(resp_agente, resp_correcta, tolerancia)
            if score > 0:
                return score
        
        # 5. COMPARACIÓN PARA VECTORES/MATRICES
        if '[' in resp_agente and '[' in resp_correcta:
            score = self._comparar_vectores_matrices(resp_agente, resp_correcta)
            if score > 0:
                return score
        
        # 6. COMPARACIÓN PARA COORDENADAS
        if '(' in resp_agente and '(' in resp_correcta:
            score = self._comparar_coordenadas(resp_agente, resp_correcta)
            if score > 0:
                return score
        
        # 7. ÚLTIMO RECURSO: Comparación numérica simple
        try:
            num_agente = float(re.findall(r'[\-]?[\d\.]+', resp_agente)[0])
            num_correcto = float(re.findall(r'[\-]?[\d\.]+', resp_correcta)[0])
            
            if abs(num_agente - num_correcto) <= tolerancia:
                print("⚠️  Coincidencia numérica (contenida) - revisar formato")
                return 0.9
            else:
                print(f"❌ Diferencia numérica: {num_agente} vs {num_correcto}")
                return 0.0
                
        except (ValueError, IndexError):
            print("❌ No se pudo comparar numéricamente")
            return 0.0

    def _es_respuesta_generica_invalida(self, respuesta_agente: str, respuesta_correcta: str) -> bool:
        """Detecta respuestas genéricas que son incorrectas - VERSIÓN CORREGIDA"""
        resp_agente_clean = respuesta_agente.strip().lower()
        resp_correcta_clean = respuesta_correcta.strip().lower()
        
        print(f"🔍 Verificando respuesta genérica: '{resp_agente_clean}' vs '{resp_correcta_clean}'")
        
        # PRIMERO: Si la respuesta genérica COINCIDE con la correcta, NO es inválida
        if resp_agente_clean == resp_correcta_clean:
            print("✅ Respuesta genérica PERO CORRECTA - permitida")
            return False
        
        # SEGUNDO: Lista de respuestas genéricas que indican error
        respuestas_genericas_invalidas = [
            'agente matemático eso+',  # ← ESTE es el problema principal
            'no se pudo extraer solución',
            'solución no extraíble',
            'error en la solución',
            'respuesta no disponible'
        ]
        
        # Solo marcar como inválida si es una respuesta genérica de ERROR
        if resp_agente_clean in respuestas_genericas_invalidas:
            print("❌ Respuesta genérica inválida detectada")
            return True
        
        # TERCERO: Patrones numéricos genéricos - SOLO invalidar si NO coinciden
        patrones_numericos_genericos = [
            r'^x\s*=\s*5$', r'^x\s*=\s*5\.0$', r'^x\s*=\s*5\.00$',
            r'^=\s*12$', r'^área\s*=\s*12$'
        ]
        
        for patron in patrones_numericos_genericos:
            if re.match(patron, resp_agente_clean):
                # Verificar si este patrón genérico COINCIDE con la respuesta correcta
                if re.match(patron, resp_correcta_clean):
                    print("✅ Patrón genérico PERO CORRECTO - permitido")
                    return False
                else:
                    print("❌ Patrón genérico INCORRECTO - invalidado")
                    return True
        
        # CUARTO: Si contiene patrones de error claros (excluyendo respuestas correctas)
        if any(patron in resp_agente_clean for patron in self.patrones_error_genericos):
            # Pero permitir si coincide exactamente con la respuesta correcta
            if resp_agente_clean == resp_correcta_clean:
                print("✅ Coincide con respuesta correcta - permitido")
                return False
            print("❌ Contiene patrones de error - invalidado")
            return True
        
        print("✅ Respuesta válida - no es genérica inválida")
        return False

    def _es_respuesta_multiple_problemas(self, respuesta: str) -> bool:
        """Detecta si la respuesta contiene múltiples problemas"""
        indicadores_multiples = [
            'problema 1', 'problema 2', 'problema 3',
            'practice_title', 'ver solución', '🏠 volver al inicio',
            'powered by fastapi', 'groq ai'
        ]
        return (len(respuesta) > 500 or 
                any(ind in respuesta.lower() for ind in indicadores_multiples))

    def _buscar_coincidencia_en_html(self, html_completo: str, respuesta_correcta: str, tolerancia: float) -> float:
        """Busca coincidencia en respuestas HTML complejas"""
        # Estrategia 1: Buscar si la respuesta correcta está contenida
        if respuesta_correcta in html_completo:
            print("✅ Coincidencia exacta encontrada en HTML")
            return 1.0
        
        # Estrategia 2: Buscar coincidencia numérica
        nums_html = re.findall(r'[\-]?[\d\.]+', html_completo)
        nums_correctos = re.findall(r'[\-]?[\d\.]+', respuesta_correcta)
        
        if nums_html and nums_correctos:
            try:
                # Buscar el número correcto en la lista de números del HTML
                num_correcto = float(nums_correctos[0])
                for num_str in nums_html:
                    try:
                        num_html = float(num_str)
                        if abs(num_html - num_correcto) <= tolerancia:
                            print(f"✅ Coincidencia numérica en HTML: {num_html}")
                            return 1.0
                    except ValueError:
                        continue
            except (ValueError, IndexError):
                pass
        
        print("❌ No se encontró coincidencia en HTML múltiple")
        return 0.0

    def _comparar_ecuaciones(self, resp_agente: str, resp_correcta: str, tolerancia: float) -> float:
        """Comparación específica para ecuaciones"""
        partes_agente = [p.strip() for p in resp_agente.split('=')]
        partes_correcta = [p.strip() for p in resp_correcta.split('=')]
        
        if len(partes_agente) == len(partes_correcta) == 2:
            if partes_agente[0] != partes_correcta[0]:
                print("❌ Lado izquierdo de ecuación no coincide")
                return 0.0
            
            try:
                num_agente = float(partes_agente[1])
                num_correcto = float(partes_correcta[1])
                
                if abs(num_agente - num_correcto) <= tolerancia:
                    print("✅ Coincidencia de ecuación exacta")
                    return 1.0
                else:
                    print(f"❌ Valores numéricos diferentes: {num_agente} vs {num_correcto}")
                    return 0.0
                    
            except ValueError:
                if partes_agente[1] == partes_correcta[1]:
                    print("✅ Coincidencia de ecuación exacta")
                    return 1.0
        
        return 0.0

    def _comparar_sistemas_ecuaciones(self, resp_agente: str, resp_correcta: str, tolerancia: float) -> float:
        """Comparación para sistemas de ecuaciones"""
        ecuaciones_agente = [eq.strip() for eq in resp_agente.split(',')]
        ecuaciones_correcta = [eq.strip() for eq in resp_correcta.split(',')]
        
        if len(ecuaciones_agente) == len(ecuaciones_correcta):
            todas_coinciden = True
            for eq_agente, eq_correcta in zip(ecuaciones_agente, ecuaciones_correcta):
                if self.comparar_respuestas(eq_agente, eq_correcta, tolerancia) < 1.0:
                    todas_coinciden = False
                    break
            
            if todas_coinciden:
                print("✅ Coincidencia de sistema de ecuaciones exacta")
                return 1.0
        
        return 0.0

    def _comparar_vectores_matrices(self, resp_agente: str, resp_correcta: str) -> float:
        """Comparación para vectores y matrices"""
        contenido_agente = re.findall(r'\[([^\]]+)\]', resp_agente)
        contenido_correcto = re.findall(r'\[([^\]]+)\]', resp_correcta)
        
        if contenido_agente and contenido_correcto:
            if contenido_agente[0] == contenido_correcto[0]:
                print("✅ Coincidencia de vector/matriz exacta")
                return 1.0
        
        return 0.0

    def _comparar_coordenadas(self, resp_agente: str, resp_correcta: str) -> float:
        """Comparación para coordenadas"""
        contenido_agente = re.findall(r'\(([^\)]+)\)', resp_agente)
        contenido_correcto = re.findall(r'\(([^\)]+)\)', resp_correcta)
        
        if contenido_agente and contenido_correcto:
            if contenido_agente[0] == contenido_correcto[0]:
                print("✅ Coincidencia de coordenadas exacta")
                return 1.0
        
        return 0.0

    def calcular_puntuacion_final(self, resultados: list) -> Dict[str, Any]:
        """Calcula métricas agregadas de todos los resultados"""
        if not resultados:
            return {"puntuacion_total": 0, "accuracy": 0}
        
        puntuacion_maxima = sum(r['puntos'] for r in resultados)
        puntuacion_obtenida = sum(r['puntuacion_obtenida'] for r in resultados)
        accuracy = puntuacion_obtenida / puntuacion_maxima if puntuacion_maxima > 0 else 0
        
        # Métricas por categoría
        categorias = {}
        for resultado in resultados:
            cat = resultado['categoria']
            if cat not in categorias:
                categorias[cat] = {'total': 0, 'obtenido': 0, 'count': 0}
            categorias[cat]['total'] += resultado['puntos']
            categorias[cat]['obtenido'] += resultado['puntuacion_obtenida']
            categorias[cat]['count'] += 1
        
        accuracy_por_categoria = {
            cat: datos['obtenido'] / datos['total'] if datos['total'] > 0 else 0
            for cat, datos in categorias.items()
        }
        
        return {
            "puntuacion_total": round(puntuacion_obtenida, 2),
            "puntuacion_maxima": puntuacion_maxima,
            "accuracy_general": round(accuracy, 4),
            "accuracy_por_categoria": accuracy_por_categoria,
            "total_problemas": len(resultados),
            "problemas_correctos": sum(1 for r in resultados if r['puntuacion_obtenida'] == r['puntos'])
        }
    
    def calcular_metricas_estandar(self, resultados: list) -> Dict[str, Any]:
        """Calcula métricas en formato estándar AgentBeats"""
        metricas_basicas = self.calcular_puntuacion_final(resultados)
        
        # Calcular tiempo promedio
        tiempo_promedio = sum(r.get('tiempo_respuesta', 0) for r in resultados) / len(resultados) if resultados else 0
        
        return {
            # MÉTRICAS ESTÁNDAR AGENTBEATS
            "overall_score": metricas_basicas["accuracy_general"],
            "total_score": metricas_basicas["puntuacion_total"],
            "max_score": metricas_basicas["puntuacion_maxima"],
            "average_response_time": round(tiempo_promedio, 2),
            "tasks_completed": metricas_basicas["problemas_correctos"],
            "total_tasks": metricas_basicas["total_problemas"],
            
            # MÉTRICAS ESPECÍFICAS DOMINIO - ACTUALIZADO
            "domain_specific_metrics": {
                "algebra_accuracy": metricas_basicas["accuracy_por_categoria"].get("algebra", 0),
                "geometry_accuracy": metricas_basicas["accuracy_por_categoria"].get("geometria", 0),
                "arithmetic_accuracy": metricas_basicas["accuracy_por_categoria"].get("aritmetica", 0),
                "statistics_accuracy": metricas_basicas["accuracy_por_categoria"].get("estadistica", 0),
                "analytic_geometry_accuracy": metricas_basicas["accuracy_por_categoria"].get("geometria_analitica", 0),
                "trigonometry_accuracy": metricas_basicas["accuracy_por_categoria"].get("trigonometria", 0),
                "functions_accuracy": metricas_basicas["accuracy_por_categoria"].get("funciones", 0),
                "sequences_accuracy": metricas_basicas["accuracy_por_categoria"].get("sucesiones", 0),
                "combinatorics_accuracy": metricas_basicas["accuracy_por_categoria"].get("combinatoria", 0),
                "patterns_accuracy": metricas_basicas["accuracy_por_categoria"].get("patrones", 0),
                "linear_algebra_accuracy": metricas_basicas["accuracy_por_categoria"].get("algebra_lineal", 0),
                "graphics_accuracy": metricas_basicas["accuracy_por_categoria"].get("graficos", 0)
            }
        }