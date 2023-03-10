from flask import Flask, request, jsonify
from funcoes import * 


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Essa é uma api para cifrar e decifrar com a máquina enigma"

@app.route("/", methods=['POST'])
def cifra():                               #(mensagem, p, e) só recebe seed e a mensagem

    data = request.json
    seed = data.get('seed')
    mensagem = data.get('mensagem')
    # mensagem_one_hot = para_one_hot(mensagem)    
    permutada = np.roll(MATRIZ_ALFABETO, seed, 1)
    e = np.roll(permutada, seed, 1)

    return enigma(mensagem, permutada, e)



@app.route("/de", methods=['POST'])
def de_cifra():                               #(mensagem, p, e) só recebe seed e a mensagem

    data = request.json
    seed = data.get('seed')
    mensagem = data.get('mensagem')
    # mensagem_one_hot = para_one_hot(mensagem)
    permutada = np.roll(MATRIZ_ALFABETO, seed, 1)
    e = np.roll(permutada, seed, 1)


    return de_enigma(mensagem,permutada,e)
  


app.run()