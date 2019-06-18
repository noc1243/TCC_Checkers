# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:46:22 2019

@author: nocera
"""

import copy
from jogador import Jogador
from partida import Partida
from seletorNatural import SeletorNatural

#Teste Partidas com o filho
seletorNatural = SeletorNatural (1)

jogador1 = Jogador ()

numeroDePartidasJogador1 = 0
numeroDePartidasJogador2 = 0
numeroDePartidasEmpate = 0
for index in range (50):
    print ("")
    print ("Criando jogador 2")
    jogador2 = seletorNatural.repdroduzJogador (copy.deepcopy(jogador1))
    
    print ("Comecando partida 1." + str (index + 1) + "!")
    partida = Partida (jogador1, jogador2)
    result = partida.realizaPartida ()
    if (result == 1):
        print ("Jogador 1 Venceu!")
        numeroDePartidasJogador1 += 1
    elif (result == -1):
        print ("Jogador 2 Venceu!")
        numeroDePartidasJogador2 += 1
    else:
        print ("EMPATE!")
        numeroDePartidasEmpate += 1
        
    print ("Numero jogadas: " + str (partida.numeroJogadas))
        
    print ("Comecando partida 2." + str (index + 1) + "!")
    partida = Partida (jogador2, jogador1)
    result = partida.realizaPartida ()
    if (result == 1):
        print ("Jogador 2 Venceu!")
        numeroDePartidasJogador1 += 1
    elif (result == -1):
        print ("Jogador 1 Venceu!")
        numeroDePartidasJogador2 += 1
    else:
        print ("EMPATE!")
        numeroDePartidasEmpate += 1
    
    print ("Numero jogadas: " + str(partida.numeroJogadas))    
        
print ("")
print ("RESULTADOS:")
print ("Vitorias Jogador 1: " + str (numeroDePartidasJogador1))
print ("Vitorias Jogador 2: " + str (numeroDePartidasJogador2))
print ("Vitorias Empate: " + str (numeroDePartidasEmpate))
