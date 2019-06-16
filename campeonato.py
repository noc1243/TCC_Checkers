# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:03:15 2019

@author: nocera
"""

import numpy as np
from partida import Partida

class Campeonato:
    
    numeroRodadasNoCampeonato = 5
    
    def __init__ (self, listaJogadores):
        self.listaJogadores = listaJogadores
        
    def criaListaDeJogos (self):
        tamanhoArray = len (self.listaJogadores)
        listaDeJogos = np.zeros (tamanhoArray)
        
        for index in range (0, tamanhoArray):
            listaDeJogos [index] = index
            
        np.random.shuffle (listaDeJogos)
        
#        print ("Lista de jogos da rodada:" + str (listaDeJogos))
        
        return listaDeJogos
    
    def iniciaJogo (self, partida):
        partida.realizaPartida ()
        
    def criaPartidas (self):
        listaDeJogos = self.criaListaDeJogos ()
        listaPartidas = []
        
        
        for index in range (0, len (listaDeJogos), 2):
            jogador1 = self.listaJogadores [int(listaDeJogos [index])]
            jogador2 = self.listaJogadores [int(listaDeJogos [index + 1])]
            partida = Partida (jogador1, jogador2)
            listaPartidas.append (partida)
        
        return listaPartidas
        
    def iniciaRodada (self):
        print ("Iniciando Rodada!")
        listaPartidas = self.criaPartidas ()
        
        for partida in listaPartidas:
            print ("Comecando a partida!")
            print (str(partida.jogador1.nomeJogador) + " VS " + str(partida.jogador2.nomeJogador))
            result = partida.realizaPartida ()
            if (result == 0):
                print ("EMPATE!")
            elif (result == 1):
                print (str(partida.jogador1.nomeJogador) + " vence!")
            else:
                print (str(partida.jogador2.nomeJogador) + " vence!")
            
    def iniciaCampeonato (self):
        print ("Iniciando Campeonato!!")
        for index in range (self.numeroRodadasNoCampeonato):
            self.iniciaRodada ()
            
        index = 0
        for jogador in self.listaJogadores:
            print ("Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao))
            index += 1
            
        
            