# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:41:59 2019

@author: nocera
"""

from keras.models import Sequential
from keras.layers import Dense
from keras import initializers
from keras.models import load_model
import numpy as np
from random import randint
from random import gauss
from gerenciadorDeTabuleiros import GerenciadorDeTabuleiros
import copy
import math
import uuid 

class Jogador:
    
    peakVal = 0.2
    sigma = 0.5
    
    numeroJogadasAFrente = 4
    
    numeroDePossiveisComidasParaNaoConsiderarJogadaForcada = 3
    
    pontosQuandoPerde = -2
    pontosQuandoGanha = 1
    pontosQuandoEmpata = 0
    
    def __init__ (self, model = None, valorDama = None, listaSigmas = None, geracao = 0, debug = False):
        self.listaSigmas = []
        listaWeights = []
        self.currentPoints = 0
        self.geracao = geracao
        
        if (valorDama is None):
            self.valorDama = (randint(10,30) /10.0)
        else:
            self.valorDama = valorDama
        
        
        if (model is None):
            initializer = initializers.random_uniform(minval=(-1) * Jogador.peakVal, maxval=Jogador.peakVal)
            self.model = Sequential ()
            self.model.add (Dense (32, input_dim=32, kernel_initializer=initializer, activation = 'tanh'))
            self.model.add (Dense (1000, kernel_initializer=initializer, activation = 'tanh'))
            self.model.add (Dense (1, kernel_initializer=initializer, activation = 'tanh'))
            self.model.compile (loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
            self.model._make_predict_function()
        else:
            self.model = model
            self.model._make_predict_function()
        
        if (listaSigmas is None):
            for layerIndex in range (3):
                layer = self.model.get_layer (index = layerIndex)
                layerWeights = layer.get_weights()
                arrayWeights = np.zeros ((layerWeights [0].shape [0], layerWeights [0].shape [1])) + self.sigma
                arrayBiases = np.zeros (layerWeights [1].shape [0]) + self.sigma
                listaWeights.clear ()
                listaWeights.append (arrayWeights)
                listaWeights.append (arrayBiases)
                self.listaSigmas.append (copy.deepcopy (listaWeights))
        else:
            self.listaSigmas = listaSigmas
            
        self.nomeJogador = "Jogador_" + str(uuid.uuid4()) + ".h5"
        
        self.debug = debug
        
        
    def predict (self, tabuleiro):
        if (tabuleiro.ndim == 1):
            tabuleiro = np.array ([tabuleiro])
        return self.model.predict (tabuleiro)
    
    def salvaModelo (self):
        self.model.save (".\modelos\\" + self.nomeJogador)
        
    def carregaModelo (self):
        self.model = load_model (".\modelos\\" + self.nomeJogador)
        self.model._make_predict_function()
        
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
        tabuleiroEscolhido = None
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
    
    def calculaScoreTabuleiroMinMax (self, tabuleiro, numeroDaJogada, jogadorJogando, alpha, beta):
        tabuleiro.inverteVisaoTabuleiro ()
        
        if (numeroDaJogada == self.numeroJogadasAFrente):
            return self.predict (tabuleiro.converteTabuleiroParaArray (self.valorDama))
        
        jogadaForcada = False
        
        gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
        listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
        if (not listaTabuleiros or listaTabuleiros is None):
            listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
        elif (len (listaTabuleiros) < self.numeroDePossiveisComidasParaNaoConsiderarJogadaForcada):
            jogadaForcada = True
        
        numeroDaProximaJogada = numeroDaJogada
        if (not jogadaForcada):
            numeroDaProximaJogada += 1 
            
        if (jogadorJogando):
            best = -9999999999
        else:
            best = 9999999999
            
        for tabuleiro in listaTabuleiros:
            if (not tabuleiro is None):
                if (jogadorJogando):
                    
                    best = max (best, self.calculaScoreTabuleiroMinMax (copy.deepcopy(tabuleiro), numeroDaProximaJogada, not jogadorJogando, alpha, beta))
                    alpha = max (alpha, best)
                    if (beta <= alpha):
                        break
                else:
                    best = min (best, self.calculaScoreTabuleiroMinMax (copy.deepcopy(tabuleiro), numeroDaProximaJogada, not jogadorJogando, alpha, beta))
                    beta = min (beta, best)
                    if (beta <= alpha):
                        break
                    
        return best
    
    def selecionaMelhorJogadaMinMax (self, tabuleiro, numeroDaJogada):
        tabuleiroEscolhido = None
        jogadaForcada = False
        
        gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
        listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
        if (not listaTabuleiros or listaTabuleiros is None):
            listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
        elif (len (listaTabuleiros) < self.numeroDePossiveisComidasParaNaoConsiderarJogadaForcada):
            jogadaForcada = True
        
        alpha = -9999999999
        beta =  9999999999
        
        numeroDaProximaJogada = numeroDaJogada
        if (not jogadaForcada):
            numeroDaProximaJogada += 1
            
            
        tabuleiroEscolhido = None    
        for tabuleiro in listaTabuleiros:
            if (not tabuleiro is None):
                
                score = self.calculaScoreTabuleiroMinMax (copy.deepcopy(tabuleiro), numeroDaProximaJogada, False, alpha, beta)
                if (score >= alpha and numeroDaJogada == 0):
                    alpha = score
                    tabuleiroEscolhido = copy.deepcopy (tabuleiro)
                    if (self.debug):
                        print ("Tabuleiro Selecionado por score: " + str (score))
                        print ("Tabuleiro:")
                        tabuleiroEscolhido.printaTabuleiro()
                    
        return tabuleiroEscolhido
    
    def ganhaPartida (self):
        self.currentPoints += self.pontosQuandoGanha
        
    def perdePartida (self):
        self.currentPoints += self.pontosQuandoPerde
        
    def empataPartida (self):
        self.currentPoints += self.pontosQuandoEmpata
        
    def calculaQuantidadeDePesos (self):
        quantidadeDePesos = 0
        for layerIndex in range (3):
            layer = self.model.get_layer (index = layerIndex)
            layerWeights = layer.get_weights()
            quantidadeDePesos += layerWeights [0].shape [0] * layerWeights [0].shape [1] + layerWeights [1].shape [0]
        
        print (quantidadeDePesos)
        
    def __del__ (self):
        del self.model
        
        
        