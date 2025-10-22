import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import os
from typing import Optional

def generar_grafico_funcion(ecuacion: str, x_range: tuple = (-10, 10)) -> Optional[str]:
    """
    Genera gráfico de una función y lo guarda como base64
    """
    try:
        # Crear datos para el gráfico
        x = np.linspace(x_range[0], x_range[1], 400)
        
        # Evaluar la ecuación (implementación básica)
        y = evaluar_funcion_simple(ecuacion, x)
        
        if y is None:
            return None
        
        # Crear figura
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {ecuacion}')
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Gráfico de f(x) = {ecuacion}')
        plt.legend()
        
        # Convertir a base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        plt.close()
        
        return f"data:image/png;base64,{image_base64}"
        
    except Exception as e:
        print(f"Error generando gráfico: {e}")
        return None

def evaluar_funcion_simple(ecuacion: str, x_values: np.ndarray) -> Optional[np.ndarray]:
    """
    Evalúa funciones simples para graficar
    """
    try:
        ecuacion = ecuacion.lower().replace('^', '**').replace(' ', '')
        
        # Mapeo de funciones matemáticas
        safe_dict = {
            'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
            'sqrt': np.sqrt, 'exp': np.exp, 'log': np.log,
            'x': x_values
        }
        
        # Evaluar de forma segura
        y = eval(ecuacion, {"__builtins__": None}, safe_dict)
        return y
        
    except Exception as e:
        print(f"Error evaluando función: {e}")
        return None

def generar_grafico_geometria(tipo: str, datos: dict) -> Optional[str]:
    """
    Genera gráficos para problemas de geometría
    """
    try:
        plt.figure(figsize=(8, 6))
        
        if tipo == "circulo":
            radio = datos.get('radio', 1)
            circle = plt.Circle((0, 0), radio, fill=False, color='blue', linewidth=2)
            plt.gca().add_artist(circle)
            plt.xlim(-radio-1, radio+1)
            plt.ylim(-radio-1, radio+1)
            plt.title(f'Círculo de radio {radio}')
            
        elif tipo == "triangulo_rectangulo":
            base = datos.get('base', 3)
            altura = datos.get('altura', 4)
            plt.plot([0, base, 0, 0], [0, 0, altura, 0], 'b-', linewidth=2)
            plt.title(f'Triángulo Rectángulo: base={base}, altura={altura}')
            
        elif tipo == "rectangulo":
            ancho = datos.get('ancho', 4)
            alto = datos.get('alto', 3)
            plt.plot([0, ancho, ancho, 0, 0], [0, 0, alto, alto, 0], 'b-', linewidth=2)
            plt.title(f'Rectángulo: {ancho}×{alto}')
        
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        
        # Convertir a base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        plt.close()
        
        return f"data:image/png;base64,{image_base64}"
        
    except Exception as e:
        print(f"Error generando gráfico de geometría: {e}")
        return None