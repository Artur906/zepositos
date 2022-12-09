from flask_restx import Resource, abort
from flask import jsonify
from flask import request

from server.postgredb import *
from server.instance import server
from models.embarques import embarque_model
from controllers.handyFunctions import has_id
app, api = server.app, server.api

ITEM_NOT_FOUND = 'Embarque não encontrado'
NO_ITEMS_FOUND = 'Nenhum embarque encontrado'


@api.route('/embarques')
class EmbarquesList(Resource):


    @api.doc('get_embarques')
    @api.marshal_list_with(embarque_model, envelope="embarques", code=200)
    @api.doc(responses={404: NO_ITEMS_FOUND})
    def get(self):
        query = Embarque.select()
        try:
            dados = [i.serialize for i in query]
        except:
            abort(404, NO_ITEMS_FOUND)
        return dados, 200
    
            



    @api.doc('create_embarque')
    @api.expect(embarque_model, validate=True)
    @api.marshal_with(embarque_model, code=201)
    @api.doc(responses={404: 'Campo id é de leitura apenas.'})
    def post(self):
        payload = api.payload
        if(has_id(payload)):
            abort(400, "Campo id é de leitura apenas.")
        try:
            embarque = Embarque(**payload)
            embarque.save()
            return embarque.serialize, 201
        except Exception as e:
            abort(400, e)



@api.route('/embarques/<int:id>')
class Embarques(Resource):

    @api.doc('get_embarques')
    @api.marshal_with(embarque_model, code=200)
    @api.doc(responses={404: ITEM_NOT_FOUND})
    def get(self, id):
        try:
            embarque = Embarque.get_by_id(id)
        except:
            abort(404, ITEM_NOT_FOUND)
        return embarque.serialize, 200
        
            
