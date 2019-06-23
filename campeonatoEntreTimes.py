# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:40:58 2019

@author: diogo
"""

import numpy as np
from partida import Partida
from variaveisGlobais import VariaveisGlobais
import threading
import time

class CampeonatoEntreTimes:    
    
    numeroRodadasNoCampeonato = 5
    
    def __init__ (self, listaJogadoresOriginais, listaJogadoresNovos):
        self.listaJogadoresOriginais = listaJogadoresOriginais
        self.listaJogadoresNovos = listaJogadoresNovos
        
        self.fileResultados = open (str(VariaveisGlobais.ARQUIVO_RESULTADOS_CAMPEONATO_ENTRE_TIMES), "a")
        
    def criaListaDeJogos (self):
        tamanhoArray = len (self.listaJogadoresOriginais)
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
        jogadoresOriginais = self.criaListaDeJogos ()
        jogadoresNovos = self.criaListaDeJogos ()
        listaPartidas = []
        
        
        for index in range (len (jogadoresOriginais)):
            jogador1 = self.listaJogadoresOriginais [int(jogadoresOriginais [index])]
            jogador2 = self.listaJogadoresNovos [int(jogadoresNovos [index])]
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
        self.fileResultados.write ("Comecando as partidas\n")
        threads = []
        results = []
        for partida in listaPartidas:
            print (str(partida.jogador1.nomeJogador) + " VS " + str(partida.jogador2.nomeJogador))
            self.fileResultados.write (str(partida.jogador1.nomeJogador) + " VS " + str(partida.jogador2.nomeJogador) + "\n")
            t = threading.Thread(target=self.iniciaJogo, args=(partida, results,))
            threads.append (t)
            t.start ()
            time.sleep (0.5)
            
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
        self.fileResultados.write ("iniciando Campeonato!!\n")
        for index in range (self.numeroRodadasNoCampeonato):
            self.iniciaRodada ()
            
        index = 0
        print ("Jogadores Originais:")
        self.fileResultados.write ("Jogadores Originais:\n")
        for jogador in self.listaJogadoresOriginais:
            print ("Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao) + " Pontos totais do jogador: " + str (jogador.totalPoints) + " Fit Real do jogador: " + str (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo)))
            self.fileResultados.write ("Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao) + " Pontos totais do jogador: " + str (jogador.totalPoints) + " Fit Real do jogador: " + str (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo)) + "\n")
            index += 1
        
        print ("Jogadores Novos:")
        self.fileResultados.write ("Jogadores Novos:\n")
        for jogador in self.listaJogadoresNovos:
            print ("Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao) + " Pontos totais do jogador: " + str (jogador.totalPoints) + " Fit Real do jogador: " + str (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo)))
            self.fileResultados.write ("Score " + str(jogador.nomeJogador) + " " + str(index) + ": " + str(jogador.currentPoints) + " Geracao Jogador: " + str (jogador.geracao) + " Pontos totais do jogador: " + str (jogador.totalPoints) + " Fit Real do jogador: " + str (float (jogador.totalPoints)/float (jogador.numeroDeGeracoesVivo)) + "\n")
            index += 1
            
        self.fileResultados.close ()
        
    def __del__ (self):
        self.fileResultados.close ()