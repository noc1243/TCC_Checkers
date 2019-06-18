# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:27:24 2019

@author: nocera
"""

from keras import backend as K
from tabuleiro import Tabuleiro
from movimento import Movimento
from casa import Casa
from gerenciadorDeTabuleiros import GerenciadorDeTabuleiros
from variaveisGlobais import VariaveisGlobais
from jogador import Jogador
from partida import Partida
from campeonato import Campeonato
from seletorNatural import SeletorNatural
import random
import copy


VARIASEED = 0

listaJogadores = []

random.seed (16062019 + VARIASEED)

K.clear_session ()


#TESTE CAMPEONATO
#jogador1 = Jogador ()
#jogador2 = Jogador ()
#jogador3 = Jogador ()
#jogador4 = Jogador ()
#jogador5 = Jogador ()
#jogador6 = Jogador ()

#listaJogadores.append (jogador1)
#listaJogadores.append (jogador2)
#listaJogadores.append (jogador3)
#listaJogadores.append (jogador4)
#listaJogadores.append (jogador5)
#listaJogadores.append (jogador6)

#campeonato = Campeonato (listaJogadores)
#campeonato.iniciaCampeonato ()

seletorNatural = SeletorNatural (840)
seletorNatural.iniciaTreinamento ()

#TESTE PARTIDA
#jogador1 = Jogador ()
#jogador2 = Jogador ()

#partida = Partida (jogador1, jogador3)
#result = partida.realizaPartida ()
##    print ("Partida: " + str (index) + " terminada")
#if (result == 1):
#    print ("Jogador 1 Venceu!")
#elif (result == -1):
#    print ("Jogador 3 Venceu!")
#else:
#    print ("EMPATE!")
#    
#partida = Partida (jogador1, jogador4)
#result = partida.realizaPartida ()
##    print ("Partida: " + str (index) + " terminada")
#if (result == 1):
#    print ("Jogador 1 Venceu!")
#elif (result == -1):
#    print ("Jogador 4 Venceu!")
#else:
#    print ("EMPATE!")


#Teste Partidas com o filho
#jogador1 = Jogador ()
#
#numeroDePartidasJogador1 = 0
#numeroDePartidasJogador2 = 0
#numeroDePartidasEmpate = 0
#for index in range (50):
#    print ("")
#    print ("Criando jogador 2")
#    jogador2 = seletorNatural.repdroduzJogador (copy.deepcopy(jogador1))
#    
#    print ("Comecando partida 1." + str (index + 1) + "!")
#    partida = Partida (jogador1, jogador2)
#    result = partida.realizaPartida ()
##    print ("Partida: " + str (index) + " terminada")
#    if (result == 1):
#        print ("Jogador 1 Venceu!")
#        numeroDePartidasJogador1 += 1
#    elif (result == -1):
#        print ("Jogador 2 Venceu!")
#        numeroDePartidasJogador2 += 1
#    else:
#        print ("EMPATE!")
#        numeroDePartidasEmpate += 1
#        
#    print ("Numero jogadas: " + str (partida.numeroJogadas))
#        
#    print ("Comecando partida 2." + str (index + 1) + "!")
#    partida = Partida (jogador2, jogador1)
#    result = partida.realizaPartida ()
##    print ("Partida: " + str (index) + " terminada")
#    if (result == 1):
#        print ("Jogador 1 Venceu!")
#        numeroDePartidasJogador1 += 1
#    elif (result == -1):
#        print ("Jogador 2 Venceu!")
#        numeroDePartidasJogador2 += 1
#    else:
#        print ("EMPATE!")
#        numeroDePartidasEmpate += 1
#    
#    print ("Numero jogadas: " + str(partida.numeroJogadas))    
#        
#print ("")
#print ("RESULTADOS:")
#print ("Vitorias Jogador 1: " + str (numeroDePartidasJogador1))
#print ("Vitorias Jogador 2: " + str (numeroDePartidasJogador2))
#print ("Vitorias Empate: " + str (numeroDePartidasEmpate))
    
#Teste pontuacao apos partida
#jogador1 = Jogador ()
#jogador2 = Jogador ()

#partida = Partida (jogador2, jogador1, True)
#partida.realizaPartida ()
##
#print (jogador1.currentPoints)
#print (jogador2.currentPoints)


#Tester inversão de tabuleiro
#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_2)
#tabuleiro.printaTabuleiro ()

#tabuleiro.inverteVisaoTabuleiro ()
#tabuleiro.printaTabuleiro ()

#Tester selecionaMelhorJogada
#jogador1 = Jogador (debug = True)

#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_2)
#tabuleiro.printaTabuleiro ()

#tabuleiro2 = jogador1.selecionaMelhorJogada (tabuleiro, 0)
#tabuleiro2.printaTabuleiro ()


#Tester valor do Predict para um tabuleiro
#jogador1 = Jogador (debug = True)

#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_2)
#tabuleiro.printaTabuleiro ()

#print (jogador1.predict (tabuleiro.converteTabuleiroParaArray (jogador1.valorDama)))
#

# Tester movimento no tabuleiro
#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE)
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

# Tester calcula Movimentos possiveis
#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_2)
#tabuleiro.printaTabuleiro ()

#gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
#listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
#if (not listaTabuleiros or listaTabuleiros is None):
#    listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
#
#if (not listTabuleirosPossiveis is None):
#    for tabuleiro in listTabuleirosPossiveis:
#        if (not tabuleiro is None):
#            tabuleiro.printaTabuleiro ()
#else:
#    print ("Nao existem movimentos!!")