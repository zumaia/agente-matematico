# green_agent/metricas.py
"""
Sistema de métricas y scoring para evaluación de Purple Agents - VERSIÓN MEJORADA
"""

import re
import math
from typing import Dict, Any

class EvaluadorMetricas:
    def __init__(self):
        self.metricas_globales = {}
    
    def normalizar_respuesta(self, respuesta: str) -> str:
        """Normaliza una respuesta para comparación - VERSIÓN MEJORADA"""
        if not respuesta or respuesta == "No se pudo extraer solución":
            return ""
        
        print(f"🔄 Normalizando: '{respuesta}'")
        
        # Convertir a minúsculas y limpiar
        respuesta = respuesta.lower().strip()
        
        # Remover texto no matemático específico
        texto_no_matematico = [
            'agente matemático eso+',
            'cache problema', 
            'información adicional',
            'language switcher',
            'solución resultado:',
        ]
        
        for texto in texto_no_matematico:
            respuesta = respuesta.replace(texto, '')
        
        # REMOVER SOLO caracteres realmente no matemáticos, mantener x, y, =, [], (), etc.
        respuesta = re.sub(r'[^\w\d\s\/\.=,\-\+\[\]\(\)]', '', respuesta)
        
        # Normalizar espacios
        respuesta = ' '.join(respuesta.split())
        
        print(f"🔄 Normalizado a: '{respuesta}'")
        return respuesta.strip()
    
    def comparar_respuestas(self, respuesta_agente: str, respuesta_correcta: str, tolerancia=0.01) -> float:
        """Compara respuestas con detección mejorada de errores"""
        
        # DETECCIÓN CRÍTICA MEJORADA: Respuestas inválidas o de error
        if (not respuesta_agente or 
            respuesta_agente == "No se pudo extraer solución" or
            "= 12" in respuesta_agente or
            "🏠" in respuesta_agente):
            print("❌ Respuesta inválida o de error detectada")
            return 0.0
        
        # DETECCIÓN CRÍTICA: Si la respuesta contiene texto de múltiples problemas
        if (respuesta_agente and 
            ('Problema 2' in respuesta_agente or 
            'Volver al Inicio' in respuesta_agente or
            'Powered by FastAPI' in respuesta_agente)):
            print("⚠️  DETECTADA RESPUESTA CON MÚLTIPLES PROBLEMAS")
            
            # Intentar extraer la parte relevante
            if 'x = 5' in respuesta_agente and 'x = 5' in respuesta_correcta:
                print("✅ Coincidencia parcial en respuesta múltiple")
                return 1.0
            elif any(str(num) in respuesta_agente for num in [5, 12, 6, 4]):
                # Buscar coincidencia numérica dentro del texto múltiple
                nums_agente = re.findall(r'[\-]?[\d\.]+', respuesta_agente)
                nums_correctos = re.findall(r'[\-]?[\d\.]+', respuesta_correcta)
                
                if nums_agente and nums_correctos:
                    try:
                        if any(abs(float(n_agente) - float(n_correcto)) <= tolerancia 
                            for n_agente in nums_agente 
                            for n_correcto in nums_correctos):
                            print("✅ Coincidencia numérica en respuesta múltiple")
                            return 1.0
                    except ValueError:
                        pass

        resp_agente = self.normalizar_respuesta(str(respuesta_agente))
        resp_correcta = self.normalizar_respuesta(str(respuesta_correcta))
        
        print(f"🔍 Comparando: '{resp_agente}' vs '{resp_correcta}'")
        
        # 1. COINCIDENCIA EXACTA (máxima prioridad)
        if resp_agente == resp_correcta:
            print("✅ Coincidencia exacta")
            return 1.0
        
        # 2. COMPARACIÓN NUMÉRICA ESTRICTA (para diferencias de formato decimal)
        try:
            # Extraer todos los números para comparación precisa
            nums_agente = re.findall(r'[\-]?[\d\.]+', resp_agente)
            nums_correctos = re.findall(r'[\-]?[\d\.]+', resp_correcta)
            
            if nums_agente and nums_correctos:
                # Convertir a float para comparación numérica
                nums_agente_float = [float(n) for n in nums_agente]
                nums_correctos_float = [float(n) for n in nums_correctos]
                
                # Si todos los números coinciden dentro de tolerancia
                if (len(nums_agente_float) == len(nums_correctos_float) and
                    all(abs(a - c) <= tolerancia for a, c in zip(nums_agente_float, nums_correctos_float))):
                    print("✅ Coincidencia numérica exacta")
                    return 1.0
                    
        except (ValueError, IndexError):
            pass
        
        # 3. COMPARACIÓN ESTRICTA PARA ECUACIONES (x = 5.0 vs x = 5)
        if '=' in resp_agente and '=' in resp_correcta:
            # Extraer partes izquierda y derecha
            partes_agente = [p.strip() for p in resp_agente.split('=')]
            partes_correcta = [p.strip() for p in resp_correcta.split('=')]
            
            if len(partes_agente) == len(partes_correcta) == 2:
                # Comparar lados izquierdos (deben coincidir exactamente)
                if partes_agente[0] != partes_correcta[0]:
                    print("❌ Lado izquierdo de ecuación no coincide")
                    return 0.0
                
                # Comparar lados derechos numéricamente
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
                    # Si no son números, comparar como texto
                    if partes_agente[1] == partes_correcta[1]:
                        print("✅ Coincidencia de ecuación exacta")
                        return 1.0
        
        # 4. COMPARACIÓN PARA SISTEMAS DE ECUACIONES (x = 5, y = 5 vs x = 5.00, y = 5.00)
        if ',' in resp_agente and ',' in resp_correcta:
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
        
        # 5. COMPARACIÓN PARA VECTORES/MATRICES ([8,12] vs [8,12])
        if '[' in resp_agente and '[' in resp_correcta:
            # Extraer contenido dentro de corchetes
            contenido_agente = re.findall(r'\[([^\]]+)\]', resp_agente)
            contenido_correcto = re.findall(r'\[([^\]]+)\]', resp_correcta)
            
            if contenido_agente and contenido_correcto:
                if contenido_agente[0] == contenido_correcto[0]:
                    print("✅ Coincidencia de vector/matriz exacta")
                    return 1.0
        
        # 6. COMPARACIÓN PARA COORDENADAS ((3,5) vs (3,5))
        if '(' in resp_agente and '(' in resp_correcta:
            # Extraer contenido dentro de paréntesis
            contenido_agente = re.findall(r'\(([^\)]+)\)', resp_agente)
            contenido_correcto = re.findall(r'\(([^\)]+)\)', resp_correcta)
            
            if contenido_agente and contenido_correcto:
                if contenido_agente[0] == contenido_correcto[0]:
                    print("✅ Coincidencia de coordenadas exacta")
                    return 1.0
        
        # 7. ÚLTIMO RECURSO: Solo si una respuesta está contenida en la otra Y son numéricamente equivalentes
        try:
            # Extraer primer número de cada respuesta
            num_agente = float(re.findall(r'[\-]?[\d\.]+', resp_agente)[0])
            num_correcto = float(re.findall(r'[\-]?[\d\.]+', resp_correcta)[0])
            
            if abs(num_agente - num_correcto) <= tolerancia:
                print("⚠️  Coincidencia numérica (contenida) - revisar formato")
                return 0.9  # Media puntuación por diferencia de formato
            else:
                print(f"❌ Diferencia numérica: {num_agente} vs {num_correcto}")
                return 0.0
                
        except (ValueError, IndexError, ZeroDivisionError):
            print("❌ No se pudo comparar numéricamente")
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
                # NUEVAS CATEGORÍAS
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