# Como usar os módulos dessa biblioteca

* A função `para_one_hot(msg : str)` pode ser usada para codificar mensagens como uma matriz usando one-hot encoding
* A função `para_string(M : np.array)` pode ser usada para converter mensagens da representação one-hot encoding para uma string legível
* A função `cifrar(msg : str, P : np.array)` aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. `P` é a matriz de permutação que realiza a cifra.
* A função `de_cifrar(msg : str, P : np.array)` recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. `P` é a matriz de permutação que realiza a cifra.
* A função `enigma(msg : str, P : np.array, E : np.array)` faz a cifra enigma na mensagem de entrada usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.
* A função `de_enigma(msg : str, P : np.array, E : np.array)` recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.



