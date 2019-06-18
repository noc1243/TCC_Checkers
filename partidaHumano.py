# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:16:07 2019

@author: nocera
"""

from variaveisGlobais import VariaveisGlobais
from tabuleiro import Tabuleiro
from jogador import Jogador
import copy

class PartidaHumano:
    
    numeroMaximoDeJogadas = 100
    
    def __init__ (self, jogadorHumano, jogador, debug = False):
        self.tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_INICIAL)
        
        self.jogadorHumano = jogadorHumano
        self.jogador = jogador
        
        self.turnoJogador1 = True
        
        self.debug = debug
        
    # RETONROS: 0 = EMPATE; 1 = VITORIA JOGADOR 1; -1 = VITORIA JOGADOR 2;
    def realizaPartida (self):
        if (self.debug):
            print ("PARTIDA INICIADA!!!")
            
        for self.numeroJogadas in range (0, self.numeroMaximoDeJogadas):
            if (self.debug):
                print ("JOGADA: " + str (self.numeroJogadas))
                if (self.turnoJogador1):
                    print ("JOGADA JOGADOR 1:")
                else:
                    print ("JOGADA JOGADOR 2:")
                
            if (self.turnoJogador1):
                tabuleiroEscolhido = self.jogadorHumano.fazJogada (copy.deepcopy(self.tabuleiro))
                
                if (tabuleiroEscolhido == None):
                    if (self.debug):
                        print ("ACABOU O JOGO NAO TEM MAIS JOGADA!!")
                        self.tabuleiro.printaTabuleiro ()
                        
                    return -1
                    
                self.tabuleiro = copy.deepcopy(tabuleiroEscolhido)
                
                if (self.debug):
                    self.tabuleiro.printaTabuleiro ()
            else:
                tabuleiroEscolhido = self.jogador.selecionaMelhorJogadaMinMax (copy.deepcopy(self.tabuleiro), 0)
                
                if (tabuleiroEscolhido == None):
                    if (self.debug):
                        print ("ACABOU O JOGO NAO TEM MAIS JOGADA!!")
                        self.tabuleiro.printaTabuleiro ()
                        
                    return 1
                    
                self.tabuleiro = copy.deepcopy (tabuleiroEscolhido)
                
                if (self.debug):
                    self.tabuleiro.printaTabuleiro ()
                
            self.tabuleiro.inverteVisaoTabuleiro ()
            self.turnoJogador1 = not self.turnoJogador1
            
        
        return 0
    
    