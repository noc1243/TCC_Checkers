# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:41:59 2019

@author: nocera
"""

from keras.models import Sequential
from keras.layers import Dense
from keras import initializers
import numpy as np
from random import randint


class Jogador:
    
    stddevJogador = 0.05
    
    def __init__ (self):
        self.valorDama = (randint(10,30) /10.0)
        
        initializer = initializers.random_normal(stddev=Jogador.stddevJogador)
        self.model = Sequential ()
        self.model.add (Dense (32, input_dim=32, kernel_initializer=initializer))
        self.model.add (Dense (1000, kernel_initializer=initializer))
        self.model.add (Dense (1, kernel_initializer=initializer))
        self.model.compile (loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        
        
    def predict (self, tabuleiro):
        if (tabuleiro.ndim == 1):
            tabuleiro = np.array ([tabuleiro])
        return self.model.predict (tabuleiro)