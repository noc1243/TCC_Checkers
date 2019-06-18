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


nomeJogador = "Jogador_cf3fbbde-530e-43de-b401-542d0d0ad867.h5"

K.clear_session ()

tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE)
tabuleiro.printaTabuleiro ()

#Tester selecionaMelhorJogada
model = load_model (".\melhores_modelos\\" + nomeJogador)
    
jogador1 = Jogador (debug = True, model = model)
    
    
tabuleiro2 = jogador1.selecionaMelhorJogadaMinMax (tabuleiro, 0)
print ("Tabuleiro Selecionado:")
tabuleiro2.printaTabuleiro ()