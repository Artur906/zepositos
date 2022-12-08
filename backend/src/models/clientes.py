from flask_restx import fields
from server.instance import server

cliente = server.api.model('Cliente', {
    'id': fields.Integer(unique=True),
    'nome': fields.String(required=True, max_lenght=50, description='O nome do cliente.'),
    'telefone': fields.String(required=False, max_lenght=11, unique=True, description='O telefone de contato do cliente.')
})