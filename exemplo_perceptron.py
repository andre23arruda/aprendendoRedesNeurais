# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:26:55 2019
@author: Andre
"""

#%% Criando entrada
import numpy as np
x = np.array([[0,0],[0,1],[1,0],[1,1]]) # Entrada para porta lógica E
classe = np.array([0,0,0,1]) # resultado para operação E

#%% Função Degrau
def stepFunction(x):
    if x>=1:
        return 1
    return 0

#%% Perceptron
tamanho = x.shape
soma = np.zeros(tamanho[0])
peso = np.array([0,0],dtype = 'float')
taxaAprendizagem = 0.1
erro = np.ones(tamanho[0])
soma_erro = 1
while True:
    for i in range(tamanho[0]):
        soma[i] = stepFunction(np.sum(x[i,:]*peso))
    erro = classe-soma
    soma_erro = np.sum(erro)
    if soma_erro == 0:
        break
    posicao_maior_erro = np.where(erro == np.max(erro))
    posicao_maior_erro = posicao_maior_erro[0]
    for i in range(tamanho[1]):
        peso[i] = peso[i] + (taxaAprendizagem*x[posicao_maior_erro,i]*erro[posicao_maior_erro])

#%% Testes
#z = [0,0]
#for i in range(tamanho[0]):
#    soma[i] = np.sum(stepFunction(x[i,:]*peso))
#erro = classe-soma
#soma_erro = np.sum(erro)
#posicao_maior_erro = np.where(erro == np.max(erro))
#posicao_maior_erro = posicao_maior_erro[0]
#for i in range(tamanho[1]):
#    peso[i] = peso[i] + (taxaAprendizagem*x[posicao_maior_erro,i]*erro[posicao_maior_erro]) 