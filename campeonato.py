# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:03:15 2019

@author: nocera
"""

import numpy as np
from partida import Partida
import threading

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
        listaPartidas = self.criaPartidas ()
        
        
        print ("COMECANDO AS PARTIDAS!!")
        for partida in listaPartidas:
            partida.realizaPartida ()
            
    def iniciaCampeonato (self):
        for index in range (self.numeroRodadasNoCampeonato):
            self.iniciaRodada ()
            
        index = 0
        for jogador in self.listaJogadores:
            print ("Score Jogador " + str(index) + ": " + str(jogador.currentPoints))
            index += 1
            
        
            