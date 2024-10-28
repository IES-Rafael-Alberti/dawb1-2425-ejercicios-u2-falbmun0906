import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_11 import dar_vuelta_palabra

def test_dar_vuelta_palabra():
    assert dar_vuelta_palabra("palabra") == "a\nr\nb\na\nl\na\np"
    assert dar_vuelta_palabra("contraseña") == "a\nñ\ne\ns\na\nr\nt\nn\no\nc"
    assert dar_vuelta_palabra("vuelta") == "a\nt\nl\ne\nu\nv"
    assert dar_vuelta_palabra("patata") == "a\nt\na\nt\na\np"
    assert dar_vuelta_palabra("arenera") == "a\nr\ne\nn\ne\nr\na"
    assert dar_vuelta_palabra("a") == "a"
    assert dar_vuelta_palabra("") == ""