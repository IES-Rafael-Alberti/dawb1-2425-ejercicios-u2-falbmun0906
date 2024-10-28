import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_08 import hacer_triangulo

@pytest.mark.parametrize("numero, expected", [
    (1, "1"),
    (3, "1\n1 3"),
    (5, "1\n1 3\n3 1 5"),
    (7, "1\n1 3\n3 1 5\n5 3 1 7"),
    (2, "1"),
    (0, ""),
    (-1, ""),
])

def test_hacer_triangulo(numero, expected):
    assert hacer_triangulo(numero) == expected