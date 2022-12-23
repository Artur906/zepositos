from flask_restx import Resource, abort

from src.server.schemadb import Embarque
from src.server.instance import server
from src.models.embarques import embarque_model, embarque_model_patch

app, api = server.app, server.api

ITEM_NOT_FOUND  = 'Nenhum embarque encontrado'
ID_IS_READ_ONLY = 'Campo id é de leitura apenas'
DELETED         = "Deletado!"


@api.route('/embarques')
class EmbarquesList(Resource):


    @api.doc('get_embarques')
    @api.marshal_list_with(embarque_model, envelope="embarques", code=200)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self):
        query = Embarque.select()
        try:
            dados = [i.serialize for i in query]
        except:
            abort(404, ITEM_NOT_FOUND)
        return dados, 200
    
            



    @api.doc('create_embarque')
    @api.expect(embarque_model, validate=True)
    @api.marshal_with(embarque_model, code=201)
    @api.doc(responses={400: ID_IS_READ_ONLY})
    def post(self):
        payload = api.payload
        if('id' in payload):
            abort(400, ID_IS_READ_ONLY)
        try:
            embarque = Embarque(**payload)
            embarque.save()
            return embarque.serialize, 201
        except Exception as e:
            abort(400, e)



@api.route('/embarques/<int:id>')
class Embarques(Resource):

    @api.doc('get_embarque')
    @api.marshal_with(embarque_model, code=200)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self, id):
        try:
            embarque = Embarque.get_by_id(id)
        except:
            abort(404, ITEM_NOT_FOUND)
        return embarque.serialize, 200
        
            

    @api.doc('update_embarque')
    @api.marshal_with(embarque_model_patch, code=200)
    @api.expect(embarque_model_patch, validate=True)
    @api.doc(responses={404: ITEM_NOT_FOUND, 400: ID_IS_READ_ONLY})
    def patch(self, id):
        payload = api.payload
        if('id' in payload):
            abort(400, ID_IS_READ_ONLY)
        try:
            Embarque.get_by_id(id)
        except:
            abort(404, ITEM_NOT_FOUND)

        try:
            Embarque.update(**payload).where(Embarque.id == id).execute()
            updatedEmbarque = Embarque.get_by_id(id)
            return updatedEmbarque.serialize, 200
        except Exception as e:
            abort(400, e)

    @api.doc('delete_embarque')
    @api.doc(responses={200: DELETED, 404: ITEM_NOT_FOUND})
    def delete(self, id):
        if(Embarque.select().where(Embarque.id == id).exists()):
            embarque = Embarque.get_by_id(id)
            try: 
                embarque.delete_instance()
                return DELETED, 200
            except Exception as e:
               abort(400, e) 
        else:
            abort(404, ITEM_NOT_FOUND)