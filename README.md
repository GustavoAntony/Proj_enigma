# Como usar os módulos dessa biblioteca : 

* A função `para_one_hot(msg : str)` pode ser usada para codificar mensagens como uma matriz usando one-hot encoding
* A função `para_string(M : np.array)` pode ser usada para converter mensagens da representação one-hot encoding para uma string legível
* A função `cifrar(msg : str, P : np.array)` aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. `P` é a matriz de permutação que realiza a cifra.
* A função `de_cifrar(msg : str, P : np.array)` recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. `P` é a matriz de permutação que realiza a cifra.
* A função `enigma(msg : str, P : np.array, E : np.array)` faz a cifra enigma na mensagem de entrada usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.
* A função `de_enigma(msg : str, P : np.array, E : np.array)` recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.



# Como utilizar a api :


* A api apresenta apenas uma rota /enigma e para ela deve ser enviado um json com as seguintes chaves :
 - acao → recebe uma string cifrar ou decifirar indicando a ação desejada
 - seed → recebe um int indicando o seed(chave) para incriptar ou decriptar a mensagem, dependendo da ação escolhida.
 - mensagem → recebe uma string contendo uma mensagem, seja incriptada ou normal.


 Assim, para incriptar uma mensagem você pode enviar ela na chave mensgem do json, e a ação cifrar na chave acao alem do seed. E para decifrar você deve enviar a mensagem incriptada na chave mensagem, a ação decifrar na chave acao e a mesma seed que foi utilizada para gerar a mensagem incriptada.


# Como funcionam os métodos da biblioteca :
 * A função `para_one_hot(msg : str)` transforma cada letra do alfabeto em um array de zeros e um afim de transformar aquela sentença em uma matriz onde cada letra vira uma coluna.

 * A função `para_string(M : np.array)` faz a operação inversa da anterior em que pega cada coluna do array, ou seja, cada letra representada no array e transforma na caractér correspondente.

* A função `cifrar(msg : str, P : np.array)` recebe uma mensagem em string, transforma em one_hot com a primeira função citada, após isso multiplica por uma matriz p que é uma matriz semelhante a matriz de alfabeto mais permutada e esse resultado da multiplicação é convertido para string usando a função `para_string`. Sendo assim, caso a matriz p troque a letra B por A na palavra "BANANA" após essa operação ficaria "ABNBNB".


* A função `de_cifrar(msg : str, P : np.array)` recebe a uma mensagem cifrada e a matriz de permutação p utilizada para gerar essa mensagem. Após isso, trasnforma a mensagem em questão em one_hot, e faz uma operação entre matrizes basíca de multiplicação pela inversa de p para obter a matriz original, por exemplo, P . O = C => P-¹. P . O = P-¹ . C, sendo C a matriz da mensagem cifrada, P a matriz p e O a matriz da mensagem original. Após conseguir a matriz original ela é tranformada em uma string com a função `para_string`.

* A função `enigma(msg : str, P : np.array, E : np.array)` faz um processo semelhante à função `cifrar` mas a difereça é que agora existe uma matriz de permutação auxiliar 'e' e o provesso é o seguinte: Para a primeira letra o processo é identico à função `cifrar`, e a aprtir da segunda letra começamos a usar a matriz auxiliar 'e' e a multiplicação fica E.P.O, sendo E a matriz e, P a matriz p e O a matriz da mensagem original. A para cada iteração nas letras do alfabeto é multiplicada uma vez a mais pela matriz auxiliar e. E após todo esse processo transformamos a matriz resultante em string gerando o resultado incriptado. 


* A função `de_enigma(msg : str, P : np.array, E : np.array)` faz um processo semelhante à função `de_cifrar` e a diferença é que para cada letra a operação de inversão para obter a matriz original é diferente já que para gerar cada letra utilizando a função engima houve uma multiplicação à mais pela matriz auxiliar 'e'.E após seguir os passos de transformar a mensagem para one_hot e fazer a operação inversa para obter a matriz original essa matriz é transformada em texto gerando o resultado decriptado.

 # Como baixar a bilbioteca utilizando o pip install :

 Para fazer o download utilizando o pip install basta rodar o comando `pip install git+https://github.com/GustavoAntony/Proj_enigma` que a biblioteca enigmatico vai ser instalada. Para acessar basta dar um `import enigma` e usar as funções citadas anteriomente. 
 Ex.: 
 ```
 import enigma

cifra = enigma.para_one_hot('Matheus')

 ````

 e o resultado será .:

 ```
 [[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 1]
 [0 0 1 0 0 0 0]
 [0 0 0 0 0 1 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]]
 ```



