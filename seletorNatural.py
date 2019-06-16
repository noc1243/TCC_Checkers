# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:27:58 2019

@author: nocera
"""

import math
import copy
import numpy as np
from random import gauss
from jogador import Jogador
from campeonato import Campeonato
from keras.models import Sequential
from keras.layers import Dense
from keras import backend as K

class SeletorNatural:
    
    mean = 0
    variance = 1
    
    meanDama = 0
    varianceDama = 1
    
    numeroJogadoresIniciais = 15
    
    def __init__ (self, numeroDeGeracoesTreinamento):
        self.numeroDeGeracoesTreinamento = numeroDeGeracoesTreinamento
        
    def repdroduzJogador (self, jogador):
        tau = 0.0839
        
        novoSigma = []
        for listaWeights in jogador.listaSigmas:
            novaListaWeights = []
            novoWeights = listaWeights [0] + math.exp (tau * gauss (self.mean, self.variance))
            novoBiases = listaWeights [1] + math.exp (tau * gauss (self.mean, self.variance))
            novaListaWeights.append (novoWeights)
            novaListaWeights.append (novoBiases)
            novoSigma.append (copy.deepcopy(novaListaWeights))
        
        novoModel = copy.deepcopy (jogador.model)
        
        for layerIndex in range (3):
            layer = novoModel.get_layer (index = layerIndex)
            layerWeights = layer.get_weights()
            layerWeightsWeights = np.add (layerWeights [0], novoSigma [layerIndex] [0])
            layerWeightsBiases = np.add  (layerWeights [1], novoSigma [layerIndex] [1])
            novaListaWeights = []
            novaListaWeights.append (layerWeightsWeights)
            novaListaWeights.append (layerWeightsBiases)
            layer.set_weights(novaListaWeights)
        
        novoValorDama = max (min (jogador.valorDama + gauss (self.meanDama, self.varianceDama), 3), 1)
        
        jogadorFilho = Jogador (novoModel, novoValorDama, novoSigma, jogador.geracao + 1)
        
        return jogadorFilho
    
    def geraJogadoresIniciais (self):
        listaJogadores = []
        for index in range (self.numeroJogadoresIniciais):
            jogador = Jogador ()
            listaJogadores.append (jogador)
            print ("Jogador criado: " + str (jogador.nomeJogador))
        
        return listaJogadores
    
    def geraFilhosDosJogadores (self, listaJogadores):
        listaFilhosJogadores = []
        for jogador in listaJogadores:
            filho = self.repdroduzJogador (copy.deepcopy (jogador))
            listaFilhosJogadores.append (filho)
            print ("Filho criado: " + str (filho.nomeJogador))
        
        return listaFilhosJogadores
    
    def limpaMemoriaDosModelos (self, listaJogadores, jogadoresParaSeremDestruidos):
        for jogador in listaJogadores:
            jogador.salvaModelo ()
            
        K.clear_session()
        
        for jogador in jogadoresParaSeremDestruidos:
            del jogador
            
        for jogador in listaJogadores:
            jogador.carregaModelo ()
            
        return listaJogadores
    
    def selecionaMelhoresJogadores (self, listaJogadores):
        listaJogadores.sort (key=lambda x: x.currentPoints, reverse=True)
        
        jogadoresParaSeremDestruidos = listaJogadores [self.numeroJogadoresIniciais:]
        
        listaJogadores = listaJogadores [0:self.numeroJogadoresIniciais]

        listaJogadores = self.limpaMemoriaDosModelos (listaJogadores, jogadoresParaSeremDestruidos)
        
        print ("Jogadores Selecionados!")
        return listaJogadores
    
    def limpaScoreJogadores (self, listaJogadores):
        for jogador in listaJogadores:
            jogador.currentPoints = 0
    
    def rodaGeracao (self, listaJogadores):
        print ("Criando filhos de uma geracao!")
        listaFilhos = self.geraFilhosDosJogadores (listaJogadores)
        listaJogadores.extend (listaFilhos)
        
        print ("Iniciando campeonato!")
        campeonato = Campeonato (listaJogadores)
        campeonato.iniciaCampeonato ()
        
        print ("Selecionando os melhores Jogadores!")
        listaJogadores = self.selecionaMelhoresJogadores (listaJogadores)
        self.limpaScoreJogadores (listaJogadores)
        
        return listaJogadores
        
        
    
    def iniciaTreinamento (self):
        print ("Criando os jogadores iniciais!")
        listaJogadores = self.geraJogadoresIniciais ()
        
        indexGeracao = 1
        for geracao in range (self.numeroDeGeracoesTreinamento):
            print ("Rodando Geracao: " + str(indexGeracao))
            listaJogadores = self.rodaGeracao (listaJogadores)
            indexGeracao += 1
            print ("Fim da Geracao!")
            print ("")
        
        K.clear_session ()