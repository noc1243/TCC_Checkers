# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 21:58:57 2019

@author: nocera
"""

import numpy as np
from tabuleiro import Tabuleiro
from movimento import Movimento
from casa import Casa

class GerenciadorDeTabuleiros:
    
    PEAO = 1
    INIMIGO = -1
    DAMA = 9
    DAMAINIMIGA = -9
    CASAVAZIA = 0
    
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
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == self.PEAO):
                    listTabuleirosPossiveis.extend (self.criaMovimentoParaOPeao (row, column))
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == self.DAMA):
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
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == self.PEAO):
                    listTabuleirosPossiveis.extend (self.criaMovimentoParaOPeaoComer (row, column))
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == self.DAMA):
                    listTabuleirosPossiveis.extend (self.criaMovimentoParaADamaComer (row, column))
                        
        listTabuleirosPossiveis