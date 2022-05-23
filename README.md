# Solitario
Este repositorio simula el juego de cartas "Solitario", con una version clasica, y unas versiones alternativas como: Solitario catorce y solitario thumb and punch
No tiene desarrollada una interfaz por lo que todo el juego se corre desde una terminal ejecutando el archivo "main.py".

Para las pruebas se usaron las librerias:
  - pytest
  - coverage
  - pytest-cov

Necesitando la instalacion de cada una con los siguientes comandos:

pip install pytest
pip install coverage
pip install pytest-cov

Se puede ver la covertura inicial del codigo es de 22%, se puede ver con los comandos:

python -m coverage run main.py
python -m coverage report -m

Para realizar las pruebas de unidad ejecutar los siguientes comandos:

python -m pytest [nombre de archivo de pruebas]


La cobertura final del codigo es de 88%
