# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 08:51:05 2019

@author: nocera
"""

from keras import backend as K
from jogadorHumano import JogadorHumano
from jogador import Jogador
from tabuleiro import Tabuleiro
from variaveisGlobais import VariaveisGlobais
from partidaHumano import PartidaHumano

from keras.models import Sequential
from keras.layers import Dense
from keras import initializers
from keras.models import load_model

nomeJogador = "Jogador_3b9c6929-d796-451e-b6d0-ea30b9b129c1.h5"

K.clear_session ()

#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_3)

#tabuleiro.printaTabuleiro ()
jogadorHumano = JogadorHumano ()
#tabuleiro = jogadorHumano.fazJogada (tabuleiro)

#tabuleiro.printaTabuleiro ()

model = load_model (".\modelos\\" + nomeJogador)
file = open (".\pesosDamas\\" + nomeJogador, "r")
peso = float (file.read())
file.close ()
jogador = Jogador (model = model, valorDama = peso)

partidaHumano = PartidaHumano (jogadorHumano, jogador)
partidaHumano.realizaPartida ()


