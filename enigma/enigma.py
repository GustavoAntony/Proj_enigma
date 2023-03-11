import numpy as np
ALFABETO = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÇçáéíóúãõàèìòù123456789 "'!@#$%¨&*()_+=§[]:;/>.<\|,?'''
TAMANHO_ALFABETO = len(ALFABETO)
MATRIZ_ALFABETO = np.identity(TAMANHO_ALFABETO,dtype=int)


#função responsável por converter uma string para uma matriz one hot
def para_one_hot(string):
    #contador é criado para verificar quando a matriz deve ser criada e quando a matriz deve ser concatenada
    contador = 0
    for letra in string:
        #caso a letra pertença ao alfabeto, ela é tem seu shape redefinido para (1,TAMANHO_ALFABETO)
        if letra in ALFABETO:
            if contador == 0:
                matriz_palavra = np.reshape(MATRIZ_ALFABETO[ALFABETO.index(letra)],(1,TAMANHO_ALFABETO))
            else:
                array2 = np.reshape(MATRIZ_ALFABETO[ALFABETO.index(letra)],(1,TAMANHO_ALFABETO))
                matriz_palavra = np.concatenate((matriz_palavra,array2),axis=0)
        #caso a mensagem receba um elemento que não pertença ao alfabeto é adicionado um ponto de interrogação no lugar       
        else:
            letra = "?"
            if contador == 0:
                matriz_palavra = np.reshape(MATRIZ_ALFABETO[ALFABETO.index(letra)],(1,TAMANHO_ALFABETO))
            else:
                array2 = np.reshape(MATRIZ_ALFABETO[ALFABETO.index(letra)],(1,TAMANHO_ALFABETO))
                matriz_palavra = np.concatenate((matriz_palavra,array2),axis=0)
        contador = 1
    #antes de retornar a matriz é transposta para seguir o modelo (i,j) = (TAMANHO,ALFABETO,TAMANHO_PALAVRA)
    matriz_palavra = matriz_palavra.T
    return matriz_palavra



#função que converte uma matriz para mensagem
def para_string(matriz):
    palavra = ""
    #para cada coluna na matriz transposta
    for coluna in matriz.T:
        #encontra o indice do 1 na coluna para localizar no alfabeto qual letra é correspondente
        i = np.where(coluna == 1)[0][0]
        palavra += ALFABETO[i]
    return palavra


#função utilizada para cifrar uma string a partir de uma matriz de permutação
def cifrar(string, p):
    # cria matriz onehot
    one_hot = para_one_hot(string)
    # multiplica a matriz de permutação pela one hot
    cifrada = p @ one_hot
    # cria a string com o resultado da matriz cifrada
    resultado = para_string(cifrada)
    return resultado




#função utilizada para decifrar uma string a partir de uma matriz de permutação
def de_cifrar(string_cifrada, p):
    #cria matriz onehot
    string_one_hot = para_one_hot(string_cifrada)
    #inverte a matriz permutação
    p_inv = np.linalg.inv(p)
    #multiplica a matriz P@M pela inversa da p, afim de voltar a matriz padrão
    de_cifrada = p_inv @ string_one_hot
    #transforma a matriz em string
    string = para_string(de_cifrada)
    return string

#função que enigma a mensagem
def enigma(mensagem, p, e):
    #cria a matriz e transpoe ela
    matriz = para_one_hot(mensagem)
    matriz = matriz.T
    #para cada letra na matriz realiza uma criptografia diferente que depende de seu indice na mensagem
    for i in range(len(matriz)):
        if i ==0: 
           #faz o reshape (1,tamanho_alfabeto) da letra para somar a matriz
            letra = np.reshape((p @ matriz[i]),(-1,TAMANHO_ALFABETO))
            matriz_palavra = letra
        else:
            #faz o reshape (1,tamanho_alfabeto) da letra para somar a matriz
            letra = np.reshape((np.linalg.matrix_power(e,i) @ p @ matriz[i]),(-1,TAMANHO_ALFABETO))
            matriz_palavra = np.concatenate([matriz_palavra,letra])
    #transforma essa matriz resultante em string 
    matriz_palavra = para_string(matriz_palavra.T)
    return matriz_palavra


#função que decifra a mensagem enigma
def de_enigma(mensagem, p, e):
    #cria a matriz e transpoe ela
    matriz = para_one_hot(mensagem)
    matriz = matriz.T
    #cria as inversas da matriz permutação e da matriz auxiliar
    p_inv = np.linalg.inv(p)
    e_inv = np.linalg.inv(e)
    #para cada letra na matriz realiza uma decriptografia diferente que depende de seu indice na mensagem
    for i in range(len(matriz)):
        if i == 0:
            letra = np.reshape((p_inv @matriz[i]), (-1,TAMANHO_ALFABETO))
            matriz_palavra = letra
        else:
            letra = np.reshape((p_inv @ np.linalg.matrix_power(e_inv,i) @ matriz[i]),(-1,TAMANHO_ALFABETO))
            matriz_palavra = np.concatenate([matriz_palavra,letra])
    #transforma essa matriz resultante em string 
    matriz_palavra = para_string(matriz_palavra.T)
    return matriz_palavra
    



    




    



