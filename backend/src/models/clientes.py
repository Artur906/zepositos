from flask_restx import fields
from src.server.instance import server

cliente = server.api.model('Cliente', {
    'id':       fields.Integer(readonly=True, description='O identificador do cliente.', example="1"),
    'nome':     fields.String(required=True, max_lenght=35, description='O nome do cliente.', example="Maria das Graças Souza"),
    'telefone': fields.String(max_lenght=11, description='O telefone de contato do cliente.', example="81999893153"),
    'quant_embarques': fields.Integer(readonly=True, description='A quantidade de embarques registrados do cliente.', example=3)
})