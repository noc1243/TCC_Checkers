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
from jogador import Jogador

jogador1 = Jogador ()

tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_INICIAL)
#tabuleiro.printaTabuleiro ()

tabuleiro2 = jogador1.selecionaMelhorJogada (tabuleiro, 0)
tabuleiro2.printaTabuleiro ()

#print (jogador1.predict (tabuleiro.converteTabuleiroParaArray (jogador1.valorDama)))
#
#casaInicial = Casa ("a", 2)
#casaFinal = Casa ("c", 4)
#movimento1 = Movimento (casaInicial, casaFinal)
#
#casaInicial = Casa ("c", 4)
#casaFinal = Casa ("e", 6)
#movimento2 = Movimento (casaInicial, casaFinal)
#
#tabuleiro.printaTabuleiro ()
#
#GerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
#listTabuleirosPossiveis = GerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
#
#if (not listTabuleirosPossiveis is None):
#    for tabuleiro in listTabuleirosPossiveis:
#        if (not tabuleiro is None):
#            print (jogador1.predict (tabuleiro.converteTabuleiroParaArray (jogador1.valorDama)))
#            tabuleiro.printaTabuleiro ()
#else:
#    print ("Nao existem movimentos!!")