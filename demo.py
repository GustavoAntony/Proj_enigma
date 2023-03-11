import sys
import time
from enigma import *

p = np.roll(MATRIZ_ALFABETO, 1, 1)
e = np.roll(p, 1, 1)



def escreva(mensagem):
    for letra in mensagem:
        sys.stdout.write(f"\033[0;37;40m{letra}")
        sys.stdout.flush()
        time.sleep(0.04)

def escreva_titulo(mensagem):
    for letra in mensagem:
        sys.stdout.write(f"\033[1;35;40m{letra}")
        sys.stdout.flush()
        time.sleep(0.04)
    

escreva_titulo("Olá, bem vindo ao demo do nosso projeto de enigma!\n")
print()
escreva_titulo("Começaremos demonstrando o funcionamento das funções básicas 'para_one_hot' e 'para_string'.")
print()
escreva('''\nA função 'para_one_hot' transforma uma mensagem em uma matriz. Para o input 'Amo álgebra linear!' seria gerada a seguinte saída:\n''')
print()
one_hot = para_one_hot('Amo álgebra linear!')
print(one_hot)
print()
escreva("Já a função 'para_string', realiza o processo oposto transformando a matriz novamente em string. Utilizando a matriz de cima seria gerada a seguinte saída:\n")
print()
string = para_string(one_hot)
print(string)
print()
time.sleep(1.5)
escreva_titulo("Continuaremos com as próximas duas funções que são a 'cifrar' e 'decifrar'.\n")
print()
escreva("A função de cifrar realiza uma cifra na mensagem passada e retorna uma outra mensagem cifrada a partir de uma matriz de permutação. Para o input 'Amo álgebra linear!' seria gerada uma saída parecida com a abaixo, dependendo da matriz de permutação:\n ")
print()
cifrada = cifrar('Amo álgebra linear!',p)
print(cifrada)
print()
escreva("Já a função de decifrar executa o processo oposto, a fim de obter a mensagem inicial. A partir da mensagem acima, devido a matriz de permutação utilizada, a saída seria igual a :\n")
print()
print(de_cifrar(cifrada,p))
print()
time.sleep(1.5)
escreva_titulo("Por fim, temos as duas últimas funções a 'enigma' e a 'de_enigma'.\n")
print()
escreva("A função enigma cria uma mensagem enigmada a partir de uma matriz de permutação e uma matriz auxiliar. Com o input 'Amo álgebra linear!', dependendo das matrizes de permutação e auxiliar, a saída seria semelhante a:\n")
enigmada = enigma('Amo álgebra linear!',p,e)
print()
print(enigmada)
print()
escreva("Já a função de_enigma retorna a mensagem original. Tendo em vista as matrizes de permutação e auxiliar e a mensagem enigmada acima, a saída seria igual a:\n")
print()
print(de_enigma(enigmada,p,e))
print()
escreva_titulo("Muito obrigada pela atenção!")