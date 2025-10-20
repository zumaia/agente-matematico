import json
import hashlib
import time
import os

class CacheMatematico:
    def __init__(self, archivo="cache_matematico.json", ttl=3600):  # 1 hora por defecto
        self.archivo = archivo
        self.ttl = ttl
        self.cache = self.cargar_cache()
    
    def cargar_cache(self):
        """Carga el cache desde archivo"""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠️  Error cargando cache: {e}")
        return {}
    
    def guardar_cache(self):
        """Guarda el cache en archivo"""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️  Error guardando cache: {e}")
    
    def obtener_clave(self, problema):
        """Genera clave única para el problema"""
        return hashlib.md5(problema.encode('utf-8')).hexdigest()
    
    def obtener(self, problema):
        """Obtiene respuesta del cache si existe y es válida"""
        clave = self.obtener_clave(problema)
        if clave in self.cache:
            entrada = self.cache[clave]
            if time.time() - entrada['timestamp'] < self.ttl:
                print(f"💾 Cache hit: {problema[:50]}...")
                return entrada['respuesta']
            else:
                # Entrada expirada, eliminarla
                del self.cache[clave]
                self.guardar_cache()
        return None
    
    def guardar(self, problema, respuesta):
        """Guarda respuesta en el cache"""
        clave = self.obtener_clave(problema)
        self.cache[clave] = {
            'respuesta': respuesta,
            'timestamp': time.time(),
            'problema': problema[:100],  # Para debugging
            'tipo': respuesta.get('tipo_problema', 'desconocido')
        }
        self.guardar_cache()
        print(f"💾 Cache save: {problema[:50]}...")

# Instancia global del cache
cache_global = CacheMatematico()