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


# ________ROTAS CLIENTES_________

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



#POST (criar)
@app.route('/clientes', methods=['POST'])
def add_cliente():
    cliente = Cliente()
    cliente.nome = request.json['nome']
    try:
        cliente.telefone = request.json['telefone']
    except:
        pass#gambiarra para deixar o telefone como parametro opicional do json.
    cliente.save()
    return {'id':cliente.get_id()}




#PUT (atualizar)
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
        try:
            cliente.telefone = request.json['telefone']
        except:
            pass#gambiarra
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


# ________ROTAS EMBARQUES_________

@app.route('/embarques')
def get_embarques():
    query = Embarque.select()
    dados = [i.serialize for i in query]
    if dados:
        res = jsonify({
            'embarques': dados
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



@app.route('/embarques/<id>')
def get_embarque(id):
    try:
        embarque = Embarque.get_by_id(id)
    except:
        embarque = None
    if(embarque):
        res = jsonify(embarque.serialize)
        res.status_code = 200
    else:
        output = {
            "error": "Sem resultados encontrados. Cheque a URL e tente outra vez.",
            "url": request.url
        }
        res = jsonify(output)
        res.status_code = 404
    return res




#POST (criar)
@app.route('/embarques', methods=['POST'])
def add_embarque():
    embarque = Embarque()
    embarque.descricao = request.json['descricao']

    # gambiarra das feias abaixo:
    # nos trys abaixo estao os parametros opicionais do json
    try:
        embarque.id_cliente = request.json['id_cliente']
    except:
        pass

    try:
        embarque.data_chegada = request.json['data_chegada']
    except:
        pass

    try:
        embarque.nota_fiscal = request.json['nota_fiscal']
    except:
        pass

    try:
        embarque.registrado = request.json['registrado']
    except:
        pass

    try:
        embarque.pago = request.json['pago']
    except:
        pass

    try:
        embarque.urgente = request.json['urgente']
    except:
        pass

    try:
        embarque.embarcado = request.json['embarcado']
    except:
        pass

    
    embarque.save()
    return {'id':embarque.get_id()}

#PUT (atualizar)
@app.route('/embarques/<id>', methods=['PUT'])
def update_embarque(id):
    #to-do: check types

    try:
        embarque = Embarque.get_by_id(id)
    except:
        embarque = None

    if embarque:
        # gambiarra das feias abaixo:
        try:
            embarque.id_cliente = request.json['id_cliente']
        except:
            pass
        
        try:
            embarque.descricao = request.json['descricao']
        except:
            pass
        
        try:
            embarque.com_nota_fiscal = request.json['com_nota_fiscal']
        except:
            pass

        try:
            embarque.registrado = request.json['registrado']
        except:
            pass

        try:
            embarque.pago = request.json['pago']
        except:
            pass

        try:
            embarque.urgente = request.json['urgente']
        except:
            pass

        try:
            embarque.embarcado = request.json['embarcado']
        except:
            pass

        embarque.save()
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
@app.route('/embarques/<id>', methods=['DELETE'])
def delete_embarque(id):
    embarque = embarque.select().where(embarque.id == id)[0]
    if(embarque):
        embarque.delete_instance()
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
