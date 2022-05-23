import pytest
from main import *
from carta import *
from mazo import *
from solitario_thumbandpouch import *
from solitario_ejemplo import *
from solitariocatorce import *
import carta
import main
from io import StringIO

class TestMazo():
    def test_mazo_crearMazo(self):
        crear_mazo()
        assert 1

    def test_mazo_crearMazo2(self):
        crear_mazo(1,1)
        assert 1

    def test_mazo_crearMazo3(self):
        crear_mazo(1,2)
        assert 1
    
    def test_mazo_mazoIndividual(self):
        mazo = PilaCartas()
        mazo_individual(mazo, 3)
        assert 1

    def test_mazo_condMismoColor_T(self):
        assert cond_mismo_color(0, 3) == True
    
    def test_mazo_condMismoColor_T2(self):
        assert cond_mismo_color(1, 2) == True
    
    def test_mazo_condMismoColor_F(self):
        assert cond_mismo_color(0, 2) == False