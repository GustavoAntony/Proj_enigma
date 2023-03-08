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
    for i in range(0,len(mensagem)-1):
        if i ==1:
            p = e @ p
        if i >= 2:    
            c = 0
            while c < i-1:
                e  = e@e
            p = e @ p
        line = cifrar(mensagem[i],p)
    pass
    

mama = para_one_hot("gustavo")
print(para_string(mama))
permutada = np.random.permutation(MATRIZ_ALFABETO)
print(permutada)
print(cifrar('gustavo', permutada))
print(de_cifrar(cifrar('gustavo', permutada),permutada))

    




    



