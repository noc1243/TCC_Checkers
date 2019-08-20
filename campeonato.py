# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:03:15 2019

@author: nocera
"""

import numpy as np
from partida import Partida
from variaveisGlobais import VariaveisGlobais
import threading
import time

class Campeonato:
    
    numeroRodadasNoCampeonato = 5
    
    def __init__ (self, listaJogadores):
        self.listaJogadores = listaJogadores
        
        self.fileResultados = open (str(VariaveisGlobais.ARQUIVO_RESULTADOS_CAMPEONATO), "a")
        
    def criaListaDeJogos (self):
        tamanhoArray = len (self.listaJogadores)
        listaDeJogos = np.zeros (tamanhoArray)
        
        for index in range (0, tamanhoArray):
            listaDeJogos [index] = index
            
        np.random.shuffle (listaDeJogos)
        
#        print ("Lista de jogos da rodada:" + str (listaDeJogos))
        
        return listaDeJogos
    
    def iniciaJogo (self, partida, results):
        resultadoString = ""
        result = partida.realizaPartida ()
        
        if (result == 0):
            resultadoString = "EMPATE!"
        elif (result == 1):
            resultadoString = str(partida.jogador1.nomeJogador) + " venceu!"
        else:
            resultadoString = str(partida.jogador2.nomeJogador) + " venceu!"
        
        results.append (resultadoString)
        
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
        self.fileResultados.write ("Iniciando Rodada!\n")
        listaPartidas = self.criaPartidas ()

        print ("Comecando as partidas!")        
        self.fileResultados.write ("Comecando as partidas!\n")
        threads = []
        results = []
        for partida in listaPartidas:
            print (str(partida.jogador1.nomeJogador) + " VS " + str(partida.jogador2.nomeJogador))
            self.fileResultados.write (str(partida.jogador1.nomeJogador) + " VS " + str(partida.jogador2.nomeJogador) + "\n")
            t = threading.Thread(target=self.iniciaJogo, args=(partida, results,))
            threads.append (t)
            t.start ()
            time.sleep (0.1)
            
        indexPartidas = 0    
        print ("Esperando partidas terminarem!")
        self.fileResultados.write ("Esperando partidas terminarem!\n")
        for thread in threads:
            thread.join ()
            print (results [indexPartidas])
            self.fileResultados.write (results [indexPartidas] + "\n")
            indexPartidas += 1
            
        
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
        self.fileResultados.write ("Iniciando Campeonato!!\n")
        for index in range (self.numeroRodadasNoCampeonato):
            self.iniciaRodada ()
            
        index = 0
        for jogador in self.listaJogadores:
            print ("Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao) + " Pontos totais do jogador: " + str (jogador.totalPoints) + " Fit Real do jogador: " + str (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo)) + " Sigma 1 Jogador: " + str (jogador.listaSigmas [0] [0]))
            self.fileResultados.write ("Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao) + " Pontos totais do jogador: " + str (jogador.totalPoints) + " Fit Real do jogador: " + str (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo)) + " Sigma 1 Jogador: " + str (jogador.listaSigmas [0] [0]) + "\n")
            index += 1
            
        self.fileResultados.close ()
        
            