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

def test_initialize_cart_object():
    valor = 5
    palo = 2
    boca_abajo = False
    carta = Carta(valor, palo, boca_abajo)
    assert carta.palo ==  2
    assert carta.valor == 5
    assert carta.boca_abajo == False

def test_voltear_carta():
    carta = Carta(5, 2, True)
    carta.voltear()
    assert carta.boca_abajo == False

def test_comp_uno():
    test_criterio = criterio()
    carta_uno = Carta(1, 1, False)
    carta_dos = Carta (2, 2, True)
    resultado = test_criterio(carta_uno, carta_dos)
    assert resultado == False


def test_comp_dos():
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

def test_comp_tres():
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


def test_comp_cuatro():
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


def test_comp_cinco():
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


def test_comp_seis():
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


def test_comp_siete():
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


def test_comp_ocho():
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


def test_comp_nueve():
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


def test_comp_diez():
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


def test_comp_once():
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


def test_comp_doce():
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


def test_comp_trece():
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


def test_comp_catorce():
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


def test_comp_quince():
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


def test_c2_one():
    carta.COLOR = True
    resultado = carta._c2s(2, 1)
    assert resultado == "\x1b[31;47m2♥\x1b[0m"


def test_c2_two():
    carta.COLOR = True
    resultado = carta._c2s(2, 0)
    assert resultado == "\x1b[30;47m2♠\x1b[0m"

def test_c2_three():
    carta.COLOR = False
    resultado = carta._c2s(1, 2)
    assert resultado == "A♦"


def test__c2_one():
    carta.UNICODE_LINDO = True
    resultado = carta.__c2s(5, 1)
    assert resultado == chr(0x1F0A0 + 5 + 1*16)


def test__c2_two():
    carta.UNICODE_LINDO = True
    resultado = carta.__c2s(12, 1)
    assert resultado == chr(0x1F0A0 + 13 + 1*16)

def test__c2_three():
    carta.UNICODE_LINDO = False
    resultado = carta.__c2s(0, 1)
    assert resultado == '▓'

def test__c2_four():
    carta.UNICODE_LINDO = False
    resultado = carta.__c2s(10, 1)
    assert resultado == '10♥'

def test_str():
    carta = Carta(5, 1, False)
    resultado = carta.__repr__()
    assert resultado == "5♥"


def test_eq():
    carta_uno = Carta(1, 1, False)
    carta_dos = Carta (2, 2, True)
    resultado = carta_uno.__eq__(carta_dos)
    assert resultado == False



# ////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////

def test_logear():
    logfile = None
    logfile = open(LOGFILE, 'w')
    main.loguear(logfile, 5)
    assert 1


def test_recuperar():
    resultado = main.recuperar()
    assert resultado == (5, '', [])


def test_fallo_recuperar():
    main.LOGFILE = 'solitario_fallo_f.log'
    resultado = main.recuperar()
    assert resultado == None


def test_pedir_juego_one(monkeypatch):
    number_inputs = StringIO('1234\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    resultado = main.pedir_juego(SOLITARIOS.keys())
    assert resultado == None

def test_pedir_juego_two(monkeypatch):
    number_inputs = StringIO(' \n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    resultado = main.pedir_juego(SOLITARIOS.keys())
    assert resultado == None

def test_name():
    resultado = main.__name__
    assert resultado == 'main'

def test_main_one(monkeypatch):
    main.LOGFILE = 'solitario.log'
    number_inputs = StringIO('1234\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    resultado = main.main()
    assert resultado == None
    

def test_main_two(monkeypatch):
    main.LOGFILE = 'solitario_juego.log'
    number_inputs = StringIO('1\nq\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    resultado = main.main()
    assert resultado == None


def test_main_three(monkeypatch):
    main.LOGFILE = 'solitario_juego.log'
    number_inputs = StringIO('1\n2\nq\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    resultado = main.main()
    assert resultado == None


def test_main_four(monkeypatch):
    main.LOGFILE = 'solitario_juego.log'
    number_inputs = StringIO('1\n10\nq\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    resultado = main.main()
    assert resultado == None

# def test_double(monkeypatch):
#     number_inputs = StringIO('1234\n')
#     monkeypatch.setattr('sys.stdin', number_inputs)
#     assert double() == 2468


'''Pruebas de mazo.py'''

def test_mazo_crearMazo():
    crear_mazo()
    assert 1

def test_mazo_crearMazo2():
    crear_mazo(1,1)
    assert 1

def test_mazo_crearMazo3():
    crear_mazo(1,2)
    assert 1
    
def test_mazo_mazoIndividual():
    mazo = PilaCartas()
    mazo_individual(mazo, 3)
    assert 1

def test_mazo_condMismoColor_T():
    assert cond_mismo_color(0, 3) == True
    
def test_mazo_condMismoColor_T2():
    assert cond_mismo_color(1, 2) == True
    
def test_mazo_condMismoColor_F():
    assert cond_mismo_color(0, 2) == False

'''Pruebas de solitario_thumbandpouch.py'''

def test_thumbandpounch_armar():
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    assert 1

def test_thumbandpounch_termino_T():
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    assert solit.termino() == True


def test_thumbandpounch_termino_F():
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    assert solit.termino() == False

def test_thumbandpounch_jugar():
    mesa = Mesa()
    jugada = mesa.parsear_jugada('m')
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    solit.jugar(jugada)
    assert 1

def test_thumbandpounch_cartaAPila_Error():
    pilaA = PilaCartas()
    pilaB = PilaCartas()
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    with pytest.raises(SolitarioError):
        solit._carta_a_pila(pilaA, pilaB)
        
def test_thumbandpounch_cartaAPila():
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
    
def test_thumbandpounch_subpilaAPila_Error():
    pilaA = PilaCartas()
    pilaB = PilaCartas()
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    with pytest.raises(SolitarioError):
        solit._subpila_a_pila(pilaA, pilaB)
        
def test_thumbandpounch_renovar():
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    jugada = mesa.parsear_jugada('m')
    solit.jugar(jugada)
    solit.renovar_mazo()
    assert 1

def test_thumbandpounch_auxJugada_Error():
    mesa = Mesa()
    jugada = mesa.parsear_jugada('q')
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    j0, p0 = jugada[0]
    j1, p1 = jugada[1] if len(jugada) == 2 else (SALIR, 0)
    with pytest.raises(SolitarioError):
        solit.auxiliar_jugar(len(jugada), j0, p0, j1, p1)

def test_thumbandpounch_auxJugada_Error2():
    mesa = Mesa()
    pila = PilaCartas()
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    jugada = mesa.parsear_jugada('n')
    with pytest.raises(SolitarioError):
        solit.jugar(jugada)
        
def test_thumbandpounch_auxJugada_Error3():
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    jugada = mesa.parsear_jugada('m')
    pila = PilaCartas()
    solit.mesa.mazo = pila
    with pytest.raises(SolitarioError):
        solit.auxiliar_jugar(1,0,1,0,1)
        
def test_thumbandpounch_auxJugada():
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    jugada = mesa.parsear_jugada('m')
    solit.auxiliar_jugar(2, 1,0,PILA_TABLERO,0)
    assert 1
    
def test_thumbandpounch_auxJugada_Error4():
    mesa = Mesa()
    solit = SolitarioThumbAndPouch(mesa)
    solit.armar()
    jugada = mesa.parsear_jugada('m')
    with pytest.raises(SolitarioError):
        solit.auxiliar_jugar(2, 1,1,PILA_TABLERO,1)


'''Pruebas de solitario_ejemplo.py'''

def test_solitEjem_armar():
    mesa = Mesa()
    solit = SolitarioEjemplo(mesa)
    solit.armar()
    assert 1
    
def test_solitEjem_Termino_T():
    mesa = Mesa()
    solit = SolitarioEjemplo(mesa)
    assert solit.termino() == True
    
def test_solitEjem_Termino_F():
    mesa = Mesa()
    solit = SolitarioEjemplo(mesa)
    solit.armar()
    assert solit.termino() == False

def test_solitEjem_jugar_Error():
    mesa = Mesa()
    jugada = mesa.parsear_jugada('m')
    solit = SolitarioEjemplo(mesa)
    solit.armar()
    with pytest.raises(SolitarioError):
        solit.jugar(jugada)

def test_solitEjem_jugar():
    mesa = Mesa()
    solit = SolitarioEjemplo(mesa)
    solit.armar()
    jugada2 = [(PILA_TABLERO,0),(PILA_TABLERO, 1)]
    jugada = mesa.parsear_jugada('1')
    print(jugada2)
    solit.jugar(jugada2)
    assert 1

def test_solitEjem_jugar2():
    mesa = Mesa()
    solit = SolitarioEjemplo(mesa)
    solit.armar()
    jugada2 = [(PILA_TABLERO,0)]
    print(jugada2)
    solit.jugar(jugada2)
    assert 1
    
'''Pruebas de solitario_catorce.py'''

def test_solitCatorce_armar():
    mesa = Mesa()
    solit = SolitarioCatorce(mesa)
    solit.armar()
    assert 1
    
def test_solitCatorce_Termino_T():
    mesa = Mesa()
    solit = SolitarioCatorce(mesa)
    assert solit.termino() == True
    
def test_solitCatorce_Termino_F():
    mesa = Mesa()
    solit = SolitarioCatorce(mesa)
    solit.armar()
    assert solit.termino() == False
    
def test_solitCatorce_jugar_Error():
    mesa = Mesa()
    jugada = mesa.parsear_jugada('m')
    solit = SolitarioCatorce(mesa)
    solit.armar()
    with pytest.raises(SolitarioError):
        solit.jugar(jugada)

def test_solitCatorce_jugar():
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
