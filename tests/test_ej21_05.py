import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_05 import es_elegible

@pytest.mark.parametrize("edad, ingresos, expected", [
    (16, 1000, True),
    (17, 1000, True),
    (16, 999, False),
    (15, 1000, False),
    (15, 999, False),
    (18, 1500, True),
    (20, 800, False),
])
def test_es_elegible(edad, ingresos, expected):
    assert es_elegible(edad, ingresos) == expected
