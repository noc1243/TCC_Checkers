# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:03:15 2019

@author: nocera
"""

import numpy as np
from partida import Partida
from variaveisGlobais import VariaveisGlobais
import multiprocessing
import time

class Campeonato:
    
    queue = multiprocessing.Queue ()
    
    numeroRodadasNoCampeonato = 5
    
    def __init__ (self, listaJogadores):
        self.listaJogadores = listaJogadores
        
        self.stringResultados = ""
        
    def criaListaDeJogos (self):
        tamanhoArray = len (self.listaJogadores)
        listaDeJogos = np.zeros (tamanhoArray)
        
        for index in range (0, tamanhoArray):
            listaDeJogos [index] = index
            
        np.random.shuffle (listaDeJogos)
        
#        print ("Lista de jogos da rodada:" + str (listaDeJogos))
        
        return listaDeJogos
    
    def iniciaJogo (self, partida, queue, index):
        resultadoString = ""
        result = partida.realizaPartida ()
        
        if (result == 0):
            resultadoString = "EMPATE!"
        elif (result == 1):
            resultadoString = str(partida.jogador1.nomeJogador) + " venceu!"
        else:
            resultadoString = str(partida.jogador2.nomeJogador) + " venceu!"
        
        queue.put ([resultadoString, result, index])
        return resultadoString
        
    def criaPartidas (self):
        listaDeJogos = self.criaListaDeJogos ()
        listaPartidas = []
        
        
        for index in range (0, len (listaDeJogos), 2):
            jogador1 = self.listaJogadores [int(listaDeJogos [index])]
            jogador2 = self.listaJogadores [int(listaDeJogos [index + 1])]
            partida = Partida (jogador1, jogador2)
            partida2 = Partida (jogador2, jogador1)
            listaPartidas.append (partida)
            listaPartidas.append (partida2)
        
        return listaPartidas
        
    def iniciaRodada (self):
        print ("Iniciando Rodada!")
        self.stringResultados += " Iniciando Rodada!\n"
        listaPartidas = self.criaPartidas ()

        print ("Comecando as partidas!")     
        self.stringResultados += " Comecando as partidas!\n"
        index = 0
        threads = []
        for partida in listaPartidas:
            print (str(partida.jogador1.nomeJogador) + " VS " + str(partida.jogador2.nomeJogador))
            self.stringResultados += " " + str(partida.jogador1.nomeJogador) + " VS " + str(partida.jogador2.nomeJogador) + "\n"
            t = multiprocessing.Process(target=self.iniciaJogo, args=(partida, self.queue, index,))
            threads.append (t)
            t.start ()
            time.sleep (0.1)
            index += 1
            
        indexPartidas = 0    
        print ("Esperando partidas terminarem!")
        self.stringResultados += " Esperando partidas terminarem!\n"
        for thread in threads:
            thread.join ()
            indexPartidas += 1
            
        self.queue.put (None)
        for q in iter(self.queue.get, None):
            if (q [1] == 1):
                listaPartidas [int(q [2])].jogador1.ganhaPartida ()
                listaPartidas [int(q [2])].jogador2.perdePartida ()
            elif (q [1] == -1):
                listaPartidas [int(q [2])].jogador1.perdePartida ()
                listaPartidas [int(q [2])].jogador2.ganhaPartida ()
            else:
                listaPartidas [int(q [2])].jogador1.empataPartida ()
                listaPartidas [int(q [2])].jogador2.empataPartida ()
        
#        CODIGO SINGLE-THREAD FUNIONANDO!!
#        for partida in listaPartidas:
#            print ("Comecando a partida!")
#            print (str(partida.jogador1.nomeJogador) + " VS " + str(partida.jogador2.nomeJogador))
#            result = partida.realizaPartida ()
#            if (result == 0):
#                print ("EMPATE!")
#            elif (result == 1):
#                print (str(partida.jogador1.nomeJogador) + " vence!")
#            else:
#                print (str(partida.jogador2.nomeJogador) + " vence!")
            
    def iniciaCampeonato (self):
        print ("Iniciando Campeonato!!")
        self.stringResultados += " Iniciando Campeonato!!\n"
        for index in range (self.numeroRodadasNoCampeonato):
            self.iniciaRodada ()
            
        index = 0
        for jogador in self.listaJogadores:
            print ("Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao) + " Pontos totais do jogador: " + str (jogador.totalPoints) + " Fit Real do jogador: " + str (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo)))
            self.stringResultados += " Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao) + " Pontos totais do jogador: " + str (jogador.totalPoints) + " Fit Real do jogador: " + str (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo)) + "\n"
            index += 1
            
        return self.stringResultados
        
            