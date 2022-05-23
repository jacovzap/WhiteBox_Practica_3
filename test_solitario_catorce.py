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

class TestSolitarioCatorce:
    def test_solitCatorce_armar(self):
        mesa = Mesa()
        solit = SolitarioCatorce(mesa)
        solit.armar()
        assert 1
        
    def test_solitCatorce_Termino_T(self):
        mesa = Mesa()
        solit = SolitarioCatorce(mesa)
        assert solit.termino() == True
        
    def test_solitCatorce_Termino_F(self):
        mesa = Mesa()
        solit = SolitarioCatorce(mesa)
        solit.armar()
        assert solit.termino() == False
        
    def test_solitCatorce_jugar_Error(self):
        mesa = Mesa()
        jugada = mesa.parsear_jugada('m')
        solit = SolitarioCatorce(mesa)
        solit.armar()
        with pytest.raises(SolitarioError):
            solit.jugar(jugada)

    def test_solitCatorce_jugar(self):
        mesa = Mesa()
        solit = SolitarioCatorce(mesa)
        solit.armar()
        jugada2 = [(PILA_TABLERO,0),(PILA_TABLERO, 1)]
        jugada = mesa.parsear_jugada('1')
        cartaA = Carta(6,2,False)
        cartaB = Carta(8,1,False)
        solit.mesa.pilas_tablero[0].apilar(cartaA, True)
        solit.mesa.pilas_tablero[1].apilar(cartaB, True)
        solit.jugar(jugada2)
        assert 1 
