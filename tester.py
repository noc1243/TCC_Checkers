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
from partida import Partida
from campeonato import Campeonato


listaJogadores = []

jogador1 = Jogador ()
jogador2 = Jogador ()
jogador3 = Jogador ()
jogador4 = Jogador ()
jogador5 = Jogador ()
jogador6 = Jogador ()

listaJogadores.append (jogador1)
listaJogadores.append (jogador2)
listaJogadores.append (jogador3)
listaJogadores.append (jogador4)
listaJogadores.append (jogador5)
listaJogadores.append (jogador6)

campeonato = Campeonato (listaJogadores)
campeonato.iniciaCampeonato ()


#
#partida = Partida (jogador1, jogador2)
#partida.realizaPartida ()
#
#print (jogador1.currentPoints)
#print (jogador2.currentPoints)


#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_2)
#tabuleiro.printaTabuleiro ()

#tabuleiro.inverteVisaoTabuleiro ()
#tabuleiro.printaTabuleiro ()

#tabuleiro2 = jogador1.selecionaMelhorJogada (tabuleiro, 0)
#tabuleiro2.printaTabuleiro ()

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
#listTabuleirosPossiveis = GerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
#
#if (not listTabuleirosPossiveis is None):
#    for tabuleiro in listTabuleirosPossiveis:
#        if (not tabuleiro is None):
#            tabuleiro.printaTabuleiro ()
#else:
#    print ("Nao existem movimentos!!")