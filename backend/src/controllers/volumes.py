from flask_restx import Resource, abort

from server.postgredb import *
from server.instance import server
from models.volumes import volume_model
from controllers.handyFunctions import has_id

app, api = server.app, server.api


ITEM_NOT_FOUND = 'Nenhum volume encontrado'




@api.route('/volumes')
class VolumesList(Resource):

    @api.doc('get_volumes')
    @api.marshal_list_with(volume_model, envelope="volumes", code=200)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self):
        query = Volume.select()
        try:
            dados = [i.serialize for i in query]
        except:
            abort(404, ITEM_NOT_FOUND)
        return dados, 200

            

    

    @api.doc('create_volume')
    @api.expect(volume_model, validate=True)
    @api.marshal_with(volume_model, code=201)
    @api.doc(responses={404: 'Campo id é de leitura apenas.'})
    def post(self):
        payload = api.payload
        if(has_id(payload)):
            abort(400, "Campo id é de leitura apenas.")
        try:
            volume = Volume(**payload)
            volume.save()
            return volume.serialize, 201
        except Exception as e:
            abort(400, e)

        


@api.route('/volumes/<int:id>')
class Clientes(Resource):

    @api.doc('get_volume')
    @api.marshal_with(volume_model, code=200)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self, id):
        try:
            volume = Volume.get_by_id(id)
        except:
            abort(404, ITEM_NOT_FOUND)
        return volume.serialize, 200
            
