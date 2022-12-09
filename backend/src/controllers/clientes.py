from flask_restx import Resource, abort
from flask import jsonify
from flask import request

from src.server.postgredb import *
from src.server.instance import server
from src.models.clientes import cliente
app, api = server.app, server.api

ITEM_NOT_FOUND = 'Cliente não encontrado'



@api.route('/clientes')
class ClientesList(Resource):

    @api.doc('get_clientes')
    @api.marshal_list_with(cliente, envelope="clientes", code=200)
    @api.doc(responses={404: 'Sem clientes registrados.'})
    def get(self):
        query = Cliente.select()
        try:
            dados = [i.serialize for i in query]
        except:
            dados = None
        if dados:
            return dados, 200
        else:
            abort(404, 'Sem clientes registrados.')


    @api.doc('create_cliente')
    @api.expect(cliente, validate=True)
    @api.marshal_with(cliente, code=201)
    @api.doc(responses={404: 'Campo id é de leitura apenas.'})
    def post(self):
        payload = api.payload

        payloadHasIdField = True
        try:
            payload['id']
            
        except:
            payloadHasIdField = False

        if(payloadHasIdField):
            abort(400, "Campo id é de leitura apenas.")

        cliente = Cliente(**payload)
        try:
            cliente.save()
            return cliente.serialize, 201
        except Exception as e:
            abort(400, e)

        


@api.route('/clientes/<int:id>')
class Clientes(Resource):

    @api.marshal_with(cliente, code=200)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self, id):
        try:
            cliente = Cliente.get_by_id(id)
        except:
            cliente = None
        if(cliente):
            return cliente.serialize, 200
            
        else:
            abort(404, ITEM_NOT_FOUND)


    #to do
    def patch(self, id):
        payload = api.payload
        try:
            cliente = Cliente.get_by_id(id)
        except:
            cliente = None

        if cliente:
            Cliente.update(**payload).where(Cliente.id == id).execute()
            updatedCliente = Cliente.get_by_id(id)
            return updatedCliente.serialize, 200
            
        else:
            abort(404, ITEM_NOT_FOUND)
        