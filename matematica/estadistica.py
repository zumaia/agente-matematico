import re
import math
from typing import List

def calcular_media(problema: str):
    """Calcula la media aritmética de números"""
    problema_lower = problema.lower()
    
    if "media" in problema_lower or "promedio" in problema_lower:
        # Buscar números en el problema
        numeros = [float(n) for n in re.findall(r'\d+\.?\d*', problema)]
        
        if len(numeros) >= 2:
            media = sum(numeros) / len(numeros)
            return {
                "tipo": "media_aritmetica",
                "solucion": f"Media = {media:.2f}",
                "pasos": [
                    f"Números: {numeros}",
                    f"Suma: {' + '.join(map(str, numeros))} = {sum(numeros)}",
                    f"Cantidad de números: {len(numeros)}",
                    f"Media = {sum(numeros)} / {len(numeros)} = {media:.2f}"
                ]
            }
    
    return None

def calcular_mediana(problema: str):
    """Calcula la mediana de números"""
    problema_lower = problema.lower()
    
    if "mediana" in problema_lower:
        numeros = [float(n) for n in re.findall(r'\d+\.?\d*', problema)]
        
        if len(numeros) >= 2:
            numeros_ordenados = sorted(numeros)
            n = len(numeros_ordenados)
            
            if n % 2 == 1:
                mediana = numeros_ordenados[n // 2]
                pasos = [f"Números ordenados: {numeros_ordenados}", f"Mediana (posición {n//2 + 1}): {mediana}"]
            else:
                mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
                pasos = [f"Números ordenados: {numeros_ordenados}", f"Mediana = ({numeros_ordenados[n//2 - 1]} + {numeros_ordenados[n//2]}) / 2 = {mediana}"]
            
            return {
                "tipo": "mediana",
                "solucion": f"Mediana = {mediana}",
                "pasos": pasos
            }
    
    return None

def calcular_moda(problema: str):
    """Calcula la moda de números"""
    problema_lower = problema.lower()
    
    if "moda" in problema_lower:
        numeros = [float(n) for n in re.findall(r'\d+\.?\d*', problema)]
        
        if len(numeros) >= 2:
            from collections import Counter
            contador = Counter(numeros)
            moda = contador.most_common(1)[0]
            
            # Verificar si hay múltiples modas
            modas = [num for num, count in contador.items() if count == moda[1]]
            
            if len(modas) == 1:
                solucion = f"Moda = {modas[0]} (aparece {moda[1]} veces)"
            else:
                solucion = f"Modas = {modas} (aparecen {moda[1]} veces cada una)"
            
            return {
                "tipo": "moda",
                "solucion": solucion,
                "pasos": [
                    f"Números: {numeros}",
                    f"Frecuencias: {dict(contador)}",
                    solucion
                ]
            }
    
    return None

def calcular_rango(problema: str):
    """Calcula el rango de números"""
    problema_lower = problema.lower()
    
    if "rango" in problema_lower:
        numeros = [float(n) for n in re.findall(r'\d+\.?\d*', problema)]
        
        if len(numeros) >= 2:
            maximo = max(numeros)
            minimo = min(numeros)
            rango = maximo - minimo
            
            return {
                "tipo": "rango",
                "solucion": f"Rango = {rango}",
                "pasos": [
                    f"Números: {numeros}",
                    f"Máximo = {maximo}, Mínimo = {minimo}",
                    f"Rango = {maximo} - {minimo} = {rango}"
                ]
            }
    
    return None

def probabilidad_basica(problema: str):
    """Calcula probabilidades básicas"""
    problema_lower = problema.lower()
    
    if "probabilidad" in problema_lower or "probable" in problema_lower:
        # Patrón: "probabilidad de sacar X en Y intentos"
        numeros = [int(n) for n in re.findall(r'\d+', problema)]
        
        if len(numeros) >= 2:
            favorable = numeros[0]
            total = numeros[1]
            
            if total > 0 and favorable <= total:
                probabilidad = favorable / total
                porcentaje = probabilidad * 100
                
                return {
                    "tipo": "probabilidad",
                    "solucion": f"Probabilidad = {probabilidad:.2f} ({porcentaje:.1f}%)",
                    "pasos": [
                        f"Casos favorables: {favorable}",
                        f"Casos totales: {total}",
                        f"Probabilidad = {favorable} / {total} = {probabilidad:.2f}",
                        f"Porcentaje: {porcentaje:.1f}%"
                    ]
                }
    
    return None