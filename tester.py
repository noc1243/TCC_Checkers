# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:27:24 2019

@author: nocera
"""

from tabuleiro import Tabuleiro
from movimento import Movimento
from casa import Casa
from gerenciadorDeTabuleiros import GerenciadorDeTabuleiros
from variaveisGlobais import VariaveisGlobais

tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE)

casaInicial = Casa ("a", 2)
casaFinal = Casa ("c", 4)
movimento1 = Movimento (casaInicial, casaFinal)

casaInicial = Casa ("c", 4)
casaFinal = Casa ("e", 6)
movimento2 = Movimento (casaInicial, casaFinal)

#listaMovimentos = []
#listaMovimentos.append (movimento1)
#listaMovimentos.append (movimento2)

tabuleiro.printaTabuleiro ()

#tabuleiro.doMultipleMovementsComer (listaMovimentos)

#tabuleiro.printaTabuleiro ()


GerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
listTabuleirosPossiveis = GerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
#
#
if (not listTabuleirosPossiveis is None):
    for tabuleiro in listTabuleirosPossiveis:
        if (not tabuleiro is None):
            tabuleiro.printaTabuleiro ()
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