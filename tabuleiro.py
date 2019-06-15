# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import math
import numpy as np
import copy
from movimento import Movimento


class Tabuleiro:
    
    PEAO = 1
    INIMIGO = -1
    DAMA = 9
    DAMAINIMIGA = -9
    CASAVAZIA = 0
    
    def __init__ (self, tabuleiroConfiguracao = np.array ([[0, -1, 0, -1, 0, -1, 0, -1], [-1, 0, -1, 0, -1, 0, -1, 0], [0, -1, 0, -1, 0, -1, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]])):
        #CASO O CONSTRUTOR USADO SEJA O COM UM TABULEIRO, O TABULEIRO CRIADO TERA A MESMA CONFIGURACAO DO USADO DE BASE
        #USADO DEEPCOPY PARA A CRIACAO DE UM NOVO OBJETO 100% DIFERENTE DO ANTERIOR PARA EVITAR PROBLEMAS DE REFERÊNCIA DE MEMÓRIA
        self.tabuleiroConfiguracao = copy.deepcopy (tabuleiroConfiguracao)

    def doNormalMovement (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        
        tempPeca = self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]]
        self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] = self.CASAVAZIA
        self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] = tempPeca
        
    def doComeMovement (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        casaPecaASerComida = self.pegaCasaPecaComida (movimento)
        
        tempPeca = self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]]
        self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] = self.CASAVAZIA
        self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] = tempPeca
        self.tabuleiroConfiguracao [casaPecaASerComida[0], casaPecaASerComida [1]] = self.CASAVAZIA
            
    def coroaPeca (self, movimento):
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        
        if (casaFinal [0] == 0):
            self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] = self.DAMA;    
    
    def doAnyMovement (self, movimento):
        #PRIMEIRO VERIFICA SE EH POSSIVEL REALIZAR O MOVIMENTO
        if (not(self.verificaValidadeMovimento (movimento))):
#            print ("Movimento nao permitido!!")
            return False
        
        tamanhoMovimento = self.calculaTamanhoMovimento (movimento);
        
        if (tamanhoMovimento == 1):
#            print ("Fazendo movimento normal!")
            self.doNormalMovement (movimento)
            
        elif(tamanhoMovimento == 2):
#            print ("Fazendo movimento para comer peca!")
            self.doComeMovement (movimento)
        else:
            return False
        
        return True;
            
    def pegaCasaPecaComida (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        
        direcao = self.normalizeVector (np.subtract (casaInicial, casaFinal))
        
        return np.add (casaFinal, direcao)
        
    def normalizeVector (self, vector):
        vectorNormalizado = np.array ([0, 0])
        for index in range (vector.shape[0]):
            vectorNormalizado [index] = vector[index] / np.abs (vector[index])
            
        return vectorNormalizado
    
    def calculaTamanhoMovimento (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        
        direcao = np.subtract (casaInicial, casaFinal)
        tamanhoMovimento = np.abs(direcao) [0]
        
        return tamanhoMovimento
        
    def verificaValidadeMovimentoNormal (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        
        tamanhoMovimento = self.calculaTamanhoMovimento (movimento)
        direcaoY = casaFinal[0] - casaInicial[0];
        
        if (tamanhoMovimento == 1 and self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] == self.CASAVAZIA and (direcaoY < 0 or self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1] == self.DAMA])):
            return True
        else:
            return False
    
    def verificaValidadeMovimentoComer (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        casaPecaASerComida = self.pegaCasaPecaComida (movimento)
        
        tamanhoMovimento = self.calculaTamanhoMovimento (movimento)
        direcaoY = casaFinal[0] - casaInicial[0];
        
        if (tamanhoMovimento == 2 and self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] == self.CASAVAZIA and (self.tabuleiroConfiguracao [casaPecaASerComida[0], casaPecaASerComida [1]] == self.INIMIGO or self.tabuleiroConfiguracao [casaPecaASerComida[0], casaPecaASerComida [1]] == self.DAMAINIMIGA) and (direcaoY < 0 or self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] == self.DAMA)):
            return True
        else:
            return False
        
    def verificaSeExistePecaParaMover (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        
        if (self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] != self.PEAO):
            return True
        else:
            return False
    
    def verificaValidadeMovimento (self, movimento):
        if (self.verificaSeExistePecaParaMover (movimento)):
#            print ("Casa Inicial de movimento nao tem peca que pode ser jogada!!")
            return False
        if (self.verificaValidadeMovimentoNormal (movimento)):
            return True
        elif (self.verificaValidadeMovimentoComer (movimento)):
            return True
        else:
            return False
    
    def printaTabuleiro (self):
        for row in range (self.tabuleiroConfiguracao.shape[0]):
            print (str (8 - row) + "   ", end = " ")
            for column in range (self.tabuleiroConfiguracao.shape[1]):
                print (self.tabuleiroConfiguracao [row, column], end = " ")
            print ("")
            
        print ("")
        print ("    ", end = " ")
        letter = ord('a')
        for row in range (self.tabuleiroConfiguracao.shape[0]):
            print (chr (letter + row), end = " ")
            
    def converteTabuleiroParaArray (self):
        indexArray = 0;
        array = np.zeros (shape = (32))
        
        for row in range (self.tabuleiroConfiguracao.shape[0]):
            for column in range (self.tabuleiroConfiguracao.shape[1]):
                if ((row + column) % 2 == 1):
                    array [indexArray] = self.tabuleiroConfiguracao [row, column]
                    indexArray += 1
                    
        return array
        
        
        