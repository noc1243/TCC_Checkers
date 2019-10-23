# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:33:17 2019

@author: nocera
"""

import sys
import math
import numpy as np
import copy
import time

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class GerenciadorDeTabuleiros:
    
    
    def __init__ (self, tabuleiro):
        self.tabuleiro = tabuleiro
        
    def geraMovimentoAPartirDeRowEColumn (self, inicialRow, inicialColumn, finalRow, finalColumn):
        inicialNumero = 7 - inicialRow
        inicialLetra = chr(ord('a') + inicialColumn)
        casaInicial = Casa (inicialLetra, inicialNumero)
        
        finalNumero = 7 - finalRow
        finalLetra = chr(ord('a') + finalColumn)
        casaFinal = Casa (finalLetra, finalNumero)
        
        movimento = Movimento (casaInicial, casaFinal)
        return movimento
        
    def criaTabuleiroAPartirDeUmMovimento (self, movimento):
        novoTabuleiro = Tabuleiro (self.tabuleiro.tabuleiroConfiguracao)
        
        if (novoTabuleiro.doAnyMovement (movimento)):
            return novoTabuleiro
        else:
            return None
        
    def criaTabuleiroAPartirDeUmaListaDeMovimentos (self, listaMovimento):
        novoTabuleiro = Tabuleiro (self.tabuleiro.tabuleiroConfiguracao)
        
        if (novoTabuleiro.doMultipleMovementsComer (listaMovimento)):
            return novoTabuleiro
        else:
            return None
        
    def criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (self, movimento, tabuleiro):
        novoTabuleiro = Tabuleiro (tabuleiro.tabuleiroConfiguracao)
        
        if (novoTabuleiro.doAnyMovement (movimento)):
            return novoTabuleiro
        else:
            return None
        
    def criaMovimentoValidoAPartirDeRowEColumn (self, inicialRow, inicialColumn, finalRow, finalColumn):
        if (finalColumn < 0 or finalColumn > 7 or finalRow < 0 or finalRow > 7):
            return None
        else:
            return self.geraMovimentoAPartirDeRowEColumn (inicialRow, inicialColumn, finalRow, finalColumn)
        
    def criaMovimentoParaOPeao (self, row, column):
        listTabuleirosPossiveis = []
        
        movimento1 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 1, column - 1)
        movimento2 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 1, column + 1)
        
        if (not movimento1 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento1))
        if (not movimento2 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento2))
            
        return listTabuleirosPossiveis
    
    def criaMovimentoParaADama (self, row, column):
        listTabuleirosPossiveis = []
        
        movimento1 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 1, column - 1)
        movimento2 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 1, column + 1)
        movimento3 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row + 1, column - 1)
        movimento4 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row + 1, column + 1)
        
        if (not movimento1 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento1))
        if (not movimento2 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento2))
        if (not movimento3 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento3))
        if (not movimento4 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento4))
            
        return listTabuleirosPossiveis
    
    def calculaPossibilidadesDeMovimentoNormal (self):
        listTabuleirosPossiveis = []
        for row in range (self.tabuleiro.tabuleiroConfiguracao.shape[0]):
            for column in range (self.tabuleiro.tabuleiroConfiguracao.shape[1]):
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.PEAO):
                    listTabuleirosPossiveis.extend (self.criaMovimentoParaOPeao (row, column))
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.DAMA):
                    listTabuleirosPossiveis.extend (self.criaMovimentoParaADama (row, column))
                
        return listTabuleirosPossiveis
    
    def criaMovimentoParaOPeaoComer (self, row, column):
        listTabuleirosPossiveis = []
        
        movimento1 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 2, column - 2)
        movimento2 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 2, column + 2)
        
        if (not movimento1 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento1))
        if (not movimento2 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento2))
            
        return listTabuleirosPossiveis
    
    def criaMovimentoParaADamaComer (self, row, column):
        listTabuleirosPossiveis = []
        
        movimento1 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 2, column - 2)
        movimento2 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 2, column + 2)
        movimento3 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row + 2, column - 2)
        movimento4 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row + 2, column + 2)
        
        if (not movimento1 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento1))
        if (not movimento2 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento2))
        if (not movimento3 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento3))
        if (not movimento4 is None):
            listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmMovimento (movimento4))
            
        return listTabuleirosPossiveis
                        
    def calculaPossibilidadesDeMovimentoComer (self):
        listTabuleirosPossiveis = []
        for row in range (self.tabuleiro.tabuleiroConfiguracao.shape[0]):
            for column in range (self.tabuleiro.tabuleiroConfiguracao.shape[1]):
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.PEAO):
                    listTabuleirosPossiveis.extend (self.criaMovimentoParaOPeaoComer (row, column))
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.DAMA):
                    listTabuleirosPossiveis.extend (self.criaMovimentoParaADamaComer (row, column))
                        
        listTabuleirosPossiveis
        
        
    #CODIGO QUE CALCULA TODOS OS MOVIMENTOS POSSIVEIS PARA QUE O PEAO COMA!
    def criaMultiplosMovimentosParaOPeaoComer (self, row, column, listaMovimentos, tabuleiro):
        listaDeListaDeMovimentos = []
        if (column < 0 or column > 7 or row < 0 or row > 7):
            return None
        
        movimento1 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 2, column - 2)
        movimento2 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 2, column + 2)
        
        if (not movimento1 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento1, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento1)
#                listaDeListaDeMovimentos.append (listaMovimentos)
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaOPeaoComer (row - 2, column - 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None and len(listaDeListaDeMovimentosResultado) > 0):
                    listaDeListaDeMovimentos = (copy.deepcopy (listaDeListaDeMovimentosResultado))
#                    listaDeListaDeMovimentos.remove (listaMovimentos)
                else:
                    listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                    
                listaMovimentos.remove (movimento1)
                
        if (not movimento2 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento2, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento2)
#                listaDeListaDeMovimentos.append (listaMovimentos)
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaOPeaoComer (row - 2, column + 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None and len(listaDeListaDeMovimentosResultado) > 0):
                    listaDeListaDeMovimentos = (copy.deepcopy (listaDeListaDeMovimentosResultado))
#                    listaDeListaDeMovimentos.remove (listaMovimentos)
                else:
                    listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                    
                listaMovimentos.remove (movimento2)
                
        return listaDeListaDeMovimentos
    
    #CODIGO QUE CALCULA TODOS OS MOVIMENTOS POSSIVEIS PARA QUE A DAMA COMA!
    def criaMultiplosMovimentosParaADamaComer (self, row, column, listaMovimentos, tabuleiro):
        listaDeListaDeMovimentos = []
        if (column < 0 or column > 7 or row < 0 or row > 7):
            return None
        
        movimento1 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 2, column - 2)
        movimento2 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row - 2, column + 2)
        movimento3 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row + 2, column - 2)
        movimento4 = self.criaMovimentoValidoAPartirDeRowEColumn (row, column, row + 2, column + 2)
        
        if (not movimento1 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento1, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento1)
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaADamaComer (row - 2, column - 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None and len(listaDeListaDeMovimentosResultado) > 0):
                    listaDeListaDeMovimentos = copy.deepcopy (listaDeListaDeMovimentosResultado)
                else:
                    listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                    
                listaMovimentos.remove (movimento1)
                
        if (not movimento2 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento2, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento2)
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaADamaComer (row - 2, column + 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None and len(listaDeListaDeMovimentosResultado) > 0):
                    listaDeListaDeMovimentos = copy.deepcopy (listaDeListaDeMovimentosResultado)
                else:
                    listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                    
                listaMovimentos.remove (movimento2)
                
        if (not movimento3 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento3, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento3)
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaADamaComer (row + 2, column - 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None and len(listaDeListaDeMovimentosResultado) > 0):
                    listaDeListaDeMovimentos = copy.deepcopy (listaDeListaDeMovimentosResultado)
                else:
                    listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                    
                listaMovimentos.remove (movimento3) 
                
        if (not movimento4 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento4, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento4)
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaADamaComer (row + 2, column + 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None and len(listaDeListaDeMovimentosResultado) > 0):
                    listaDeListaDeMovimentos = copy.deepcopy (listaDeListaDeMovimentosResultado)
                else:
                    listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                    
                listaMovimentos.remove (movimento4) 
        
        return listaDeListaDeMovimentos
    
    def calculaPossibilidadesDeMultiplasComidas (self):
        listTabuleirosPossiveis = []
        for row in range (self.tabuleiro.tabuleiroConfiguracao.shape[0]):
            for column in range (self.tabuleiro.tabuleiroConfiguracao.shape[1]):
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.PEAO):
                    listaDeListaDeMovimentos = self.criaMultiplosMovimentosParaOPeaoComer (row, column, [], self.tabuleiro)
                    if (not listaDeListaDeMovimentos is None):
                        for listaDeMovimentos in listaDeListaDeMovimentos:
                            if (not listaDeMovimentos is None):
                                listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmaListaDeMovimentos(listaDeMovimentos))
                
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.DAMA):
                    listaDeListaDeMovimentos = self.criaMultiplosMovimentosParaADamaComer (row, column, [], self.tabuleiro)
                    if (not listaDeListaDeMovimentos is None):
                        for listaDeMovimentos in listaDeListaDeMovimentos:
                            if (not listaDeMovimentos is None):
                                listTabuleirosPossiveis.append (self.criaTabuleiroAPartirDeUmaListaDeMovimentos(listaDeMovimentos))
                    
        return listTabuleirosPossiveis

class Casa:
    
    def __init__(self, letra, numero):
        self.letra = letra
        self.numero = numero
        
    def converteMovimentoParaArray (self):
        #FEITO DESSA FORMA PARA CORRESPONDER A UM TABULEIRO NORMAL
        numeroLetra = ord(self.letra) - ord('a')
        numeroNumero = 7 - self.numero
        return np.array([numeroNumero, numeroLetra])
    
    def printaCasa (self):
        print (self.letra + " " + str(self.numero), file=sys.stderr)
        
class Movimento:
    
    def __init__(self, casaInicial, casaFinal):
        self.casaInicial = casaInicial
        self.casaFinal = casaFinal
        
    def printaMovimento (self):
        self.casaInicial.printaCasa ()
        self.casaFinal.printaCasa ()
        print ("")
        
class VariaveisGlobais :
    TABULEIRO_INICIAL = np.array ([[0, -1, 0, -1, 0, -1, 0, -1], 
                                   [-1, 0, -1, 0, -1, 0, -1, 0], 
                                   [0, -1, 0, -1, 0, -1, 0, -1], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [1, 0, 1, 0, 1, 0, 1, 0], 
                                   [0, 1, 0, 1, 0, 1, 0, 1], 
                                   [1, 0, 1, 0, 1, 0, 1, 0]])
    
    TABULEIRO_TESTE =   np.array ([[0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, -1, 0, -1, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, -1, 0, -1, 0, 0, 0, 0], 
                                   [0, 0, 9, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
    
    TABULEIRO_TESTE_2 =   np.array ([[0, 0, 0, 0, 0, 0, 0, -1], 
                                   [-1, 0, 0, 0, -1, 0, -1, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [-1, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, -1, 0, 0, 0, -1], 
                                   [-9, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, -9, 0, 1, 0]])
    
    TABULEIRO_TESTE_3 =   np.array ([[0, -1, 0, -1, 0, -1, 0, -1], 
                                   [0, 0, -1, 0, -1, 0, -1, 0], 
                                   [0, -1, 0, -1, 0, -1, 0, 0], 
                                   [0, 0, -1, 0, 0, 0, -1, 0], 
                                   [0, 1, 0, 0, 0, 0, 0, 1], 
                                   [1, 0, 1, 0, 1, 0, 0, 0], 
                                   [0, 0, 0, 1, 0, 1, 0, 1], 
                                   [1, 0, 1, 0, 1, 0, 1, 0]])
    
    TABULEIRO_TESTE_4 =   np.array ([[0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, -1, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, -1, 0], 
                                   [0, 0, 0, 0, 0, 9, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, -1, 0], 
                                   [0, 0, 0, 0, 0, 1, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
    
    PEAO = 1
    INIMIGO = -1
    DAMA = 9
    DAMAINIMIGA = -9
    CASAVAZIA = 0
    
    ARQUIVO_RESULTADOS_SELETOR = ".\\resultados_treinamento\\resultados_seletor.txt"
    ARQUIVO_RESULTADOS_CAMPEONATO = ".\\resultados_treinamento\\resultados_campeonato.txt"
    ARQUIVO_RESULTADOS_CAMPEONATO_ENTRE_TIMES = ".\\resultados_treinamento\\resultados_campeonato_entre_times.txt"
    
class Tabuleiro:
    
    def __init__ (self, tabuleiroConfiguracao = VariaveisGlobais.TABULEIRO_INICIAL):
        #CASO O CONSTRUTOR USADO SEJA O COM UM TABULEIRO, O TABULEIRO CRIADO TERA A MESMA CONFIGURACAO DO USADO DE BASE
        #USADO DEEPCOPY PARA A CRIACAO DE UM NOVO OBJETO 100% DIFERENTE DO ANTERIOR PARA EVITAR PROBLEMAS DE REFERÊNCIA DE MEMÓRIA
        self.tabuleiroConfiguracao = copy.deepcopy (tabuleiroConfiguracao)

    def doNormalMovement (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        
        tempPeca = self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]]
        self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] = VariaveisGlobais.CASAVAZIA
        self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] = tempPeca
        
    def doComeMovement (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        casaPecaASerComida = self.pegaCasaPecaComida (movimento)
        
        tempPeca = self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]]
        self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] = VariaveisGlobais.CASAVAZIA
        self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] = tempPeca
        self.tabuleiroConfiguracao [casaPecaASerComida[0], casaPecaASerComida [1]] = VariaveisGlobais.CASAVAZIA
            
    def coroaPeca (self, movimento):
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        
        if (casaFinal [0] == 0):
            self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] = VariaveisGlobais.DAMA;    
            
    def doMultipleMovementsComer (self, listaMovimento):
        #Salva o tabuleiro original para que, caso algum movimento nao role, o tabuleiro possa voltar para a configuracao original
        tabuleiroOriginal = copy.deepcopy (self.tabuleiroConfiguracao)
        
        for movimento in listaMovimento:
            tamanhoMovimento = self.calculaTamanhoMovimento (movimento);
            
            if (tamanhoMovimento != 2):
                print ("Movimento nao eh de comer. Movimento Invalido, tabuleiro sera resetado para o estado inicial")
                self.tabuleiroConfiguracao = copy.deepcopy (tabuleiroOriginal)
                return False
                
            if (not (self.doAnyMovement (movimento))):
                print ("Movimento nao permitido. Tabuleiro sera resetado para o estado inicial")
                self.tabuleiroConfiguracao = copy.deepcopy (tabuleiroOriginal)
                return False
            
        return True
                
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
        
        self.coroaPeca (movimento)
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
        tamanhoMovimento = max (np.abs(direcao) [0], np.abs(direcao) [1])
        
        return tamanhoMovimento
        
    def verificaValidadeMovimentoNormal (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        
        tamanhoMovimento = self.calculaTamanhoMovimento (movimento)
        direcaoY = casaFinal[0] - casaInicial[0];
        
        if (tamanhoMovimento == 1 and self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] == VariaveisGlobais.CASAVAZIA and (direcaoY < 0 or self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] == VariaveisGlobais.DAMA)):
            return True
        else:
            return False
    
    def verificaValidadeMovimentoComer (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        casaFinal = movimento.casaFinal.converteMovimentoParaArray()
        casaPecaASerComida = self.pegaCasaPecaComida (movimento)
        
        tamanhoMovimento = self.calculaTamanhoMovimento (movimento)
        direcaoY = casaFinal[0] - casaInicial[0];
        
        if (tamanhoMovimento == 2 and self.tabuleiroConfiguracao [casaFinal[0], casaFinal [1]] == VariaveisGlobais.CASAVAZIA and (self.tabuleiroConfiguracao [casaPecaASerComida[0], casaPecaASerComida [1]] == VariaveisGlobais.INIMIGO or self.tabuleiroConfiguracao [casaPecaASerComida[0], casaPecaASerComida [1]] == VariaveisGlobais.DAMAINIMIGA) and (direcaoY < 0 or self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] == VariaveisGlobais.DAMA)):
            return True
        else:
            return False
        
    def verificaSeExistePecaParaMover (self, movimento):
        casaInicial = movimento.casaInicial.converteMovimentoParaArray()
        
        if (self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] != VariaveisGlobais.PEAO and self.tabuleiroConfiguracao [casaInicial[0], casaInicial [1]] != VariaveisGlobais.DAMA):
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
            print (str (8 - row) + "   ", end = " ", file=sys.stderr)
            for column in range (self.tabuleiroConfiguracao.shape[1]):
                if (self.tabuleiroConfiguracao [row, column] == VariaveisGlobais.INIMIGO):
                    print ("x", end = " ", file=sys.stderr)
                elif (self.tabuleiroConfiguracao [row, column] == VariaveisGlobais.DAMAINIMIGA):
                    print ("y", end = " ", file=sys.stderr)
                else:
                    print (self.tabuleiroConfiguracao [row, column], end = " ", file=sys.stderr)
            print ("", file=sys.stderr)
            
        print ("", file=sys.stderr)
        print ("    ", end = " ", file=sys.stderr)
        letter = ord('a')
        for row in range (self.tabuleiroConfiguracao.shape[0]):
            print (chr (letter + row), end = " ", file=sys.stderr)
            
        print ("", file=sys.stderr)
            
    def converteTabuleiroParaArray (self, valorDama):
        indexArray = 0;
        array = np.zeros (shape = (32))
        
        for row in range (self.tabuleiroConfiguracao.shape[0]):
            for column in range (self.tabuleiroConfiguracao.shape[1]):
                if ((row + column) % 2 == 1):
                    array [indexArray] = self.tabuleiroConfiguracao [row, column]
                    
                    if (array [indexArray] == VariaveisGlobais.DAMA):
                        array [indexArray] = valorDama
                    
                    indexArray += 1
                    
        return array
    
    def inverteVisaoTabuleiro (self):
        self.tabuleiroConfiguracao = np.rot90 (np.rot90 (self.tabuleiroConfiguracao)) * (-1)
        
def converteInputParaTabuleiro (listaLinhas, cor, valorK):
    print (cor, file=sys.stderr)
    if (cor != "r" and cor != "b"):
        print ("ERRO AQUI: " + cor, file=sys.stderr)
        cor = "r"
    if (cor == "w"):
        cor = "r"
    listaTabuleiro = []
    for linha in listaLinhas:
        linhaArray = []
        for index in range (len(linha)):
            casa = linha [index].strip()
            #print (casa, file=sys.stderr)
            if (casa == "."):
                linhaArray.append (0)
            elif (casa == cor):
                linhaArray.append (1)
            elif (casa == cor.upper ()):
                linhaArray.append (valorK)
            else:
                print (casa, file=sys.stderr)
                if (casa.isupper()):
                    linhaArray.append (-valorK)
                else:
                    linhaArray.append (-1)
        listaTabuleiro.append (np.array (linhaArray))
    
    tabuleiroArray = np.array (listaTabuleiro)
    if (cor == "r"):
        tabuleiroArray = np.rot90 (np.rot90 (tabuleiroArray))
    tabuleiro = Tabuleiro (tabuleiroArray)
    return tabuleiro


def fazJogada (tabuleiro, jogadas, cor):
        jogadaEfetuada = False
        
        tabuleiroASerJogado = copy.deepcopy (tabuleiro)
        
        while (not jogadaEfetuada):
            listaJogadas = getListaMovimentos (jogadas, cor)
            
            if (len (listaJogadas) == 1):
                if (tabuleiroASerJogado.doAnyMovement (listaJogadas [0])):
                    jogadaEfetuada = True
            else:
                tabuleiroASerJogado.doMultipleMovementsComer (listaJogadas)
                if (not np.array_equal (tabuleiroASerJogado.tabuleiroConfiguracao, tabuleiro.tabuleiroConfiguracao)):
                    jogadaEfetuada = True
            
            if (not jogadaEfetuada):
                return None
                
            
        return tabuleiroASerJogado
    
def getListaMovimentos (jogadas, cor):
    listaJogadas = []
    # print ("pegando input do tabuleiro", file=sys.stderr)
    
    if (cor != "r" and cor != "b"):
        cor = "r"
        
    jogadas = jogadas.split ("\"")
        
    for jogada in jogadas:
        if (jogada and not jogada == " "):
            separados = jogada.split (" ")
            
            if (cor == "b"):                
                letraInicial = separados [0]
                numeroInicial = int (separados [1])
            else:
                letraInicial = chr(ord('h') - (ord(separados[0]) - ord('a')))
                numeroInicial = 7 - int (separados [1])
            casaInicial = Casa (letraInicial, numeroInicial)
                
            if (cor =="b"):    
                letraFinal = separados [2]
                numeroFinal = int(separados [3])
            else:
                letraFinal = chr(ord('h') - (ord(separados[2]) - ord('a')))
                numeroFinal = 7 - int (separados [3])
                
            casaFinal = Casa (letraFinal, numeroFinal)
                
            movimento = Movimento (casaInicial, casaFinal)
            
            # movimento.printaMovimento ()
            listaJogadas.append (movimento)
            
    return listaJogadas

def converteJogadaParaInputDoTabuleiro (jogadas):
    listaJogadas = "\""
    comecouAParsear = True
    for index in range (0, len(jogadas), 2):
        listaJogadas += jogadas [index].lower() + " " + str(int(jogadas [index + 1]) - 1)
        if (index + 2 < len(jogadas)):
            if (not comecouAParsear):
                listaJogadas += "\"" + " \"" + jogadas [index].lower() + " " + str(int(jogadas [index + 1]) - 1) + " "
            else:
                listaJogadas += " "
        else:
            listaJogadas += "\""
        
        comecouAParsear = False
        
        
    print (listaJogadas, file=sys.stderr)
    return listaJogadas

def predict (tabuleiroArray):
    global camada0
    global camada1
    global camada2
    global pesoCamada0
    global pesoaCamada1
    global pesoCamada2
    
    arrayTabuleiro = np.array ([tabuleiroArray])
    score = np.tanh(np.tanh(np.tanh(arrayTabuleiro.dot(camada0) + pesoCamada0).dot(camada1) + pesoCamada1).dot(camada2) + pesoCamada2)
    return score

numeroJogadasAFrente = 3
timeStart = 0

def calculaScoreTabuleiroMedia (tabuleiro, numeroDaJogada, jogadorJogando):
    global numeroJogadasAFrente
    global pesoDama
    global timeStart
    print ("Numero da jogada: " + str (numeroDaJogada) + " tempo de jogo: " + str (time.time() - timeStart), file=sys.stderr)
    if (numeroDaJogada >= numeroJogadasAFrente or (time.time() - timeStart) >= 0.077):
        if (jogadorJogando):
            tabuleiro.inverteVisaoTabuleiro()
            score = predict (tabuleiro.converteTabuleiroParaArray (pesoDama))

            gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
            listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
            if (not listaTabuleiros or listaTabuleiros is None):
                listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
                    
            if (len (listaTabuleiros) == 0 or listaTabuleiros is None):
                score = -1.1
                    
            return score
        else:
            score = predict (tabuleiro.converteTabuleiroParaArray (pesoDama))
            tabuleiro.inverteVisaoTabuleiro()
            gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
            listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
            if (not listaTabuleiros or listaTabuleiros is None):
                listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
                    
            if (len (listaTabuleiros) == 0 or listaTabuleiros is None):
                score = 1.1
                    
            return score
        
    tabuleiro.inverteVisaoTabuleiro ()
        
    jogadaForcada = False
        
    gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiro)
    listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
    if (not listaTabuleiros or listaTabuleiros is None):
        listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
#    elif (len (listaTabuleiros) < self.numeroDePossiveisComidasParaNaoConsiderarJogadaForcada):
#        jogadaForcada = True
        
    numeroDaProximaJogada = numeroDaJogada
    numeroDaProximaJogada += 1 
#        if (not jogadaForcada):
#            numeroDaProximaJogada += 1 
            
    if (len (listaTabuleiros) == 0):
        if (jogadorJogando):
            return -1
        else:
            return 1
    soma = 0
    for tabuleiro in listaTabuleiros:
        if (not tabuleiro is None):
            if (jogadorJogando):
                soma += calculaScoreTabuleiroMedia (copy.deepcopy(tabuleiro), copy.deepcopy(numeroDaProximaJogada), False)
            else:
                soma += calculaScoreTabuleiroMedia (copy.deepcopy(tabuleiro), copy.deepcopy(numeroDaProximaJogada), True)
                    
        
    return soma/len(listaTabuleiros)
    
camada0 = np.array ([[ 0.13479249   ,-0.1843504    , 0.12612464   , 0.093718156  ,
  -0.059366494  , 0.10360056   ,-0.08070613   , 0.0003078085 ,
   0.357663     ,-0.14828017   ,-0.1260941    ,-0.14415608   ,
   0.15506452   ,-0.012091037  , 0.07836644   , 0.21538612   ,
   0.16141748   ,-0.05771788   ,-0.14640102   ,-0.055872608  ,
  -0.122098476  , 0.062094513  ,-0.17284597   , 0.04578997   ,
   0.05362403   ,-0.18975203   ,-0.017473781  , 0.13340935   ,
  -0.11577365   , 0.003658184  ,-0.054732148  ,-0.039055806  ,
   0.04105836   , 0.04684228   ,-0.033023126  , 0.08265309   ,
   0.15034682   , 0.31532702   , 0.23130125   , 0.12791543   ],
 [-0.03887308   , 0.08512969   , 0.55108804   ,-0.10439647   ,
   0.01478189   , 0.13814299   , 0.025377383  ,-0.011644966  ,
  -0.11728164   , 0.1367364    , 0.046446856  ,-0.0999209    ,
  -0.1485709    ,-0.12947303   ,-0.035040874  ,-0.025473313  ,
   0.10970288   , 0.0675135    ,-0.16956092   ,-0.1471347    ,
   0.011913115  ,-0.07812027   ,-0.19829513   , 0.17826702   ,
  -0.022528566  ,-0.70007294   ,-0.08157428   ,-0.020586783  ,
   0.77886546   , 0.07939358   , 0.18457064   , 0.026644908  ,
  -0.13613689   , 0.203518     ,-0.14938855   ,-0.12746698   ,
   0.0330219    ,-0.12919      , 0.121490054  ,-0.38489756   ],
 [ 0.25989294   , 0.014026082  , 0.08875881   ,-0.12679625   ,
  -0.059629604  , 0.09746727   , 0.08824363   , 0.19389372   ,
   0.12698078   ,-0.016924568  , 0.15162654   ,-0.20313671   ,
   0.105025195  ,-0.29711404   ,-0.19020315   , 0.040739555  ,
   0.1213128    , 0.036412437  , 0.08194816   ,-0.11807857   ,
  -0.06112673   , 0.04484662   ,-0.1840235    , 0.0618183    ,
   0.20207338   , 0.17240994   , 0.0054803547 , 0.18808833   ,
  -0.029345715  , 0.034533445  ,-0.27124816   , 0.018581266  ,
  -0.013268472  , 0.18667036   ,-0.21255928   , 0.013298999  ,
   0.068858236  ,-0.0033724573 , 0.1561485    ,-0.1095376    ],
 [ 0.17852175   , 0.22458194   , 0.1402323    , 0.19027872   ,
  -0.052487973  , 0.11097074   ,-0.05613123   ,-0.012269093  ,
   0.042079072  ,-0.19847102   ,-0.10285566   ,-0.08013961   ,
  -0.10810011   ,-0.11536159   , 0.092372596  ,-0.036457986  ,
   0.032288905  , 0.06284656   , 0.059583683  , 0.22597049   ,
  -0.10678665   ,-0.042932022  , 0.22107482   , 0.1698437    ,
   0.097083606  , 0.072927855  , 0.48796135   ,-0.0005629264 ,
  -0.13443203   ,-0.07349956   ,-0.06956155   , 0.1612213    ,
   0.22746141   ,-0.15592055   , 0.13943474   ,-0.20668408   ,
   0.09703289   , 0.2061176    ,-0.13979228   ,-0.10021568   ],
 [ 0.06705219   ,-0.007966042  ,-0.10913092   ,-0.014246386  ,
   0.13274921   , 0.08952715   ,-0.034503363  ,-0.0077298046 ,
  -0.0060296925 ,-0.035408262  ,-0.13958707   ,-0.20433415   ,
   0.9062125    , 0.14746618   , 0.16657616   , 0.06681167   ,
  -0.10244638   ,-0.16833256   , 0.15691622   , 0.15136574   ,
  -0.30605552   ,-0.057549078  , 0.0010979433 , 0.05349851   ,
   0.10518966   , 0.09942546   ,-0.081197225  ,-0.0825759    ,
   0.21813919   , 0.11757523   , 0.12811266   ,-0.081985824  ,
   0.17200842   ,-0.1665909    ,-0.21478605   ,-0.07005108   ,
  -0.2173327    , 0.4282968    , 0.0931966    ,-0.17763665   ],
 [ 0.18101572   , 0.09808841   ,-0.040037274  , 0.08764215   ,
   0.2581863    , 0.07141      , 0.29354668   ,-0.18561944   ,
  -0.18286747   , 0.052578524  , 0.07756587   ,-0.2598074    ,
   0.08214973   ,-0.012691902  ,-0.05052974   , 0.10696082   ,
   0.061098177  ,-0.14342019   , 0.08956484   , 0.119937494  ,
   0.023231741  , 0.101242974  ,-0.33322087   ,-0.030776301  ,
   0.13263041   ,-0.06101204   ,-0.17778698   , 0.1620949    ,
   0.06829345   ,-0.12949657   ,-0.15622993   , 0.07703282   ,
  -0.21466067   , 0.118690684  ,-0.032157943  ,-0.00007108098,
  -0.13239901   , 0.17390203   ,-0.1315703    ,-0.11211211   ],
 [ 0.4951642    , 0.14573963   , 0.19128123   , 0.07449189   ,
  -0.13838      , 0.0030266426 ,-0.17014723   , 0.15880978   ,
   0.007298171  , 0.035693284  , 0.09305898   ,-0.02960347   ,
  -0.059828777  ,-0.0055459957 , 0.023403194  , 0.14546809   ,
   0.022744955  , 0.05338862   , 0.04811371   , 0.066027164  ,
  -0.13175723   ,-0.059061073  , 0.06870566   ,-0.05330925   ,
  -0.09416804   ,-0.14396293   ,-0.11108261   ,-0.08979136   ,
   0.10477413   ,-0.17769589   , 0.07442514   , 0.11791788   ,
  -0.03152704   , 0.20426416   , 0.5323451    ,-0.12729844   ,
   0.18157883   , 0.07908979   , 0.13517952   ,-0.10048286   ],
 [-0.21332777   , 0.09581647   , 0.18810825   , 0.115020946  ,
   0.031132212  ,-0.11183079   , 0.16345127   , 0.024507456  ,
  -0.23845762   ,-0.033952598  ,-0.17966759   , 0.16171014   ,
   0.13089438   ,-0.1638626    , 0.16738228   ,-0.0425738    ,
   0.03947166   , 0.08327482   , 0.13463755   ,-0.056968577  ,
   0.15185837   , 0.14540805   ,-0.11956698   , 0.22003925   ,
   0.02523386   , 0.01122042   , 0.1861016    ,-0.17191859   ,
  -0.0243803    , 0.147918     , 0.058281858  ,-0.007178561  ,
   0.61187136   , 0.10553583   ,-0.009411133  ,-0.16854627   ,
  -1.1770483    ,-0.016502663  ,-0.107098356  , 0.033337325  ],
 [ 0.16727062   , 0.10802359   , 0.123220354  ,-0.118086606  ,
   0.040433485  ,-0.17341338   , 0.13300231   , 0.18633737   ,
  -0.18018718   ,-0.16622435   , 0.14961986   , 0.004518016  ,
   0.102806635  , 0.040536966  ,-0.09862666   , 0.01549543   ,
  -0.177121     ,-0.16932398   ,-0.118640184  ,-0.21742438   ,
   0.27344137   ,-0.066449426  , 0.06731369   ,-0.00017289825,
  -0.08910993   , 0.049859732  , 0.12581414   , 0.068649545  ,
   0.057428528  , 0.011654538  ,-0.17158778   , 0.080905706  ,
   0.11516829   , 0.14422974   ,-0.19105022   ,-0.17814858   ,
   0.08348074   ,-0.1147255    ,-0.12933064   , 0.3803449    ],
 [-0.025695588  , 0.5768631    , 0.12733918   , 0.05374374   ,
  -0.098595135  ,-0.025567075  ,-0.14846972   ,-0.074813075  ,
  -0.123392336  , 0.10788586   ,-0.28775725   ,-0.07196604   ,
   0.079348266  ,-0.069621     , 0.22524373   ,-0.17701587   ,
  -0.12758283   ,-0.17494418   , 0.057681017  , 0.052219212  ,
  -0.03251094   , 0.04112441   ,-0.31434938   ,-0.14436299   ,
   0.052316885  , 0.003143658  ,-0.1713925    , 0.13661535   ,
  -0.18978357   , 0.14643626   , 0.11959592   ,-0.078376584  ,
  -0.033740275  , 0.17042011   , 0.030524481  ,-0.034151446  ,
   0.16095915   , 0.092656806  , 0.2985436    ,-0.18476857   ],
 [ 0.14233458   ,-0.00040335013,-0.19324122   , 0.18372229   ,
   0.0024094123 , 0.12085464   , 0.17016345   , 0.18946604   ,
  -0.0043668216 ,-0.058486126  ,-0.096535295  , 0.15625347   ,
   0.010466865  ,-0.008384963  , 0.08721067   , 0.3029729    ,
  -0.33725402   , 0.074411795  , 0.25148404   ,-0.16126336   ,
  -0.024052657  , 0.17113891   ,-0.16527052   , 0.090310924  ,
   0.099110276  , 0.04212058   ,-0.16387455   ,-0.11873804   ,
  -0.12826587   ,-0.09703107   , 0.43704718   ,-0.13088322   ,
  -0.06071729   ,-0.13539055   , 0.02515311   ,-0.10736585   ,
  -0.30723873   ,-0.14828518   , 0.21725227   ,-0.14140448   ],
 [-0.33394215   , 0.80973405   , 0.12410997   , 0.13740648   ,
  -0.0227797    , 0.07076265   ,-0.18394423   , 0.113999106  ,
   0.08667785   , 0.14113899   ,-0.053450063  , 0.08865269   ,
   0.083552904  ,-0.14361489   , 0.15621454   , 0.15243164   ,
   0.10263814   ,-0.038721424  ,-0.02799491   ,-0.050174553  ,
  -0.17644992   , 0.050099827  , 0.00040905355,-0.10828612   ,
  -0.16101278   , 0.121505946  ,-0.0112468405 ,-0.031594634  ,
   0.041021932  , 0.16065134   , 0.19532171   ,-0.18569805   ,
   0.038642943  ,-0.15588352   , 0.021876508  , 0.18334794   ,
  -0.19809407   , 0.12223405   ,-0.013012139  , 0.09071346   ],
 [-0.12105997   , 0.09015224   , 0.16355069   , 0.107421316  ,
   0.05337818   ,-0.09327387   ,-0.008690709  , 0.72261214   ,
   0.32609525   , 0.17972772   , 0.04746599   ,-0.14092375   ,
  -0.07406391   , 0.16730925   ,-0.10514645   ,-0.18593797   ,
   0.06647959   , 0.097663455  , 0.11107943   ,-0.10636111   ,
   0.06413007   ,-0.17348309   , 0.08258642   , 0.19310306   ,
  -0.19027914   ,-0.07064016   , 0.031328425  , 0.17226565   ,
  -0.06322083   ,-0.15396665   , 0.05423591   , 0.106124006  ,
  -0.17146333   , 0.06890124   , 0.07778646   ,-0.05825611   ,
  -0.10942162   , 0.09714315   , 0.10862155   , 0.16637534   ],
 [ 0.026769549  ,-0.017323004  ,-0.14979085   , 0.02216931   ,
  -0.17126028   ,-0.07706838   , 0.021760717  , 0.18410334   ,
   0.11863397   , 0.11546173   ,-0.119047806  , 0.030174566  ,
   0.035010967  ,-0.04972508   , 0.11368669   , 0.20595783   ,
   0.11053066   , 0.14434566   ,-0.11960687   , 0.0036415234 ,
  -0.048959717  , 0.04715613   , 0.1088409    ,-0.17393242   ,
  -0.066941306  ,-0.067942865  , 0.16822273   ,-0.12970172   ,
  -0.20387283   ,-0.05810347   , 0.05206264   ,-0.12038591   ,
   0.16609904   ,-0.09172537   , 0.111167185  ,-0.042346943  ,
  -0.108794846  ,-0.088876955  ,-0.0270666    ,-0.19038604   ],
 [ 0.03604139   , 1.3663037    ,-0.1331228    ,-0.12398123   ,
   0.041264538  , 0.14594093   , 0.075148426  , 0.21433541   ,
  -0.14139457   ,-0.004382778  , 0.0542301    ,-0.16878632   ,
   0.01659987   ,-0.042665996  , 0.12617035   , 0.19036545   ,
  -0.0007797066 ,-0.17143434   ,-0.04248293   , 0.10874652   ,
  -0.053580992  ,-0.082250215  ,-0.10240653   , 0.09236909   ,
  -0.015482794  ,-0.03859373   ,-0.1194785    , 0.14822811   ,
  -0.094201654  ,-0.00053016207,-0.28102353   ,-0.07570931   ,
  -0.06283038   , 0.118868664  , 0.123892404  ,-0.032101613  ,
  -0.11313875   , 0.081124336  ,-0.114268996  ,-0.14440238   ],
 [ 0.009424386  ,-0.050636962  ,-0.18711975   , 0.17795499   ,
  -0.18631226   ,-0.042634517  ,-0.100363985  , 0.16133171   ,
   0.08721592   , 0.09670759   ,-0.13063766   ,-0.0011389608 ,
  -0.19719796   , 0.11427496   ,-0.09425378   , 0.043747194  ,
  -0.16772023   , 0.10745285   ,-0.06676556   ,-0.09674905   ,
   0.037418462  ,-0.100022204  , 0.08495551   ,-0.18117593   ,
   0.1444742    , 0.22616489   ,-0.3860373    , 0.0026530446 ,
  -0.2464719    , 0.12495569   , 0.2124026    , 0.038398754  ,
  -0.026392754  , 0.043979492  , 0.1661331    ,-0.011345939  ,
  -0.07067508   , 0.04755165   , 0.23575614   , 0.08803517   ],
 [ 0.034026224  , 0.24546018   , 1.9951868    ,-0.175498     ,
   0.026132096  , 0.050835364  , 0.10568712   , 0.010470338  ,
  -0.028712817  , 0.12897477   ,-0.014962614  ,-0.0234697    ,
   0.035313178  ,-0.14081217   ,-0.050782427  ,-0.09999686   ,
  -0.17488912   ,-0.0067070145 ,-0.11473417   , 0.044808313  ,
   0.11632058   ,-0.048347514  ,-0.18707015   , 0.04756792   ,
  -0.092641     , 0.084723264  ,-0.1260111    ,-0.017636042  ,
   0.1878808    ,-0.15863578   ,-0.08651243   , 0.50667554   ,
  -0.06645715   , 0.039463524  ,-0.12451727   ,-0.02322753   ,
  -0.24410605   ,-0.11041159   , 0.17126296   , 0.021436086  ],
 [ 0.18268909   , 0.36032826   , 0.13706683   , 0.03669473   ,
  -0.103041254  ,-0.059475202  , 0.06000726   , 0.24248102   ,
  -0.01941599   ,-0.16296981   , 0.03459611   , 0.20445682   ,
  -0.004397777  ,-0.34654018   ,-0.2826391    ,-0.009848347  ,
   0.048705347  , 0.19943573   , 0.19981189   ,-0.09112576   ,
  -0.011291432  ,-0.12040187   , 0.22116502   ,-0.038919736  ,
  -0.07340269   ,-0.019712755  ,-0.1617661    ,-0.04502395   ,
  -0.00038347478,-0.10153249   ,-0.5608147    , 0.06488065   ,
   0.08214487   ,-0.28415596   ,-0.21679915   , 0.05247948   ,
   0.0008698986 ,-0.113564715  , 0.2087084    , 0.046820868  ],
 [ 0.21040456   , 0.065475896  ,-0.0019300088 ,-0.028811743  ,
   0.12171701   ,-0.11282127   , 0.015526857  ,-0.1771976    ,
  -0.20487541   ,-0.17387065   ,-0.066866666  ,-0.015355592  ,
   0.07465917   ,-0.007239204  ,-0.101488724  , 0.04840159   ,
   0.41242242   , 0.08983297   ,-0.115393505  , 0.27070484   ,
  -0.0083914455 ,-0.1251729    , 0.08579372   , 0.14531007   ,
   0.078865245  , 0.14030707   ,-0.16550891   , 0.18092735   ,
   0.08482903   ,-0.091581     ,-0.010762731  ,-0.07740602   ,
  -0.0153717585 , 0.0056246035 , 0.08230548   ,-0.14081506   ,
  -0.13870233   ,-0.13788033   , 0.101957045  , 0.14814278   ],
 [ 0.055446856  ,-0.17380951   , 0.07081471   , 0.059029784  ,
  -0.15955588   , 0.11435756   , 0.18979466   ,-0.076108165  ,
  -0.18184346   , 0.062360432  ,-0.031389713  , 0.16849205   ,
  -0.4256609    , 0.0380354    , 0.14794604   , 0.080191545  ,
  -0.06593383   , 0.052197624  ,-0.12348026   ,-0.1285194    ,
  -0.06522697   ,-0.06501602   ,-0.14374313   , 0.103013106  ,
   0.088282846  , 0.19708951   ,-0.04274952   , 0.073862635  ,
  -0.16320845   , 0.097651064  ,-0.1023239    ,-0.096453935  ,
   0.13273571   ,-0.7237675    ,-0.09354847   ,-0.05074353   ,
  -0.07621462   , 0.14533503   , 0.08081034   , 0.8405965    ],
 [ 0.08320408   , 0.05619137   ,-0.15437806   ,-0.18918172   ,
   0.17174798   , 0.15993269   , 0.075566     ,-0.01082681   ,
  -0.06963878   , 0.13817734   , 0.1736599    , 0.124190636  ,
  -0.13741164   , 0.0038262373 , 0.13090314   , 0.1752082    ,
   0.09053426   , 0.15877403   ,-0.015711458  ,-0.008655316  ,
  -0.24522625   ,-0.014185719  , 0.1630883    , 0.15362288   ,
   0.3510922    ,-0.11011008   ,-0.0031903067 , 0.07085862   ,
   0.052034795  ,-0.066648774  , 0.19390461   ,-0.78454524   ,
   0.14455006   , 0.04825592   , 0.16738214   , 0.16347118   ,
   0.13477108   ,-0.08660293   ,-0.16279428   ,-0.0147136925 ],
 [ 0.07410639   ,-0.27006656   ,-0.16119716   , 0.1481203    ,
  -0.044125438  ,-0.041888703  ,-0.10971373   ,-0.1524727    ,
   0.059415985  ,-0.18335246   ,-0.09487369   ,-0.16306347   ,
   0.117142744  ,-0.18677765   , 0.085450225  ,-0.03641682   ,
  -0.18284917   ,-0.0134990895 , 0.15166208   ,-0.14297724   ,
   0.07001619   ,-0.049578264  , 0.014963503  , 0.14191955   ,
   0.12521036   ,-0.07696023   , 0.22381662   ,-0.13448407   ,
   0.5004778    ,-0.082942     , 0.069328085  ,-0.35304797   ,
  -0.07864868   , 0.0728067    ,-0.098319076  ,-0.19579133   ,
   0.15993036   ,-0.19311018   ,-0.059710573  , 0.056029454  ],
 [ 0.60346216   , 0.16034953   ,-0.15568934   ,-0.19169936   ,
  -0.010518329  , 0.2092581    ,-0.049111962  ,-0.11815836   ,
  -0.075932026  , 0.13855699   , 0.14216365   ,-0.15316422   ,
   0.08728178   ,-0.2982105    , 0.016713625  , 0.09527942   ,
   0.042740006  , 0.0013365573 , 0.18300755   , 0.08148487   ,
   0.1890452    , 0.020314999  ,-0.031396385  , 0.19071369   ,
  -0.13464756   , 0.081727214  ,-0.10262702   , 0.06424238   ,
  -0.1242583    , 0.039562475  ,-0.34990734   ,-0.056532364  ,
   0.086203136  , 0.039038412  ,-0.08521612   , 0.17485455   ,
  -0.14695737   ,-0.10851088   , 0.09877023   , 0.13366732   ],
 [ 0.11663975   ,-0.011147068  ,-0.17197636   , 0.07574581   ,
  -0.09069561   ,-0.010189274  ,-0.107981935  , 0.7852761    ,
  -0.11119883   , 0.12717807   , 0.07302407   , 0.12559976   ,
   0.06353355   , 0.029634915  ,-0.19600844   ,-0.10739413   ,
  -0.20180279   , 0.123978354  ,-0.113776326  , 0.14127943   ,
  -0.30358696   ,-0.09474776   ,-0.029295897  , 0.14964134   ,
  -0.109094694  ,-0.16788648   , 0.11548296   , 0.11744538   ,
  -0.19373822   ,-0.21118738   , 0.15484647   ,-0.17186216   ,
   0.040923703  ,-0.011889128  ,-0.107648015  , 0.0650381    ,
  -0.08472272   , 0.15144593   , 0.15599437   , 0.14393918   ],
 [ 0.1170969    , 0.1993515    , 0.009320713  ,-0.020398803  ,
  -0.023582038  , 0.004757535  , 0.08043915   ,-0.009546013  ,
  -0.030339004  , 0.080088384  , 0.07009135   , 0.027077667  ,
   0.1401502    , 0.044002336  , 0.19523749   , 0.07485252   ,
  -0.06397053   ,-0.24566603   , 0.17773354   ,-0.09480529   ,
  -0.071935944  , 0.013038418  , 0.18229766   ,-0.10014291   ,
  -0.11280025   ,-0.29635614   ,-0.09982745   , 0.16304591   ,
   0.041090436  ,-0.005079198  ,-0.08953351   , 0.075463966  ,
   0.113495454  , 0.13093747   ,-0.15746751   ,-0.15815768   ,
   0.16034219   , 0.05088754   ,-0.1566261    , 0.16212662   ],
 [ 0.060281154  , 0.0986107    , 0.043468006  , 0.15676013   ,
  -0.11578145   ,-0.11727682   , 0.0807914    , 0.15226504   ,
  -0.1454701    ,-0.029311344  , 0.23592217   ,-0.0046194987 ,
  -0.18628973   , 0.16333506   ,-0.06765017   ,-0.17874934   ,
  -0.025085438  , 0.14550097   , 0.103351206  , 0.16606495   ,
   0.13609399   ,-0.1457153    ,-0.05247398   , 0.091779225  ,
   0.012351693  , 0.13348705   ,-0.15950736   , 0.0071471273 ,
  -0.098197356  ,-0.20487988   , 0.1249381    , 0.40566933   ,
  -0.026744764  ,-0.12586114   , 0.079000264  ,-0.21180809   ,
   0.066906035  ,-0.06796294   , 0.1080544    , 0.0921792    ],
 [ 0.019977648  ,-0.11627874   ,-0.2880288    , 0.024702141  ,
  -0.13635792   ,-0.08337297   ,-0.10472697   ,-0.04713915   ,
   0.08619938   , 0.13058364   , 0.18154468   ,-0.052356195  ,
  -0.1579206    , 0.044092484  , 0.22297174   , 0.045495693  ,
  -0.017048141  , 0.15438703   , 0.14745241   ,-0.04000363   ,
  -0.1002549    ,-0.048474222  ,-0.07810755   , 0.031431843  ,
   0.33217812   , 0.122203     ,-0.034005053  , 0.2706962    ,
   0.107356824  ,-0.18927811   , 0.12988524   , 0.14283432   ,
  -0.1827028    ,-0.18279964   ,-0.07422745   ,-0.1791087    ,
   0.1861627    , 0.08856941   , 0.13943233   ,-0.113842376  ],
 [-0.05545732   ,-0.09686506   , 0.19617452   , 0.171533     ,
  -0.25161162   ,-0.111063115  ,-0.010354822  ,-0.041300833  ,
   0.14090228   ,-0.17365079   ,-0.1030024    , 0.20943888   ,
   0.14127496   ,-0.008903813  , 0.1583107    ,-0.12250939   ,
   0.22559854   , 0.19484365   ,-0.013914223  , 0.12626684   ,
  -0.15574634   , 0.1455736    , 0.064070664  , 0.11382135   ,
  -0.08115631   , 0.4142233    , 0.060761012  , 0.16937673   ,
   0.04121737   , 0.032503545  ,-0.03951197   , 0.16240725   ,
   0.011990134  , 0.08713634   , 0.05572881   ,-0.08763421   ,
   0.09890619   ,-0.16882062   ,-0.055449516  , 0.13743593   ],
 [-0.09820424   ,-0.18611005   ,-0.012564567  ,-0.07072763   ,
  -0.27691144   , 0.16523843   , 0.07709125   ,-0.042573012  ,
   0.13330407   , 0.06779227   ,-0.042018082  , 0.074933805  ,
  -0.1126353    ,-0.0678768    ,-0.17342918   , 0.17663233   ,
  -0.06492544   , 0.19495559   , 0.13252473   , 0.16228124   ,
   0.056864932  , 0.025903923  ,-0.17972173   ,-0.31569326   ,
   0.12187607   ,-0.139469     , 0.054917797  , 0.1094281    ,
   0.0724058    , 0.16775297   ,-0.0055531734 ,-0.106855094  ,
  -0.05711636   , 0.0677381    , 0.060613826  , 0.25899494   ,
  -0.062030815  , 0.13433574   , 0.060854282  ,-0.12287236   ],
 [-0.07830394   , 0.055407353  ,-0.009066733  ,-0.08359299   ,
   0.11520605   , 0.07096342   , 0.18160868   , 0.15683094   ,
  -0.013879647  ,-0.18901925   ,-0.1785427    , 0.18869807   ,
   0.07398241   ,-0.09160005   ,-0.6159428    ,-0.082996115  ,
   0.09335376   , 0.051639147  , 0.17992373   ,-0.19318393   ,
   0.1541179    ,-0.1236105    ,-0.18166873   ,-0.08548926   ,
   0.043293066  ,-0.058896814  ,-0.14791086   ,-0.08486858   ,
   0.04470202   ,-0.03009827   , 0.18652299   , 0.3597591    ,
  -0.02150471   , 0.049702305  ,-0.16179882   , 0.09359999   ,
  -0.1618282    ,-0.17243718   ,-0.008467295  , 0.11275123   ],
 [-0.1169182    ,-0.105779625  , 0.06409023   ,-0.06735416   ,
   0.007519471  , 0.14956582   ,-0.084728     ,-0.04446871   ,
   0.35879204   , 0.16844773   , 0.12866431   ,-0.25325882   ,
   0.11081952   ,-0.102295525  , 0.07949247   , 0.09560767   ,
   0.2070176    ,-0.023818268  , 0.046424672  , 0.12479131   ,
   0.084062606  , 0.0026714795 ,-0.15534674   , 0.092309475  ,
  -0.19135246   , 0.21696186   ,-0.16798502   , 0.09689521   ,
   0.14080897   , 0.2092302    ,-0.006433687  , 0.12667245   ,
   0.09806625   , 0.18900007   ,-0.2216738    ,-0.052587524  ,
  -0.011335979  , 0.10348517   ,-0.14630227   , 0.06438761   ],
 [ 0.08956092   ,-0.116395354  ,-0.15261649   , 0.103135765  ,
  -0.11087433   ,-0.08595648   , 0.11412976   ,-0.11110953   ,
   0.17681378   , 0.05825054   , 0.1274999    ,-0.068530485  ,
  -0.06707516   ,-0.038495492  , 0.1126013    , 0.0863854    ,
   0.02880931   , 0.0065148477 ,-0.050990943  ,-0.118842624  ,
  -0.1886296    , 0.052947715  , 0.0071209203 , 0.018482702  ,
  -0.11025247   , 0.21266547   , 0.15570953   , 0.021323014  ,
   0.1699606    ,-0.0066698464 , 0.06294445   , 0.06680883   ,
   0.015715273  ,-0.1431359    , 0.11726293   ,-0.092366345  ,
   0.16045524   , 0.13086751   , 0.040713158  ,-0.16292831   ]])
pesoCamada0 = np.array ([-0.0012052491, 0.012673226 , 0.008484748 ,-0.0066260877,-0.009616705 ,
 -0.0010596522, 0.020045817 , 0.053909    ,-0.011561308 , 0.0069527104,
 -0.012350604 ,-0.047095977 ,-0.027400216 , 0.0025376063,-0.059275378 ,
 -0.13146047  ,-0.004647279 ,-0.0013408855,-0.023569828 , 0.0062276646,
 -0.016356    ,-0.0074656294, 0.27613974  , 0.007576589 ,-0.009225568 ,
  0.032624394 ,-0.0015805181,-0.0016269274,-0.0125375595,-0.0075902576,
  0.008111819 ,-0.024908178 , 0.011043925 ,-0.005947697 , 0.024740456 ,
 -0.006472567 ,-0.0006288285, 0.021536494 , 0.03957334  ,-1.5653516   ])
camada1 = np.array ([[ 0.041258126 , 0.116602264 , 0.14107619  , 0.12767594  ,-0.07406205  ,
   0.10229201  ,-0.17895335  , 0.15154012  ,-0.21437018  , 0.08323555  ],
 [ 0.12282495  , 0.1032289   ,-0.79845124  , 0.083835304 , 0.088580556 ,
  -0.17844802  ,-0.075910844 , 0.097529456 , 0.08081441  , 0.20958485  ],
 [ 0.24198894  ,-0.052143298 , 0.056640472 , 0.036393683 , 0.13592777  ,
   0.15348382  ,-0.1411449   ,-0.15004271  ,-0.070018284 , 0.03560643  ],
 [-0.14223528  , 0.08419781  ,-0.1512566   ,-0.07744099  ,-0.07823007  ,
   0.024501381 , 0.18819445  ,-0.05065412  , 0.12592499  , 0.2934639   ],
 [-0.03410621  ,-0.4757766   , 0.01787961  , 0.043727532 , 0.12577681  ,
  -0.0724179   , 0.12496178  ,-0.013366735 , 0.17155406  ,-0.623931    ],
 [ 0.11630688  ,-0.016617151 , 0.024926193 , 0.19697717  , 0.20378967  ,
   0.124955304 , 0.03991137  , 0.43021655  , 0.020616729 , 0.19588973  ],
 [ 0.0042666793,-0.20261641  ,-0.18012945  , 0.1664349   ,-0.06093503  ,
  -0.12836719  , 0.13282709  , 0.090783074 ,-0.033721108 , 0.28472814  ],
 [-0.04146926  , 0.0010757837, 0.037793756 ,-0.040455684 ,-0.098362595 ,
   0.09685327  , 0.1801239   ,-0.14500387  ,-0.04973326  , 0.16091383  ],
 [-0.1506926   ,-0.15413633  ,-0.12200291  ,-0.11093018  , 0.23156074  ,
  -0.09846549  , 0.11623625  , 0.36527735  , 0.19655998  ,-0.46961376  ],
 [-0.056351837 ,-0.15870485  , 0.10797198  , 0.15524647  ,-1.90224     ,
   0.0016923806, 0.33310127  , 0.020001544 , 0.090064175 ,-0.06316111  ],
 [ 0.01755327  , 0.011001605 ,-0.10069535  , 0.12418659  , 0.17351368  ,
  -0.098726295 ,-0.011526823 ,-0.25147715  , 0.31447387  ,-0.027267229 ],
 [ 0.016877076 ,-0.07742244  ,-0.18255754  ,-0.07766327  , 0.14406575  ,
   0.0068394355, 0.13510302  , 0.11707918  , 0.08899353  , 0.07129017  ],
 [-0.12439444  , 0.037189975 , 0.09368748  ,-0.041940983 ,-0.020631215 ,
  -0.12587109  ,-0.060097266 ,-0.009240462 , 0.15848702  , 0.18548468  ],
 [ 0.07409267  ,-0.019005582 , 0.13207234  ,-0.0674154   ,-0.03754154  ,
   0.5707095   ,-0.20832436  ,-0.05863251  ,-0.17941414  , 0.18015969  ],
 [-0.14765203  ,-0.0019972143,-0.046897262 , 0.13769487  , 0.029477851 ,
  -0.124431424 ,-0.0031819697, 0.0044115256, 0.1307983   ,-0.23662157  ],
 [ 0.17383306  ,-0.10536244  , 0.09282208  , 0.12146948  ,-0.027050452 ,
  -0.16364425  , 0.06655897  , 0.047648013 , 0.04487364  ,-0.05453375  ],
 [ 0.02551838  , 0.19852826  , 0.042067584 , 0.07808086  ,-0.13167073  ,
  -0.057023425 , 0.14794226  , 0.14404796  , 0.04197875  ,-0.006933985 ],
 [ 0.24201606  , 0.0182873   , 0.16604115  ,-0.016940078 , 0.03781893  ,
   0.03153096  ,-0.13984202  ,-0.007506358 , 0.07256791  , 0.011276118 ],
 [-0.16330083  , 0.03533584  ,-0.08417515  , 0.018262088 ,-0.16311394  ,
  -0.043594882 , 0.111150555 ,-0.1674053   , 0.115125716 , 0.1914532   ],
 [ 0.2510564   ,-0.14398938  , 0.050914355 , 0.0028924455,-0.0016518799,
   0.02297207  ,-0.10492008  , 0.16191866  , 0.12656751  , 0.12421195  ],
 [ 0.09892611  , 0.22227784  ,-0.15806703  ,-0.12372758  , 0.27543086  ,
   0.17699865  , 0.24796055  , 0.0943613   ,-0.011560572 ,-0.09149542  ],
 [ 0.06980075  , 0.14411032  ,-0.17246585  , 0.04535922  , 0.15614344  ,
   0.105321884 ,-0.34534395  , 0.124320105 , 0.04078385  ,-0.0005699365],
 [-1.3262403   ,-0.05813475  , 0.15976578  ,-0.16718878  , 0.10677123  ,
  -0.18618107  ,-0.12866488  , 0.08260146  ,-0.038657296 ,-0.08963758  ],
 [-0.13600755  , 0.05977911  ,-0.103125654 ,-0.22304308  ,-0.119611956 ,
   0.03866936  , 0.1457249   , 0.13547024  , 0.18912102  ,-0.16995506  ],
 [ 0.031950664 , 0.036799908 , 0.19924185  , 0.020978134 ,-0.15838917  ,
   0.0030810968,-0.049869608 ,-0.009953191 ,-0.053615794 ,-0.010398078 ],
 [ 0.068036914 , 0.21134038  , 0.2148867   , 0.059576936 ,-0.17996427  ,
   0.15595114  , 0.008232196 ,-0.07833171  , 0.16426116  ,-0.10827174  ],
 [ 0.069434114 , 0.004515622 , 0.1475982   , 0.12658383  ,-0.10403232  ,
  -0.008214444 ,-0.15171716  , 0.07594173  ,-0.08022391  , 0.03929981  ],
 [ 0.097895294 , 0.2156698   ,-0.028288012 ,-0.12441606  , 0.037518464 ,
  -0.12703685  ,-0.029692562 , 0.15575571  , 0.0746739   ,-0.050470043 ],
 [ 0.0078028566, 0.031353377 , 0.24276543  , 0.18884502  , 0.1152914   ,
  -0.13677871  ,-0.14385152  ,-0.19850993  , 0.30882645  ,-0.097649276 ],
 [-0.16809829  , 0.050116986 ,-0.15895891  , 0.07793018  ,-0.013172007 ,
   0.017337183 , 0.13639775  ,-0.061578672 , 0.026496977 ,-0.17645195  ],
 [-0.11465938  ,-0.17323233  ,-0.1582129   ,-0.09778342  , 0.10998887  ,
  -0.14019664  , 0.18239717  , 0.1801939   , 0.08183651  , 0.0033356994],
 [ 0.061703943 ,-0.008247313 ,-0.08260815  ,-0.14701676  , 0.11220814  ,
   0.021782827 , 0.14404719  , 0.3325449   ,-0.17851579  , 0.118550636 ],
 [-0.14613976  , 0.06490287  , 0.03549047  ,-0.18885452  ,-0.05647644  ,
  -0.070293024 , 0.192147    , 0.03823673  , 0.11766158  , 0.24402052  ],
 [ 0.081355385 ,-0.19124106  ,-0.018232921 , 0.06404845  ,-0.15914387  ,
  -0.14128211  , 0.0821313   , 0.037586354 , 0.060007643 , 0.009144118 ],
 [-0.13517499  ,-0.045327812 , 0.07033     , 0.112546645 ,-0.19718324  ,
   0.18961714  , 0.067056194 ,-0.09121062  ,-0.044356164 ,-0.07215563  ],
 [-0.13561131  , 0.14392766  ,-0.5173176   ,-0.1406488   ,-0.06293606  ,
  -0.04241642  , 0.08304559  ,-0.05484852  ,-0.022347536 , 0.14074261  ],
 [-0.7697802   , 0.18710901  ,-0.10670795  ,-0.15477362  , 0.2475592   ,
   0.1182363   , 0.12391859  , 0.027477467 ,-0.04288049  , 0.020820754 ],
 [-0.18045029  , 0.018289335 ,-0.058161493 , 0.054377835 , 0.17009175  ,
  -0.09424813  , 0.071126334 ,-0.04869051  , 0.1661114   ,-0.040856794 ],
 [ 0.07193331  ,-0.33296722  ,-0.19616595  , 0.15987878  ,-0.19828516  ,
  -0.15400374  , 0.066875376 , 0.19406821  , 0.057298902 ,-0.10152041  ],
 [-0.55153435  , 0.08200924  , 0.16548365  , 0.10930418  , 0.05184392  ,
  -0.07230887  , 1.0386854   , 0.0072258944, 0.01838425  ,-0.14798042  ]])
pesoCamada1 = np.array ([ 0.00574899  ,-0.6159712   ,-0.05956015  ,-0.022665476 , 0.0013211644,
 -0.0033788008, 0.03142346  , 0.017755795 ,-0.0046523814,-0.0393332   ])
camada2 = np.array ([[ 0.07495359 ],
 [ 0.065080084],
 [ 0.1918767  ],
 [ 0.17638625 ],
 [ 0.016440336],
 [-0.17054099 ],
 [ 0.15792824 ],
 [ 0.17208068 ],
 [ 0.15634793 ],
 [ 0.1668728  ]])
pesoCamada2 = np.array ([-0.028416945])
pesoDama = 1.842248124903451

my_color = input()  # r or b
print (my_color, file=sys.stderr)

# game loop
while True:
    listaLinhas = []
    for i in range(8):
        input_line = input()  # board line
        listaLinhas.append (input_line)
        
    tabuleiro = converteInputParaTabuleiro (listaLinhas, copy.deepcopy(my_color), 9)
    
    melhorMovimento = -10
    jogadaSelecionada = ""
    primeiroMovimento = True
    
    timeStart = time.time()
    legal_moves = int(input())  # number of legal moves
    for i in range(legal_moves):
        move_string = input()  # move
        print (move_string,  file=sys.stderr)
        jogadas = converteJogadaParaInputDoTabuleiro (move_string)
        tabuleiroNovo = fazJogada (tabuleiro, jogadas, copy.deepcopy(my_color))
        if (primeiroMovimento):
            jogadaSelecionada = move_string
            primeiroMovimento = False
        
        if (tabuleiroNovo == None):
            print("Erro no movimento!!", file=sys.stderr)
            tabuleiro.printaTabuleiro ()
            print(move_string, file=sys.stderr)
            continue
        
        alpha = -9999999999
        beta =  9999999999
        
        scoreTabuleiro = calculaScoreTabuleiroMedia (copy.deepcopy(tabuleiroNovo), 1, False)
            
        print(str(scoreTabuleiro), file=sys.stderr)
        
        if (scoreTabuleiro > melhorMovimento):
            melhorMovimento = scoreTabuleiro
            jogadaSelecionada = move_string
            
    print (jogadaSelecionada)