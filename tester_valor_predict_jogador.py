# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:56:30 2019

@author: nocera
"""

from tabuleiro import Tabuleiro
from jogador import Jogador
from variaveisGlobais import VariaveisGlobais

#Tester valor do Predict para um tabuleiro
jogador1 = Jogador (debug = True)

tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_2)
tabuleiro.printaTabuleiro ()

print (jogador1.predict (tabuleiro.converteTabuleiroParaArray (jogador1.valorDama)))