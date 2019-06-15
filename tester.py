# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:27:24 2019

@author: nocera
"""

from tabuleiro import Tabuleiro
from movimento import Movimento
from casa import Casa
from gerenciadorDeTabuleiros import GerenciadorDeTabuleiros

tabuleiro = Tabuleiro ()
GerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
listTabuleirosPossiveis = GerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()


if (not listTabuleirosPossiveis is None):
    for previsaoDeTabuleiro in listTabuleirosPossiveis:
        if (not previsaoDeTabuleiro is None):
            previsaoDeTabuleiro.printaTabuleiro ()
            print ("")
else:
    print ("Nao existem movimentos!!")

#tabuleiro.printaTabuleiro ()
#
#print ("")
#casaInicial = Casa ("a", 2)
#casaFinal = Casa ("b", 3)
#print (casaInicial.converteMovimentoParaArray ())
#print (casaFinal.converteMovimentoParaArray ())
#
#movimento = Movimento (casaInicial, casaFinal)
#tabuleiro.doAnyMovement (movimento)
#
#tabuleiro.printaTabuleiro ()
#
#print ("")
#
#casaInicial = Casa ("b", 3)
#casaFinal = Casa ("c", 4)
#movimento = Movimento (casaInicial, casaFinal)
#tabuleiro.doAnyMovement (movimento)
#
#tabuleiro.printaTabuleiro ()
#
#print ("")
#
#casaInicial = Casa ("c", 4)
#casaFinal = Casa ("d", 5)
#movimento = Movimento (casaInicial, casaFinal)
#tabuleiro.doAnyMovement (movimento)
#
#tabuleiro.printaTabuleiro ()