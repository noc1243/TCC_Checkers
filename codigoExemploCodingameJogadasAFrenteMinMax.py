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

def calculaScoreTabuleiroMinMax2 (tabuleiro, numeroDaJogada, jogadorJogando):
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
    if (not jogadaForcada):
        numeroDaProximaJogada += 1 
            
    if (jogadorJogando):
        best = -1.1
    else:
        best = 1.1
            
    if (len (listaTabuleiros) == 0):
        if (jogadorJogando):
            return -1
        else:
            return 1
            
    for tabuleiro in listaTabuleiros:
        if (not tabuleiro is None):
            if (jogadorJogando):
                best = max (best, calculaScoreTabuleiroMinMax2 (copy.deepcopy(tabuleiro), copy.deepcopy(numeroDaProximaJogada), False))
            else:
                best = min (best, calculaScoreTabuleiroMinMax2 (copy.deepcopy(tabuleiro), copy.deepcopy(numeroDaProximaJogada), True ))
        
    return best
    
camada0 = np.array ([[ 0.12667081    , 0.044372432   , 0.12017042    , 0.09658249    ,
  -0.04732807    , 0.11584385    ,-0.11034691    ,-0.002851818   ,
   0.029074356   ,-0.14008878    ,-0.038905904   ,-0.13768706    ,
   0.1660671     ,-0.07682296    , 0.07342582    , 0.21235189    ,
   0.1669942     ,-0.06480736    ,-0.14517197    ,-0.054966595   ,
  -0.16050255    ,-0.04102643    ,-0.15112367    , 0.043701176   ,
   0.051728178   ,-0.17409405    , 0.010492812   , 0.11784592    ,
  -0.11422808    ,-0.013810243   ,-0.054077674   ,-0.046188205   ,
   0.124823526   , 0.009749984   ,-0.033178866   , 0.056119207   ,
   0.16632588    ,-0.44475037    , 0.16391505    , 0.11559754    ],
 [-0.038718414   , 0.065618955   , 0.16684715    ,-0.12692395    ,
   0.03758727    , 0.15520905    , 0.029418183   ,-0.0037296787  ,
  -0.114028305   , 0.13721131    , 0.04627786    ,-0.07602456    ,
  -0.14211936    ,-0.07394912    ,-0.035025235   ,-0.05168893    ,
   0.09520207    , 0.062369388   ,-0.16936977    ,-0.16911839    ,
   0.03696782    ,-0.059079863   ,-0.14522563    , 0.12000272    ,
  -0.026863297   ,-0.06679686    ,-0.06922667    ,-0.015364741   ,
   0.104006276   , 0.04201684    , 0.13697802    , 0.011655603   ,
  -0.13143264    , 0.22278437    ,-0.15097551    ,-0.13178341    ,
   0.044954866   ,-0.14965968    , 0.18167442    ,-0.1441043     ],
 [ 0.00418151    , 0.15895914    , 0.08326992    ,-0.11963314    ,
  -0.06485178    , 0.10371791    , 0.089381844   , 0.20103875    ,
  -0.020444287   ,-0.011724624   , 0.14604509    ,-0.20234606    ,
   0.043659266   ,-0.05094624    ,-0.17635019    , 0.038264297   ,
   0.12007461    , 0.0039552967  , 0.07251137    ,-0.104614824   ,
  -0.060499966   ,-0.00023080343 ,-0.19213457    , 0.06936196    ,
   0.19023655    , 0.15068272    , 0.013634357   , 0.13785458    ,
  -0.028694937   , 0.06262385    ,-0.141822      , 0.019063393   ,
  -0.016509688   , 0.12553592    ,-0.18732561    , 0.07579525    ,
   0.06729425    ,-0.0050646337  ,-0.028308466   ,-0.12593167    ],
 [ 0.28405568    ,-0.0317535     , 0.14960673    , 0.19173194    ,
   0.10371101    , 0.15895416    ,-0.057824627   ,-0.009884575   ,
   0.014451323   ,-0.30316466    ,-0.10739229    ,-0.08178853    ,
  -0.13794702    ,-0.112292714   , 0.0719562     ,-0.030957572   ,
   0.029350927   , 0.019014433   , 0.03987679    , 0.07322463    ,
  -0.12282953    ,-0.009718041   , 0.3251767     , 0.20092516    ,
   0.09725122    , 0.039291553   , 0.29171482    , 0.11157909    ,
   0.046975117   ,-0.074311525   ,-0.06935011    , 0.17799991    ,
   0.17490518    ,-0.1506765     , 0.15169251    ,-0.12343722    ,
   0.09703603    , 0.26446486    ,-0.1591125     ,-0.07477249    ],
 [ 0.052414164   ,-0.01299857    ,-0.09284448    ,-0.0050738784  ,
  -0.08772906    , 0.08982599    , 0.3252759     ,-0.010046774   ,
  -0.009784043   ,-0.03254849    ,-0.14417341    ,-0.20853575    ,
   0.06504591    ,-0.35969654    , 0.05707469    , 0.035974782   ,
  -0.35605967    ,-0.16211183    , 0.14086987    , 0.15225446    ,
  -0.1925406     ,-0.06317133    , 0.010650965   , 0.1744843     ,
   0.2631192     , 0.18452695    ,-0.0680266     ,-0.08227766    ,
   0.13932858    , 0.122144796   , 0.13509095    ,-0.08083757    ,
   0.16854447    ,-0.16845654    ,-0.2160789     , 0.03722605    ,
   0.29054922    , 0.016743926   , 0.12597407    ,-0.17974       ],
 [ 0.113560274   , 0.10586743    ,-0.07365451    , 0.074132904   ,
   0.24328716    , 0.07284718    , 0.058830082   ,-0.18275747    ,
  -0.19123548    , 0.1692365     , 0.08066474    ,-0.21556939    ,
   0.08362846    , 0.0092802225  ,-0.06292989    , 0.022794373   ,
   0.059087317   ,-0.148762      , 0.22794907    ,-0.18684718    ,
  -0.025557065   , 0.09869229    ,-0.13446635    ,-0.027976342   ,
   0.13865928    ,-0.05193192    , 0.13767372    , 0.13465773    ,
  -0.028611738   ,-0.12949584    , 0.3984561     , 0.11377561    ,
  -0.03186536    , 0.12757055    ,-0.06058014    ,-0.13646245    ,
  -0.13359448    , 0.14311066    ,-0.06786612    ,-0.07322852    ],
 [ 0.20159405    , 0.17433728    , 0.20211886    , 0.152213      ,
  -0.17656693    , 0.010816029   ,-0.1848303     , 0.15333359    ,
   0.011239563   ,-0.042537224   ,-0.052886594   ,-0.06592916    ,
  -0.08431459    , 0.0008021285  , 0.0030955872  , 0.12879992    ,
   0.013221826   , 0.07374533    , 0.050213557   , 0.036316987   ,
  -0.18496436    ,-0.059813824   , 0.06494335    ,-0.021217685   ,
  -0.0582439     ,-0.14598098    ,-0.110978834   ,-0.08923436    ,
   0.105372764   ,-0.21799156    , 0.07430536    , 0.122998066   ,
  -0.03895388    , 0.20128669    ,-0.046049096   ,-0.10226553    ,
   0.17796929    , 0.05787892    , 0.15288213    ,-0.10320003    ],
 [-0.1671653     , 0.2191195     ,-0.04594404    , 0.09436727    ,
   0.15938364    ,-0.11154201    , 0.1407818     , 0.035946485   ,
  -0.17155097    ,-0.038165156   ,-0.17501904    , 0.20193492    ,
   0.14520958    ,-0.1643536     , 0.1714695     ,-0.041482903   ,
   0.18101537    , 0.07803135    , 0.13689329    ,-0.13418007    ,
   0.16652277    , 0.13786763    ,-0.12778541    , 0.092595235   ,
   0.023871556   , 0.12407638    , 0.13818683    ,-0.17290217    ,
  -0.09170561    , 0.14736374    , 0.11856864    , 0.009896162   ,
  -0.18761756    , 0.10240411    ,-0.011842579   ,-0.0974715     ,
  -0.42761442    ,-0.053463116   , 0.04569238    , 0.052595355   ],
 [ 0.23386376    , 0.0925109     , 0.10082402    ,-0.12525584    ,
  -0.004003645   ,-0.1961134     , 0.14444771    , 0.17527205    ,
  -0.18049607    ,-0.15800078    , 0.15235592    , 0.019554544   ,
   0.11158842    , 0.039928745   ,-0.05262993    , 0.03933402    ,
  -0.17354038    ,-0.1673211     ,-0.1366012     ,-0.13344416    ,
   0.29342958    ,-0.246739      , 0.082571045   ,-0.0044074464  ,
  -0.108981594   , 0.14395751    , 0.13561043    , 0.072834186   ,
   0.063002266   , 0.04761495    ,-0.16363458    , 0.087486535   ,
   0.10619386    , 0.179979      ,-0.19926201    ,-0.18275039    ,
   0.09739212    ,-0.11699623    ,-0.16021545    , 0.046697013   ],
 [-0.02574379    , 0.5983646     , 0.13709772    , 0.009217733   ,
  -0.09403643    ,-0.032165576   ,-0.14254947    ,-0.078616954   ,
  -0.12551118    , 0.12581134    ,-0.2867156     ,-0.071446486   ,
   0.06831253    ,-0.06491685    ,-0.00767115    ,-0.17107135    ,
  -0.14595988    ,-0.17543791    , 0.055808224   , 0.034498524   ,
  -0.03995417    , 0.023861542   ,-1.2168238     ,-0.1485854     ,
   0.076950595   ,-0.044098727   ,-0.18787757    , 0.12664822    ,
  -0.2287557     , 0.13362236    , 0.11844809    ,-0.07668977    ,
  -0.031043362   , 0.15448157    , 0.030564386   ,-0.036185384   ,
   0.12820475    , 0.0719668     ,-0.047727693   ,-0.18787107    ],
 [ 0.18652602    ,-0.0020594953  ,-0.19458756    , 0.17985994    ,
   0.0137580745  , 0.12565793    , 0.16109148    , 0.17572273    ,
  -0.0766893     ,-0.070307285   ,-0.085438274   , 0.16501649    ,
   0.024883509   ,-0.0029492048  , 0.12208386    , 0.1795126     ,
  -0.09707716    , 0.07814858    , 0.2241242     ,-0.094645984   ,
   0.021936595   , 0.18037921    ,-0.1637094     , 0.07071954    ,
   0.116853006   , 0.09107295    ,-0.15376072    ,-0.120100625   ,
  -0.14024492    ,-0.13411805    , 0.1691686     ,-0.14366089    ,
  -0.022273477   ,-0.12809016    ,-0.17846145    , 0.010050346   ,
  -0.17372863    ,-0.11505685    , 0.20426105    ,-0.022428155   ],
 [-0.33231243    ,-0.2572289     , 0.12308297    , 0.118491605   ,
  -0.03665708    , 0.045761      ,-0.18712975    , 0.057381693   ,
   0.050594524   , 0.16232707    ,-0.09760749    , 0.09378711    ,
   0.0753885     ,-0.13476631    , 0.17186357    , 0.15216655    ,
   0.104203485   ,-0.030428413   ,-0.022673132   ,-0.05040103    ,
  -0.167734      , 0.042527743   , 0.0010458851  ,-0.10717874    ,
  -0.15757874    , 0.12141996    , 0.12221577    ,-0.03026951    ,
   0.042904098   , 0.06379208    , 0.1962787     ,-0.16189341    ,
   0.023422861   ,-0.15962154    ,-0.014730043   , 0.16814944    ,
  -0.2055557     , 0.13881645    ,-0.013511655   , 0.017269323   ],
 [-0.097298935   , 0.092653096   , 0.17713839    , 0.091208436   ,
   0.06542316    ,-0.13215998    ,-0.0406495     , 0.15336756    ,
   0.15512212    , 0.17669845    , 0.053971205   ,-0.14164974    ,
  -0.13748066    , 0.16680805    ,-0.09929672    ,-0.18505523    ,
   0.077130966   , 0.1197333     , 0.1025262     ,-0.0723178     ,
  -0.15147191    ,-0.15373813    , 0.0026885108  , 0.18264648    ,
  -0.17587186    ,-0.054829277   , 0.041851353   , 0.19382676    ,
  -0.061524563   ,-0.1450427     , 0.05731442    , 0.13137287    ,
  -0.17591926    , 0.061941378   , 0.009571911   ,-0.058313668   ,
  -0.10198756    , 0.08166891    , 0.15027583    , 0.16694811    ],
 [ 0.031664744   ,-0.023365455   ,-0.08562728    , 0.018616965   ,
  -0.18059753    ,-0.101099536   , 0.021434123   , 0.16912533    ,
   0.11844221    , 0.11478168    ,-0.12078997    , 0.0750059     ,
   0.039552066   ,-0.093917355   , 0.10959437    , 0.19855267    ,
   0.10715196    , 0.15332317    ,-0.09818806    ,-0.003175708   ,
  -0.04868751    , 0.046732318   ,-0.060193557   ,-0.22385749    ,
  -0.05874955    ,-0.076051004   , 0.16386405    ,-0.13097644    ,
  -0.19746384    ,-0.092159875   , 0.04992435    ,-0.11179869    ,
   0.16668446    ,-0.026986478   , 0.09425554    ,-0.04760052    ,
  -0.12567808    ,-0.08787814    ,-0.029811118   ,-0.20467332    ],
 [ 0.03296996    , 0.36046916    ,-0.15725692    ,-0.10981827    ,
   0.06438601    , 0.13915794    , 0.07417005    ,-0.050610438   ,
  -0.1266206     ,-0.0066290563  , 0.029300958   , 0.049500324   ,
   0.012829917   ,-0.047480404   , 0.12668513    , 0.25698444    ,
  -0.008133157   ,-0.16429175    ,-0.04785619    , 0.10716577    ,
   0.077415735   ,-0.08970068    ,-0.106338106   , 0.09285729    ,
  -0.016126536   ,-0.056866646   ,-0.15191416    , 0.13238975    ,
  -0.10691967    ,-0.056927245   ,-0.89255124    ,-0.071776584   ,
  -0.06894       , 0.06975175    , 0.0235463     ,-0.025114492   ,
  -0.1158029     , 0.085311666   ,-0.10985218    ,-0.1448312     ],
 [-0.035271462   , 0.054420114   ,-0.18886964    , 0.15772174    ,
  -0.13700648    ,-0.04070652    ,-0.19144446    , 0.1780981     ,
   0.11286351    , 0.10412576    ,-0.11096793    ,-0.000004400878,
  -0.08259737    , 0.1152136     ,-0.059772655   , 0.058831718   ,
  -0.17951985    , 0.09253334    ,-0.07358295    ,-0.08063845    ,
   0.04147975    ,-0.09007608    , 0.14255075    ,-0.18259738    ,
   0.14069422    , 0.099021554   ,-0.032386664   , 0.06534808    ,
   0.0944788     , 0.124298684   , 0.2176427     , 0.06451091    ,
  -0.008429532   , 0.099532865   , 0.18277685    ,-0.0059725577  ,
  -0.06906437    , 0.055481337   , 0.20713581    , 0.06965989    ],
 [ 0.0364259     , 0.19875023    ,-0.19065994    ,-0.1538784     ,
   0.031783298   ,-0.049985945   , 0.10947804    , 0.08114215    ,
  -0.023007862   , 0.05622021    ,-0.037373487   ,-0.009165582   ,
   0.053230133   ,-0.16405725    ,-0.08571407    ,-0.061584223   ,
  -0.23855038    ,-0.011310504   ,-0.11977694    , 0.072513364   ,
   0.06899095    ,-0.050108492   ,-0.1802087     , 0.020171436   ,
  -0.07718123    , 0.0677359     ,-0.13521999    ,-0.0165184     ,
   0.18260017    ,-0.159275      ,-0.086504854   ,-0.05911865    ,
  -0.106724076   , 0.037198886   , 0.03489033    , 0.018037135   ,
  -0.25440043    ,-0.109888285   , 0.17363067    , 0.007375285   ],
 [ 0.17578368    , 0.08977113    , 0.17042194    , 0.012252858   ,
  -0.10596193    ,-0.06197045    , 0.05422665    , 0.24572086    ,
  -0.030972129   ,-0.12914632    , 0.03654271    , 0.19359908    ,
  -0.0027217872  ,-0.03333171    ,-0.1555506     ,-0.0066486676  ,
   0.042185877   , 0.17832772    , 0.19917098    ,-0.049036354   ,
  -0.03638922    ,-0.129147      , 0.11329633    , 0.08502773    ,
  -0.069416314   , 0.03613715    ,-0.1540746     ,-0.0705831     ,
   0.0012254616  ,-0.10167014    ,-0.21393521    , 0.13449174    ,
  -0.0021018842  ,-0.24356462    ,-0.14114434    , 0.09061891    ,
   0.005430159   ,-0.11288315    , 0.17888494    , 0.046668094   ],
 [-0.05203087    , 0.065257445   ,-0.015220609   ,-0.03615355    ,
   0.12705082    ,-0.18279399    , 0.02259064    ,-0.1568176     ,
  -0.20823902    ,-0.17807488    , 0.0035296627  ,-0.022607516   ,
   0.023998044   ,-0.06046228    ,-0.16451798    ,-0.10954083    ,
   0.3486771     , 0.07330401    ,-0.09796107    , 0.0993233     ,
  -0.009028933   ,-0.13256712    , 0.08627317    , 0.14670822    ,
   0.07638892    , 0.13119729    ,-0.1348512     , 0.1816482     ,
   0.11276814    ,-0.12501918    ,-0.012944416   ,-0.03373778    ,
  -0.120278865   , 0.016706478   , 0.06368073    ,-0.12388573    ,
  -0.14001945    ,-0.10025189    , 0.09924013    , 0.032835092   ],
 [ 0.055079002   ,-0.16295628    , 0.07521528    , 0.6006676     ,
  -0.16000825    , 0.11330613    ,-0.113536894   ,-0.029568719   ,
  -0.18429185    , 0.08499362    ,-0.031318586   , 0.17711954    ,
  -0.28574795    , 0.038082402   , 0.11366501    , 0.07941862    ,
  -0.060700234   , 0.059232052   ,-0.12746969    ,-0.10584902    ,
  -0.06442506    ,-0.09890186    ,-0.14584002    , 0.10562989    ,
   0.087314956   , 0.19354573    ,-0.045041863   , 0.082477614   ,
  -0.15466824    , 0.115152776   ,-0.12672457    ,-0.09858508    ,
   0.13287981    ,-0.23409061    ,-0.08743816    , 0.029343126   ,
  -0.07480376    , 0.13618492    , 0.10508935    ,-0.057686772   ],
 [ 0.1174617     , 0.062270436   ,-0.12596121    ,-0.23828904    ,
   0.17007361    , 0.15720417    , 0.104565024   ,-0.0164576     ,
  -0.07871495    , 0.113818556   , 0.12180446    , 0.14185642    ,
  -0.13243629    , 0.004381944   , 0.15361236    , 0.17729938    ,
   0.1106204     , 0.1564159     ,-0.02266251    ,-0.010997135   ,
  -0.24479078    ,-0.03114139    , 0.178641      , 0.13061327    ,
   0.8789618     ,-0.14400262    , 0.016734062   , 0.17033921    ,
   0.05853706    ,-0.058101557   , 0.19800301    ,-0.18583602    ,
   0.17106411    , 0.049225274   , 0.19129701    , 0.15599017    ,
   0.07592293    ,-0.012957453   ,-0.15774804    ,-0.010525865   ],
 [ 0.07208066    , 0.068173766   ,-0.14966944    ,-0.03966493    ,
  -0.05256088    ,-0.027444942   ,-0.116412126   ,-0.07232168    ,
   0.05861036    ,-0.1797789     ,-0.14581564    ,-0.1731799     ,
   0.11971225    ,-0.20095555    , 0.08387333    ,-0.027906878   ,
  -0.19348253    ,-0.009200534   , 0.14303479    ,-0.15013453    ,
   0.08229727    ,-0.054007433   , 0.017686935   , 0.14357658    ,
   0.117899634   ,-0.38520032    ,-0.18506883    ,-0.14955305    ,
   0.17987624    ,-0.08268888    , 0.039132416   , 0.13720506    ,
  -0.12616453    , 0.06487973    ,-0.023257906   ,-0.12918858    ,
   0.18492682    ,-0.19334215    ,-0.063215375   , 0.056731038   ],
 [-0.2664317     , 0.13532783    ,-0.17451948    ,-0.18616359    ,
  -0.02477088    , 0.2156528     ,-0.045902286   ,-0.10629187    ,
  -0.09943098    , 0.13917217    , 0.14192657    ,-0.14490108    ,
   0.094324745   ,-0.1558558     , 0.032818284   , 0.09376953    ,
   0.102716446   , 0.010471719   , 0.18201093    , 0.066012874   ,
   0.14833798    , 0.026078818   ,-0.0051043653  , 0.12749794    ,
  -0.13447937    , 0.06868414    , 0.34253788    , 0.027688783   ,
  -0.12691157    , 0.040611133   , 0.7469527     ,-0.060784645   ,
   0.085050635   , 0.007226527   ,-0.23913048    , 0.16826095    ,
  -0.15985024    ,-0.17683169    , 0.06895191    , 0.13522121    ],
 [ 0.118188344   ,-0.017587088   ,-0.11630379    , 0.027212923   ,
  -0.091950536   , 0.013941713   ,-0.109191775   , 0.07006479    ,
  -0.067013934   , 0.13727434    , 0.052683365   , 0.12544236    ,
   0.066420466   , 0.03336815    ,-0.12861271    ,-0.12082117    ,
  -0.19581407    , 0.12407629    ,-0.14758834    , 0.15696383    ,
  -0.32171562    ,-0.056906343   ,-0.015226274   , 0.1516076     ,
  -0.08884815    ,-0.16724081    , 0.10639227    , 0.10012818    ,
  -0.07925365    ,-0.18321045    , 0.084023595   ,-0.15509522    ,
   0.03765856    , 0.07448633    ,-0.10634723    , 0.071166806   ,
  -0.08586883    , 0.17472151    , 0.13613625    , 0.11476303    ],
 [-0.05264443    , 0.19728027    , 0.035717923   ,-0.020534927   ,
  -0.035340857   ,-0.27016696    , 0.0832667     ,-0.058023136   ,
  -0.034604423   ,-0.06485287    , 0.043823272   ,-0.045531325   ,
  -0.07834226    , 0.058006365   , 0.19570157    , 0.06773099    ,
  -0.051582318   ,-0.17547749    , 0.11061873    ,-0.1264233     ,
  -0.14497522    , 0.020172704   , 0.17687072    ,-0.102534205   ,
  -0.112540916   ,-0.18925677    ,-0.10106608    , 0.154768      ,
   0.036562614   , 0.18068688    ,-0.12248668    , 0.07537752    ,
   0.113400586   , 0.119111545   ,-0.14294194    ,-0.1516511     ,
   0.14309344    , 0.03776791    ,-0.15051939    , 0.16537671    ],
 [ 0.06127085    , 0.09650665    , 0.0058731227  , 0.0722528     ,
  -0.11611032    ,-0.11065269    , 0.08259387    , 0.16479985    ,
  -0.14817834    , 0.044587437   , 0.10114944    ,-0.0050447593  ,
  -0.17828004    , 0.05477959    ,-0.061265588   ,-0.20437923    ,
  -0.019245354   , 0.12634726    , 0.11147       , 0.1636938     ,
   0.13188264    ,-0.14566383    ,-0.046751477   ,-0.004957467   ,
   0.12575732    , 0.13611726    ,-0.13520065    , 0.03174212    ,
  -0.10271969    ,-0.2029804     , 0.17602117    , 0.13992584    ,
   0.08538879    ,-0.12429141    , 0.07876871    ,-0.19803958    ,
  -0.007499101   ,-0.051294032   , 0.10769171    , 0.091634415   ],
 [ 0.026784535   ,-0.11022795    , 0.072919324   , 0.016191004   ,
  -0.15511206    ,-0.07609325    ,-0.19738355    ,-0.04792638    ,
   0.09074463    , 0.103744075   , 0.18505047    ,-0.052998137   ,
  -0.16467562    , 0.034835324   , 0.058146745   ,-0.08722927    ,
  -0.015238533   , 0.15097043    , 0.16471371    ,-0.04460839    ,
  -0.13252848    ,-0.043653537   ,-0.04409676    , 0.04006887    ,
   0.078296974   , 0.07214897    ,-0.020988831   , 0.24547514    ,
   0.106645584   ,-0.21987988    , 0.14525598    , 0.14537774    ,
  -0.18913019    ,-0.182996      ,-0.10912548    ,-0.16637045    ,
   0.17291504    , 0.067071885   , 0.14427403    ,-0.0863828     ],
 [-0.027963122   ,-0.117474794   , 0.15594964    , 0.16896358    ,
  -0.13800041    ,-0.104118764   ,-0.16569304    ,-0.032730974   ,
   0.13709357    ,-0.1712914     ,-0.10178641    ,-0.030903002   ,
   0.10690213    ,-0.0019605085  , 0.1594245     ,-0.10875241    ,
   0.1398325     , 0.19183335    ,-0.025159365   , 0.12049429    ,
  -0.18483458    , 0.09853109    , 0.1568513     , 0.11511839    ,
  -0.08630425    , 0.37446648    ,-0.10851707    , 0.16195051    ,
   0.027189873   , 0.013545834   ,-0.036863055   , 0.16743408    ,
  -0.019917091   , 0.058625717   , 0.06825078    ,-0.08457665    ,
   0.100655735   ,-0.16339038    ,-0.060529705   , 0.12736724    ],
 [-0.101552114   ,-0.1816927     ,-0.013184644   ,-0.0009652271  ,
  -0.19321555    , 0.11993364    , 0.05485607    ,-0.024612902   ,
   0.062088743   , 0.06750024    ,-0.040532123   , 0.07363634    ,
  -0.17149217    ,-0.05568715    ,-0.22188552    , 0.16806538    ,
  -0.06255737    , 0.1935188     , 0.14401254    , 0.15486544    ,
   0.023239747   , 0.02935853    , 0.09659421    ,-0.32138997    ,
   0.09368686    ,-0.12589654    , 0.113731384   , 0.11116199    ,
   0.065011166   , 0.17250611    ,-0.027296538   ,-0.10843403    ,
  -0.061241042   , 0.07255748    , 0.029796103   , 0.21872906    ,
  -0.01138107    , 0.16638434    , 0.05930292    ,-0.120578736   ],
 [-0.08574717    , 0.062545426   , 0.018220425   ,-0.086180724   ,
   0.12305582    , 0.10299877    , 0.17901188    , 0.16196835    ,
  -0.011715499   ,-0.19607323    ,-0.18028599    , 0.17750801    ,
   0.07851618    ,-0.298071      , 0.3621622     ,-0.086098835   ,
   0.101759136   , 0.053045493   , 0.1785402     ,-0.19280805    ,
   0.117106214   ,-0.12444464    ,-0.16741218    ,-0.09390761    ,
   0.0199156     ,-0.06832592    ,-0.1642587     ,-0.060707334   ,
   0.027418528   ,-0.027830534   , 0.18245403    ,-0.04435199    ,
  -0.035450872   , 0.049932647   ,-0.16256706    , 0.10542763    ,
   0.6306128     ,-0.14705016    , 0.15796916    , 0.10614857    ],
 [-0.124557376   ,-0.109391384   , 0.100114614   ,-0.033603147   ,
  -0.049885705   , 0.20424797    ,-0.009731426   ,-0.048448127   ,
   0.01596421    , 0.13309902    , 0.09803683    ,-0.18659753    ,
   0.11644505    ,-0.07027349    , 0.07978364    , 0.09158642    ,
   0.20571473    ,-0.03190478    , 0.058910523   , 0.12261474    ,
   0.08373392    , 0.0029304996  ,-0.15013655    , 0.09548056    ,
  -0.19983324    , 0.21406531    ,-0.17114253    , 0.097145624   ,
   0.14404231    , 0.18292582    ,-0.019471407   , 0.07317406    ,
   0.05254761    , 0.19905032    ,-0.0110294605  ,-0.04119576    ,
   0.067988284   ,-0.09752917    ,-0.14553939    ,-0.4725035     ],
 [-0.19976449    ,-0.120099016   ,-0.13542153    , 0.061523106   ,
  -0.11354512    ,-0.06636395    , 0.07112405    ,-0.12178815    ,
   0.17948133    , 0.052338786   , 0.12773226    ,-0.06895276    ,
  -0.15395732    ,-0.016267436   , 0.13713738    , 0.08406045    ,
   0.01590019    , 0.009641428   , 0.0049252426  ,-0.12230847    ,
  -0.19414997    , 0.042854503   , 0.017919164   , 0.01675504    ,
   0.056323778   , 0.18878245    , 0.15437473    , 0.023070201   ,
   0.09409667    ,-0.014006572   , 0.12639925    , 0.06719173    ,
   0.0152991675  ,-0.15616775    , 0.11757364    ,-0.16218327    ,
   0.15926188    , 0.13213111    ,-0.0049494538  ,-0.17195928    ]])
pesoCamada0 = np.array ([ 0.009233024   ,-0.0033258565  , 0.006025264   ,-0.0036742527  ,
 -0.047337066   ,-0.0051404857  , 0.01253199    ,-0.11951774    ,
 -0.012508118   ,-0.020413384   ,-0.011128373   ,-0.10716805    ,
 -0.023825977   , 0.016839553   ,-0.04106173    ,-0.02149842    ,
  0.0098093655  ,-0.00073694903 , 0.024080396   ,-0.0075957817  ,
  0.000042988722,-0.01285181    ,-0.023237795   , 0.019735927   ,
 -0.0018374053  , 0.0043661026  ,-0.047008213   , 0.0024130864  ,
 -0.016720966   ,-0.003954622   , 0.0028787062  ,-0.03026533    ,
  0.08750756    ,-0.0076965443  ,-0.0014207141  ,-0.0022151493  ,
  0.01907375    , 0.01681146    , 0.026175182   ,-0.050140604   ])
camada1 = np.array ([[ 0.04787625  , 0.12521258  , 0.14279406  , 0.12639578  ,-0.07906221  ,
   0.101953335 ,-0.18092667  , 0.049425304 ,-0.22007099  , 0.09198471  ],
 [ 0.12491366  , 0.16192004  , 0.16390125  , 0.10786243  , 0.07953098  ,
  -0.15889667  ,-0.073811136 , 0.063668296 , 0.05599861  , 0.0349933   ],
 [ 0.20571119  ,-0.054547224 ,-0.038707666 , 0.022229379 , 0.13828197  ,
   0.07198978  ,-0.093988106 ,-0.18031947  ,-0.07326159  , 0.037303213 ],
 [-0.06911021  , 0.09079888  ,-0.15388928  ,-0.07439512  ,-0.06382592  ,
  -0.088123724 , 0.19455078  ,-0.064982854 , 0.33979097  , 0.21120888  ],
 [ 0.21377398  ,-0.14230563  ,-0.14048167  , 0.025117159 , 0.10003638  ,
  -0.069493845 , 0.11562148  , 0.006754028 , 0.13640554  ,-0.25186408  ],
 [ 0.1150609   , 0.0073593864, 0.025158107 ,-0.069312416 , 0.18861681  ,
   0.11580713  ,-0.06060123  ,-0.09165719  , 0.016604874 , 0.18861915  ],
 [-0.21773162  ,-0.21124667  ,-0.1796241   , 0.0771323   ,-0.055287942 ,
  -0.12840594  , 0.11680799  , 0.091328256 ,-0.04126728  ,-0.0150149455],
 [-0.07632174  ,-0.05457413  , 0.04043714  ,-0.027271444 ,-0.11085681  ,
   0.19390774  , 0.17805025  ,-0.14489304  ,-0.047776658 , 0.1378749   ],
 [-0.14497443  ,-0.15194319  ,-0.13114437  ,-0.04887469  ,-0.017392073 ,
  -0.07839326  , 0.114732586 , 0.26429674  , 0.1482168   ,-0.2015286   ],
 [-0.07366962  ,-0.16069423  , 0.07891749  , 0.094400235 , 0.24091665  ,
   0.047249503 , 0.13422999  , 0.045092966 , 0.067573294 ,-0.075969025 ],
 [-0.104972646 , 0.010570507 ,-0.16767664  , 0.14716604  , 0.17710479  ,
  -0.08742634  , 0.15173592  ,-0.21012676  , 0.19421296  ,-0.046645477 ],
 [-0.035536744 ,-0.08705295  ,-0.18469012  ,-0.07793393  , 0.14249754  ,
   0.008003051 , 0.20364195  , 0.12750539  , 0.08104632  , 0.070034206 ],
 [-0.1414988   , 0.04054494  , 0.11822764  ,-0.0010831456,-0.013170738 ,
  -0.10670637  ,-0.06424562  ,-0.012978674 , 0.14645109  , 0.1847486   ],
 [-0.13847493  ,-0.004697467 ,-0.037890878 ,-0.09062954  ,-0.031730596 ,
   0.09197841  ,-0.18341821  ,-0.050814733 ,-0.20007803  , 0.21445382  ],
 [-0.15813723  , 0.069205634 ,-0.1559241   , 0.13652292  , 0.043906577 ,
   0.041310966 ,-0.0073815994, 0.009431141 , 0.5140671   ,-0.1059907   ],
 [ 0.17507657  ,-0.10918938  , 0.092172645 , 0.114568345 , 0.025044175 ,
  -0.1799059   , 0.08044097  , 0.034195922 , 0.048806075 ,-0.001971449 ],
 [ 0.032543156 ,-0.071568936 , 0.09489288  , 0.18883193  ,-0.15720743  ,
  -0.053120416 , 0.1573571   , 0.14540328  ,-0.014074411 ,-0.013165504 ],
 [ 0.20429593  , 0.14099872  , 0.15620986  , 0.006395294 , 0.06489647  ,
   0.020310987 ,-0.12486603  ,-0.008018646 , 0.07111451  , 0.013405498 ],
 [-0.16583717  , 0.039873213 ,-0.08462614  , 0.01628458  ,-0.13136505  ,
  -0.052777033 , 0.11303281  ,-0.2297137   , 0.15789151  , 0.13405675  ],
 [-0.0024168633,-0.10843513  , 0.04619212  ,-0.02954938  , 0.10646827  ,
   0.041614365 ,-0.116242416 , 0.15501596  , 0.12672028  , 0.12283277  ],
 [ 0.103838205 , 0.22029531  ,-0.16357383  ,-0.15646689  , 0.31944466  ,
   0.18628286  , 0.26663983  , 0.08988234  , 0.006728905 ,-0.06459203  ],
 [ 0.152357    , 0.13994044  ,-0.18917683  , 0.53631765  , 0.1272237   ,
   0.072622515 ,-0.15814695  , 0.21217707  , 0.08286808  ,-0.021922698 ],
 [ 0.0526662   ,-0.058748387 , 0.1960472   ,-0.1496072   , 0.119890966 ,
  -0.18736061  ,-0.12699695  , 0.0940297   ,-0.041235324 ,-0.039029818 ],
 [-0.13580178  , 0.072822124 ,-0.11429542  ,-0.21059655  ,-0.115959965 ,
   0.046361458 , 0.15303929  , 0.0978783   , 0.18907754  ,-0.16543107  ],
 [ 0.0337367   , 0.037575338 , 0.20178579  , 0.018822178 ,-0.16576204  ,
  -0.02070232  ,-0.050418865 , 0.0074613835,-0.06158949  ,-0.013684443 ],
 [ 0.06470607  , 0.08295538  , 0.14269656  , 0.05856664  ,-0.02112145  ,
   0.15260102  , 0.006270488 ,-0.13691233  , 0.15159748  ,-0.10998532  ],
 [ 0.014084354 ,-0.03241419  , 0.14440502  , 0.01723273  ,-0.098839864 ,
   0.0005306581,-0.1534284   , 0.074688785 ,-0.09426724  , 0.037824787 ],
 [ 0.1207648   , 0.16853969  ,-0.02641738  ,-0.10056005  , 0.09250766  ,
  -0.07802961  , 0.018428024 , 0.11526868  , 0.1425304   ,-0.044134576 ],
 [ 0.008123754 ,-0.044618864 , 0.1420692   , 0.15743998  , 0.114087924 ,
  -0.14074768  ,-0.14397033  ,-0.20523985  , 0.17569782  ,-0.016182136 ],
 [-0.008838036 , 0.054133646 ,-0.17495039  , 0.22357744  , 0.025883418 ,
  -0.055820554 , 0.15564056  ,-0.044097908 , 0.02449577  ,-0.118092336 ],
 [-0.08413643  ,-0.17508186  ,-0.18376765  ,-0.07599395  , 0.096913174 ,
  -0.13567872  , 0.20028245  , 0.18036638  , 0.04304533  , 0.008816564 ],
 [ 0.080976166 ,-0.011531769 ,-0.08194146  ,-0.15463862  , 0.1082444   ,
  -0.061626658 , 0.09934502  , 0.18327886  ,-0.20731516  , 0.13949175  ],
 [-0.14688918  , 0.036775786 , 0.03484329  ,-0.19046184  ,-0.063932575 ,
  -0.06884876  , 0.19233567  , 0.002329068 , 0.19033822  , 0.2011746   ],
 [ 0.13204083  ,-0.14580469  , 0.018702274 , 0.092233524 ,-0.14511204  ,
  -0.13853058  , 0.084776014 , 0.028663613 , 0.065587856 , 0.05411404  ],
 [-0.13003024  ,-0.069055915 , 0.06451021  , 0.13007468  ,-0.20627025  ,
   0.1690229   , 0.11174096  ,-0.05112692  ,-0.042471997 ,-0.06830771  ],
 [-0.10245539  , 0.14228047  ,-0.09994757  ,-0.124392875 ,-0.12779674  ,
  -0.059614904 , 0.08731776  ,-0.0045264666,-0.036095247 , 0.14390948  ],
 [-0.6262011   , 0.17805162  , 0.03119571  ,-0.14824988  ,-0.10184503  ,
   0.117309    , 0.1545265   ,-0.46931145  ,-0.036227167 ,-0.011009317 ],
 [-0.18229245  , 0.048198156 ,-0.062040456 , 0.053523596 , 0.17368641  ,
  -0.104350716 , 0.075161815 ,-0.044136878 , 0.163292    ,-0.029894425 ],
 [ 0.08925154  , 0.21496387  ,-0.19524848  , 0.15591048  ,-0.16280739  ,
  -0.17191334  , 0.07262517  , 0.13407488  , 0.082969084 ,-0.104375    ],
 [-0.063404314 , 0.076047204 , 0.16086602  , 0.10326488  ,-0.015297343 ,
  -0.18584624  ,-0.2282509   , 0.034644905 , 0.016947672 ,-0.14888814  ]])
pesoCamada1 = np.array ([-0.02314357  ,-0.0445006   ,-0.031490643 , 0.13383745  ,-0.044132642 ,
 -0.010067738 , 0.03957661  ,-0.008841846 ,-0.0033995756, 0.024004593 ])
camada2 = np.array ([[ 0.062032763 ],
 [ 0.032437235 ],
 [ 0.2015655   ],
 [ 0.18207936  ],
 [ 0.0005545607],
 [-0.046858374 ],
 [ 0.16708529  ],
 [ 0.03137219  ],
 [ 0.16311121  ],
 [ 0.16768889  ]])
pesoCamada2 = np.array ([-0.008500406])
pesoDama = 1.2784568226082176

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
        
        scoreTabuleiro = calculaScoreTabuleiroMinMax2 (copy.deepcopy(tabuleiroNovo), 1, False)
            
        print(str(scoreTabuleiro), file=sys.stderr)
        
        if (scoreTabuleiro > melhorMovimento):
            melhorMovimento = scoreTabuleiro
            jogadaSelecionada = move_string
            
    print (jogadaSelecionada)