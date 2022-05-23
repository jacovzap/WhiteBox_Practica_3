from mesa import *
from mazo import *
from carta import *
from solitario_clasico import SolitarioClasico
from pila_cartas import *
import mazo
import pytest
class TestSolitarioClasico:
    def test_armar(self):
        mesa=Mesa()
        sol_cla=SolitarioClasico(mesa)
        sol_cla.armar()
        assert 1
    def test_termino(self):
        mesa=Mesa()
        sol_cla=SolitarioClasico(mesa)
        assert sol_cla.termino()==True
    def test_terminoV2(self):
        mesa=Mesa()
        pila1=PilaCartas()
        mesa.fundaciones=[pila1]
        sol_cla=SolitarioClasico(mesa)
        assert sol_cla.termino()==False
    def test_carta_pila(self):
        mesa=Mesa()
        pila1=PilaCartas()
        pila2=PilaCartas()
        sol_cla=SolitarioClasico(mesa)
        with pytest.raises(SolitarioError):
                sol_cla._carta_a_pila(pila1,pila2)
    def test_carta_pilaV2(self):
        mesa=Mesa()
        carta=Carta(1,2,True)
        pila1=PilaCartas()
        pila1.apilar(carta)
        pila2=PilaCartas()
        sol_cla=SolitarioClasico(mesa)
        sol_cla._carta_a_pila(pila1,pila2)
        assert 1            
    def test_subpila_pila(self):
        mesa=Mesa()
        pila1=PilaCartas()
        pila2=PilaCartas()
        sol_cla=SolitarioClasico(mesa)
        with pytest.raises(SolitarioError):
                sol_cla._subpila_a_pila(pila1,pila2)
    def test_subpila_pilaV2(self):
        mesa=Mesa()
        carta=Carta(1,2,True)
        pila1=PilaCartas()
        pila1.apilar(carta)
        pila2=PilaCartas()
        sol_cla=SolitarioClasico(mesa)
        sol_cla._subpila_a_pila(pila1,pila2)
        assert 1
    def test_auxJugada(self):
        mesa = Mesa()
        solit = SolitarioClasico(mesa)
        solit.armar()
        jugada = mesa.parsear_jugada('m')
        solit.auxiliar_jugar(2, 1,0,PILA_TABLERO,0)
        assert 1
    def test_auxJugadaV2(self):
        mesa = Mesa()
        solit = SolitarioClasico(mesa)
        solit.armar()
        jugada = mesa.parsear_jugada('m')
        with pytest.raises(SolitarioError):
            solit.auxiliar_jugar(1, 1,0,PILA_TABLERO,0)
        assert 1
