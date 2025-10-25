# green_agent/__init__.py
"""
Green Agent para evaluación matemática ESO
"""

from .evaluador import GreenAgentMatematico
from .dataset_matematico import MATEMATICAS_DATASET, obtener_problemas_aleatorios
from .metricas import EvaluadorMetricas

__all__ = [
    'GreenAgentMatematico', 
    'MATEMATICAS_DATASET', 
    'obtener_problemas_aleatorios',
    'EvaluadorMetricas'
]