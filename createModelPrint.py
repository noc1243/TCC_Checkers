# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 23:28:19 2019

@author: nocera
"""

import numpy as np

from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras import initializers
from keras.models import load_model

np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)


nomeJogador = "Jogador_3b9c6929-d796-451e-b6d0-ea30b9b129c1.h5"

K.clear_session ()

model = load_model (".\modelos\\" + nomeJogador)
file = open (".\pesosDamas\\" + nomeJogador, "r")
peso = float (file.read())
file.close ()

text_file = open("Pesos.txt", "w")

for layerIndex in range (3):
            layer = model.get_layer (index = layerIndex)
            layerWeights = layer.get_weights()
            text_file.write ("camada" + str(layerIndex) + " = " + "np.array (" + str(np.array2string(layerWeights [0], separator = ',', precision = 15, suppress_small=True)) + ")\n")
            text_file.write("pesoCamada" + str(layerIndex) + " = " + "np.array (" + str(np.array2string(layerWeights [1], separator = ',', precision = 15, suppress_small=True)) + ")\n")
            
            
text_file.write ("pesoDama = " + str (peso))
text_file.close ()


