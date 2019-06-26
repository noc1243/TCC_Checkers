# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:08:50 2019

@author: nocera
"""

import random
from keras import backend as K
from seletorNatural import SeletorNatural

# VARIAVEL PARA FORCAR UMA SEED DIFERENTE CASO SEJA NECESSARIO ALGUM TESTE
VARIASEED = 0

listaJogadores = []

# FEITO PARA QUE OS RESULTADOS TENDAM A SER IGUAIS SEMPRE
random.seed (16062019 + VARIASEED)

# FEITO PARA GARANTIR QUE NAO EXISTE NENHUM LIXO DE MEMORIA DE MODELO DEIXANDO O CODIGO LENTO
K.clear_session ()

# INPUT = NUMERO DE GERACOES
if __name__ == '__main__':
    seletorNatural = SeletorNatural (500)
    seletorNatural.iniciaTreinamento ()