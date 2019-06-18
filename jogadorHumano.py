# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 08:41:18 2019

@author: nocera
"""

import copy
import numpy as np
from tabuleiro import Tabuleiro
from movimento import Movimento
from casa import Casa

class JogadorHumano:
    
    def __init__ (self):
        print ("Joagador Humano Inicializado!")
        
    def getListaMovimentos (self):
        listaJogadas = []
        
        jogadas = input ("Insira sua jogadas. Cada jogada deve estar demarcada entre \": ")
        jogadas = jogadas.split ("\"")
        
        for jogada in jogadas:
            if (jogada and not jogada == " "):
                separados = jogada.split (" ")
                
                letraInicial = separados [0]
                numeroInicial = int (separados [1])
                casaInicial = Casa (letraInicial, numeroInicial)
                
                
                letraFinal = separados [2]
                numeroFinal = int(separados [3])
                casaFinal = Casa (letraFinal, numeroFinal)
                
                movimento = Movimento (casaInicial, casaFinal)
                
                listaJogadas.append (movimento)
            
        return listaJogadas
            
        
        
    def fazJogada (self, tabuleiro):
        jogadaEfetuada = False
        
        tabuleiroASerJogado = copy.deepcopy (tabuleiro)
        
        tabuleiro.printaTabuleiro ()
        while (not jogadaEfetuada):
            listaJogadas = self.getListaMovimentos ()
            
            if (len (listaJogadas) == 1):
                if (tabuleiroASerJogado.doAnyMovement (listaJogadas [0])):
                    jogadaEfetuada = True
            else:
                tabuleiroASerJogado.doMultipleMovementsComer (listaJogadas)
                if (not np.array_equal (tabuleiroASerJogado.tabuleiroConfiguracao, tabuleiro.tabuleiroConfiguracao)):
                    jogadaEfetuada = True
            
            if (not jogadaEfetuada):
                print ("Jogada inválida! Insira sua jogada novamente")
                
            
        return tabuleiroASerJogado
        
#        for jogada in listaJogadas:
#            jogada.printaMovimento ()
        
