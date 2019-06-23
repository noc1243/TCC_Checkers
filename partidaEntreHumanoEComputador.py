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

nomeJogador = "Jogador_ab522a91-9c91-4822-b776-8626f91539f5.h5"

K.clear_session ()

#tabuleiro = Tabuleiro (VariaveisGlobais.TABULEIRO_TESTE_3)

#tabuleiro.printaTabuleiro ()
jogadorHumano = JogadorHumano ()
#tabuleiro = jogadorHumano.fazJogada (tabuleiro)

#tabuleiro.printaTabuleiro ()

model = load_model (".\melhores_modelos\\" + nomeJogador)
file = open (".\melhores_pesos\\" + nomeJogador, "r")
peso = float (file.read())
file.close ()
jogador = Jogador (model = model, valorDama = peso)

partidaHumano = PartidaHumano (jogadorHumano, jogador)
partidaHumano.realizaPartida ()


