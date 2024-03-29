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
    
    numeroDeJogadasParaChecarTabuleiro = 50
    numeroDePecasParaChecarTabuleiro = 2
    diferencaDePecasParaDarDerrota = 3
    
    numeroMaximoDeJogadas = 100
    
    def __init__ (self, jogador1, jogador2, debug = False):
        self.tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_INICIAL)
        
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        
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
                tabuleiroEscolhido = self.jogador1.selecionaMelhorJogadaMinMax (copy.deepcopy(self.tabuleiro), 0)
                
                if (tabuleiroEscolhido == None or self.avaliaTabuleiroDerrota ()):
                    if (self.debug):
                        print ("ACABOU O JOGO NAO TEM MAIS JOGADA!!")
                        self.tabuleiro.printaTabuleiro ()
                        
                    self.jogador1.perdePartida()
                    self.jogador2.ganhaPartida()
                    return -1
                    
                self.tabuleiro = copy.deepcopy(tabuleiroEscolhido)
                
                if (self.debug):
                    self.tabuleiro.printaTabuleiro ()
            else:
                tabuleiroEscolhido = self.jogador2.selecionaMelhorJogadaMinMax (copy.deepcopy(self.tabuleiro), 0)
                
                if (tabuleiroEscolhido == None or self.avaliaTabuleiroDerrota ()):
                    if (self.debug):
                        print ("ACABOU O JOGO NAO TEM MAIS JOGADA!!")
                        self.tabuleiro.printaTabuleiro ()
                        
                    self.jogador1.ganhaPartida()
                    self.jogador2.perdePartida()
                    return 1
                    
                self.tabuleiro = copy.deepcopy (tabuleiroEscolhido)
                
                if (self.debug):
                    self.tabuleiro.printaTabuleiro ()
                
            self.tabuleiro.inverteVisaoTabuleiro ()
            self.turnoJogador1 = not self.turnoJogador1
            
        self.jogador1.empataPartida()
        self.jogador2.empataPartida()
        
        return 0
    
    def contaNumeroPecasJogador (self):
        numeroDePecas = 0
        for row in range (self.tabuleiro.tabuleiroConfiguracao.shape [0]):
            for column in range (self.tabuleiro.tabuleiroConfiguracao.shape [1]):
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.PEAO or self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.DAMA):
                    numeroDePecas += 1
        
        return numeroDePecas
    
    def contaDiferencaDePecas (self):
        numeroDePecas = 0
        for row in range (self.tabuleiro.tabuleiroConfiguracao.shape [0]):
            for column in range (self.tabuleiro.tabuleiroConfiguracao.shape [1]):
                if (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.PEAO or self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.DAMA):
                    numeroDePecas += 1
                elif (self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.INIMIGO or self.tabuleiro.tabuleiroConfiguracao [row, column] == VariaveisGlobais.DAMAINIMIGA):
                    numeroDePecas -= 1
        
        return numeroDePecas
    
    def avaliaTabuleiroDerrota (self):
        return False
#        if (self.numeroJogadas >= self.numeroDeJogadasParaChecarTabuleiro):
#            numeroDePecas = self.contaNumeroPecasJogador ()
#            
#            if (numeroDePecas <= self.numeroDePecasParaChecarTabuleiro):
#                numeroDeDiferecaDePecas = self.contaDiferencaDePecas ()
#                if (numeroDeDiferecaDePecas <= (-1) * self.diferencaDePecasParaDarDerrota):
#                    return True
#                else:
#                    return False
#            else:
#                return False
#        else:
#            return False
            