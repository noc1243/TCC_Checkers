# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:42:50 2019

@author: nocera
"""

from campeonato import Campeonato
from jogador import Jogador
from variaveisGlobais import VariaveisGlobais

#print (__name__)

#TESTE CAMPEONATO
if __name__ == '__main__':
    fileResultados = open (VariaveisGlobais.ARQUIVO_RESULTADOS_CAMPEONATO, "a")
    listaJogadores = []
    
    jogador1 = Jogador ()
    jogador2 = Jogador ()
    jogador3 = Jogador ()
    jogador4 = Jogador ()
    jogador5 = Jogador ()
    jogador6 = Jogador ()
    
    listaJogadores.append (jogador1)
    listaJogadores.append (jogador2)
    listaJogadores.append (jogador3)
    listaJogadores.append (jogador4)
    listaJogadores.append (jogador5)
    listaJogadores.append (jogador6)
    
    campeonato = Campeonato (listaJogadores)
    fileResultados.write (campeonato.iniciaCampeonato ())
    fileResultados.close ()