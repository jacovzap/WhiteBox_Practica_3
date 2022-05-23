import pytest
from pila_cartas import *
from carta import *
from mazo import *

class TestPila():
        def test_pila_esvacia(self):
                pila = PilaCartas()
                assert pila.es_vacia() == True
        def test_apilar(self):
                pila = PilaCartas()
                cartaA = Carta(2,2,True)
                pila.apilar(cartaA)
                assert 1    
        def test_noesvacia(self):
                pila = PilaCartas()
                cartaA = Carta(2,2,True)
                pila.apilar(cartaA)
                assert pila.es_vacia() == False
        def test_pila_topeVacia(self):
                pila = PilaCartas()
                with pytest.raises(SolitarioError):
                        pila.tope()
        def test_pila_tope(self):
                pila = PilaCartas()
                cartaA = Carta(2,2,True)
                pila.apilar(cartaA)
                pila.tope()
                assert 1
        def test_desapilar(self):
                pila = PilaCartas()
                cartaA = Carta(2,2,True)
                pila.apilar(cartaA)
                pila.desapilar()
                assert 1
        def test_desapilar_vacio(self):
                pila = PilaCartas()
                cartaA = Carta(2,2,True)
                with pytest.raises(SolitarioError):
                        pila.desapilar()
                 
        def test_apilar_V2(self):
                pila = PilaCartas()
                pila.valor_inicial=2
                """Indica que el valor de la ultima carta es 2""" 
                cartaA = Carta(2,3,False)
                pila.valor_inicial=2
                pila.apilar(cartaA)
                assert 1
        def test_apilar_V3(self):
                pila2 = PilaCartas()
                cartaA = Carta(1,3,True)
                cartaB = Carta(2,3,True)
                cartaC = Carta(3,3,True)
                pila2.apilar(cartaA)
                pila2.apilar(cartaB)
                pila2.apilar(cartaC)
                assert 1                                                
        def test_apilar_V4(self):#56
                pila2 = PilaCartas(pila_visible=False, valor_inicial=None, puede_desapilar=True, criterio_apilar=True, criterio_mover=None)
                cartaA = Carta(1,3,False)
                pila2.apilar(cartaA,False)
                assert 1      
        def test_apilar_V5(self):
                pila2 = PilaCartas(pila_visible=False, valor_inicial=None, puede_desapilar=True, criterio_apilar=True, criterio_mover=None)
                cartaA = Carta(1,3,False)
                pila2.apilar(cartaA,False)
                assert 1             
        def test_apilar_raiseerror(self):
                pila2 = PilaCartas(pila_visible=False, valor_inicial=2, puede_desapilar=True, criterio_apilar=True, criterio_mover=None)
                cartaA = Carta(1,3)
                with pytest.raises(SolitarioError):
                        pila2.apilar(cartaA,False)
                            
        def test_Mover(self):
                pila1 = PilaCartas()
                pila2 = PilaCartas()
                with pytest.raises(SolitarioError):
                        pila2.mover(pila1)
                                    
        def test_str(self):
                pila1 = PilaCartas()
                cartaA = Carta(1,3,True)
                assert pila1.__str__()=='X' 
        def test_str2(self):
                pila1 = PilaCartas()
                cartaA = Carta(1,3,True)
                pila1.apilar(cartaA)
                pila1.pila_visible=True 
                assert pila1.__str__()=='▓'                                               