# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 21:58:57 2019

@author: nocera
"""

import numpy as np
from tabuleiro import Tabuleiro
from movimento import Movimento
from casa import Casa
from variaveisGlobais import VariaveisGlobais
import copy

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
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaOPeaoComer (row - 2, column - 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None):
                    listaDeListaDeMovimentos.extend (copy.deepcopy (listaDeListaDeMovimentosResultado))
                    
                listaMovimentos.remove (movimento1)
                
        if (not movimento2 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento2, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento2)
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaOPeaoComer (row - 2, column + 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None or not listaDeListaDeMovimentosResultado):
                    listaDeListaDeMovimentos.extend (copy.deepcopy (listaDeListaDeMovimentosResultado))
                    
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
                
                if (not listaDeListaDeMovimentosResultado is None):
                    listaDeListaDeMovimentos.extend (copy.deepcopy (listaDeListaDeMovimentosResultado))
                    
                listaMovimentos.remove (movimento1)
                
        if (not movimento2 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento2, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento2)
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaADamaComer (row - 2, column + 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None or not listaDeListaDeMovimentosResultado):
                    listaDeListaDeMovimentos.extend (copy.deepcopy (listaDeListaDeMovimentosResultado))
                    
                listaMovimentos.remove (movimento2)
                
        if (not movimento3 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento3, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento3)
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaADamaComer (row - 2, column - 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None):
                    listaDeListaDeMovimentos.extend (copy.deepcopy (listaDeListaDeMovimentosResultado))
                    
                listaMovimentos.remove (movimento3) 
                
        if (not movimento4 is None):
            novoTabuleiro = self.criaTabuleiroAPartirDeUmMovimentoEUmTabuleiro (movimento4, tabuleiro)
            if (not novoTabuleiro is None):
                listaMovimentos.append (movimento4)
                listaDeListaDeMovimentos.append (copy.deepcopy (listaMovimentos))
                listaDeListaDeMovimentosResultado = self.criaMultiplosMovimentosParaADamaComer (row - 2, column - 2, copy.deepcopy(listaMovimentos), novoTabuleiro)
                
                if (not listaDeListaDeMovimentosResultado is None):
                    listaDeListaDeMovimentos.extend (copy.deepcopy (listaDeListaDeMovimentosResultado))
                    
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