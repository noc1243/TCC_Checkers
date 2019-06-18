# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:44:25 2019

@author: nocera
"""
from jogador import Jogador
from partida import Partida


#TESTE PARTIDA
jogador1 = Jogador ()
jogador2 = Jogador ()

partida = Partida (jogador1, jogador2, True)
result = partida.realizaPartida ()
#    print ("Partida: " + str (index) + " terminada")
if (result == 1):
    print ("Jogador 1 Venceu!")
elif (result == -1):
    print ("Jogador 3 Venceu!")
else:
    print ("EMPATE!")