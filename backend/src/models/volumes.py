from flask_restx import fields
from server.instance import server

volume_model = server.api.model('Volume', {
    'id':          fields.Integer(readonly=True, description='O identificador do volume.', example=1),
    'id_embarque': fields.Integer(required=True, description='O identificador do embarque a qual pertence o volume.', example=1),
    'largura':     fields.Integer(required=True, min=5, description='A largura do volume em centímetros.', example=100),
    'altura':      fields.Integer(required=True, min=5, description='A altura do volume em centímetros.', example=250),
    'comprimento': fields.Integer(required=True, min=5, description='O comprimento do volume em centímetros.', example=300),
    'peso':        fields.Fixed(required=True, min=0.1, description='O peso do volume em quilogramas.', example=10.5)
})
