from flask_restx import fields
from src.server.instance import server

cliente_model = server.api.model('Cliente', {
    'id':              fields.Integer(readonly=True, description='O identificador do cliente.', example="1"),
    'nome':            fields.String(required=True,  max_length=100, description='O nome do cliente.', example="Maria das Graças Souza"),
    'telefone':        fields.String(max_length=13, default=None, description='O telefone de contato do cliente (também pode ser fixo).', example="83 92646 2141"),
    'quant_embarques': fields.Integer(readonly=True, description='A quantidade de embarques registrados do cliente.', example=3)
})

cliente_model_patch = server.api.clone('PatchCliente', cliente_model,{
    'nome': fields.String(required=False, max_length=100, description='O nome do cliente.', example="Maria das Graças Souza")
})