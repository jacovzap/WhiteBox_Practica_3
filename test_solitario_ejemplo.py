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

class TestSolitarioEjemplo:
    def test_solitEjem_armar(self):
        mesa = Mesa()
        solit = SolitarioEjemplo(mesa)
        solit.armar()
        assert 1
    
    def test_solitEjem_Termino_T(self):
        mesa = Mesa()
        solit = SolitarioEjemplo(mesa)
        assert solit.termino() == True
    
    def test_solitEjem_Termino_F(self):
        mesa = Mesa()
        solit = SolitarioEjemplo(mesa)
        solit.armar()
        assert solit.termino() == False

    def test_solitEjem_jugar_Error(self):
        mesa = Mesa()
        jugada = mesa.parsear_jugada('m')
        solit = SolitarioEjemplo(mesa)
        solit.armar()
        with pytest.raises(SolitarioError):
            solit.jugar(jugada)

    def test_solitEjem_jugar(self):
        mesa = Mesa()
        solit = SolitarioEjemplo(mesa)
        solit.armar()
        jugada2 = [(PILA_TABLERO,0),(PILA_TABLERO, 1)]
        jugada = mesa.parsear_jugada('1')
        print(jugada2)
        solit.jugar(jugada2)
        assert 1

    def test_solitEjem_jugar2(self):
        mesa = Mesa()
        solit = SolitarioEjemplo(mesa)
        solit.armar()
        jugada2 = [(PILA_TABLERO,0)]
        print(jugada2)
        solit.jugar(jugada2)
        assert 1
        
