# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:49:40 2019

@author: nocera
"""
from tabuleiro import Tabuleiro
from variaveisGlobais import VariaveisGlobais

#Tester inversão de tabuleiro
tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_2)
tabuleiro.printaTabuleiro ()

tabuleiro.inverteVisaoTabuleiro ()
tabuleiro.printaTabuleiro ()