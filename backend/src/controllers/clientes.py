from flask_restx import Resource, abort

from server.postgredb import *
from server.instance import server
from models.clientes import cliente_model
from controllers.handyFunctions import has_id

app, api = server.app, server.api

ITEM_NOT_FOUND = 'Nenhum cliente não encontrado'





@api.route('/clientes')
class ClientesList(Resource):

    @api.doc('get_clientes')
    @api.marshal_list_with(cliente_model, envelope="clientes", code=200)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self):
        query = Cliente.select()
        try:
            dados = [i.serialize for i in query]
        except:
            abort(404, ITEM_NOT_FOUND)
        return dados, 200

            
    

    @api.doc('create_cliente')
    @api.expect(cliente_model, validate=True)
    @api.marshal_with(cliente_model, code=201)
    @api.doc(responses={404: 'Campo id é de leitura apenas.'})
    def post(self):
        payload = api.payload
        if(has_id(payload)):
            abort(400, "Campo id é de leitura apenas.")
        try:
            cliente = Cliente(**payload)
            cliente.save()
            return cliente.serialize, 201
        except Exception as e:
            abort(400, e)

        


@api.route('/clientes/<int:id>')
class Clientes(Resource):

    @api.doc('get_cliente')
    @api.marshal_with(cliente_model, code=200)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self, id):
        try:
            cliente = Cliente.get_by_id(id)
        except:
            abort(404, ITEM_NOT_FOUND)
        return cliente.serialize, 200
            

    '''
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
    '''