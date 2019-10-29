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
    
camada0 = np.array ([[ 0.14107223   ,-0.19814566   , 0.116574936  , 0.09732784   ,
   0.03688879   , 0.10274725   ,-0.6614686    , 0.0007789451 ,
  -1.1853743    ,-0.24830541   ,-0.31360698   ,-0.14470427   ,
   0.1427243    , 0.08865603   , 0.05849993   , 0.6988936    ,
   0.18594265   ,-0.07362624   ,-0.15806295   ,-0.055811103  ,
  -0.061678227  ,-0.4125911    ,-0.13594614   , 0.04511187   ,
   0.04707659   ,-0.16623946   ,-0.01452949   , 0.15916502   ,
  -0.14392833   ,-0.034108233  ,-0.05458294   ,-0.03759648   ,
  -0.80333316   , 0.04353637   ,-0.033283964  ,-0.93502426   ,
   0.15214945   , 0.33313558   , 0.28995505   , 0.12786987   ],
 [-0.03594903   , 0.07686409   ,-9.497942     ,-0.08574625   ,
  -0.059244923  , 0.14901048   , 0.044035986  , 0.024632547  ,
   0.11440686   , 0.1477402    , 0.053381797  ,-0.15545866   ,
  -0.19440469   ,-0.13693798   ,-0.037737045  ,-0.082531005  ,
   0.106225535  , 0.071439125  ,-0.16698971   ,-0.1736421    ,
  -0.03973637   ,-0.057099804  ,-0.22696811   , 0.021351269  ,
  -0.020559996  ,-0.66226375   , 0.038639907  ,-0.0012869386 ,
   1.1991588    , 0.083486415  , 0.22215076   , 0.018772492  ,
  -0.15420026   , 0.29940554   ,-0.12875448   ,-0.1256062    ,
   0.034823414  ,-0.23197669   , 0.28196588   ,-0.9648923    ],
 [ 0.29624107   , 0.013546455  , 0.09283515   ,-0.113110356  ,
  -0.06060057   , 0.15570723   , 0.08155762   , 0.19410703   ,
   0.16427644   ,-0.0068202424 , 0.20953459   ,-0.20298281   ,
   0.078345895  ,-2.7966607    ,-0.3347799    , 0.03904332   ,
   0.12551995   , 0.03808828   , 0.09028665   ,-0.11898662   ,
  -0.060659193  , 0.09102131   ,-0.1810974    , 0.06677631   ,
   0.19721219   , 0.17628673   , 0.0021277163 , 0.17833576   ,
  -0.024324212  ,-0.23639338   ,-2.0235295    , 0.013727717  ,
  -0.009647918  , 0.1899576    ,-0.20520902   , 0.0036702089 ,
   0.065649025  , 0.0030105088 , 2.8558304    ,-0.13953196   ],
 [ 0.113313474  , 0.40971586   , 0.12524413   , 0.18974921   ,
  -0.06341849   , 0.47962323   ,-0.039226167  ,-0.01242201   ,
  -0.020214466  ,-0.13876612   ,-0.09884141   ,-0.099076495  ,
   0.0036325525 ,-0.08273108   , 0.09227006   ,-0.08319837   ,
   0.021795368  , 0.043676205  , 0.05493827   ,-0.28639296   ,
  -0.10652497   ,-0.10931112   , 0.3269557    , 0.09245354   ,
   0.09706084   , 0.07571743   , 0.5877838    , 0.08687554   ,
  -0.12829395   ,-0.073815376  ,-0.064047925  , 0.25827134   ,
   0.32026595   ,-0.15185228   , 0.1375537    ,-0.28268835   ,
   0.09681842   , 0.20827371   ,-0.17499807   ,-0.10237251   ],
 [ 0.06564811   ,-0.009063546  ,-0.10882563   ,-0.017164528  ,
   0.0787355    , 0.09098158   ,-0.29768115   ,-0.008116519  ,
  -0.0058305864 ,-0.03420948   ,-0.13516045   ,-0.18483281   ,
   2.2259436    , 0.13290039   , 0.29318306   ,-0.81997544   ,
  -0.1894259    ,-0.14979474   , 0.2476633    , 0.13985756   ,
  -0.22958942   ,-0.064639375  ,-0.002796258  , 0.090837546  ,
   0.10194416   , 0.11854888   , 0.105510786  ,-0.08518455   ,
  -0.028008655  , 0.09969289   , 0.13011654   ,-0.078474484  ,
   0.17392562   ,-0.1672359    ,-0.22302675   ,-0.03510385   ,
   0.31034306   ,-0.023254404  , 0.05197815   ,-0.18224312   ],
 [ 0.26579854   , 0.09375411   , 0.019206265  , 0.08527597   ,
   0.25425133   , 0.08088931   , 0.21817239   ,-0.18678716   ,
  -0.187001     , 0.55058134   , 0.075867705  ,-0.186048     ,
   0.085080504  ,-0.086809     ,-0.04374536   , 0.22067457   ,
   0.05781003   ,-0.1425404    ,-0.01889717   , 0.12787357   ,
   0.019865355  , 0.114468046  ,-0.9498354    ,-0.024595225  ,
  -0.061786536  ,-0.06893669   , 0.5495629    , 0.16976562   ,
   0.4692071    ,-0.13011801   , 1.2979302    , 0.077271774  ,
  -0.39196566   ,-0.35171932   ,-0.077990614  , 0.02465209   ,
  -0.121520884  , 0.09419722   , 9.937481     ,-0.1592088    ],
 [-0.029632976  , 0.19797038   , 0.20277825   , 0.033182934  ,
  -0.09442622   ,-0.0409711    ,-0.19136581   , 0.2594488    ,
   0.020078447  ,-0.009644323  , 0.06801702   ,-0.027549788  ,
   0.042287078  , 0.030355595  , 0.12017598   , 0.14066847   ,
   0.021555703  , 0.12557648   , 0.053441446  , 0.14714693   ,
   0.0082693435 ,-0.058784954  , 0.04402193   ,-0.0570965    ,
  -0.2776971    ,-0.14448914   ,-0.11022654   ,-0.081945315  ,
   0.105444714  ,-0.18064995   , 0.0903057    , 0.12558576   ,
  -0.031195372  , 0.20434493   , 5.18215      ,-0.12888423   ,
   0.18164922   ,-0.3213057    , 0.13192153   ,-0.23165949   ],
 [-0.19263804   , 0.2034581    , 0.16564769   , 0.11519004   ,
  -0.011575751  ,-0.11208426   ,-0.16754003   , 0.09391268   ,
   0.15642694   ,-0.005119782  ,-0.18702626   , 0.15933502   ,
   0.12982783   ,-0.1648764    , 0.16879904   ,-0.040171422  ,
   0.02950602   , 0.08308045   , 0.13715309   ,-0.02902292   ,
   0.16067736   , 0.14523983   ,-0.20194796   , 0.11073182   ,
   0.025157137  , 0.52686757   ,-1.4442036    ,-0.17536603   ,
  -0.0130251    , 0.33417016   , 0.07307224   ,-0.0128526185 ,
  -0.066588685  , 0.10247953   , 0.027996656  ,-0.16026157   ,
  -2.012815     , 0.02435181   ,-0.10047986   , 0.04752684   ],
 [ 0.18873669   , 0.10306166   , 0.12350466   ,-0.11456104   ,
   0.034493137  ,-0.20421389   , 0.1346924    , 0.18568249   ,
  -0.18037936   , 0.18745136   , 0.14768945   ,-0.07341861   ,
   0.10673463   , 0.039182678  ,-0.12135391   , 0.019486813  ,
  -0.18175678   ,-0.17412677   ,-0.11866743   ,-0.2563832    ,
   0.17126805   , 0.08450821   , 0.069322616  ,-0.00956489   ,
  -0.10172908   , 0.2513378    , 0.10101086   , 0.07033245   ,
   0.054437645  , 0.042313013  ,-0.23973098   , 0.083294384  ,
   0.10722007   , 0.14040568   ,-0.19741829   ,-0.17331481   ,
   0.083703555  ,-0.11437003   ,-0.08248573   ,-0.45069805   ],
 [-0.025425693  , 0.217645     , 0.13460591   , 0.07610652   ,
  -0.085602164  ,-0.027937567  ,-0.11214696   ,-0.077777155  ,
  -0.12425041   , 0.08179396   ,-0.4553881    ,-0.07561323   ,
   0.12599882   ,-0.049133778  , 0.24603091   ,-0.17636071   ,
  -0.10078462   ,-0.17899568   , 0.032751493  , 0.19763273   ,
  -0.006005213  , 0.25720263   ,-0.2824278    ,-0.14056928   ,
   0.06908473   , 0.11575309   ,-0.1794069    , 0.15616205   ,
  -0.19418687   , 0.15230738   , 0.13751113   ,-0.077086955  ,
  -0.03444071   , 0.15833548   , 0.03100223   ,-0.03118761   ,
   0.14710037   , 0.092201926  , 0.50906336   ,-0.1843652    ],
 [ 0.16417244   , 0.0048985775 ,-0.19328055   , 0.28960142   ,
   0.006969848  , 0.11538068   , 0.17015837   , 0.18917091   ,
  -0.017114732  ,-0.07382797   ,-0.0966694    , 0.14256972   ,
   0.0012715294 ,-0.015848678  , 0.12262662   , 0.2215426    ,
  -0.62738      , 0.066322185  , 0.12377171   ,-0.1950401    ,
  -0.08124705   , 0.17230631   ,-0.16398092   , 0.09079531   ,
   0.11513106   , 0.06719691   ,-0.15361655   ,-0.066241115  ,
  -0.13518175   ,-0.14024812   , 1.8235161    ,-0.10762082   ,
  -0.05821882   ,-0.13746051   ,-2.483803     ,-0.04192793   ,
  -0.34853888   ,-0.15879256   , 0.2163604    ,-0.1256908    ],
 [-0.3375138    , 1.8528787    , 0.12797199   , 0.20555983   ,
  -0.022213966  , 0.085717306  ,-0.18180916   , 0.114051566  ,
   0.17159073   , 0.64482206   ,-0.029392153  , 0.08545526   ,
   0.07074868   ,-0.14609201   , 0.15437953   , 0.15507148   ,
   0.10532544   ,-0.07752006   ,-0.03082347   ,-0.051802233  ,
  -0.1830568    , 0.10751246   ,-0.19689408   ,-0.085953034  ,
  -0.1609925    , 0.123810366  ,-0.15796183   ,-0.03389245   ,
   0.03810626   , 0.18690048   , 0.19562964   ,-0.1838513    ,
   0.037658505  ,-0.1576604    ,-0.020822702  , 0.1796036    ,
  -2.3961458    , 0.12080119   ,-0.012192772  , 0.09120575   ],
 [-0.10482353   , 0.12538925   , 0.5692372    , 0.08673202   ,
   0.09026375   , 0.23310637   ,-0.014677896  , 3.934553     ,
  -0.6514293    , 0.17969579   , 0.059438936  ,-0.14099449   ,
   0.004428591  , 0.1658205    ,-0.10519256   ,-0.17169131   ,
   0.06312327   , 0.0973694    , 0.10470541   ,-0.12465919   ,
   0.08996864   ,-0.17424054   , 0.03250244   , 0.19171864   ,
  -0.32947198   ,-0.0803195    , 0.037674304  , 0.1710756    ,
  -0.0030609046 ,-0.15219964   , 0.017091926  , 0.02444116   ,
  -0.16968128   , 0.13526687   , 0.03102809   ,-0.057509463  ,
  -0.11118298   , 0.10689345   , 0.14884193   , 0.16547681   ],
 [ 0.0027709117 ,-0.026663603  ,-0.13880558   ,-0.01674718   ,
  -0.12753633   , 0.0941132    , 0.024548454  , 0.16348453   ,
   0.11819526   , 0.123774454  ,-0.12124001   , 0.076783605  ,
   0.032143015  ,-0.05153081   , 0.1130935    , 0.20500106   ,
   0.089565404  , 0.15848893   , 0.021304872  , 0.0016105718 ,
  -0.048227817  , 0.076950654  ,-0.29366332   ,-0.40789214   ,
  -0.023062928  ,-0.072849646  , 0.16770539   ,-0.11864461   ,
  -0.17089738   ,-0.010770644  , 0.055071697  ,-0.11732919   ,
   0.1660537    ,-0.095620714  , 0.11982651   , 0.024444247  ,
  -0.1114779    ,-0.089557864  ,-0.025783537  ,-0.13458388   ],
 [ 0.025648875  ,-2.3292117    ,-0.1332546    ,-0.11635583   ,
  -0.0024167118 , 0.15136641   , 0.06970355   , 0.573279     ,
  -0.14883795   , 0.023808947  ,-0.05944371   ,-0.06999464   ,
   0.016321544  ,-0.042133067  , 0.11296436   , 0.16989295   ,
   0.014466532  ,-0.16638407   , 0.037485592  , 0.10806142   ,
   0.05665788   ,-0.08999377   ,-0.10243166   , 0.031130897  ,
   0.03902224   ,-0.040942542  ,-0.13068907   , 0.16709594   ,
  -0.09877569   , 0.1742818    ,-0.66361004   ,-0.068813704  ,
  -0.06522386   , 0.15380171   , 0.008898989  ,-0.028794143  ,
  -0.12622926   , 0.0792454    ,-0.10941009   ,-0.14725672   ],
 [-0.02392956   , 0.15539177   ,-0.17303066   ,-0.026933672  ,
  -0.19734284   ,-0.034934096  ,-0.055136062  , 0.17531012   ,
   0.062574595  , 0.100976154  ,-0.16429503   , 0.009993064  ,
  -0.3927216    , 0.11419509   ,-0.09857527   , 0.049521506  ,
  -0.16617444   , 0.108991295  , 0.2116719    ,-0.09784683   ,
   0.036129136  ,-0.30163175   , 0.014527448  ,-0.18095902   ,
   0.1426386    , 2.5647423    ,-0.35638997   , 0.05884064   ,
   0.0992362    , 0.13408333   , 0.19465433   , 0.06331735   ,
  -0.030045971  , 0.27835193   , 0.1576368    ,-0.011293122  ,
  -0.0666125    , 0.049803663  , 0.16397417   , 0.05148874   ],
 [ 0.03383845   , 0.0764049    ,-1.181334     ,-0.17588232   ,
   0.028613465  ,-0.04640632   , 0.09317352   ,-0.038629003  ,
  -0.026074067  , 0.13453016   ,-0.012818855  , 0.109736554  ,
   0.037494462  ,-0.24299166   ,-0.054210577  ,-0.17523713   ,
  -1.3369958    ,-0.008221274  ,-0.117762834  , 0.6068954    ,
   0.10477422   ,-0.05575448   ,-0.13737084   ,-0.040488232  ,
  -0.010749508  , 0.093947865  ,-0.13026395   ,-0.030231904  ,
   0.18418418   ,-0.15470842   ,-0.088147834  , 1.7194247    ,
  -0.017574633  , 0.021006498  , 0.0075156437 , 0.113127366  ,
  -0.24931316   ,-0.11614823   , 0.16052273   , 0.01909987   ],
 [ 0.19528662   , 0.37114698   ,-0.12379083   , 0.05286138   ,
  -0.08876327   ,-0.11390763   , 0.010504616  , 0.2617667    ,
  -0.010393898  ,-0.16877067   , 0.041940574  , 0.18033904   ,
  -0.0040606833 , 0.25272423   ,-0.027207542  ,-0.0116162095 ,
   0.049783405  , 0.2800017    , 0.17897947   ,-0.070313826  ,
  -0.06299118   ,-0.11478541   , 0.22877774   , 1.1373991    ,
  -0.07213305   ,-0.008371345  , 0.03237671   ,-0.078282     ,
   0.0011725262 ,-0.09999801   , 2.7176392    , 0.46091816   ,
  -0.07082725   ,-0.2800671    ,-0.39449495   ,-0.82394606   ,
   0.005786303  ,-0.113458835  , 0.20281318   , 0.045813218  ],
 [ 0.3548876    , 0.06525448   ,-0.00017280527, 0.003565663  ,
  -0.8029397    ,-0.46155983   ,-0.00685797   ,-0.16996138   ,
  -0.2104811    ,-0.14083871   ,-0.15325664   ,-0.041452613  ,
   0.13271177   , 0.22622104   ,-0.72045636   , 0.6530096    ,
   0.4598163    , 0.089734     ,-0.10671037   ,-0.08340286   ,
  -0.006773103  ,-0.13188255   , 0.08410327   , 0.14535901   ,
   0.074356414  , 0.16711195   ,-0.16624221   , 0.18260248   ,
   0.18851712   ,-0.05958294   ,-0.010807683  ,-0.082579     ,
  -0.4615745    , 0.008043858  , 0.08127763   ,-0.13116322   ,
  -0.1414147    ,-0.20331562   , 0.18734616   ,-0.024404515  ],
 [ 0.060499236  ,-0.1750283    , 0.0764448    , 0.39356932   ,
  -0.15796249   , 0.11438368   ,-1.9297122    ,-0.12754437   ,
  -0.18055709   , 0.056369465  ,-0.031860538  , 0.18005055   ,
  -1.2867609    , 0.037465937  , 0.13132092   , 0.05285639   ,
  -0.00016060186, 0.040540386  ,-0.13801175   ,-0.13087095   ,
  -0.06525128   ,-0.060617514  ,-0.14379312   , 0.10561528   ,
   0.07643475   , 0.1850899    ,-0.04239681   , 0.08067874   ,
  -0.1627718    , 0.102049     , 0.28067172   ,-0.10151072   ,
   0.1330485    ,-1.1998328    ,-0.1233464    , 2.2019966    ,
  -0.07574721   , 0.13941726   , 0.12713966   , 0.8725293    ],
 [ 0.14235605   , 0.056768343  ,-0.15023233   ,-0.17925641   ,
   0.16607936   , 0.16724445   , 0.08574945   ,-0.010820684  ,
  -0.063459285  , 0.14918837   ,-0.018432071  , 0.12850018   ,
  -0.13714807   , 0.00444445   , 0.12652121   , 0.16189203   ,
   0.08895042   , 0.16004863   ,-0.017964765  ,-0.008185454  ,
  -0.2556204    ,-0.041834194  , 0.23009378   , 0.096214175  ,
   1.0996976    , 0.79619825   ,-0.005605397  , 0.15685731   ,
   0.060229454  ,-0.066533715  , 0.19230397   , 1.0347236    ,
   0.14320497   , 0.047860906  ,-0.25972617   , 0.15888608   ,
   0.015172008  ,-0.083246164  ,-0.16505556   ,-0.011763918  ],
 [ 0.21104623   ,-1.2293215    ,-0.16042106   ,-0.0036356156 ,
  -0.17306316   , 0.07654551   ,-0.11275869   , 0.135114     ,
   0.058836583  ,-0.18275805   ,-1.6439488    ,-0.16802642   ,
   0.09969692   ,-0.18887201   , 0.08194083   ,-0.04421734   ,
  -0.18391638   ,-0.01832808   , 0.112790965  ,-0.13991039   ,
   0.06849732   , 0.24369521   , 0.010977649  , 0.13157389   ,
   0.11974307   , 0.22208774   , 2.3906       ,-0.13235003   ,
   0.42264536   , 0.011859903  ,-0.18584646   , 1.76154      ,
   0.38163313   , 0.04242015   ,-0.06750006   ,-0.21798657   ,
   0.15709484   ,-0.19334528   ,-0.03741848   , 0.0561548    ],
 [ 0.34312925   , 0.15306972   ,-0.1584645    ,-0.19618404   ,
  -0.020143837  , 0.21878974   ,-0.048539456  ,-0.13869219   ,
  -0.14774886   , 0.13695496   , 0.14097029   ,-0.1550571    ,
   0.19687533   ,-0.2821555    , 0.019913632  , 0.07674533   ,
   0.82934403   , 0.024315031  , 0.18836902   , 0.06845444   ,
   0.26218837   , 0.011117733  ,-0.09867415   , 0.16225018   ,
  -0.14327373   , 0.07752082   , 0.83888644   , 0.09998476   ,
  -0.12689547   , 0.042926356  ,-0.35869703   ,-0.050690543  ,
   0.08514639   , 0.03353057   , 0.48155203   , 0.1890761    ,
  -0.15720017   ,-0.3337017    , 0.09850406   , 0.13798691   ],
 [ 0.11553137   ,-0.020959344  ,-0.14491673   ,-0.1505938    ,
  -0.056428578  , 0.48205453   ,-0.11091145   , 1.9938385    ,
  -0.8117735    , 0.09625217   , 0.4388541    , 0.15023114   ,
   0.063922435  , 0.03049455   ,-0.20696339   ,-0.1077127    ,
  -0.2232925    , 0.12264497   ,-0.10178804   , 0.14113204   ,
  -0.02407181   ,-0.07793571   ,-0.13373226   , 0.16250269   ,
  -0.11443986   ,-0.14576368   , 0.17724556   , 0.14031568   ,
  -0.17061453   ,-0.18972026   , 0.10036789   ,-0.1753525    ,
   0.040448654  , 0.14891191   ,-0.10216729   , 0.067078926  ,
  -0.08221863   , 0.15297236   , 0.16100377   , 0.03941834   ],
 [ 0.0024134694 , 0.19437766   , 0.012107341  ,-0.013482737  ,
   0.061979417  , 0.519479     , 0.083635226  , 0.3333666    ,
  -0.035992097  ,-0.48169813   , 0.07069563   , 0.031002697  ,
  -0.002250193  , 0.08647954   , 0.19470367   , 0.09519415   ,
  -0.054745056  ,-0.23155001   , 0.19093038   ,-0.07953311   ,
  -0.0396654    , 0.01642002   , 0.18893181   ,-0.0926307    ,
  -0.1174551    ,-0.87348187   ,-0.101292014  , 0.16518371   ,
  -0.12340744   , 0.33290324   ,-0.16252594   , 0.11580151   ,
   0.11279486   , 0.13274679   ,-0.16961516   ,-0.16158508   ,
   0.16320711   , 0.047565646  ,-0.14121075   , 0.16093302   ],
 [ 0.062381748  , 0.09860128   , 0.046322376  , 0.17747797   ,
  -0.11558997   ,-0.11754408   , 0.06626628   , 0.11696077   ,
  -0.14674443   ,-0.0021258364 , 0.22243969   ,-0.005246708  ,
  -0.18527089   ,-1.3543764    ,-0.067375004  ,-0.17499916   ,
  -0.026408084  , 0.15203488   , 0.088873625  , 0.16614603   ,
   0.13618417   ,-0.13943022   ,-0.053838853  ,-0.16441914   ,
  -0.36878303   , 0.12980877   , 0.112126164  ,-0.03063859   ,
  -0.09978481   ,-0.20356457   , 0.09060916   , 0.40168932   ,
  -0.46681023   ,-0.12572476   , 0.054614674  ,-0.22349806   ,
   0.06159024   ,-0.060424574  , 0.10483732   , 0.09317272   ],
 [ 0.014591284  ,-0.075629756  ,-0.41353804   , 0.025449665  ,
  -0.10995634   ,-0.0649951    ,-0.19412448   ,-0.04633596   ,
   0.087274745  , 0.09981712   , 0.16143173   ,-0.07470991   ,
  -0.1547481    ,-0.024944289  , 0.5533056    , 0.24148694   ,
  -0.018153079  , 0.18795109   , 0.12410992   ,-0.016645797  ,
  -0.16150637   ,-0.058272734  ,-0.090037376  ,-0.011969212  ,
  -0.7171085    , 0.46699145   ,-0.017767351  , 0.6788755    ,
   0.10593508   ,-0.2693286    , 0.13145433   , 0.14244847   ,
  -0.18273567   ,-0.18038256   , 0.38271943   ,-0.20431082   ,
   0.12561858   , 0.2583075    , 0.13509996   ,-0.12353872   ],
 [-0.013555443  ,-0.045127682  , 0.18939883   , 0.17745829   ,
  -0.08761399   ,-0.11089437   ,-0.122452684  ,-0.12837143   ,
   0.14007618   ,-0.17610691   ,-0.10472936   , 0.12994082   ,
   0.16318971   ,-0.008531534  , 0.14560013   ,-0.1074875    ,
   0.22594272   , 0.2007454    ,-0.024044644  , 0.019823859  ,
  -0.19775838   , 0.28280723   , 0.2677415    , 0.11264382   ,
  -0.065889314  , 0.43398362   , 0.07490513   , 0.16942313   ,
   0.11580358   ,-0.08920993   ,-0.1652273    , 0.16762953   ,
   0.030106766  , 0.31407472   , 0.07859837   ,-0.08815946   ,
   0.0993064    , 0.44459647   ,-0.056711018  , 0.14304407   ],
 [-0.10186382   ,-0.20890924   ,-0.016545108  ,-0.0751979    ,
  -0.1400408    , 0.21670392   , 0.03849845   , 0.029714461  ,
   0.122405164  ,-0.0003015067 ,-0.037353314  , 0.07531357   ,
  -0.6110356    ,-0.08808881   ,-0.1939581    , 0.16859864   ,
   0.1718262    , 0.21843088   , 0.101946004  , 0.17364103   ,
   0.055847626  , 0.025363976  ,-0.21461177   ,-0.16006272   ,
   0.20455119   ,-0.13880113   , 0.17570099   , 0.11011891   ,
   0.09819117   , 0.16753797   ,-0.0071481154 ,-0.09041693   ,
  -0.060169943  , 0.07144626   , 0.09724085   , 0.21296819   ,
  -0.039729577  , 0.14063406   , 0.06352723   ,-0.119655095  ],
 [-0.07750776   , 0.062309556  , 0.060076833  ,-0.09145665   ,
   0.114653766  , 0.38114098   , 0.17559943   , 0.118733205  ,
  -0.18453346   ,-0.14197266   ,-0.18041395   , 0.18556565   ,
   0.07587036   ,-1.9661418    ,-0.595284     ,-0.06766111   ,
   0.10690835   , 0.05244133   , 0.18004893   ,-0.19317798   ,
   0.15244381   ,-0.12250682   ,-0.18040083   ,-0.092354305  ,
   0.10142599   ,-0.059144102  ,-0.16619614   ,-0.07993993   ,
   0.047882896  ,-0.032652184  , 0.1791116    , 0.26469097   ,
  -0.024197327  , 0.086169966  ,-0.18863335   , 0.09502961   ,
  -2.8696115    ,-0.16761442   , 0.42540565   , 0.06528912   ],
 [-0.1563787    ,-0.14755446   ,-0.4324864    ,-0.045708526  ,
   0.123549476  , 0.1935908    , 0.08734626   ,-0.051594142  ,
   0.28713354   , 0.07716587   , 0.13841328   ,-0.2564703    ,
   0.100466244  ,-0.10738736   , 0.06996277   , 0.09391453   ,
   0.20313181   ,-0.026110403  , 0.16114162   , 0.111248076  ,
   0.083867244  , 0.0032833524 ,-0.15338689   , 0.13680781   ,
  -0.19283712   , 0.11787554   ,-0.16880725   , 0.09084978   ,
   0.13996308   , 0.4602536    ,-0.01206962   , 0.15365633   ,
   0.089141175  , 0.20973405   ,-0.16419676   ,-0.083436355  ,
   0.013830783  ,-0.4965611    ,-0.14482427   , 0.114663295  ],
 [ 0.09885167   ,-0.088890985  ,-0.1529446    , 0.11846444   ,
  -0.11655191   ,-0.23607638   , 0.11657887   ,-0.08892057   ,
   0.18327233   , 0.053836856  , 0.12776622   ,-0.08507921   ,
  -0.05437944   ,-0.055353887  , 0.09106353   , 0.08643264   ,
   0.015676774  , 0.008647775  ,-0.10076623   ,-0.14337464   ,
  -0.18402071   , 0.04791574   ,-0.0022321485 , 0.016738635  ,
   0.6419747    , 0.20776606   ,-0.194525     , 0.02481427   ,
   0.073438264  , 0.44072545   , 0.25123766   , 0.06753751   ,
   0.017506193  ,-0.12508035   , 0.11761499   ,-0.17025518   ,
   0.16039334   ,-0.029834095  , 0.16406849   ,-0.19667587   ]])
pesoCamada0 = np.array ([-0.0014282183 , 0.0075588594 , 0.04557969   ,-0.0017753531 ,
 -0.06452112   , 0.00043079286,-0.049573008  , 0.19852245   ,
 -0.00690507   ,-0.120582126  ,-0.008209909  , 0.094723046  ,
 -0.024083927  ,-0.023818977  ,-0.042911183  ,-0.13088848   ,
  0.01106074   ,-0.006749072  ,-0.026581332  , 0.04582808   ,
 -0.086073816  ,-0.00275211   ,-5.147911     , 0.015309149  ,
 -0.014480305  ,-0.0065003135 , 0.013843258  ,-0.0012960042 ,
 -0.01804154   ,-0.008422312  , 0.010246101  ,-0.011150962  ,
  0.012687004  , 0.00010015376, 0.018688114  ,-0.006807766  ,
 -0.00084405404,-0.07480222   , 0.06603104   ,-5.511991     ])
camada1 = np.array ([[  0.028182847   ,  0.06361091    ,  0.14156592    ,  0.12820598    ,
   -0.056932077   ,  0.10380517    , -0.18113853    ,  0.20962468    ,
   -0.14456114    ,  0.089588344   ],
 [  0.11899205    ,  0.08932249    , -0.29559204    ,  0.012745668   ,
    0.08894012    , -0.025572604   , -0.06533346    ,  0.05412807    ,
    0.07892879    ,  0.13546646    ],
 [  0.14642315    , -0.052064087   ,  0.07793656    , -0.011362378   ,
    0.1428069     ,  0.028951569   , -0.13503651    , -0.14042926    ,
   -0.0723048     ,  0.25218445    ],
 [ -0.14213046    ,  0.07814411    , -0.15428415    , -0.097557545   ,
   -0.077276506   ,  0.06429838    ,  0.2726567     , -0.05054106    ,
    0.17111856    ,  0.89448744    ],
 [  0.020555919   , -0.27294785    , -0.010740181   ,  0.29365602    ,
    0.16691945    , -0.1443504     ,  0.12961875    , -0.024399241   ,
    0.17282748    , -2.2235723     ],
 [  0.11706282    , -0.00808135    ,  0.024572337   ,  0.9730632     ,
    0.108740434   ,  0.12729256    ,  0.08086101    ,  0.49016303    ,
    0.02111065    ,  0.19200942    ],
 [  0.036975995   , -0.2017354     , -0.18061401    , -0.80249876    ,
   -0.061838485   , -0.12839307    ,  0.021159973   ,  0.08981189    ,
   -0.03657352    , -1.6563097     ],
 [ -0.039371885   ,  0.010640253   ,  0.034206565   , -0.03948822    ,
   -0.098156005   ,  0.51699275    ,  0.23845989    , -0.14837964    ,
   -0.050973907   ,  0.24830554    ],
 [ -0.19443452    , -0.15504673    , -0.12172418    , -0.11092299    ,
    0.24691862    , -0.09953228    ,  0.12116458    ,  0.4228176     ,
    0.14352275    , -1.7440578     ],
 [ -0.049118713   , -0.16012812    ,  0.1211608     ,  0.16345115    ,
   -1.1680096     , -0.15183698    , -0.33714092    , -0.05386796    ,
    0.19146003    , -0.024220351   ],
 [  0.15552542    ,  0.012944855   , -0.15135227    ,  0.13234073    ,
    0.1641081     , -0.10005143    ,  0.17266817    , -0.2890626     ,
    0.15943892    , -0.0117799835  ],
 [  0.0149202645  , -0.07995651    , -0.1675667     , -0.078425206   ,
    0.14386296    , -0.00535712    ,  0.10195323    ,  0.11527611    ,
    0.06381254    ,  0.07224317    ],
 [ -0.11475033    ,  0.04121915    ,  0.111379206   , -0.13211845    ,
   -0.027564697   ,  0.30472195    , -0.059675112   , -0.010364812   ,
    0.35332716    ,  0.18596427    ],
 [ -0.21489918    , -0.016064584   ,  0.052319307   , -0.06200749    ,
   -0.030103996   ,  1.9569764     , -0.20257764    , -0.066876516   ,
   -0.16525836    ,  0.19059001    ],
 [ -0.17968842    , -0.020458752   , -0.0930496     ,  0.13695161    ,
    0.4681242     , -0.07233376    , -0.012418275   ,  0.062177777   ,
   -0.05598322    , -0.37881032    ],
 [  0.18500412    , -0.10501827    ,  0.09321956    ,  0.0826156     ,
   -0.034747556   , -0.16766353    , -0.000067806206,  0.04596872    ,
   -0.0045649637  , -0.02612732    ],
 [  0.011235251   ,  1.0063297     ,  0.024029758   ,  0.08255202    ,
   -0.38194144    , -0.054964803   ,  0.17111178    ,  0.14482935    ,
    0.052417647   , -0.0765682     ],
 [  0.23792487    ,  0.10793349    ,  0.13298804    ,  0.001250916   ,
   -0.449461      ,  0.72405505    , -0.6267363     , -0.008279953   ,
    0.067887135   ,  0.014540129   ],
 [ -0.16008058    ,  0.042455442   , -0.08537136    ,  0.02323677    ,
   -0.14470024    , -0.037522025   ,  0.10552685    , -0.105553545   ,
    0.11470275    ,  0.18039761    ],
 [  0.34621003    , -0.24563588    ,  0.047791798   , -0.015257325   ,
   -0.0014930635  ,  0.5802175     , -0.10487626    ,  0.19016843    ,
    0.12461976    ,  0.12373672    ],
 [  0.09899107    ,  0.22097696    , -0.40669206    , -0.25439382    ,
    0.31379166    ,  0.17636134    ,  0.27348486    ,  0.0945415     ,
    0.005175835   , -0.18198402    ],
 [  0.038654756   ,  0.13718295    , -0.13236856    , -0.3598375     ,
    0.27010953    ,  0.19184688    ,  7.2366548     ,  0.13593674    ,
    0.0468088     , -0.30842152    ],
 [  1.6634264     , -0.057507016   ,  0.16548938    , -0.17214456    ,
    0.11084337    , -0.24921064    , -0.12990694    ,  0.07772387    ,
   -0.04484088    , -0.09563009    ],
 [ -0.15187389    ,  0.060153298   , -0.34253657    , -0.18322769    ,
   -0.117821164   ,  0.058797993   ,  0.120321594   ,  0.124609485   ,
    0.19179018    , -0.20555258    ],
 [  0.03230416    ,  0.03995883    ,  0.19869561    ,  0.021025699   ,
   -0.16737583    , -0.34785616    , -0.16472861    , -0.009746262   ,
   -0.06879695    , -0.03718492    ],
 [  0.06517225    ,  0.42197353    ,  0.17697658    ,  0.05303943    ,
   -0.12879644    ,  0.16089885    ,  0.0034778772  , -0.122702464   ,
    0.1634723     , -0.110589124   ],
 [  0.061271384   , -0.0065153986  ,  0.14685959    ,  0.13517334    ,
   -0.11093524    ,  0.11515722    , -0.16525894    ,  0.10101588    ,
   -0.09636752    ,  0.038690377   ],
 [  0.11158916    ,  0.18516946    , -0.033923045   , -0.08329038    ,
   -0.08082935    , -0.23746221    , -0.046946857   ,  0.06594277    ,
    0.06656628    , -0.05698861    ],
 [  0.007936199   ,  0.05096919    ,  1.8627595     ,  0.17270957    ,
    0.114756644   , -0.16080116    , -0.17832004    , -0.2004873     ,
    0.36257687    , -0.12543727    ],
 [ -0.12559485    ,  0.04959954    , -0.08092064    , -0.061225835   ,
    1.5956287     ,  0.10402442    ,  0.136537      , -0.06536928    ,
    0.017968234   , -0.38636515    ],
 [ -0.13072199    , -0.17090593    , -0.23381633    , -0.09575466    ,
    0.11470724    ,  0.4457513     ,  0.18984601    ,  0.18053164    ,
    0.27252918    ,  0.010261215   ],
 [  0.5387214     , -0.0072840904  , -0.06853777    , -0.14369743    ,
    0.101282135   , -0.1283935     ,  0.14551884    ,  0.47290522    ,
   -0.17419021    ,  0.11394306    ],
 [ -0.14709078    ,  0.08646929    ,  0.03552915    , -0.19190912    ,
   -0.05932755    , -0.060325682   ,  0.19394852    ,  0.0369009     ,
    0.104978845   ,  0.24633375    ],
 [  0.07526051    ,  0.8068411     , -0.039555166   ,  0.03766644    ,
   -0.1593147     , -0.16711159    ,  0.08409307    ,  0.03568989    ,
    0.06355005    ,  0.0028739704  ],
 [ -0.14108318    ,  0.03191136    ,  0.070127115   ,  0.11368964    ,
   -0.4068573     ,  0.21859299    ,  0.20336254    , -0.09088156    ,
   -0.059867833   , -0.072535686   ],
 [ -0.059475463   ,  0.14670776    , -1.2106378     , -0.15251514    ,
   -0.028210975   , -0.04923562    ,  0.08107296    , -0.026450416   ,
   -0.018867481   ,  0.13189732    ],
 [-37.84231       ,  0.1875618     , -0.26418906    , -0.27702534    ,
  -10.504692      ,  0.12822421    ,  0.13139527    , -0.7999185     ,
    0.13123204    , -0.049093213   ],
 [ -0.21911184    ,  0.048199255   , -0.06652796    ,  0.05263166    ,
    0.16778034    , -0.08621917    ,  0.07013375    , -0.04864577    ,
    0.1629834     ,  0.067955576   ],
 [  0.072908774   , -0.18573603    , -0.19206922    ,  0.16055825    ,
   -0.16663352    , -0.037625443   ,  0.057287257   ,  0.21144944    ,
    0.061710376   , -0.10090963    ],
 [ -0.61477405    ,  0.084007315   ,  0.1636227     ,  0.11023615    ,
    0.061242647   ,  0.1591133     ,  6.1033735     , -0.04004097    ,
    0.018119488   , -0.14474201    ]])
pesoCamada1 = np.array ([-0.015363132 ,-0.9434953   ,-0.04612717  ,-0.013849409 ,-0.010895005 ,
  0.012646056 , 0.032233123 ,-0.018088443 ,-0.0014758013,-0.089094244 ])
camada2 = np.array ([[ 0.019159624 ],
 [ 0.06302889  ],
 [ 0.18882304  ],
 [ 0.17616095  ],
 [ 0.0017609937],
 [-0.23380789  ],
 [ 0.20251517  ],
 [ 0.11378392  ],
 [ 0.14320041  ],
 [ 0.1671509   ]])
pesoCamada2 = np.array ([-0.030777458])
pesoDama = 3.0

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