from postgredb import *

from flask import Flask
from flask import jsonify
from flask import request
from os import abort
from flask_cors import CORS

''' Rode este arquivo, e a API estará funcionando! '''


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/')
def index():
    return 'Bem vindo(a) a API do Zé Pósitos!'


# ________ROTAS CLIENTES_________

#GET
@app.route('/clientes', methods=['GET'])
def get_clientes():
    query = Cliente.select()
    dados = [i.serialize for i in query]

    if dados:
        res = jsonify({
            'clientes': dados
        })
        res.status_code = 200
    else:
        res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url)
        res.status_code = 404

    return res



#GET
@app.route('/clientes/<id>', methods=['GET'])
def get_cliente(id):
    try:
        cliente = Cliente.get_by_id(id)
    except:
        cliente = None
    if(cliente):
        res = jsonify(cliente.serialize)
        res.status_code = 200
    else:
        res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url
        )
        res.status_code = 404
    return res



#POST (criar)
@app.route('/clientes', methods=['POST'])
def add_cliente():
    try:
        request.json['nome']
    except:
        res = jsonify(message = 'Campo obrigatório (nome) em falta.')
        res.status_code = 400
        return res
        
    
    cliente = Cliente(**(request.get_json()))
    cliente.save()
    res = jsonify(message = 'Cliente criado.', id = cliente.get_id())
    res.status_code = 201
    return res


#PATCH (atualizar)
@app.route('/clientes/<id>', methods=['PATCH'])
def update_cliente(id):
    try:
        cliente = Cliente.get_by_id(id)
    except:
        cliente = None

    if cliente:
        Cliente.update( **(request.get_json()) ).where(Cliente.id == id).execute()
        
        res = jsonify(message = "Atualizado!", cliente = Cliente.get_by_id(id).serialize)
        res.status_code = 200
    else:
        res = jsonify(error = 'Não encontrado.', url = request.url)
        res.status_code = 404
    return res


#DELETE
@app.route('/clientes/<id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.select().where(Cliente.id == id)[0]
    if(cliente):
        cliente.delete_instance()
        res = jsonify(message = "Deletado!")
        res.status_code = 200
    else:
        res = jsonify( error = 'Não encontrado.', url = request.url)
        res.status_code = 404
    return res



# ________ROTAS EMBARQUES_________

@app.route('/embarques', methods=['GET'])
def get_embarques():
    query = Embarque.select()
    try:
        dados = [i.serialize for i in query]
    except:
        dados = None
    if dados:
        res = jsonify(embarques = dados)
        res.status_code = 200
    else:
        res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url)
        res.status_code = 404
    return res



@app.route('/embarques/<id>', methods=['GET'])
def get_embarque(id):
    try:
        embarque = Embarque.get_by_id(id)
    except:
        embarque = None
    if(embarque):
        res = jsonify(embarque.serialize)
        res.status_code = 200
    else:
        res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url)
        res.status_code = 404
    return res


#POST (criar)
@app.route('/embarques', methods=['POST'])
def add_embarque():
    try:
        request.json['descricao']
    except:
        res = jsonify(message = 'Campo obrigatório (descricao) em falta.')
        res.status_code = 400
        return res
    
    embarque = Embarque(**(request.get_json()))
    embarque.save()
    res = jsonify(
        message = 'Embarque criado.',
        id = embarque.get_id()
    )
    res.status_code = 201
    return res 



#PATCH (atualizar)
@app.route('/embarques/<id>', methods=['PATCH'])
def update_embarque(id):
    try:
        embarque = Embarque.get_by_id(id)
    except:
        embarque = None

    if embarque:
        Embarque.update( **(request.get_json()) ).where(Embarque.id == id).execute()
        res = jsonify(message = "Atualizado!", embarque = Embarque.get_by_id(id).serialize)
        res.status_code = 200
    else:
        res = jsonify(error = 'Não encontrado.', url = request.url)
        res.status_code = 404
    return res


#DELETE
@app.route('/embarques/<id>', methods=['DELETE'])
def delete_embarque(id):
    embarque = Embarque.get_by_id(id)
    if(embarque):
        embarque.delete_instance()
        res = jsonify(message = "Deletado!")
        res.status_code = 200
    else:
        res = jsonify(error = 'Não encontrado.', url = request.url)
        res.status_code = 404
    return res


# ________ROTAS VOLUMES_________


@app.route('/volumes', methods=['GET'])
def get_volumes():
    query = Volume.select()
    try:
        dados = [i.serialize for i in query]
    except:
        dados = None
    if dados:
        res = jsonify(volumes = dados)
        res.status_code = 200
    else:
        res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url)
        res.status_code = 404
    return res



@app.route('/volumes/<id>', methods=['GET'])
def get_volume(id):
    try:
        volume = Volume.get_by_id(id)
    except:
        volume = None
    if(volume):
        res = jsonify(volume.serialize)
        res.status_code = 200
    else:
        res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url)
        res.status_code = 404
    return res


#POST (criar)
@app.route('/volumes', methods=['POST'])
def add_volume():
    try:
        request.json['id_embarque']
        request.json['largura']
        request.json['comprimento']
        request.json['altura']
        request.json['peso']
    except:
        res = jsonify(message = 'Campo(s) obrigatório(s) em falta.')
        res.status_code = 400
        return res
    
    volume = Volume(**(request.get_json()))
    volume.save()
    res = jsonify(
        message = 'Volume criado.',
        id = volume.get_id()
    )
    res.status_code = 201
    return res 



#PATCH (atualizar)
@app.route('/volumes/<id>', methods=['PATCH'])
def update_volume(id):
    try:
        request.json['id_embarque']
        res = jsonify(error = 'Em volumes não é permitida a mudança de id_embarque.')
        res.status_code = 400
        return res
    except:
        pass
    
    try:
        volume = Volume.get_by_id(id)
    except:
        volume = None

    if volume:
        Volume.update( **(request.get_json()) ).where(Volume.id == id).execute()
        res = jsonify(message = "Atualizado!", embarque = Volume.get_by_id(id).serialize)
        res.status_code = 200
    else:
        res = jsonify(error = 'Não encontrado.', url = request.url)
        res.status_code = 404
    return res


#DELETE
@app.route('/volumes/<id>', methods=['DELETE'])
def delete_volume(id):
    volume = Volume.get_by_id(id)
    if(volume):
        volume.delete_instance()
        res = jsonify(message = "Deletado!")
        res.status_code = 200
    else:
        res = jsonify(error = 'Não encontrado.', url = request.url)
        res.status_code = 404
    return res



''' ][________________ROTAS CUSTOMIZADAS_________________]['''

# ________ROTAS EMBARQUES DE CLIENTE_________

@app.route('/clientes/<id_cliente>/embarques', methods=['GET'])
def get_embarques_of_cliente(id_cliente):
    query = Embarque.select().where(Embarque.id_cliente == id_cliente)
    dados = [i.serialize for i in query]
    if dados:
        res = jsonify(embarques = dados)
        res.status_code = 200
    else:
        res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url)
        res.status_code = 404
    return res



#POST (criar)
@app.route('/clientes/<id_cliente>/embarques', methods=['POST'])
def add_embarque_of_cliente(id_cliente):

    try:
        request.json['id_cliente']
        res = jsonify(error = 'Não é possível usar um id_cliente que não o da URL.')
        res.status_code = 400
        return res
    except:
        pass

    try:
        request.json['descricao']
    except:
        res = jsonify(message = 'Campo obrigatório (descricao) em falta.')
        res.status_code = 400
        return res
    
    embarque = Embarque(**(request.get_json()))
    embarque.id_cliente = id_cliente
    embarque.save()
    res = jsonify(
        message = 'Embarque criado.',
        id = embarque.get_id()
    )
    res.status_code = 201
    return res 



# ________ROTAS VOLUMES DE EMBARQUE_________


@app.route('/embarques/<id_embarque>/volumes', methods=['GET'])
def get_volumes_of_embarque(id_embarque):
    query = Volume.select().where(Volume.id_embarque == id_embarque)
    try:
        dados = [i.serialize for i in query]
    except:
        dados = None
    if dados:
        res = jsonify(volumes = dados)
        res.status_code = 200
    else:
        res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url)
        res.status_code = 404
    return res


@app.route('/embarques/<id_embarque>/volumes', methods=['POST'])
def add_volume_of_embarque(id_embarque):
    try:
        request.json['id_embarque']
        res = jsonify(error = 'Não é possível usar um id_embarque que não o da URL.')
        res.status_code = 400
        return res
    except:
        pass

    try:
        request.json['largura']
        request.json['comprimento']
        request.json['altura']
        request.json['peso']
    except:
        res = jsonify(message = 'Campo(s) obrigatório(s) em falta.')
        res.status_code = 400
        return res
    
    volume = Volume(**(request.get_json()))
    volume.id_embarque = id_embarque
    volume.save()
    res = jsonify(
        message = 'Volume criado.',
        id = volume.get_id()
    )
    res.status_code = 201
    return res 

app.run()