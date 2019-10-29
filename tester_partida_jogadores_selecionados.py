# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 00:26:14 2019

@author: diogo
"""

from keras import backend as K
from jogador import Jogador
from partida import Partida
from keras.models import Sequential
from keras.layers import Dense
from keras import initializers
from keras.models import load_model

nomeJogador1 = "Jogador_3b9c6929-d796-451e-b6d0-ea30b9b129c1.h5"
nomeJogador2 = "Jogador_38c6ee4c-bae6-4715-98fe-8f298079f0e5.h5"

K.clear_session ()

#TESTE PARTIDA
#INICIALIZANDO JOGADOR 1
model = load_model (".\modelos\\" + nomeJogador1)
file = open (".\pesosDamas\\" + nomeJogador1, "r")
peso = float (file.read())
file.close ()
jogador1 = Jogador (model = model, valorDama = peso)

#INICIALIZANDO JOGADOR 2
model = load_model (".\modelos\\" + nomeJogador2)
file = open (".\pesosDamas\\" + nomeJogador2, "r")
peso = float (file.read())
file.close ()
jogador2 = Jogador (model = model, valorDama = peso)

partida = Partida (jogador1, jogador2, True)
#partida = Partida (jogador2, jogador1, True)
result = partida.realizaPartida ()
#    print ("Partida: " + str (index) + " terminada")
if (result == 1):
    print ("Jogador 1 Venceu!")
elif (result == -1):
    print ("Jogador 2 Venceu!")
else:
    print ("EMPATE!")