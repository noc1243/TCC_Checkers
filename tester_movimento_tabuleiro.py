# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:59:08 2019

@author: nocera
"""

from tabuleiro import Tabuleiro
from movimento import Movimento
from casa import Casa
from variaveisGlobais import VariaveisGlobais

# Tester movimento no tabuleiro
listaMovimento = []

#PRIMEIRO TESTE
print ("Começando teste 1:")
print ("Tabuleiro inicial teste 1:")
tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE)
tabuleiro.printaTabuleiro ()

casaInicial = Casa ("a", 2)
casaFinal = Casa ("c", 4)
movimento1 = Movimento (casaInicial, casaFinal)

casaInicial = Casa ("c", 4)
casaFinal = Casa ("e", 6)
movimento2 = Movimento (casaInicial, casaFinal)

listaMovimento.append (movimento1)
listaMovimento.append (movimento2)

print ("Tabuleiro apos movimento teste 1:")
tabuleiro.doMultipleMovementsComer (listaMovimento)
tabuleiro.printaTabuleiro ()

listaMovimento.clear ()

#SEGUNDO TESTE
print ("Começando teste 2:")
print ("Tabuleiro inicial teste 2:")
tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_INICIAL)
tabuleiro.printaTabuleiro ()

casaInicial = Casa ("a", 2)
casaFinal = Casa ("b", 3)
movimento3 = Movimento (casaInicial, casaFinal)

print ("Tabuleiro apos movimento teste 2:")
tabuleiro.doAnyMovement (movimento3)
tabuleiro.printaTabuleiro ()

#TERCEIRO TESTE
print ("Começando teste 3:")
print ("Tabuleiro inicial teste 3:")
tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE)
tabuleiro.printaTabuleiro ()

casaInicial = Casa ("a", 2)
casaFinal = Casa ("c", 4)
movimento4 = Movimento (casaInicial, casaFinal)

casaInicial = Casa ("c", 4)
casaFinal = Casa ("e", 2)
movimento5 = Movimento (casaInicial, casaFinal)

listaMovimento.append (movimento4)
listaMovimento.append (movimento5)

print ("Tabuleiro apos movimento teste 3:")
tabuleiro.doMultipleMovementsComer (listaMovimento)
tabuleiro.printaTabuleiro ()
