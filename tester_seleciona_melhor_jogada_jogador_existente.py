# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:51:29 2019

@author: nocera
"""

from keras import backend as K
from tabuleiro import Tabuleiro
from variaveisGlobais import VariaveisGlobais
from jogador import Jogador
from keras.models import Sequential
from keras.layers import Dense
from keras import initializers
from keras.models import load_model


nomeJogador = "Jogador_ab522a91-9c91-4822-b776-8626f91539f5.h5"

K.clear_session ()

tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_4)
tabuleiro.printaTabuleiro ()

#Tester selecionaMelhorJogada
model = load_model (".\melhores_modelos\\" + nomeJogador)
file = open (".\melhores_pesos\\" + nomeJogador, "r")
peso = float (file.read())
    
jogador1 = Jogador (debug = True, model = model, valorDama = peso)
#jogador1.printaPesos()
    
    
tabuleiro2 = jogador1.selecionaMelhorJogadaMinMax (tabuleiro, 0)
print ("Tabuleiro Selecionado:")
tabuleiro2.printaTabuleiro ()