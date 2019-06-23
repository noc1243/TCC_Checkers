# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:06:42 2019

@author: nocera
"""

import numpy as np

class VariaveisGlobais :
    TABULEIRO_INICIAL = np.array ([[0, -1, 0, -1, 0, -1, 0, -1], 
                                   [-1, 0, -1, 0, -1, 0, -1, 0], 
                                   [0, -1, 0, -1, 0, -1, 0, -1], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [1, 0, 1, 0, 1, 0, 1, 0], 
                                   [0, 1, 0, 1, 0, 1, 0, 1], 
                                   [1, 0, 1, 0, 1, 0, 1, 0]])
    
    TABULEIRO_TESTE =   np.array ([[0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, -1, 0, -1, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, -1, 0, -1, 0, 0, 0, 0], 
                                   [0, 0, 9, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
    
    TABULEIRO_TESTE_2 =   np.array ([[0, 0, 0, 0, 0, 0, 0, -1], 
                                   [-1, 0, 0, 0, -1, 0, -1, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [-1, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, -1, 0, 0, 0, -1], 
                                   [-9, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, -9, 0, 1, 0]])
    
    TABULEIRO_TESTE_3 =   np.array ([[0, -1, 0, -1, 0, -1, 0, -1], 
                                   [0, 0, -1, 0, -1, 0, -1, 0], 
                                   [0, -1, 0, -1, 0, -1, 0, 0], 
                                   [0, 0, -1, 0, 0, 0, -1, 0], 
                                   [0, 1, 0, 0, 0, 0, 0, 1], 
                                   [1, 0, 1, 0, 1, 0, 0, 0], 
                                   [0, 0, 0, 1, 0, 1, 0, 1], 
                                   [1, 0, 1, 0, 1, 0, 1, 0]])
    
    TABULEIRO_TESTE_4 =   np.array ([[0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, -1, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, -1, 0], 
                                   [0, 0, 0, 0, 0, 1, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, -1, 0], 
                                   [0, 0, 0, 0, 0, 1, 0, 0], 
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
    
    PEAO = 1
    INIMIGO = -1
    DAMA = 9
    DAMAINIMIGA = -9
    CASAVAZIA = 0
    
    ARQUIVO_RESULTADOS_SELETOR = ".\\resultados_treinamento\\resultados_seletor.txt"
    ARQUIVO_RESULTADOS_CAMPEONATO = ".\\resultados_treinamento\\resultados_campeonato.txt"
    ARQUIVO_RESULTADOS_CAMPEONATO_ENTRE_TIMES = ".\\resultados_treinamento\\resultados_campeonato_entre_times.txt"