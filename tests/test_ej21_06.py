import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_06 import letra_nombre
from src.condicionales.ej21_06 import elegir_clase

@pytest.mark.parametrize("nombre, abc, expected", [
    ("fran", "abcdefghijklmnñopqrstuvwxyz", True),
    ("pablo", "abcdefghijklmnñopqrstuvwxyz", False),
    ("beni", "abcdefghijklmnñopqrstuvwxyz", True),
    ("viti", "abcdefghijklmnñopqrstuvwxyz", False),
    ("", "abcdefghijklmnñopqrstuvwxyz", False),
    ("david", "abcdefghijklmnñopqrstuvwxyz", True),
    ("jose", "abcdefghijklmnñopqrstuvwxyz", True),
])
def test_letra_nombre(nombre, abc, expected):
    assert letra_nombre(nombre, abc) == expected

@pytest.mark.parametrize("letra_inicial, sexo, expected", [
    (True, False, True),
    (False, True, True),
    (True, True, False),
    (False, False, False),
])
def test_elegir_clase(letra_inicial, sexo, expected):
    assert elegir_clase(letra_inicial, sexo) == expected