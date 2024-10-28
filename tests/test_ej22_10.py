import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_10 import es_primo

@pytest.mark.parametrize("numero, expected", [
    (2, True),
    (3, True),
    (4, False),
    (11, True),
    (15, False),
    (1, False),
    (0, False),
    (-3, False)
])

def test_es_primo(numero, expected):
    assert es_primo(numero) == expected