import numpy as np
ALFABETO = 'abcdefghijklmnopqrstuvwxyz ,.@:-_'
TAMANHO_ALFABETO = len(ALFABETO)
MATRIZ_ALFABETO = np.identity(TAMANHO_ALFABETO,dtype=int)
# print(MATRIZ_ALFABETO)
import random
import copy


def para_one_hot(string):
    contador = 0
    for letra in string:
        if letra in ALFABETO:
            if contador == 0:
                matriz_palavra = np.reshape(MATRIZ_ALFABETO[ALFABETO.index(letra)],(1,TAMANHO_ALFABETO))
            else:
                array2 = np.reshape(MATRIZ_ALFABETO[ALFABETO.index(letra)],(1,TAMANHO_ALFABETO))
                matriz_palavra = np.concatenate((matriz_palavra,array2),axis=0)
        contador = 1
    matriz_palavra = matriz_palavra.T
    return matriz_palavra




def para_string(matriz):
    palavra = ""
    for coluna in matriz.T:
        i = np.where(coluna == 1)[0][0]
        palavra += ALFABETO[i]
    return palavra



def cifrar(string, p):
    one_hot = para_one_hot(string)
    cifrada = p @ one_hot
    resultado = para_string(cifrada)
    return resultado




def de_cifrar(string_cifrada, p):

    string_one_hot = para_one_hot(string_cifrada)
    p_inv = np.linalg.inv(p)
    de_cifrada = p_inv @ string_one_hot
    string = para_string(de_cifrada)

    return string

def enigma(mensagem, p, e):
    matriz = para_one_hot(mensagem)
    matriz = matriz.T
    for i in range(len(matriz)):
        if i ==0:
            letra = np.reshape((p @ matriz[i]),(-1,TAMANHO_ALFABETO))
            matriz_palavra = letra
        else:
            letra = np.reshape((np.linalg.matrix_power(e,i) @ p @ matriz[i]),(-1,TAMANHO_ALFABETO))
            matriz_palavra = np.concatenate([matriz_palavra,letra])
    matriz_palavra = para_string(matriz_palavra.T)
    return matriz_palavra

def de_enigma(mensagem, p, e):
    matriz = para_one_hot(mensagem)
    matriz = matriz.T
    p_inv = np.linalg.inv(p)
    e_inv = np.linalg.inv(e)
    for i in range(len(matriz)):
        if i == 0:
            letra = np.reshape((p_inv @matriz[i]), (-1,TAMANHO_ALFABETO))
            matriz_palavra = letra
        else:
            letra = np.reshape((p_inv @ np.linalg.matrix_power(e_inv,i) @ matriz[i]),(-1,TAMANHO_ALFABETO))
            matriz_palavra = np.concatenate([matriz_palavra,letra])
    matriz_palavra = para_string(matriz_palavra.T)
    return matriz_palavra
    
# permutada = copy.deepcopy(MATRIZ_ALFABETO)
# permutada = np.roll(permutada.T, 3)
# e = copy.deepcopy(permutada)
# e = np.roll(e, 3)
# permutada = np.roll(MATRIZ_ALFABETO, 3)
# e = np.roll(permutada, 3)
mama = para_one_hot("gustavo")
# print(para_string(mama))

# rng = np.random.seed(3)
# a = copy.deepcopy(MATRIZ_ALFABETO)
permutada = np.roll(MATRIZ_ALFABETO, 3, 1)

e = np.roll(permutada, 3, 1)

# c =  a == b
# print(a == b)
# print(cifrar('gustavo', permutada))
# print(de_cifrar(cifrar('gustavo', permutada),permutada))
nwp = enigma("gustavo",permutada,e)
print(nwp)
print(de_enigma(nwp,permutada,e))


    




    



