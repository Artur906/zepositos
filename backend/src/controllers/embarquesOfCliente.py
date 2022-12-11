from flask_restx import Resource, abort

from server.postgredb import *
from server.instance import server
from models.embarques import embarque_model

app, api = server.app, server.api

ITEM_NOT_FOUND = 'Nenhum embarque encontrado'


@api.route('/clientes/<int:id_cliente>/embarques')
class EmbarquesOfCliente(Resource):

    @api.doc('get_embarques_of_cliente')
    @api.marshal_list_with(embarque_model, code=200, envelope="embarques")
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self, id_cliente):

        query = Embarque.select().where(Embarque.id_cliente == id_cliente)
        if(query.count() == 0):
            abort(404, ITEM_NOT_FOUND)    
        dados = [i.serialize for i in query]
        return dados, 200
        
