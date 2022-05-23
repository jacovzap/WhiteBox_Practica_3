import pytest
from main import *
from carta import *
from mazo import *
from solitario_thumbandpouch import *
from solitario_ejemplo import *
from solitariocatorce import *
import main
from io import StringIO


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

