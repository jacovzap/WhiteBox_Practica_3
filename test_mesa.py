from operator import truediv
from re import M
import pytest
from mesa import *
from carta import *
from mazo import *
from pila_cartas import *
class TestMesa():
        def test_imprimir(self):
                mesa = Mesa()
                mesa.imprimir()
                assert 1
        def test_imprimirV2(self):
                mesa = Mesa()
                pila1=PilaCartas()
                pila2=PilaCartas()
                pila3=PilaCartas()
                pila4=PilaCartas()
                mesa.fundaciones=[pila1,pila2]
                mesa.pilas_tablero=[pila3,pila4]
                mesa.imprimir()
                assert 1
        def test_descarte(self):
                mesa = Mesa()
                mesa.descarte=True
                mesa.imprimir()
                assert 1
        def test_mensaje_jugada_descarte(self):
                mesa = Mesa()
                pila1=PilaCartas()
                pila2=PilaCartas()
                mesa.fundaciones=[pila1,pila2]
                mesa.descarte=True
                mesa.mensaje_jugada()
                assert 1
        def test_mensaje_jugada_return(self):
                mesa = Mesa()
                pila1=PilaCartas()
                pila2=PilaCartas()
                pila3=PilaCartas()
                pila4=PilaCartas()
                mesa.fundaciones=[pila1,pila2]
                mesa.pilas_tablero=[pila3,pila4]
                assert mesa.mensaje_jugada()=='Ingrese [1-2] [A-B] M Q: '
        def test_parsear_jugadada_mazo(self):
                mesa = Mesa()
                res=mesa.parsear_jugada('M')
                assert res==[(2,0)]
        def test_parsear_jugadada_Descarte(self):
                mesa = Mesa()
                res=mesa.parsear_jugada('N')
                assert res==None
                
      
                