
import pytest
from main import *
from carta import *
from mazo import *
class TestCarta:
    def test_initialize_cart_object(self):
        valor = 5
        palo = 2
        boca_abajo = False
        carta = Carta(valor, palo, boca_abajo)
        assert carta.palo ==  2
        assert carta.valor == 5
        assert carta.boca_abajo == False

    def test_voltear_carta(self):
        carta = Carta(5, 2, True)
        carta.voltear()
        assert carta.boca_abajo == False

    def test_comp_uno(self):
        test_criterio = criterio()
        carta_uno = Carta(1, 1, False)
        carta_dos = Carta (2, 2, True)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False


    def test_comp_dos(self):
        test_criterio = criterio(None, 0)
        carta_uno_valor = 4
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 3
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False

    def test_comp_tres(self):
        test_criterio = criterio(None, 1)
        carta_uno_valor = 6
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 4
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False


    def test_comp_cuatro(self):
        test_criterio = criterio(None, 2)
        carta_uno_valor = 5
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 5
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False


    def test_comp_cinco(self):
        test_criterio = criterio(0, 5)
        carta_uno_valor = 2
        carta_uno_palo = 2
        carta_uno_boca_abajo = False
        carta_dos_valor = 2
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False


    def test_comp_seis(self):
        test_criterio = criterio(0, None)
        carta_uno_valor = 5
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 5
        carta_dos_palo = 2
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False


    def test_comp_siete(self):
        test_criterio = criterio(None, None)
        carta_uno_valor = 5
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 5
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == True


    def test_comp_ocho(self):
        test_criterio = criterio(1, None)
        carta_uno_valor = 5
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 5
        carta_dos_palo = 0
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False


    def test_comp_nueve(self):
        test_criterio = criterio(3, None)
        carta_uno_valor = 5
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 5
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False


    def test_comp_diez(self):
        test_criterio = criterio(2, None)
        carta_uno_valor = 5
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 5
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == False


    def test_comp_once(self):
        test_criterio = criterio(2, None)
        carta_uno_valor = 5
        carta_uno_palo = 0
        carta_uno_boca_abajo = False
        carta_dos_valor = 5
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == True


    def test_comp_doce(self):
        test_criterio = criterio(0, 0)
        carta_uno_valor = 5
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 6
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == True


    def test_comp_trece(self):
        test_criterio = criterio(1, 1)
        carta_uno_valor = 6
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 5
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == True


    def test_comp_catorce(self):
        test_criterio = criterio(3, 2)
        carta_uno_valor = 5
        carta_uno_palo = 1
        carta_uno_boca_abajo = False
        carta_dos_valor = 6
        carta_dos_palo = 2
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == True


    def test_comp_quince(self):
        test_criterio = criterio(2, None)
        carta_uno_valor = 5
        carta_uno_palo = 0
        carta_uno_boca_abajo = False
        carta_dos_valor = 6
        carta_dos_palo = 1
        carta_dos_boca_abajo = False

        carta_uno = Carta(carta_uno_valor, carta_uno_palo, carta_uno_boca_abajo)
        carta_dos = Carta (carta_dos_valor, carta_dos_palo, carta_dos_boca_abajo)
        resultado = test_criterio(carta_uno, carta_dos)
        assert resultado == True

    def test_str(self):
        carta = Carta(5, 1, False)
        resultado = carta.__repr__()
        assert resultado == "5♥"
    def test_eq(self):
        carta_uno = Carta(1, 1, False)
        carta_dos = Carta (2, 2, True)
        resultado = carta_uno.__eq__(carta_dos)
        assert resultado == False
