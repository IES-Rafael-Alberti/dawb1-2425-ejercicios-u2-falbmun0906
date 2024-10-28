import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_01 import es_mayor

@pytest.mark.parametrize("edad, expected", [
    (20, "Eres mayor de edad."),
    (15, "Eres menor de edad."),
    (0, "Aún no has nacido."),
    (-5, "Aún no has nacido."),
    (18, "Eres mayor de edad.")
])

def test_es_mayor(monkeypatch, edad, expected):
    monkeypatch.setattr('src.condicionales.ej21_01.dame_edad', lambda: edad)

    assert es_mayor() == expected