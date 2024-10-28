import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_04 import es_par

@pytest.mark.parametrize("input_numero, expected", [
    (4, (4, True)),
    (3, (3, False)),
    (0, (0, True)),
    (-2, (-2, True)),
    (-3, (-3, False)),
])
def test_es_par(monkeypatch, input_numero, expected):
    monkeypatch.setattr('src.condicionales.ej21_04.dame_numero', lambda: input_numero)
    
    assert es_par() == expected