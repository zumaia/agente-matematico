# green_agent/evaluador.py
"""
Evaluador principal para Green Agent matemático - VERSIÓN DE EMERGENCIA
"""

import time
import requests
import re
from typing import List, Dict, Any
from .dataset_matematico import MATEMATICAS_DATASET, obtener_problemas_aleatorios
from .metricas import EvaluadorMetricas

class GreenAgentMatematico:
    def __init__(self):
        self.dataset = MATEMATICAS_DATASET
        self.evaluador_metricas = EvaluadorMetricas()
        self.nombre = "MathESO-Evaluator"
        self.version = "1.0.0"
    
    def enviar_problema_a_agente(self, purple_agent_url: str, problema: str, timeout=30) -> Dict:
        """Envía un problema a un Purple Agent y obtiene respuesta"""
        try:
            response = requests.post(
                f"{purple_agent_url}/resolver-web",
                data={"problema": problema, "lang": "es"},
                timeout=timeout
            )
            
            if response.status_code == 200:
                return {
                    "exito": True,
                    "respuesta": response.text,
                    "estado": "completado"
                }
            else:
                return {
                    "exito": False,
                    "error": f"HTTP {response.status_code}",
                    "estado": "error"
                }
                
        except requests.exceptions.Timeout:
            return {
                "exito": False,
                "error": "Timeout",
                "estado": "timeout"
            }
        except Exception as e:
            return {
                "exito": False,
                "error": str(e),
                "estado": "error"
            }
    
    def extraer_solucion_de_respuesta(self, respuesta_html: str) -> str:
        """Extrae la solución del HTML - VERSIÓN DE EMERGENCIA COMPLETA"""
        print("🔍 INICIANDO EXTRACCIÓN DE EMERGENCIA...")
        
        # Limpiar HTML y convertir a texto
        texto_plano = re.sub(r'<[^>]+>', ' ', respuesta_html)
        texto_plano = re.sub(r'\s+', ' ', texto_plano).strip()
        
        print(f"📄 Texto limpio ({len(texto_plano)} chars): {texto_plano[:200]}...")
        # PRIMER INTENTO: Extraer la solución desde el bloque principal si existe
        # Buscar la clase 'solution-text' generada por el servidor (evitar extracciones de práctica)
        main_block_match = re.search(r'<div[^>]+class=["\']solution-text["\'][^>]*>(.*?)</div>', respuesta_html, re.IGNORECASE | re.DOTALL)
        if main_block_match:
            candidate = self._limpiar_respuesta(main_block_match.group(1))
            if candidate and self._es_respuesta_valida(candidate):
                print(f"🎯 EXTRAÍDO DESDE BLOQUE PRINCIPAL: '{candidate}'")
                return candidate
        
        # DETECCIÓN DE FALLO CRÍTICO: Si contiene "= 12 🏠" o texto similar, es un error
        if "= 12" in texto_plano and "🏠" in texto_plano:
            print("❌ DETECTADO: Respuesta de error genérica - usando extracción agresiva")
            return self._extraccion_agresiva(texto_plano)
        
        # ESTRATEGIA 1: Buscar patrones de solución estructurados
        solucion = self._buscar_patrones_estructurados(texto_plano)
        if solucion:
            return solucion
        
        # ESTRATEGIA 2: Búsqueda contextual por tipo de problema
        solucion = self._busqueda_contextual(texto_plano)
        if solucion:
            return solucion
        
        # ESTRATEGIA 3: Extracción agresiva como último recurso
        return self._extraccion_agresiva(texto_plano)
    
    def _buscar_patrones_estructurados(self, texto: str) -> str:
        """Busca patrones de solución bien estructurados"""
        patrones = [
            # Patrones con formato "Solución: valor"
            r'Solución\s*[:\-]\s*([^\n\.]{1,50}?)(?=\.|\n|$)',
            r'Resultado\s*[:\-]\s*([^\n\.]{1,50}?)(?=\.|\n|$)',
            r'Respuesta\s*[:\-]\s*([^\n\.]{1,50}?)(?=\.|\n|$)',
            
            # Patrones con formato "= valor"
            r'=\s*([^\n\.]{1,30}?)(?=\.|\n|$)',
            
            # Patrones con formato "es valor"  
            r'es\s+([^\n\.]{1,30}?)(?=\.|\n|$)',
            
            # Expresiones matemáticas específicas
            r'x\s*=\s*[\d\.]+',
            r'\[[\d,\s]+\]',
            r'\([\d,\s]+\)',
            r'[\-]?[\d\.]+\s*\/\s*[\d\.]+',  # Fracciones
        ]
        
        for patron in patrones:
            matches = re.findall(patron, texto, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0]
                cleaned = self._limpiar_respuesta(match)
                if cleaned and self._es_respuesta_valida(cleaned):
                    print(f"🎯 PATRÓN ESTRUCTURADO: '{cleaned}'")
                    return cleaned
        return ""
    
    def _busqueda_contextual(self, texto: str) -> str:
        """Búsqueda inteligente basada en el contexto del problema"""
        # Buscar en párrafos que contengan palabras clave matemáticas
        parrafos = texto.split('.')
        
        for parrafo in parrafos:
            parrafo = parrafo.strip()
            if any(keyword in parrafo.lower() for keyword in 
                  ['solución', 'resultado', 'respuesta', 'calculamos', 'obtenemos']):
                
                # Extraer expresiones matemáticas del párrafo
                expresiones = self._extraer_expresiones_matematicas(parrafo)
                for expr in expresiones:
                    if self._es_respuesta_valida(expr):
                        print(f"🎯 CONTEXTO MATEMÁTICO: '{expr}'")
                        return expr
        
        return ""
    
    def _extraccion_agresiva(self, texto: str) -> str:
        """Extracción agresiva como último recurso"""
        print("🔍 EXTRACCIÓN AGRESIVA...")
        
        # Extraer TODAS las expresiones matemáticas
        todas_expresiones = self._extraer_expresiones_matematicas(texto)
        print(f"🔍 Todas las expresiones: {todas_expresiones}")
        
        # Filtrar y priorizar
        for expr in todas_expresiones:
            if self._es_respuesta_valida(expr):
                print(f"🎯 EXPRESIÓN VÁLIDA: '{expr}'")
                return expr
        
        # Último recurso: primer número que parezca respuesta
        numeros = re.findall(r'[\-]?[\d\.]+', texto)
        numeros_filtrados = [n for n in numeros if self._es_numero_valido(n)]
        
        if numeros_filtrados:
            resultado = numeros_filtrados[0]
            print(f"🎯 ÚLTIMO RECURSO: '{resultado}'")
            return resultado
        
        print("❌ EXTRACCIÓN FALLIDA")
        return "No se pudo extraer solución"
    
    def _extraer_expresiones_matematicas(self, texto: str) -> List[str]:
        """Extrae todas las expresiones matemáticas potenciales"""
        expresiones = []
        
        # Patrones complejos primero
        patrones_complejos = [
            r'x\s*=\s*[\d\.]+',                    # x = 5
            r'[xy]\s*=\s*[\-]?[\d\.]+',           # x = -2, y = 3
            r'\[[\d,\s]+\]',                      # [8,12]
            r'\([\d,\s]+\)',                      # (3,5)
            r'[\-]?[\d\.]+\s*\/\s*[\d\.]+',      # 5/6
            r'f⁻¹\(x\)\s*=\s*[^\)]+',            # f⁻¹(x) = (x+1)/3
            r'aₙ\s*=\s*[^\n]+',                  # aₙ = 3n
            r'[\-]?[\d\.]+',                     # Números simples
        ]
        
        for patron in patrones_complejos:
            matches = re.findall(patron, texto)
            expresiones.extend(matches)
        
        return expresiones
    
    def _limpiar_respuesta(self, respuesta: str) -> str:
        """Limpia una respuesta eliminando caracteres no deseados"""
        if not respuesta:
            return ""
        
        # Eliminar emojis y caracteres especiales
        respuesta = re.sub(r'[^\w\d\s\/\.=,\-\+\[\]\(\)]', '', respuesta)
        respuesta = respuesta.strip()
        
        # Eliminar espacios múltiples
        respuesta = re.sub(r'\s+', ' ', respuesta)
        
        return respuesta

    def _es_respuesta_plausible_text(self, texto: str) -> bool:
        """Filtros adicionales para evitar artefactos de plantilla o rutas como '/lang'."""
        t = texto.strip()
        if not t:
            return False

        # Excluir tokens que claramente son rutas o fragmentos del template
        if '/' in t:
            # Permitir fracciones simples como '5/6' o expresiones con paréntesis '(x+1)/3'
            frac_pattern = re.compile(r'^[\-]?[0-9]+\/[0-9]+$')
            expr_frac_pattern = re.compile(r'[\w\)\]]+\s*\/\s*[\w\(\[]+')
            if frac_pattern.match(t) or expr_frac_pattern.search(t):
                return True
            return False

        # Excluir tokens que parecen rutas o nombres de plantilla
        if t.startswith('/') or t.lower().startswith('powered by') or 'language-switcher' in t.lower():
            return False

        # Excluir textos que tengan caracteres no útiles (p. ej., '/lang' o tokens aislados)
        if re.match(r'^\/\w+$', t):
            return False

        return True
    
    def _es_respuesta_valida(self, respuesta: str) -> bool:
        """Determina si una respuesta parece ser válida"""
        if not respuesta or len(respuesta) < 1:
            return False
        
        # Excluir respuestas obviamente incorrectas
        exclusiones = ['= 12', '🏠', 'volver', 'inicio', 'fastapi', 'groq']
        if any(excl in respuesta.lower() for excl in exclusiones):
            return False
        
        # Excluir respuestas demasiado largas (probablemente no son respuestas)
        if len(respuesta) > 50:
            return False
        
        # Debe contener algún contenido matemático
        if not any(char in respuesta for char in '0123456789x[](),/-'):
            return False

        # Filtros adicionales para evitar artefactos de plantilla
        if not self._es_respuesta_plausible_text(respuesta):
            return False
        
        return True
    
    def _es_numero_valido(self, numero: str) -> bool:
        """Determina si un número parece ser una respuesta válida"""
        try:
            num = float(numero)
            # Excluir números que son comúnmente parte del problema, no la solución
            numeros_excluir = ['12', '6', '4', '5', '3', '2', '1', '7', '8']  # Números comunes en enunciados
            return numero not in numeros_excluir and abs(num) > 1
        except ValueError:
            return False
    
    def evaluar_purple_agent(self, purple_agent_url: str, problemas_a_usar=None) -> Dict[str, Any]:
        """Evalúa un Purple Agent con problemas matemáticos"""
        if problemas_a_usar is None:
            problemas_a_usar = obtener_problemas_aleatorios(5)
        
        resultados = []
        tiempos_respuesta = []
        
        for problema_data in problemas_a_usar:
            start_time = time.time()
            
            respuesta_raw = self.enviar_problema_a_agente(purple_agent_url, problema_data["problema"])
            tiempo_respuesta = time.time() - start_time
            tiempos_respuesta.append(tiempo_respuesta)
            
            if respuesta_raw["exito"]:
                solucion_extraida = self.extraer_solucion_de_respuesta(respuesta_raw["respuesta"])
                puntuacion = self.evaluador_metricas.comparar_respuestas(
                    solucion_extraida, 
                    problema_data["solucion_esperada"]
                )
                puntuacion_obtenida = puntuacion * problema_data["puntos"]
            else:
                solucion_extraida = f"Error: {respuesta_raw['error']}"
                puntuacion_obtenida = 0
            
            resultados.append({
                "task_id": problema_data["id"],
                "problema": problema_data["problema"],
                "solucion_correcta": problema_data["solucion_esperada"],
                "solucion_agente": solucion_extraida,
                "puntuacion_obtenida": round(puntuacion_obtenida, 2),
                "puntos": problema_data["puntos"],
                "tiempo_respuesta": round(tiempo_respuesta, 2),
                "categoria": problema_data["categoria"],
                "dificultad": problema_data["dificultad"],
                "tipo": problema_data["tipo"],
                "estado": respuesta_raw["estado"]
            })
        
        # Calcular métricas
        metricas_finales = self.evaluador_metricas.calcular_puntuacion_final(resultados)
        metricas_estandar = self.evaluador_metricas.calcular_metricas_estandar(resultados)
        
        metricas_finales.update({
            "tiempo_promedio_respuesta": round(sum(tiempos_respuesta) / len(tiempos_respuesta), 2),
            "green_agent": self.nombre,
            "version": self.version
        })
        
        return {
            "metricas_generales": metricas_finales,
            "metricas_estandar": metricas_estandar,
            "resultados_detallados": resultados
        }