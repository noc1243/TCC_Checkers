# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:06:45 2019

@author: nocera
"""

from tabuleiro import Tabuleiro
from gerenciadorDeTabuleiros import GerenciadorDeTabuleiros
from variaveisGlobais import VariaveisGlobais

# Tester calcula Movimentos possiveis

# TESTE 1
print ("Comecando teste 1:")
print ("Tabuleiro inicial teste 1:")
tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_7)
tabuleiro.printaTabuleiro ()

gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
if (not listaTabuleiros or listaTabuleiros is None):
    listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()

print ("Printando tabuleiros possiveis:")
if (not listaTabuleiros is None and len(listaTabuleiros) > 0):
    for tabuleiro in listaTabuleiros:
        if (not tabuleiro is None):
            tabuleiro.printaTabuleiro ()
else:
    print ("Nao existem movimentos!!")

print ("")
# TESTE 2
#print ("Comecando teste 2:")
#print ("Tabuleiro inicial teste 2:")
#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_INICIAL)
#tabuleiro.printaTabuleiro ()
#
#gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
#listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
#if (not listaTabuleiros or listaTabuleiros is None):
#    listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
#
#print ("Printando tabuleiros possiveis:")
#if (not listaTabuleiros is None):
#    for tabuleiro in listaTabuleiros:
#        if (not tabuleiro is None):
#            tabuleiro.printaTabuleiro ()
#else:
#    print ("Nao existem movimentos!!")