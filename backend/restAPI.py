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



#GET
@app.route('/clientes/<id>')
def get_cliente(id):
    try:
        cliente = Cliente.get_by_id(id)
    except:
        cliente = None
    if(cliente):
        res = jsonify(cliente.serialize)
        res.status_code = 200
    else:
        output = {
            "error": "Sem resultados encontrados. Cheque a URL e tente outra vez.",
            "url": request.url
        }
        res = jsonify(output)
        res.status_code = 404
    return res



#POST
@app.route('/clientes', methods=['POST'])
def add_cliente():
    cliente = Cliente(nome=request.json['nome'], telefone=request.json['telefone'])
    cliente.save()
    return {'id':cliente.get_id()}




#PUT
@app.route('/clientes/<id>', methods=['PUT'])
def update_cliente(id):
    if (type(request.json['nome']) != str) or (type(request.json['telefone']) != str):
        abort(400)
    try:
        cliente = Cliente.get_by_id(id)
    except:
        cliente = None

    if cliente:
        cliente.nome = request.json['nome']
        cliente.telefone = request.json['telefone']
        cliente.save()
        res = jsonify({"message": "Atualizado!"})
        res.status_code = 200
    else:
        output = {
            "error": "Não encontrado.",
            "url": request.url
        }
        res = jsonify(output)
        res.status_code = 404
    return res


#DELETE
@app.route('/clientes/<id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.select().where(Cliente.id == id)[0]
    if(cliente):
        cliente.delete_instance()
        res = jsonify({"message": "Deletado!"})
        res.status_code = 200
    else:
        output = {
            "error": "Não encontrado.",
            "url": request.url
        }
        res = jsonify(output)
        res.status_code = 404
    return res


