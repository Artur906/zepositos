from esquemabd import *
from flask import Flask
from flask import jsonify
from flask import request
from os import abort
from flask_cors import CORS


'''
Para rodar este arquivo, execute os seguintes comandos no terminal (do vscode):

export FLASK_APP=restAPI.py
export FLASK_DEBUG=1
flask run
'''


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Bem vindo a API!'


#GET
@app.route('/clientes')
def get_clientes():

    query = Cliente.select()
    dados = [i.serialize for i in query]

    if dados:
        res = jsonify({
            'clientes': dados
        })
        res.status_code = 200
    else:
        output = {
            "error": "Sem resultados encontrados. Cheque a URL e tente outra vez.",
            "url": request.url
        }
        res = jsonify(output)
        res.status_code = 404

    return res