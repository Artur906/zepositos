from flask_restx import Resource
from flask import jsonify
from flask import request

from postgredb import *
from src.server.instance import server

app, api = server.app, server.api

@api.route('/clientes')
class ClienteEndPoints(Resource):
    def get(self):
        response = api.payload
        print('response: ', response)
        print('request json:',  request.json)
        print('request get json:',  request.get_json())
        query = Cliente.select()
        try:
            dados = [i.serialize for i in query]
        except:
            dados = None

        if dados:
            res = jsonify({
                'clientes': dados
            })
            res.status_code = 200
        else:
            res = jsonify(error = 'Sem resultados encontrados. Cheque a URL e tente outra vez.', url = request.url)
            res.status_code = 404

        return res
    

    def post(self):
        response = api.payload
        #return response['nome'], 200
        try:
            response['nome']
        except:
            res = jsonify(message = 'Campo obrigatório (nome) em falta.')
            return res, 400
        
        print(response)
        cliente = Cliente(response)
        cliente.save()
        res = jsonify(message = 'Cliente criado.', id = cliente.get_id())
        return 201