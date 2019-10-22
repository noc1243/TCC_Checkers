# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:33:17 2019

@author: nocera
"""

import sys
import math
import numpy as np
import copy

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
    
camada0 = np.array ([[ 0.11611718   ,-0.16153526   , 0.10482688   , 0.10294203   ,
   0.00095612445, 0.11161298   ,-0.08054119   ,-0.012788461  ,
  -0.0023298198 ,-0.12645306   ,-0.07235043   ,-0.14181061   ,
   0.15896526   ,-0.1058746    , 0.058355797  , 0.15175495   ,
   0.16275668   ,-0.05737016   ,-0.15438293   ,-0.055386033  ,
  -0.09189548   , 0.017881876  ,-0.16780527   , 0.03788321   ,
   0.03638918   ,-0.118534625  ,-0.050720368  , 0.12027846   ,
  -0.115806654  , 0.037878245  ,-0.055547956  ,-0.03305009   ,
   0.10828398   , 0.06998852   ,-0.037179213  , 0.079103895  ,
   0.13465913   , 0.041393463  , 0.19496945   , 0.11667705   ],
 [-0.03807274   , 0.101724826  , 0.14619446   ,-0.17286018   ,
   0.0470127    , 0.14038748   , 0.027688617  ,-0.012616292  ,
  -0.10942586   , 0.14087892   , 0.047754813  ,-0.06255281   ,
  -0.14078335   ,-0.07111662   ,-0.033545475  ,-0.05102995   ,
   0.088640064  , 0.061587445  ,-0.16883917   ,-0.14911506   ,
  -0.011297027  ,-0.06843469   ,-0.19019014   , 0.083724245  ,
  -0.017426897  ,-0.0037036864 ,-0.11587127   , 0.012043766  ,
   0.07814749   , 0.033567637  , 0.13004233   ,-0.019164814  ,
  -0.13788848   , 0.20558965   ,-0.14972523   ,-0.12196895   ,
   0.04448477   ,-0.13407663   , 0.15833688   , 0.0059073092 ],
 [ 0.14651325   , 0.075996354  , 0.09177031   ,-0.14510839   ,
  -0.07384086   , 0.08715433   , 0.080894336  , 0.19815747   ,
   0.14277136   ,-0.007546503  , 0.14566752   ,-0.1973208    ,
   0.041941594  ,-0.110302374  ,-0.18088152   , 0.051679816  ,
   0.12000373   , 0.052362144  , 0.051050115  ,-0.09696296   ,
  -0.05886403   , 0.025051685  ,-0.17887221   , 0.0721763    ,
   0.18613584   , 0.172663     , 0.032365266  , 0.17012085   ,
  -0.024663107  , 0.07998901   ,-0.17332454   , 0.015676226  ,
  -0.03225951   , 0.19436495   ,-0.18418664   , 0.05839667   ,
   0.067489706  ,-0.0028424698 ,-0.10570415   ,-0.05418169   ],
 [ 0.156315     ,-0.08334707   , 0.13393275   , 0.17418376   ,
   0.1336754    , 0.19816306   ,-0.0773252    ,-0.007681518  ,
  -0.10062795   ,-0.16879658   ,-0.11978353   ,-0.008330755  ,
  -0.13938557   ,-0.12947764   , 0.09172296   ,-0.02182451   ,
   0.04145472   , 0.016151993  ,-0.047702644  , 0.1349934    ,
  -0.12123806   ,-0.0009725321 , 0.16439354   , 0.16362654   ,
   0.09794908   , 0.0264872    , 0.1971491    , 0.1236172    ,
   0.1629269    ,-0.0730858    ,-0.05936719   , 0.1736031    ,
   0.19302003   ,-0.15594651   , 0.14940889   ,-0.10383836   ,
   0.09785182   , 0.118377835  ,-0.14677438   ,-0.101939194  ],
 [ 0.05849707   ,-0.0040215263 ,-0.11615022   , 0.0039161188 ,
  -0.14517072   , 0.08590173   , 0.037908368  ,-0.010322184  ,
  -0.0021429856 ,-0.0369435    ,-0.14138374   ,-0.1964522    ,
   0.08851747   ,-0.060980238  ,-0.036667146  , 0.043159578  ,
  -0.10615667   ,-0.16810302   , 0.14996369   , 0.15496871   ,
  -0.13638307   ,-0.06139033   , 0.009429157  , 0.17429145   ,
   0.08690999   , 0.12021875   ,-0.10081543   ,-0.093505085  ,
  -0.016243078  , 0.08977709   , 0.13482043   ,-0.084012076  ,
   0.17191255   ,-0.16668768   ,-0.20985067   , 0.017091136  ,
   0.18521796   ,-0.002914866  , 0.0742671    ,-0.19243297   ],
 [ 0.112412505  , 0.10184595   ,-0.050877936  , 0.076630026  ,
   0.1702037    , 0.07458604   , 0.118338734  ,-0.1897019    ,
  -0.18984674   , 0.12161762   , 0.09045336   ,-0.20010075   ,
   0.08937193   , 0.1117625    , 0.020653645  , 0.012339658  ,
   0.062111154  ,-0.14379531   , 0.042630035  ,-0.043500554  ,
   0.02086373   , 0.09793054   ,-0.06823345   ,-0.01573203   ,
   0.13343239   ,-0.098293655  , 0.2003078    , 0.14748925   ,
  -0.08899107   ,-0.1266153    , 0.20837629   , 0.090401605  ,
  -0.15177228   , 0.03355957   ,-0.11411421   ,-0.108419575  ,
  -0.14102095   , 0.14758627   ,-0.11713551   ,-0.0509096    ],
 [ 0.15581566   , 0.17796357   , 0.14494576   , 0.14149603   ,
  -0.13304576   ,-0.008697252  ,-0.19974568   , 0.119365014  ,
   0.01999581   ,-0.061805062  ,-0.08866741   ,-0.038402062  ,
  -0.07675862   , 0.006185876  , 0.07296325   , 0.122830726  ,
   0.019752197  , 0.12856652   , 0.0526574    , 0.00015837143,
  -0.18969686   ,-0.05859353   , 0.06043089   ,-0.0051196087 ,
  -0.0629803    ,-0.14174308   ,-0.12152741   ,-0.09210903   ,
   0.10446592   ,-0.17038488   , 0.07631705   , 0.12109893   ,
  -0.033080228  , 0.2052866    ,-0.016290685  ,-0.122619994  ,
   0.1759509    , 0.15082203   , 0.1623948    ,-0.1049049    ],
 [-0.20244312   , 0.075458534  , 0.00022499863, 0.11476106   ,
   0.056479562  ,-0.11012171   , 0.15416844   , 0.020602385  ,
  -0.18959624   ,-0.027144942  ,-0.17474276   , 0.15158293   ,
   0.10146517   ,-0.16968085   , 0.16949953   ,-0.04413884   ,
   0.16768295   , 0.072737195  , 0.13325812   ,-0.14043187   ,
   0.17732081   , 0.16316202   ,-0.13596325   , 0.07487833   ,
   0.021709029  , 0.17120287   , 0.007017884  ,-0.17086236   ,
  -0.020853685  , 0.14938664   , 0.1897149    ,-0.018760344  ,
  -0.018868113  , 0.09457093   , 0.023488546  ,-0.062066313  ,
   0.2112114    ,-0.011563012  , 0.07218626   , 0.03814655   ],
 [ 0.17822142   , 0.04643314   , 0.08808281   ,-0.10395999   ,
   0.02627617   ,-0.16946277   , 0.1502932    , 0.20196788   ,
  -0.18008028   ,-0.14514536   , 0.1438216    , 0.0026011455 ,
   0.12453737   , 0.036705684  ,-0.062352236  , 0.013060058  ,
  -0.16426483   ,-0.17839496   ,-0.11454001   ,-0.18287158   ,
   0.18368551   ,-0.06426531   , 0.04045527   ,-0.008849267  ,
  -0.074996635  , 0.15650594   , 0.13954909   , 0.07917812   ,
   0.07923159   , 0.008035501  ,-0.15809745   , 0.09154069   ,
   0.11581304   , 0.17557804   ,-0.17314248   ,-0.16546392   ,
   0.08655738   ,-0.11082419   ,-0.16390206   , 0.0253443    ],
 [-0.020730404  ,-0.04488596   , 0.11319344   , 0.04094022   ,
  -0.122446425  ,-0.023595173  ,-0.1604219    ,-0.08192883   ,
  -0.11856889   , 0.14258677   ,-0.18004611   ,-0.06666646   ,
   0.06983794   ,-0.08337354   , 0.13661657   ,-0.1891934    ,
  -0.15800498   ,-0.1876687    , 0.05040653   , 0.042602766  ,
  -0.033299156  , 0.038796864  , 0.019231724  ,-0.13822146   ,
   0.061642665  ,-0.044334814  ,-0.19634871   , 0.1407431    ,
  -0.17691348   , 0.13247874   , 0.11724687   ,-0.07738313   ,
  -0.037608135  , 0.12811068   , 0.02659099   ,-0.029830307  ,
   0.1594618    , 0.11427855   ,-0.003836874  ,-0.18547401   ],
 [ 0.18415888   ,-0.003600624  ,-0.19336613   , 0.17330354   ,
   0.016715202  , 0.11707719   , 0.17324324   , 0.1725041    ,
  -0.031472027  ,-0.05251607   ,-0.11397803   , 0.17263302   ,
   0.02437476   ,-0.0037017635 , 0.08821295   , 0.1800541    ,
  -0.098664194  , 0.014050651  , 0.1768682    ,-0.13543558   ,
   0.023277467  , 0.17419198   ,-0.16766755   , 0.08953377   ,
   0.1202074    , 0.088958055  ,-0.13195182   ,-0.09270426   ,
  -0.1361301    ,-0.12007461   , 0.0780379    ,-0.026327576  ,
  -0.013606118  ,-0.104686365  ,-0.18282461   ,-0.13046381   ,
  -0.13549234   ,-0.13044322   , 0.19806762   ,-0.09144227   ],
 [-0.15803513   ,-0.18439066   , 0.13189907   , 0.11163578   ,
  -0.02847199   , 0.07725985   ,-0.18509744   , 0.17037895   ,
   0.07282702   , 0.1784476    ,-0.05836757   , 0.09166575   ,
   0.07228729   ,-0.1365387    , 0.15640593   , 0.1680047    ,
   0.093646705  ,-0.034781132  ,-0.023968276  ,-0.06423033   ,
  -0.15045008   , 0.032978833  ,-0.056496024  ,-0.11455456   ,
  -0.17152692   , 0.105391614  , 0.088336945  ,-0.0363901    ,
   0.04050889   , 0.07130988   , 0.19593476   ,-0.15726025   ,
   0.020771066  ,-0.1581234    ,-0.021031205  , 0.16745126   ,
  -0.16873235   , 0.13064533   ,-0.040372144  , 0.020813165  ],
 [-0.11981599   , 0.015215791  , 0.16378543   , 0.09776929   ,
   0.032347895  ,-0.092558354  ,-0.056614712  , 0.11971299   ,
   0.16840628   , 0.18590394   , 0.05365195   ,-0.13752252   ,
  -0.09808164   , 0.17034467   ,-0.051173717  ,-0.18214805   ,
   0.05410184   , 0.032348216  , 0.0974206    ,-0.10669211   ,
   0.036484808  ,-0.16736692   , 0.064592645  , 0.17455441   ,
  -0.19183782   ,-0.032097384  , 0.028390208  , 0.16797525   ,
  -0.06379671   ,-0.150525     , 0.036396645  , 0.13223585   ,
  -0.17215616   , 0.07386715   , 0.059821498  ,-0.060769558  ,
  -0.0873171    , 0.05335822   , 0.13341452   , 0.1633007    ],
 [ 0.017181423  ,-0.001781179  ,-0.06062297   , 0.02556963   ,
  -0.17520846   ,-0.07338724   , 0.024118893  , 0.14487714   ,
   0.10868866   , 0.118919864  ,-0.12387388   , 0.055484325  ,
   0.061003387  ,-0.03824549   , 0.076290324  , 0.1908855    ,
   0.10524967   , 0.15618859   ,-0.105070494  , 0.006308197  ,
  -0.049876295  , 0.03338931   , 0.038882762  ,-0.19157624   ,
   0.008251086  ,-0.071570665  , 0.16573258   ,-0.12579027   ,
  -0.17154177   ,-0.10265231   , 0.052375816  ,-0.094559416  ,
   0.1645277    ,-0.11521597   , 0.1269353    ,-0.040998716  ,
  -0.09204311   ,-0.096496195  ,-0.023893246  ,-0.18801656   ],
 [ 0.041980587  , 0.19399574   ,-0.1311934    ,-0.114289805  ,
   0.082203425  , 0.16647303   , 0.071475014  , 0.12664565   ,
  -0.15951473   ,-0.0026381507 ,-0.00017106967,-0.058233194  ,
   0.017931862  ,-0.04004193   , 0.1304218    , 0.0854011    ,
  -0.060794543  ,-0.15648268   ,-0.023929242  , 0.117923714  ,
   0.06856917   ,-0.10582094   ,-0.09490005   , 0.0796864    ,
  -0.017934361  ,-0.026159506  ,-0.13269363   , 0.13007955   ,
  -0.10054547   ,-0.06211591   ,-0.083620794  ,-0.077915855  ,
  -0.066725984  , 0.05660315   , 0.023425054  ,-0.028045973  ,
  -0.1172997    , 0.08820387   ,-0.109232     ,-0.13987267   ],
 [-0.05117172   ,-0.08606922   ,-0.19391756   , 0.15908736   ,
  -0.16154636   ,-0.03712431   ,-0.11880719   , 0.17275514   ,
   0.1024017    , 0.105144136  ,-0.16951314   , 0.013851726  ,
  -0.037286144  , 0.111776225  ,-0.094252564  , 0.02181752   ,
  -0.16767034   , 0.10776712   ,-0.11028077   ,-0.124054946  ,
   0.037343327  ,-0.1270466    , 0.1532389    ,-0.18312883   ,
   0.14652571   , 0.0904096    ,-0.026728883  , 0.05999274   ,
   0.0994849    , 0.12486938   , 0.18470843   , 0.036248766  ,
  -0.013119962  , 0.063865125  , 0.18041943   ,-0.012690325  ,
  -0.055352595  , 0.06258485   , 0.19774026   , 0.0847185    ],
 [ 0.03260864   , 0.19013825   , 0.04336256   ,-0.15443498   ,
   0.03411092   , 0.009406655  , 0.105676666  , 0.043093663  ,
  -0.021106767  , 0.087195896  ,-0.02846344   ,-0.041669413  ,
   0.04572975   ,-0.151691     ,-0.053719137  ,-0.05863391   ,
  -0.13407166   ,-0.0057451953 ,-0.121007614  , 0.08265478   ,
   0.10137977   ,-0.0606972    ,-0.20499803   ,-0.06790365   ,
  -0.09459924   , 0.083345175  ,-0.13205425   ,-0.017164767  ,
   0.20462225   ,-0.1588622    ,-0.08998401   , 0.1685116    ,
  -0.09443611   , 0.039311472  , 0.1170706    , 0.014120685  ,
  -0.17185482   ,-0.11600429   , 0.1676087    , 0.022976717  ],
 [ 0.18636812   , 0.08472394   , 0.15786316   ,-0.048829854  ,
  -0.12488034   ,-0.06782067   , 0.0756343    , 0.1827595    ,
  -0.027818495  ,-0.1466748    , 0.019582305  , 0.15612195   ,
  -0.02580897   ,-0.17339079   ,-0.13137686   ,-0.0077896803 ,
   0.0496857    , 0.18198678   , 0.18106191   ,-0.015970191  ,
  -0.037817176  ,-0.12574546   , 0.045636706  ,-0.0018372387 ,
  -0.07631238   , 0.025997674  ,-0.11468373   ,-0.06552867   ,
   0.003918831  ,-0.101872     ,-0.052428633  ,-0.008583496  ,
   0.024015706  ,-0.20072855   ,-0.054156274  , 0.16719481   ,
  -0.00091470167,-0.114381835  , 0.19689621   , 0.0472442    ],
 [ 0.03527302   , 0.066404365  ,-0.03520875   ,-0.033346884  ,
   0.098460004  ,-0.1519456    , 0.0140346885 ,-0.16408423   ,
  -0.19332883   ,-0.19057587   , 0.015891716  ,-0.016379906  ,
  -0.0052653165 ,-0.0881922    ,-0.118753955  ,-0.11971815   ,
   0.16243555   , 0.03279602   ,-0.1408444    , 0.10760522   ,
  -0.01959975   ,-0.13323857   , 0.08666349   , 0.15655056   ,
   0.08268408   , 0.11685856   ,-0.14545588   , 0.19248068   ,
   0.12422896   ,-0.13817292   ,-0.010790506  ,-0.06367585   ,
  -0.14207776   ,-0.018095661  , 0.046194073  ,-0.17791578   ,
  -0.13060303   ,-0.16082557   , 0.07930025   , 0.054970406  ],
 [ 0.062293693  ,-0.17109995   , 0.07063362   , 0.079902336  ,
  -0.15571985   , 0.11286102   ,-0.008295596  , 0.002995332  ,
  -0.18343      , 0.09379575   ,-0.04136162   , 0.16886729   ,
   0.029414637  , 0.030771885  , 0.10601164   , 0.078504115  ,
  -0.05539178   , 0.043317355  ,-0.15085188   ,-0.106468394  ,
  -0.065729015  ,-0.06583256   ,-0.15650749   , 0.11275603   ,
   0.083672605  , 0.19910538   ,-0.034057323  , 0.08901042   ,
  -0.16936667   , 0.11231049   ,-0.0826007    ,-0.09462434   ,
   0.13316588   ,-0.17727241   , 0.033422783  , 0.12047312   ,
  -0.07792617   , 0.13726622   , 0.09350605   , 0.1493245    ],
 [ 0.13241369   , 0.07168989   ,-0.15079513   ,-0.182311     ,
   0.16969068   , 0.16802013   , 0.11352894   ,-0.005837585  ,
  -0.10393445   , 0.10840327   , 0.13513282   , 0.120917805  ,
  -0.15042982   , 0.006889995  , 0.1758018    , 0.18886167   ,
   0.09802197   , 0.15444818   ,-0.020581946  ,-0.01987366   ,
  -0.2017648    ,-0.045504484  , 0.19061884   , 0.10941064   ,
   0.16240251   ,-0.13535354   ,-0.004310892  , 0.1339228    ,
   0.03753127   ,-0.059860777  , 0.19124827   ,-0.16423509   ,
   0.15738635   , 0.051973622  , 0.096517846  , 0.16097018   ,
   0.115167454  ,-0.0022310487 ,-0.16108543   ,-0.008688012  ],
 [ 0.046137456  , 0.03855255   ,-0.14438002   , 0.119149216  ,
  -0.051731225  ,-0.10575599   ,-0.12223081   ,-0.06700801   ,
   0.10770645   ,-0.18587586   ,-0.16751182   ,-0.15263948   ,
   0.11356104   ,-0.20219868   , 0.0854765    ,-0.023065481  ,
  -0.19092931   ,-0.013146716  , 0.144455     ,-0.14123306   ,
   0.0726059    ,-0.07919677   , 0.04029079   , 0.07343929   ,
   0.1142264    , 0.02869446   , 0.01731472   ,-0.14470786   ,
  -0.14508325   ,-0.06189325   , 0.05429804   , 0.14859462   ,
  -0.14638439   , 0.07230828   ,-0.07660135   ,-0.16646786   ,
   0.17211011   ,-0.19657744   ,-0.056107     , 0.055483934  ],
 [-0.18625571   , 0.15955539   ,-0.18608226   ,-0.18434542   ,
   0.0012579795 , 0.15920338   ,-0.046088338  ,-0.09384801   ,
  -0.11114684   , 0.13975956   , 0.13790393   ,-0.15104865   ,
   0.12898731   ,-0.16376512   , 0.03026201   , 0.0948455    ,
   0.119542055  , 0.016910419  , 0.18809207   , 0.061518766  ,
   0.14592002   , 0.023225572  , 0.02683889   , 0.17382947   ,
  -0.10529474   , 0.065834895  , 0.17450513   , 0.037823293  ,
  -0.117945515  , 0.04409011   ,-0.031837218  ,-0.04489077   ,
   0.08178838   , 0.08056125   , 0.07052786   , 0.17190033   ,
  -0.14180379   ,-0.12568037   , 0.086527064  , 0.14641744   ],
 [ 0.12262729   ,-0.021243857  ,-0.09739844   , 0.0018574027 ,
  -0.09791685   ,-0.020895235  ,-0.12879176   ,-0.13735412   ,
  -0.074686065  , 0.12262206   , 0.08029955   , 0.13052103   ,
   0.068040304  , 0.03807924   ,-0.15617569   ,-0.108669     ,
  -0.1961037    , 0.12306309   ,-0.080869734  , 0.13846363   ,
  -0.15277462   ,-0.06714539   ,-0.028728535  , 0.16626455   ,
  -0.091787785  ,-0.15109895   , 0.120722525  , 0.09474767   ,
  -0.10941242   ,-0.19650902   , 0.14350039   ,-0.12782525   ,
   0.042042993  ,-0.058809083  ,-0.096754365  , 0.059790406  ,
  -0.09168479   , 0.14692101   , 0.13217664   , 0.09883169   ],
 [-0.1356695    , 0.19992796   , 0.041149806  ,-0.016916638  ,
  -0.0530529    , 0.0034836277 , 0.07648935   ,-0.13641754   ,
  -0.027231878  ,-0.10797518   , 0.061547097  , 0.010734813  ,
  -0.03130963   , 0.052396554  , 0.19224091   , 0.06552922   ,
  -0.057891134  ,-0.15919435   , 0.19094644   ,-0.14566408   ,
  -0.112581104  , 0.0005324959 , 0.1518616    ,-0.06979458   ,
  -0.11712198   ,-0.12989208   ,-0.10822181   , 0.14731817   ,
   0.019662714  , 0.16632004   ,-0.12007512   , 0.08251037   ,
   0.11840742   , 0.12867787   ,-0.13733841   ,-0.17685916   ,
   0.15288699   , 0.02755258   ,-0.13361418   , 0.1514839    ],
 [ 0.07573131   , 0.099739335  , 0.0059464057 , 0.06806138   ,
  -0.11420974   ,-0.10522009   , 0.0675077    , 0.16198547   ,
  -0.16130592   ,-0.009028773  , 0.10437704   ,-0.0040070903 ,
  -0.17641976   , 0.06657419   ,-0.062729955  ,-0.18572702   ,
  -0.030222006  , 0.152571     , 0.12462531   , 0.17901057   ,
   0.13758202   ,-0.15913045   ,-0.05066215   ,-0.02550058   ,
  -0.066091776  , 0.12669224   ,-0.12466525   , 0.061476737  ,
  -0.06872774   ,-0.2031841    , 0.14285482   , 0.12400883   ,
   0.04019163   ,-0.12454315   , 0.08465158   ,-0.18504116   ,
   0.09578554   ,-0.019226355  , 0.11510387   , 0.096591026  ],
 [ 0.009549812  ,-0.12631103   , 0.047791366  , 0.009563963  ,
  -0.15002103   ,-0.080280155  ,-0.18690652   ,-0.0499685    ,
   0.09452141   , 0.08281835   , 0.1954581    ,-0.03703408   ,
  -0.17609063   , 0.049165536  , 0.13698949   , 0.20063825   ,
  -0.011211645  , 0.14781865   , 0.15816383   ,-0.05105058   ,
  -0.14138025   ,-0.04117599   ,-0.056533605  , 0.022331422  ,
  -0.013277973  , 0.13031548   ,-0.011952222  , 0.18761337   ,
   0.10860474   ,-0.13871416   , 0.14108697   , 0.14211102   ,
  -0.19123028   ,-0.16955996   ,-0.10419696   ,-0.15586218   ,
   0.18260676   , 0.09693015   , 0.13660917   ,-0.122058734  ],
 [-0.036450204  ,-0.144748     , 0.15492703   , 0.17811796   ,
  -0.17525251   ,-0.10601726   ,-0.009084385  ,-0.018687094  ,
   0.14452209   ,-0.16921307   ,-0.102543965  ,-0.13115604   ,
   0.13583821   ,-0.017458592  , 0.16932818   ,-0.11273746   ,
   0.19465706   , 0.17895523   ,-0.0074941143 , 0.11958959   ,
  -0.17834413   , 0.08938856   , 0.11050885   , 0.11551054   ,
  -0.06390449   , 0.17501752   , 0.20376875   , 0.15439524   ,
  -0.007899094  , 0.03526749   ,-0.08832526   , 0.17280823   ,
   0.011950636  , 0.08935961   , 0.06993255   ,-0.0877472    ,
   0.089603916  ,-0.16642301   ,-0.0656005    , 0.12873158   ],
 [-0.09703547   ,-0.19741386   ,-0.0075284047 , 0.005031499  ,
  -0.18231079   , 0.12367711   , 0.101314105  ,-0.022917608  ,
   0.09473078   , 0.06543445   ,-0.031595387  , 0.07471173   ,
  -0.113418855  ,-0.06501601   ,-0.18785453   , 0.16128361   ,
  -0.068065055  , 0.17890085   , 0.06704016   , 0.17249505   ,
   0.026003279  , 0.035395496  , 0.19857892   ,-0.19732098   ,
   0.113701425  ,-0.12132047   , 0.17794012   , 0.100725256  ,
   0.082850516  , 0.16216475   ,-0.008522106  ,-0.108478405  ,
  -0.050518647  , 0.07235113   , 0.038150847  , 0.19017604   ,
  -0.040364552  , 0.054656647  , 0.06964015   ,-0.120175995  ],
 [-0.06937185   , 0.07038172   ,-0.0027683426 ,-0.09931545   ,
   0.1358366    ,-0.048648216  , 0.180407     , 0.20138195   ,
  -0.009814588  ,-0.18315351   ,-0.18535241   , 0.18543656   ,
   0.0759       , 0.18331271   ,-0.00687519   ,-0.08016818   ,
   0.10634876   , 0.05332407   , 0.1908764    ,-0.19240376   ,
   0.13772115   ,-0.1229106    ,-0.16910775   ,-0.08974249   ,
  -0.09412484   ,-0.026606942  ,-0.1645966    ,-0.089761265  ,
   0.041127674  ,-0.018883377  , 0.16928832   , 0.085107245  ,
  -0.032700557  , 0.06498784   ,-0.18754214   , 0.11855163   ,
  -0.026506389  ,-0.15496872   , 0.14662768   , 0.10465858   ],
 [-0.13222072   ,-0.0959256    , 0.09957802   ,-0.070630156  ,
  -0.035803575  , 0.1817797    ,-0.031244418  ,-0.053083006  ,
   0.10246288   , 0.15519455   , 0.14081162   ,-0.17863853   ,
   0.10831632   ,-0.059211455  , 0.07911521   , 0.114276074  ,
   0.20193002   ,-0.044045813  , 0.059750583  , 0.11930817   ,
   0.08877661   , 0.011666727  ,-0.15801728   , 0.09801044   ,
  -0.19378836   , 0.20364882   ,-0.16927823   , 0.10099727   ,
   0.1483364    , 0.18106936   ,-0.042781614  , 0.08159475   ,
   0.08624811   , 0.2032388    ,-0.021828765  ,-0.049450707  ,
   0.06800798   , 0.1054148    ,-0.15061872   ,-0.10536488   ],
 [ 0.061163757  ,-0.123337545  ,-0.16839755   , 0.048687153  ,
  -0.115564086  ,-0.0823858    , 0.1276498    ,-0.15085019   ,
   0.15570804   , 0.051109675  , 0.13466436   ,-0.06593365   ,
  -0.15534161   ,-0.04494818   , 0.14413273   , 0.08010506   ,
   0.13002257   , 0.0027463192 ,-0.014818511  ,-0.10951889   ,
  -0.18688457   , 0.12753914   , 0.031988945  , 0.021788659  ,
   0.06359681   , 0.20121539   , 0.15499574   , 0.006919486  ,
  -0.018694457  ,-0.028283093  , 0.15146042   , 0.07495741   ,
   0.013051093  ,-0.1354658    , 0.1165229    ,-0.112576075  ,
   0.15953724   , 0.14679256   , 0.0055724336 ,-0.18193953   ]])
pesoCamada0 = np.array ([-0.006925694  ,-0.0043847472 , 0.0019122694 ,-0.013417839  ,
 -0.0019036032 , 0.0062931795 ,-0.0012656841 , 0.003561302  ,
 -0.020754054  ,-0.00037905006,-0.0067723705 , 0.0053441194 ,
 -0.010977586  , 0.0035144596 , 0.0009915227 , 0.0044323835 ,
 -0.00050595467, 0.0025656105 , 0.0031640893 ,-0.00014696081,
  0.0019023775 ,-0.011536229  ,-0.0122881485 ,-0.002806244  ,
  0.0031786456 , 0.0021993248 ,-0.0014317582 ,-0.0016314922 ,
 -0.015225991  ,-0.0030324524 ,-0.009769926  ,-0.002494784  ,
  0.011062772  , 0.0024005608 ,-0.006987887  ,-0.0019277785 ,
 -0.010185061  ,-0.0040757232 ,-0.002020863  , 0.009427707  ])
camada1 = np.array ([[ 0.04325666  , 0.12709978  , 0.15846942  , 0.10718184  ,-0.09582965  ,
   0.09458674  ,-0.16611056  , 0.06265183  ,-0.17449541  , 0.08770031  ],
 [ 0.12284818  , 0.08498813  , 0.19069669  , 0.0743503   , 0.10005795  ,
  -0.14911462  ,-0.07674716  , 0.06370644  , 0.08522619  , 0.056250546 ],
 [ 0.18786871  ,-0.0630122   , 0.017974863 , 0.057456765 , 0.11740467  ,
   0.072623186 ,-0.07182145  ,-0.1990978   ,-0.069541074 , 0.03304012  ],
 [-0.11622824  , 0.075737655 ,-0.15841874  ,-0.07756661  ,-0.08125452  ,
  -0.10789747  , 0.19440724  ,-0.040764604 , 0.18240395  , 0.19017433  ],
 [-0.0050067576,-0.17626934  ,-0.019564183 , 0.020523021 , 0.10113186  ,
  -0.039328236 , 0.15634103  ,-0.010588465 , 0.18474987  ,-0.15077344  ],
 [ 0.09689963  , 0.0004221915, 0.026037803 ,-0.05230031  , 0.17851344  ,
   0.12760383  ,-0.17785022  ,-0.12219447  , 0.018199084 , 0.19319357  ],
 [-0.115580246 ,-0.17952694  ,-0.17865986  , 0.007649263 ,-0.045581046 ,
  -0.14108393  , 0.07173508  , 0.09083178  ,-0.033979107 , 0.07808451  ],
 [-0.06639817  , 0.027054463 , 0.05316094  ,-0.029380092 ,-0.104164235 ,
   0.09610258  , 0.18116055  ,-0.15550564  ,-0.042400736 , 0.1263266   ],
 [-0.13938001  ,-0.192311    ,-0.1232141   ,-0.12376396  ,-0.05024695  ,
  -0.098295584 , 0.12354879  , 0.09526803  , 0.18031056  ,-0.00761587  ],
 [-0.07779744  ,-0.16776608  , 0.09654884  , 0.10670392  , 0.1774789   ,
   0.0381376   , 0.13323809  , 0.04765423  , 0.0937234   ,-0.06893554  ],
 [ 0.106504984 , 0.011801434 ,-0.10894003  , 0.12717248  , 0.16921757  ,
  -0.09410214  , 0.094214514 ,-0.19192222  , 0.15004724  ,-0.05203586  ],
 [ 0.09692466  ,-0.08520748  ,-0.17659855  ,-0.07975604  , 0.14787202  ,
   0.0034011756, 0.004414204 , 0.107072614 , 0.15694284  , 0.08140988  ],
 [-0.13741761  , 0.052255914 , 0.13291183  , 0.033239983 ,-0.019796481 ,
  -0.17296833  , 0.0030493836,-0.013666489 , 0.16609292  , 0.17927328  ],
 [ 0.12548253  ,-0.03555674  ,-0.020364128 ,-0.08085866  ,-0.04148369  ,
  -0.16177686  ,-0.16347975  ,-0.046204936 ,-0.13492015  , 0.1997892   ],
 [-0.1812314   , 0.04124959  ,-0.19606538  , 0.13042818  , 0.0314894   ,
  -0.0075135073, 0.027109224 , 0.0033039113, 0.19586092  ,-0.12858653  ],
 [ 0.17688495  ,-0.08058894  , 0.09330138  , 0.12394279  ,-0.008692882 ,
  -0.1662663   , 0.07791751  , 0.050874595 , 0.06496359  ,-0.011956191 ],
 [ 0.016252212 , 0.051964615 ,-0.07029411  ,-0.13037246  ,-0.16555849  ,
  -0.05400267  , 0.11854222  , 0.13284458  ,-0.018367983 ,-0.03298185  ],
 [ 0.19995172  , 0.12908587  , 0.14701253  ,-0.047456477 , 0.012948072 ,
   0.036189925 ,-0.13994725  ,-0.006505405 , 0.058254316 , 0.008574738 ],
 [-0.16926861  , 0.045398224 ,-0.08428064  , 0.013436257 ,-0.18750423  ,
  -0.046932798 , 0.11095461  ,-0.08489493  , 0.14698447  , 0.18084198  ],
 [-0.037789103 ,-0.0407506   , 0.053804208 ,-0.02903073  , 0.092213914 ,
   0.025604535 ,-0.08088855  , 0.14757688  , 0.10359439  , 0.1228254   ],
 [ 0.114266686 , 0.19376436  ,-0.1618668   ,-0.1052095   ,-0.0523821   ,
   0.18537681  , 0.17977148  , 0.09182232  , 0.0012154834,-0.05366998  ],
 [ 0.1523299   , 0.14760467  ,-0.17959657  , 0.028966794 , 0.13540998  ,
   0.06676716  ,-0.1638501   , 0.15591824  , 0.07753467  ,-0.02533858  ],
 [-0.13252406  ,-0.055799983 , 0.18616748  ,-0.16068637  , 0.11001572  ,
  -0.18669333  ,-0.1355632   , 0.09239825  ,-0.03821315  ,-0.06277596  ],
 [-0.13903672  , 0.06857322  ,-0.11339683  ,-0.20758736  ,-0.110609025 ,
   0.09958184  , 0.1195844   , 0.06616663  , 0.16815957  ,-0.16641474  ],
 [ 0.028791415 , 0.046360876 , 0.19737704  , 0.019260833 ,-0.12364582  ,
   0.01093839  ,-0.0549656   ,-0.008999486 ,-0.029384376 ,-0.011975144 ],
 [ 0.05742752  , 0.13564189  , 0.18519257  , 0.05869058  , 0.094047695 ,
   0.16455692  , 0.009961128 ,-0.07500366  , 0.122356646 ,-0.11253323  ],
 [ 0.018362038 , 0.020041179 , 0.14237668  , 0.031370625 ,-0.12081886  ,
   0.013660003 ,-0.15025963  , 0.07331084  ,-0.07721713  , 0.03777272  ],
 [ 0.16240653  , 0.18090405  ,-0.025152482 ,-0.08924772  , 0.067334525 ,
  -0.12648     ,-0.039513763 , 0.11551685  , 0.07031858  ,-0.038334455 ],
 [ 0.0068809176,-0.028150156 , 0.14307803  , 0.13986826  , 0.11460891  ,
  -0.14320262  ,-0.1280904   ,-0.19521777  , 0.18666157  ,-0.07816817  ],
 [ 0.011460083 , 0.04973631  ,-0.16696508  , 0.017937424 ,-0.16506277  ,
  -0.09095173  , 0.14069583  ,-0.056905713 , 0.09498966  ,-0.11921252  ],
 [-0.1234443   ,-0.16165784  ,-0.17043382  ,-0.09009372  , 0.092418045 ,
  -0.13606425  , 0.20743805  , 0.16959444  , 0.10312272  , 0.00554649  ],
 [ 0.08844516  ,-0.005632269 ,-0.09886073  ,-0.16589428  , 0.12813765  ,
  -0.0044535086, 0.14624608  , 0.18592675  ,-0.17961311  , 0.027649626 ],
 [-0.15149693  , 0.052637648 , 0.039310817 ,-0.18963046  ,-0.054008164 ,
  -0.05970518  , 0.18133955  ,-0.05953567  , 0.19647308  , 0.16281326  ],
 [ 0.15442567  ,-0.16698486  , 0.023658937 , 0.08334873  ,-0.15562263  ,
  -0.13109568  , 0.0914367   , 0.0180101   , 0.107837714 , 0.050209597 ],
 [-0.12677492  ,-0.06945218  , 0.11715714  , 0.13230176  ,-0.17476137  ,
   0.016565775 , 0.118514575 ,-0.081516914 ,-0.028115213 ,-0.05412039  ],
 [-0.116906404 , 0.14428559  ,-0.13595103  ,-0.11925814  ,-0.08993767  ,
  -0.029185554 , 0.095646486 , 0.0027388246,-0.0045320024, 0.14913562  ],
 [-0.19721164  , 0.18459825  , 0.048021156 ,-0.12218715  ,-0.051984586 ,
   0.1214288   , 0.13200589  , 0.14333314  ,-0.04473167  ,-0.01568008  ],
 [-0.18037237  , 0.04600811  ,-0.05125997  , 0.056355894 , 0.19191581  ,
  -0.11157605  , 0.061512638 ,-0.049562667 , 0.16867492  ,-0.025155382 ],
 [ 0.07328952  , 0.16571492  ,-0.19546396  , 0.15994619  ,-0.1421041   ,
  -0.15574837  , 0.08984733  , 0.110086136 , 0.0632213   ,-0.1021761   ],
 [-0.18515722  , 0.06193917  , 0.17012607  , 0.102345094 ,-0.03323662  ,
  -0.18397023  , 0.111596905 , 0.07764647  ,-0.04609008  ,-0.13118334  ]])
pesoCamada1 = np.array ([ 0.00157482   ,-0.0010030741 ,-0.0053610345 ,-0.011866594  ,
 -0.00497655   ,-0.002673876  , 0.011971884  , 0.010067145  ,
  0.00053093646, 0.0037751945 ])
camada2 = np.array ([[ 0.07054437 ],
 [ 0.1343195  ],
 [ 0.18689728 ],
 [ 0.16392595 ],
 [ 0.0341718  ],
 [-0.015035666],
 [ 0.16494663 ],
 [ 0.060408495],
 [ 0.14224765 ],
 [ 0.1684669  ]])
pesoCamada2 = np.array ([0.0071226093])
pesoDama = 1.942304742424172

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
        arrayTabuleiro = np.array ([tabuleiroNovo.converteTabuleiroParaArray (pesoDama)])
        
        tabuleiroInvertido = copy.deepcopy (tabuleiroNovo)
        tabuleiroInvertido.inverteVisaoTabuleiro ()
        gerenciadorDeTabuleiros = GerenciadorDeTabuleiros (tabuleiroInvertido)
        listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMultiplasComidas ()
        if (not listaTabuleiros or listaTabuleiros is None):
            listaTabuleiros = gerenciadorDeTabuleiros.calculaPossibilidadesDeMovimentoNormal ()
            
        if (len (listaTabuleiros) == 0 or listaTabuleiros is None):
            scoreTabuleiro = 1.1
        else :
            scoreTabuleiro = np.tanh(np.tanh(np.tanh(arrayTabuleiro.dot(camada0) + pesoCamada0).dot(camada1) + pesoCamada1).dot(camada2) + pesoCamada2)
            
        print(str(scoreTabuleiro), file=sys.stderr)
#        print("Tabuleiro movimento " + str (i), file=sys.stderr)
#        tabuleiroNovo.printaTabuleiro ()
        
        if (scoreTabuleiro > melhorMovimento):
            melhorMovimento = scoreTabuleiro
            jogadaSelecionada = move_string
            
    print (jogadaSelecionada)