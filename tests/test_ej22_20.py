import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_20 import coincidencias

@pytest.mark.parametrize("letra, frase, expected", [
    ("a", "hola que tal", "Posición 3: Sí coincide (a)"),
    ("b", "hola que tal", ""),
    ("", "hola que tal", ""),
    ("z", "hola que tal", ""),
    ("t", "hola que tal", "Posición 9: Sí coincide (t)"),

])

def test_coincidencias(letra, frase, expected):
    assert coincidencias(letra, frase) == expected
