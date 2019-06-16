# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 21:13:23 2019

@author: nocera
"""

from variaveisGlobais import VariaveisGlobais
from tabuleiro import Tabuleiro
from jogador import Jogador
import copy

class Partida:    
    
    numeroMaximoDeJogadas = 100
    
    def __init__ (self, jogador1, jogador2):
        self.tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_INICIAL)
        
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        
        self.turnoJogador1 = True
        
    def realizaPartida (self):
        for numeroJogadas in range (0, self.numeroMaximoDeJogadas):
            print ("JOGADA: " + str (numeroJogadas))
            if (self.turnoJogador1):
                print ("JOGADA JOGADOR 1:")
            else:
                print ("JOGADA JOGADOR 2:")
                
            if (self.turnoJogador1):
                tabuleiroEscolhido = self.jogador1.selecionaMelhorJogada (copy.deepcopy(self.tabuleiro), 0)
                
                if (tabuleiroEscolhido == None):
                    print ("ACABOU O JOGO NAO TEM MAIS JOGADA!!")
                    self.tabuleiro.printaTabuleiro ()
                    break
                    
                self.tabuleiro = copy.deepcopy(tabuleiroEscolhido)
                self.tabuleiro.printaTabuleiro ()
            else:
                tabuleiroEscolhido = self.jogador2.selecionaMelhorJogada (copy.deepcopy(self.tabuleiro), 0)
                
                if (tabuleiroEscolhido == None):
                    print ("ACABOU O JOGO NAO TEM MAIS JOGADA!!")
                    self.tabuleiro.printaTabuleiro ()
                    break
                    
                self.tabuleiro = copy.deepcopy (tabuleiroEscolhido)
                self.tabuleiro.printaTabuleiro ()
                
            self.tabuleiro.inverteVisaoTabuleiro ()
            self.turnoJogador1 = not self.turnoJogador1
        