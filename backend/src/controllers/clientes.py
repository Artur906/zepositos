from flask_restx import Resource
from flask import jsonify
from flask import request

from server.postgredb import *
from server.instance import server
from models.clientes import cliente
app, api = server.app, server.api

ITEM_NOT_FOUND = 'Cliente não encontrado'

@api.route('/clientes')
class ClientesEndPoints(Resource):
    @api.marshal_list_with(cliente)
    def get(self):
        
        query = Cliente.select()
        try:
            dados = [i.serialize for i in query]
        except:
            dados = None

        if dados:
            res = {'clientes': dados}
            return res, 200
        else:
            res = jsonify(error = ITEM_NOT_FOUND, url = request.url)
            res.status_code = 404

        return res
    
    @api.expect(cliente, validate=True)
    @api.marshal_with(cliente)
    def post(self):
        response = api.payload

        '''try:
            response['nome']
        except:
            res = {"message":"Campo obrigatório (nome) em falta."}
            return res, 400'''
        
        
        cliente = Cliente(**response)
        cliente.save()
        res = {"message": 'Cliente criado.', "id": cliente.get_id()}
        return res, 201

    