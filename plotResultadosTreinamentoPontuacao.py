# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:06:05 2019

@author: nocera
"""

import csv
import matplotlib.pyplot as plt
from variaveisGlobais import VariaveisGlobais

geracaoInicial = 0
numeroDeGeracoesASeremAnalisadas = 50
colocacoesJogadoresASeremAnalisados = 30

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
                if (not (row[i].split("_")[0] + row[i].split("_")[1] in dictPlots)):
                    dictPlots [row[i].split("_")[0] + row[i].split("_")[1]] = []
                    listaY = []
                    listaX = []
                    listaY.append (index + geracaoAtual)
                    listaX.append (float(row[i].split("_")[2]))
                    dictPlots [row[i].split("_")[0] + row[i].split("_")[1]].append (listaY)
                    dictPlots [row[i].split("_")[0] + row[i].split("_")[1]].append (listaX)
                else:
                    dictPlots [row[i].split("_")[0] + row[i].split("_")[1]] [0].append (index + geracaoAtual)
                    dictPlots [row[i].split("_")[0] + row[i].split("_")[1]] [1].append (float(row[i].split("_")[2]))
                    print (row[i].split("_")[2])
            index += 1
        
        return dictPlots
    
def plotJogadores (dictPlots):
    maxTicks = -20
    legenda = []
    plt.figure(num=None, figsize=(100, 30), dpi=80, facecolor='w', edgecolor='k')
    for jogador in dictPlots:
#        print (str(dictPlots [jogador] [0]) + ", " + str(dictPlots [jogador] [1]))
        plt.plot(dictPlots [jogador] [0], dictPlots [jogador] [1])
        legenda.append (jogador)
        print ("plotando!! : " + jogador)
        
#        if (maxTicks < dictPlots [jogador] [1]):
#            maxTicks = dictPlots [jogador] [1]
    
    plt.xticks(range (numeroDeGeracoesASeremAnalisadas))
    plt.grid ()
    plt.xlabel('Geracao')
    plt.ylabel('Pontuacao')
    plt.title('Caminho dos Jogadores ao longo das geracoes')
#    plt.legend (legenda)
    plt.savefig(VariaveisGlobais.IMAGEM_RESULTADO_TREINAMENTO_PONTUACAO)
    
dictPlots = getListaParaPlot ()
plotJogadores (dictPlots)
