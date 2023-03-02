import numpy as np
ALFABETO = 'abcdefghijklmnopqrstuvwxyz '
TAMANHO_ALFABETO = len(ALFABETO)

#FUNÇÕES ÚTEIS
# def one_hot_individual(letra):
#     # alfabeto = {'a' : 0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

#     if letra not in alfabeto:
#         return np.zeros(27)
#     else:
#         lista = []
#         for a in range(len(alfabeto)):
#             if letra == alfabeto[a]:

def para_one_hot(string):
    matriz_alfabeto = np.identity(TAMANHO_ALFABETO,dtype=int)
    contador = 0
    for letra in string:
        if letra in ALFABETO:
            if contador == 0:
                matriz_palavra = np.reshape(matriz_alfabeto[ALFABETO.index(letra)],(1,TAMANHO_ALFABETO))
            else:
                array2 = np.reshape(matriz_alfabeto[ALFABETO.index(letra)],(1,TAMANHO_ALFABETO))
                matriz_palavra = np.concatenate((matriz_palavra,array2),axis=0)
        contador = 1
    matriz_palavra = matriz_palavra.T
    return matriz_palavra

print(para_one_hot("gustavo"))


