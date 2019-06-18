# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:48:39 2019

@author: nocera
"""

from jogador import Jogador
from partida import Partida

#Teste pontuacao apos partida
jogador1 = Jogador ()
jogador2 = Jogador ()

partida = Partida (jogador2, jogador1, True)
partida.realizaPartida ()
#
print (jogador1.currentPoints)
print (jogador2.currentPoints)