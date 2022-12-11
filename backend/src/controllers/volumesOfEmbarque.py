from flask_restx import Resource, abort

from server.postgredb import *
from server.instance import server
from models.volumes import volume_model

app, api = server.app, server.api

ITEM_NOT_FOUND = 'Nenhum volume encontrado'


@api.route('/embarques/<int:id_embarque>/volumes')
class EmbarquesOfCliente(Resource):
    @api.doc('get_volumes_of_embarque')
    @api.marshal_list_with(volume_model, code=200, envelope="volumes")
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self, id_embarque):
        query = Volume.select().where(Volume.id_embarque == id_embarque)
        if(query.count() == 0):
            abort(404, ITEM_NOT_FOUND)
        
        dados = [i.serialize for i in query]
        return dados, 200
        
