# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:37:06 2019

@author: nocera
"""

import math
import numpy as np
from casa import Casa

class Movimento:
    
    def __init__(self, casaInicial, casaFinal):
        self.casaInicial = casaInicial
        self.casaFinal = casaFinal
        
    def printaMovimento (self):
        self.casaInicial.printaCasa ()
        self.casaFinal.printaCasa ()
        print ("")