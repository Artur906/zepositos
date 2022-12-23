from flask_restx import fields
from src.server.instance import server

volume_model = server.api.model('Volume', {
    'largura':     fields.Integer(required=True, min=1, description='A largura do volume em centímetros.', example=110),
    'altura':      fields.Integer(required=True, min=1, description='A altura do volume em centímetros.', example=75),
    'comprimento': fields.Integer(required=True, min=1, description='O comprimento do volume em centímetros.', example=100),
    'peso':        fields.Fixed(required=True, min=0.1, description='O peso do volume em quilogramas.', example=10.5)
})
