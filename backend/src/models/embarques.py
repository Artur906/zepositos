from datetime import date
from flask_restx import fields
from server.instance import server

embarque_model = server.api.model('Embarque', {
    'id':               fields.Integer(readonly=True, description='O identificador do embarque.', example=1),
    'id_cliente':       fields.Integer(description='O identificador do cliente dono do embarque.', example=1),
    'descricao':        fields.String(required=True, max_length=200, description='A descricao do embarque.', example="Caixas pretas grandes, entrega em domicílio."),
    'data_chegada':     fields.Date(default=date.today(), description='Data em que o embarque chegou ao depósito.'),
    'quant_volumes':    fields.Integer(readonly=True, description='A quantidade de volumes do embarque.', example = 3),
    'peso_total':       fields.Fixed(readonly=True, description='O peso total do embarque (soma do peso dos volumes).', example = 10.5),
    'com_nota_fiscal':  fields.Boolean(default=False, description="Embarque tem nota fiscal ou ainda não."),
    'registrado':       fields.Boolean(default=False, description="Embarque foi registrado no sistema próprio da transportadora ou ainda não."),
    'pago':             fields.Boolean(default=False, description="Embarque foi pago pelo cliente ou ainda não."),
    'urgente':          fields.Boolean(default=False, description="Embarque tem prioridade sobre outros ou não."),
    'embarcado':        fields.Boolean(default=False, description="Embarcado para chegar ao seu destino ou ainda está no depósito.")
})

