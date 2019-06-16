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
from gerenciadorDeTabuleiros import GerenciadorDeTabuleiros
import copy

class Jogador:
    
    stddevJogador = 5
    numeroJogadasAFrente = 2
    numeroDePossiveisComidasParaNaoConsiderarJogadaForcada = 3
    
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
        
    def calculaScoreTabuleiro (self, tabuleiro, numeroDaJogada):
        if (numeroDaJogada == self.numeroJogadasAFrente):
            return 0.0
        
        jogadaForcada = False
        
        gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
        listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
        if (not listaTabuleiros or listaTabuleiros is None):
            listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
        elif (len (listaTabuleiros) < self.numeroDePossiveisComidasParaNaoConsiderarJogadaForcada):
            jogadaForcada = True
        
        maxScore = -9999999999
        
        numeroDaProximaJogada = numeroDaJogada
        if (not jogadaForcada):
            numeroDaProximaJogada += 1
            
        for tabuleiro in listaTabuleiros:
            if (not tabuleiro is None):
                score = (self.predict (tabuleiro.converteTabuleiroParaArray (self.valorDama)) + self.calculaScoreTabuleiro (tabuleiro, numeroDaProximaJogada)) / 2.0
                if (score > maxScore and numeroDaJogada == 0):
                    maxScore = score
        
        return maxScore
    
    def selecionaMelhorJogada (self, tabuleiro, numeroDaJogada):
        jogadaForcada = False
        
        gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
        listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
        if (not listaTabuleiros or listaTabuleiros is None):
            listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
        elif (len (listaTabuleiros) < self.numeroDePossiveisComidasParaNaoConsiderarJogadaForcada):
            jogadaForcada = True
        
        maxScore = -9999999999
        
        numeroDaProximaJogada = numeroDaJogada
        if (not jogadaForcada):
            numeroDaProximaJogada += 1
            
        for tabuleiro in listaTabuleiros:
            if (not tabuleiro is None):
                score = (self.predict (tabuleiro.converteTabuleiroParaArray (self.valorDama)) + self.calculaScoreTabuleiro (tabuleiro, numeroDaProximaJogada)) / 2.0
                if (score > maxScore and numeroDaJogada == 0):
#                    print ("SCORE MAIOR: " + str(score))
#                    tabuleiro.printaTabuleiro ()
                    maxScore = score
                    tabuleiroEscolhido = copy.deepcopy (tabuleiro)
                    
        return tabuleiroEscolhido