from flask_restx import Resource, abort

from src.server.schemadb import Cliente
from src.server.instance import server
from src.models.clientes import cliente_model, cliente_model_patch  
from src.utils.validators import BrazilianPhoneValidator

app, api = server.app, server.api

ITEM_NOT_FOUND  = 'Nenhum cliente encontrado'
ID_IS_READ_ONLY = 'Campo id é de leitura apenas'
INVALID_PHONE   = 'Telefone inválido'
DELETED         = "Deletado!"


@api.route('/clientes')
class ClientesRoute(Resource):

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
    @api.doc(responses={400: f"{ID_IS_READ_ONLY} || {INVALID_PHONE}"})
    def post(self):
        payload = api.payload
        if('id' in payload):
            abort(400, ID_IS_READ_ONLY)
        if('telefone' in payload):
            phoneValidator = BrazilianPhoneValidator(payload['telefone'])
            if(not phoneValidator.isPhone()):
                abort(400, INVALID_PHONE)
        try:
            cliente = Cliente(**payload)
            cliente.save()
            return cliente.serialize, 201
        except Exception as e:
            abort(400, e)

        


@api.route('/clientes/<int:id>')
class ClienteRoute(Resource):

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
    @api.doc(responses={404: ITEM_NOT_FOUND, 400: f'{ID_IS_READ_ONLY} || {INVALID_PHONE}'})
    def patch(self, id):
        payload = api.payload
        if('id' in payload):
            abort(400, ID_IS_READ_ONLY)

        if('telefone' in payload):
            phoneValidator = BrazilianPhoneValidator(payload['telefone'])
            if(not phoneValidator.isPhone()):
                abort(400, INVALID_PHONE)

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
    @api.doc(responses={200: DELETED, 404: ITEM_NOT_FOUND})
    def delete(self, id):
        if(Cliente.select().where(Cliente.id == id).exists()):
            cliente = Cliente.get_by_id(id)
            try: 
                cliente.delete_instance()
                return DELETED, 200
            except Exception as e:
               abort(400, e) 
        else:
            abort(404, ITEM_NOT_FOUND)

       