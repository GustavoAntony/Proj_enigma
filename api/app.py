from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Essa é uma api para cifrar e decifrar com a máquina enigma"

@app.route("/", methods=['POST'])
def cifra():
    seed = request.form['seed']
    
    return 'a'