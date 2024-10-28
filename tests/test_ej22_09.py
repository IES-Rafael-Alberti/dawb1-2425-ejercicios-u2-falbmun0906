import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_09 import comprobar_contrasenia

def test_comprobar_contrasenia_correcta(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "contraseña")
    assert comprobar_contrasenia() == True

def test_comprobar_contrasenia_incorrecta_y_correcta(monkeypatch):
    inputs = iter(["mal_contraseña", "contraseña"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert comprobar_contrasenia() == True

def test_comprobar_contrasenia_todas_incorrectas(monkeypatch):
    inputs = iter(["mal_contraseña", "otra_contraseña"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        comprobar_contrasenia()