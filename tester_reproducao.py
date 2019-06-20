# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:41:23 2019

@author: nocera
"""

from tabuleiro import Tabuleiro
from variaveisGlobais import VariaveisGlobais
from jogador import Jogador
from seletorNatural import SeletorNatural
import copy

#Tester selecionaMelhorJogada
jogador1 = Jogador (debug = True)
jogador1.printaPesos ()

print ("")
print ("")
print ("")
print ("")
print ("")

seletorNatural = SeletorNatural (1)
jogador2 = seletorNatural.repdroduzJogador (jogador1)
jogador2.printaPesos ()
jogador2.debug = True

print ("")
print ("")
print ("")
print ("")
print ("")

tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE)
tabuleiro.printaTabuleiro ()

tabuleiro2 = jogador1.selecionaMelhorJogadaMinMax (copy.deepcopy(tabuleiro), 0)

print ("")
print ("")
print ("")
print ("")
print ("JOGADOR 2")

tabuleiro3 = jogador2.selecionaMelhorJogadaMinMax (tabuleiro, 0)
print ("Tabuleiro Selecionado:")
#tabuleiro2.printaTabuleiro ()