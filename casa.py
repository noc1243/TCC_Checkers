# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:44:31 2019

@author: nocera
"""

import math
import numpy as np

class Casa:
    
    def __init__(self, letra, numero):
        self.letra = letra
        self.numero = numero
        
    def converteMovimentoParaArray (self):
        #FEITO DESSA FORMA PARA CORRESPONDER A UM TABULEIRO NORMAL
        numeroLetra = ord(self.letra) - ord('a')
        numeroNumero = 7 - self.numero
        return np.array([numeroNumero, numeroLetra])
    
    def printaCasa (self):
        print (self.letra + " " + str(self.numero))