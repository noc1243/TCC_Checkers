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

nomeJogador1 = "Jogador_11829f51-fa95-4973-8c66-87f758adb75b.h5"
nomeJogador2 = "Jogador_3775f37e-933e-4879-8297-32bed039f822.h5"

K.clear_session ()

#TESTE PARTIDA
#INICIALIZANDO JOGADOR 1
model = load_model (".\melhores_modelos\\" + nomeJogador1)
file = open (".\melhores_pesos\\" + nomeJogador1, "r")
peso = float (file.read())
file.close ()
jogador1 = Jogador (model = model, valorDama = peso)

#INICIALIZANDO JOGADOR 2
model = load_model (".\melhores_modelos\\" + nomeJogador2)
file = open (".\melhores_pesos\\" + nomeJogador2, "r")
peso = float (file.read())
file.close ()
jogador2 = Jogador (model = model, valorDama = peso)

partida = Partida (jogador1, jogador2, True)
result = partida.realizaPartida ()
#    print ("Partida: " + str (index) + " terminada")
if (result == 1):
    print ("Jogador 1 Venceu!")
elif (result == -1):
    print ("Jogador 2 Venceu!")
else:
    print ("EMPATE!")