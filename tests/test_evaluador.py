import pytest
from green_agent.evaluador import GreenAgentMatematico


def test_extrae_desde_bloque_principal():
    g = GreenAgentMatematico()
    html = '<div class="solution-text">20</div><div class="practice">Solución: x = 5</div>'
    sol = g.extraer_solucion_de_respuesta(html)
    assert sol.strip() == '20'


def test_no_extrae_lang_token():
    g = GreenAgentMatematico()
    # HTML con token /lang y un número válido
    html = '<div>/lang</div><div>Solución: 15</div>'
    sol = g.extraer_solucion_de_respuesta(html)
    assert 'lang' not in sol.lower()
    assert '15' in sol or sol.strip() == '15'


def test_permite_fraccion_con_barra():
    g = GreenAgentMatematico()
    html = '<div>Solución: 5/6</div>'
    sol = g.extraer_solucion_de_respuesta(html)
    assert '5/6' in sol
