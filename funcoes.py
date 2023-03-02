import numpy as np
ALFABETO = 'abcdefghijklmnopqrstuvwxyz '
TAMANHO_ALFABETO = len(ALFABETO)
MATRIZ_ALFABETO = np.identity(TAMANHO_ALFABETO,dtype=int)


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

mama = para_one_hot("gustavo")
print(para_string(mama))
    
    



