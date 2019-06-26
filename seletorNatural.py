# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:27:58 2019

@author: nocera
"""

import math
import copy
import numpy as np
import gc
from random import gauss
from jogador import Jogador
from campeonato import Campeonato
from campeonatoEntreTimes import CampeonatoEntreTimes
from keras.models import Sequential
from keras.layers import Dense
from keras import backend as K
from variaveisGlobais import VariaveisGlobais

class SeletorNatural:
    
    mean = 0
    variance = 1
    
    meanDama = 0
    varianceDama = 0.1
    
    numeroJogadoresIniciais = 15
    
    fitMaximoJogador = 200
    fitRealJogador = 8
    
    tempoEntreVerificacoes = 100
    
    def __init__ (self, numeroDeGeracoesTreinamento):
        self.numeroDeGeracoesTreinamento = numeroDeGeracoesTreinamento
        self.listaJogadoresBase = []
        
        self.fileResultados = open (VariaveisGlobais.ARQUIVO_RESULTADOS_SELETOR, "w+")
        
    def geraMatrizDeVariaveisGaussianas (self, shape1, shape2):
        arrayGaussianas = np.zeros ((shape1, shape2))
        for row in range(arrayGaussianas.shape [0]):
            for column in range(arrayGaussianas.shape [1]):
                arrayGaussianas [row, column] = gauss (self.mean, self.variance)
        
        return arrayGaussianas
    
    def geraExponencialDeGaussianas (self, shape1, shape2, tau):
        arrayGaussianas = np.zeros ((shape1, shape2))
        for row in range(arrayGaussianas.shape [0]):
            for column in range(arrayGaussianas.shape [1]):
                arrayGaussianas [row, column] = math.exp (gauss (self.mean, self.variance) * tau)
        
        return arrayGaussianas
    
    def geraArrayDeVariaveisGaussianas (self, shape):
        arrayGaussianas = np.zeros (shape)
        for index in range(arrayGaussianas.shape[0]):
            arrayGaussianas [index] = gauss (self.mean, self.variance)
        
        return arrayGaussianas
    
    def geraExponencialDeGaussianasArray (self, shape, tau):
        arrayGaussianas = np.zeros (shape)
        for index in range(arrayGaussianas.shape[0]):
            arrayGaussianas [index] = math.exp (gauss (self.mean, self.variance) * tau)
        
        return arrayGaussianas
        
    def repdroduzJogador (self, jogador):
#        tau = 0.0839
        tau = 1/math.sqrt(2 * math.sqrt (jogador.calculaQuantidadeDePesos ()))
        
        novoSigma = []
        for listaWeights in jogador.listaSigmas:
            novaListaWeights = []
            changedGaussWeights = self.geraExponencialDeGaussianas (listaWeights[0].shape[0], listaWeights[0].shape[1], tau)
            changedGaussBiases = self.geraExponencialDeGaussianasArray (listaWeights[1].shape[0], tau)
            novoWeights = np.multiply (listaWeights [0], changedGaussWeights)
            novoBiases = np.multiply (listaWeights [1], changedGaussBiases)
            novaListaWeights.append (novoWeights)
            novaListaWeights.append (novoBiases)
            novoSigma.append (copy.deepcopy(novaListaWeights))
        
        novoModel = copy.deepcopy (jogador.model)
        
        for layerIndex in range (3):
            layer = novoModel.get_layer (index = layerIndex)
            layerWeights = layer.get_weights()
            changedGaussWeights = self.geraMatrizDeVariaveisGaussianas (layerWeights[0].shape[0], layerWeights[0].shape[1])
            changedGaussBiases = self.geraArrayDeVariaveisGaussianas (layerWeights[1].shape[0])
            layerWeightsWeights = np.add (layerWeights [0], np.multiply (novoSigma [layerIndex] [0], changedGaussWeights))
            layerWeightsBiases = np.add  (layerWeights [1], np.multiply (novoSigma [layerIndex] [1], changedGaussBiases))
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
            self.listaJogadoresBase.append (copy.deepcopy(jogador))
            jogador.salvaModelo ()
            print ("Jogador criado: " + str (jogador.nomeJogador))
            self.fileResultados.write ("Jogador criado: " + str (jogador.nomeJogador) + "\n")
            
        
        return listaJogadores
    
    def geraFilhosDosJogadores (self, listaJogadores):
        listaFilhosJogadores = []
        for jogador in listaJogadores:
            filho = self.repdroduzJogador (copy.deepcopy (jogador))
            listaFilhosJogadores.append (filho)
            print ("Filho criado: " + str (filho.nomeJogador))
            self.fileResultados.write ("Filho criado: " + str (filho.nomeJogador) + "\n")
            
        
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
        listaJogadores.sort (key=lambda x: (x.currentPoints, x.geracao), reverse=True)
#        listaJogadores.sort (key=lambda x: (float (x.totalPoints)/float (x.numeroDeGeracoesVivo), x.geracao), reverse=True)
        
        jogadoresParaSeremDestruidos = listaJogadores [self.numeroJogadoresIniciais:]
        
        listaJogadores = listaJogadores [0:self.numeroJogadoresIniciais]

        listaJogadores = self.limpaMemoriaDosModelos (listaJogadores, jogadoresParaSeremDestruidos)
        
        print ("Jogadores Selecionados!")
        self.fileResultados.write ("Jogadores Selecionados!\n")
        
        return listaJogadores
    
    def limpaScoreJogadores (self, listaJogadores):
        for jogador in listaJogadores:
            jogador.currentPoints = 0
            
    def somaGeracoesVivoJogador (self, listaJogadores):
        for jogador in listaJogadores:
            jogador.numeroDeGeracoesVivo += 1
    
    def rodaGeracao (self, listaJogadores):
        print ("Criando filhos de uma geracao!")
        self.fileResultados.write ("Criando filhos de uma geracao!\n")
        
        listaFilhos = self.geraFilhosDosJogadores (listaJogadores)
        listaJogadores.extend (listaFilhos)
        
        print ("Iniciando campeonato!")
        self.fileResultados.write ("Iniciando campeonato!\n")
        
        campeonato = Campeonato (listaJogadores)
        fileResultadosCampeonato = open (VariaveisGlobais.ARQUIVO_RESULTADOS_CAMPEONATO, "a")
        fileResultadosCampeonato.write (campeonato.iniciaCampeonato ())
        fileResultadosCampeonato.close ()
        
        print ("Selecionando os melhores Jogadores!")
        self.fileResultados.write ("Selecionando os melhores Jogadores!\n")
        
        listaJogadores = self.selecionaMelhoresJogadores (listaJogadores)
        self.limpaScoreJogadores (listaJogadores)
        self.somaGeracoesVivoJogador (listaJogadores)
        
        return listaJogadores
    
    def copiaListaJogadores (self, listaJogadores):
        novaListaJogadores = []
        for jogador in listaJogadores:
            novaListaJogadores.append (copy.deepcopy(jogador))
            
        return novaListaJogadores
    
    def carregaOsModelosDosJogadoresBase (self):
        for jogador in self.listaJogadoresBase:
            jogador.carregaModelo()
    
    def rodaCampeonatoEntreTimes (self, listaJogadores):
        print ("Iniciando campeonato entre os times base para verificar a qualidade do treinamento!")
        self.fileResultados.write ("Iniciando campeonato entre os times base para verificar a qualidade do treinamento!")
        
        self.carregaOsModelosDosJogadoresBase ()
        self.limpaScoreJogadores (self.listaJogadoresBase)
        
        for jogador in listaJogadores:
            jogador.carregaModelo ()
        
        campeonatoEntreTimes = CampeonatoEntreTimes (self.listaJogadoresBase, listaJogadores)
        campeonatoEntreTimes.iniciaCampeonato ()
        
        self.listaJogadoresBase.extend (listaJogadores)
        self.listaJogadoresBase = self.selecionaMelhoresJogadores(self.listaJogadoresBase)
        self.limpaScoreJogadores (self.listaJogadoresBase)
        self.limpaScoreJogadores (listaJogadores)
        
    def iniciaTreinamento (self):
        print ("Criando os jogadores iniciais!")
        self.fileResultados.write ("Criando os jogadores iniciais!\n")
        
        listaJogadores = self.geraJogadoresIniciais ()
        
        indexGeracao = 1
        for geracao in range (self.numeroDeGeracoesTreinamento):
            self.fileResultados.close ()
            self.fileResultados = open (VariaveisGlobais.ARQUIVO_RESULTADOS_SELETOR, "a")
            
            gc.collect ()
            
            print ("Rodando Geracao: " + str(indexGeracao))
            self.fileResultados.write ("Rodando Geracao: " + str(indexGeracao) + "\n")
            
            listaJogadores = self.rodaGeracao (listaJogadores)
            indexGeracao += 1
            print ("Fim da Geracao!")
            self.fileResultados.write ("Fim da Geracao!\n")
            
            print ("")
            self.fileResultados.write ("\n")
            
            
            if (indexGeracao % self.tempoEntreVerificacoes == 0 and indexGeracao > 0):
                print ("Verificando se os jogadores melhoraram!")
                self.fileResultados.write ("Verificando se os jogadores melhoraram!\n")
                
                self.rodaCampeonatoEntreTimes (self.copiaListaJogadores(listaJogadores))
                
                for jogador in listaJogadores:
                    jogador.carregaModelo ()
            
            for jogador in listaJogadores:
                if (jogador.totalPoints >= self.fitMaximoJogador and (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo) > self.fitRealJogador)):
                    print ("Grande jogador selecionado: " + str (jogador.nomeJogador))
                    self.fileResultados.write ("Grande jogador selecionado: " + str (jogador.nomeJogador) + "\n")
                    
                    print ("Terminando a rodada de geracoes!")
                    self.fileResultados.write ("Terminando a rodade de geracoes!\n")
                    
                    break
        
        K.clear_session ()
        self.fileResultados.close ()