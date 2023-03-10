from flask import Flask, request, jsonify
from enigma.enigma import * 


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Essa é uma api para cifrar e decifrar com a máquina enigma"

@app.route("/enigma", methods=['POST'])
def cifra():                               #(mensagem, p, e) só recebe seed e a mensagem

    data = request.json
    seed = data.get('seed')
    acao = data.get('acao')
    mensagem = data.get('mensagem')
    permutada = np.roll(MATRIZ_ALFABETO, seed, 1)
    e = np.roll(permutada, seed, 1)

    if acao == 'cifrar':
        return enigma(mensagem, permutada, e)
    elif acao == 'decifrar':
        return de_enigma(mensagem,permutada,e)

  

app.run()