from flask_restx import Resource, abort

from server.postgredb import *
from server.instance import server
from models.clientes import cliente_model, cliente_model_patch  
from controllers.handyFunctions import has_field, brazilian_phone_number_validation_check

app, api = server.app, server.api

ITEM_NOT_FOUND = 'Nenhum cliente encontrado'





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
    @api.doc(responses={400: 'Campo id é de leitura apenas.'})
    def post(self):
        payload = api.payload
        print(payload)
        if(has_field(payload, 'id')):
            abort(400, "Campo id é de leitura apenas.")
        if(has_field(payload, 'telefone')):
            if(brazilian_phone_number_validation_check(payload['telefone']) == False):
                abort(400, "Telefone inválido.")
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
            

    
    @api.doc('update_cliente')
    @api.marshal_with(cliente_model_patch, code=200)
    @api.expect(cliente_model_patch, validate=True)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def patch(self, id):
        payload = api.payload
        if(has_field(payload, 'id')):
            abort(400,"Campo id é de leitura apenas.")

        if(has_field(payload, 'telefone')):
            if(brazilian_phone_number_validation_check(payload['telefone']) == False):
                abort(400, "Telefone inválido.")

        try:
            Cliente.get_by_id(id)
        except:
            abort(404, ITEM_NOT_FOUND)

        try:
            Cliente.update(**payload).where(Cliente.id == id).execute()
            updatedCliente = Cliente.get_by_id(id)
            return updatedCliente.serialize, 200
        except Exception as e:
            abort(400, e)

    @api.doc('delete_cliente')
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def delete(self, id):
        if(Cliente.select().where(Cliente.id == id).exists()):
            cliente = Cliente.get_by_id(id)
            try: 
                cliente.delete_instance()
                return "Deletado!", 200
            except Exception as e:
               abort(400, e) 
        else:
            abort(404, ITEM_NOT_FOUND)

        
    '''
    @api.doc('create_or_replace_cliente')
    @api.marshal_with(cliente_model)
    @api.expect(cliente_model, validate=True)    
    def put(self, id):
        payload = api.payload

        if(has_field(payload, 'telefone')):
            if(brazilian_phone_number_validation_check(payload['telefone']) == False):
                abort(400, "Telefone inválido.")

        alreadyExists = Cliente.select().where(Cliente.id == id).exists()
        if(alreadyExists):
            # REPLACE!

            auxC = Cliente(**payload)
            auxC.id = id

            auxC_dict = auxC.serialize
            # get rid of readOnly fields (id and quant_embarques):
            auxC_dict.pop('id')
            auxC_dict.pop('quant_embarques')
            
            Cliente.update(**auxC_dict).where(Cliente.id == id).execute()

            updatedCliente = Cliente.get_by_id(id)
            return updatedCliente.serialize, 200

        else:
            # INSERT!

            newCliente = Cliente(**payload)
            newCliente.id = id
            try:
                newCliente.save()
                return newCliente.serialize, 201
            except Exception as e:
                abort(400, e)
'''