# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:51:29 2019

@author: nocera
"""

from tabuleiro import Tabuleiro
from variaveisGlobais import VariaveisGlobais
from jogador import Jogador

#Tester selecionaMelhorJogada
jogador1 = Jogador (debug = True)

tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE)
tabuleiro.printaTabuleiro ()

tabuleiro2 = jogador1.selecionaMelhorJogadaMinMax (tabuleiro, 0)
print ("Tabuleiro Selecionado:")
tabuleiro2.printaTabuleiro ()