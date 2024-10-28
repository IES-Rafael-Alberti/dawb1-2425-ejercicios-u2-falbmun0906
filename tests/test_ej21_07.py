import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_07 import comprobar_tipo

@pytest.mark.parametrize("renta, expected", [
    (0, 0.0),
    (5000, 0.05),
    (15000, 0.15),
    (25000, 0.20),
    (40000, 0.30),
    (70000, 0.45)
])

def test_comprobar_tipo(monkeypatch, renta, expected):
    monkeypatch.setattr('src.condicionales.ej21_07.introduce_renta', lambda: renta)
    assert comprobar_tipo() == expected