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

class TestThumbandpunch:

    def test_thumbandpounch_armar(self):
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        assert 1

    def test_thumbandpounch_termino_T(self):
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        assert solit.termino() == True


    def test_thumbandpounch_termino_F(self):
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        assert solit.termino() == False

    def test_thumbandpounch_jugar(self):
        mesa = Mesa()
        jugada = mesa.parsear_jugada('m')
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        solit.jugar(jugada)
        assert 1

    def test_thumbandpounch_cartaAPila_Error(self):
        pilaA = PilaCartas()
        pilaB = PilaCartas()
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        with pytest.raises(SolitarioError):
            solit._carta_a_pila(pilaA, pilaB)
            
    def test_thumbandpounch_cartaAPila(self):
        pilaA = PilaCartas()
        pilaB = PilaCartas()
        cartaA = Carta(2,2,True)
        cartaB = Carta(3,2,False)
        mesa = Mesa()
        mesa.pilas_tablero.append(pilaA)
        mesa.pilas_tablero.append(pilaB)
        solit = SolitarioThumbAndPouch(mesa)
        pilaA.apilar(cartaA)
        pilaA.apilar(cartaB)
        solit._carta_a_pila(pilaA, pilaB)
        assert 1
        
    def test_thumbandpounch_subpilaAPila_Error(self):
        pilaA = PilaCartas()
        pilaB = PilaCartas()
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        with pytest.raises(SolitarioError):
            solit._subpila_a_pila(pilaA, pilaB)
            
    def test_thumbandpounch_renovar(self):
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        jugada = mesa.parsear_jugada('m')
        solit.jugar(jugada)
        solit.renovar_mazo()
        assert 1

    def test_thumbandpounch_auxJugada_Error(self):
        mesa = Mesa()
        jugada = mesa.parsear_jugada('q')
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        j0, p0 = jugada[0]
        j1, p1 = jugada[1] if len(jugada) == 2 else (SALIR, 0)
        with pytest.raises(SolitarioError):
            solit.auxiliar_jugar(len(jugada), j0, p0, j1, p1)

    def test_thumbandpounch_auxJugada_Error2(self):
        mesa = Mesa()
        pila = PilaCartas()
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        jugada = mesa.parsear_jugada('n')
        with pytest.raises(SolitarioError):
            solit.jugar(jugada)
            
    def test_thumbandpounch_auxJugada_Error3(self):
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        jugada = mesa.parsear_jugada('m')
        pila = PilaCartas()
        solit.mesa.mazo = pila
        with pytest.raises(SolitarioError):
            solit.auxiliar_jugar(1,0,1,0,1)
            
    def test_thumbandpounch_auxJugada(self):
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        jugada = mesa.parsear_jugada('m')
        solit.auxiliar_jugar(2, 1,0,PILA_TABLERO,0)
        assert 1
        
    def test_thumbandpounch_auxJugada_Error4(self):
        mesa = Mesa()
        solit = SolitarioThumbAndPouch(mesa)
        solit.armar()
        jugada = mesa.parsear_jugada('m')
        with pytest.raises(SolitarioError):
            solit.auxiliar_jugar(2, 1,1,PILA_TABLERO,1)
