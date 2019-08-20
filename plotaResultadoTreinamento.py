# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:06:05 2019

@author: nocera
"""

import csv
import matplotlib.pyplot as plt
from variaveisGlobais import VariaveisGlobais

geracaoInicial = 100
numeroDeGeracoesASeremAnalisadas = 15
colocacoesJogadoresASeremAnalisados = 15

def getListaParaPlot ():
    global numeroDeGeracoesASeremAnalisadas
    global geracaoInicial
    global colocacoesJogadoresASeremAnalisados
    
    with open(VariaveisGlobais.ARQUIVO_LISTA_JOGADORES_GERACAO) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        index = 0
        geracaoAtual = 0
        dictPlots = {}
        primeiraLinha = True
        for row in readCSV:
            
            if (index >= numeroDeGeracoesASeremAnalisadas):
                break
            if (primeiraLinha):
                primeiraLinha = False
                continue
            if (geracaoAtual < geracaoInicial):
                geracaoAtual += 1
                continue
            
            for i in range (colocacoesJogadoresASeremAnalisados):
                if (not (row[i] in dictPlots)):
                    dictPlots [row[i]] = []
                    listaY = []
                    listaX = []
                    listaY.append (index + geracaoAtual)
                    listaX.append (i)
                    dictPlots [row[i]].append (listaY)
                    dictPlots [row[i]].append (listaX)
                else:
                    dictPlots [row[i]] [0].append (index + geracaoAtual)
                    dictPlots [row[i]] [1].append (i)
            index += 1
        
        return dictPlots
    
def plotJogadores (dictPlots):
    legenda = []
    plt.figure(num=None, figsize=(30, 30), dpi=80, facecolor='w', edgecolor='k')
    for jogador in dictPlots:
        plt.plot(dictPlots [jogador] [0], dictPlots [jogador] [1])
        legenda.append (jogador)
        print ("plotando!! : " + jogador)
    
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    plt.grid ()
    plt.xlabel('Geracao')
    plt.ylabel('Colocacao')
    plt.title('Caminho dos Jogadores ao longo das geracoes')
#    plt.legend (legenda)
    plt.savefig(VariaveisGlobais.IMAGEM_RESULTADO_TREINAMENTO)
    
dictPlots = getListaParaPlot ()
plotJogadores (dictPlots)
