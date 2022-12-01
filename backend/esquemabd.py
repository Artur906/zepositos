from peewee import Model, TextField,ForeignKeyField, BooleanField, DateField, DecimalField, IntegerField
from postgredb import *
from datetime import datetime

'''
CLIENTE(id, nome, telefone)

EMBARQUE(id, id_cliente, data_chegada, com_nota_fiscal, registrado, pago, embarcado)

VOLUME(id, id_embarque, largura, comprimento, altura, peso)
'''

class BaseModel(Model):
    class Meta:
        database = db

    @property
    def serialize(self):# to-do: make it abstract, so children classes MUST implement it.
        # MUST return self in dict format. ex: {'key1': self.value1, 'key2': self.value2, ...}
        pass
   

class Cliente(BaseModel):
    nome     = TextField(null=False)
    telefone = TextField()

class Embarque(BaseModel):
    id_cliente      = ForeignKeyField(Cliente, backref='embarque')
    data_chegada    = DateField(default = datetime.now)
    com_nota_fiscal = BooleanField(default = False)
    registrado      = BooleanField(default = False)
    pago            = BooleanField(default = False)
    embarcado       = BooleanField(default = False)
    
class Volume(BaseModel):
    id_embarque = ForeignKeyField(Embarque, backref='volume')
    largura     = DecimalField(null=False)
    comprimento = DecimalField(null=False)
    altura      = DecimalField(null=False)
    peso        = DecimalField(null=False)
    

lista_tabelas = [
    Cliente, Embarque, Volume
]

db.connect()
db.create_tables(lista_tabelas)
db.close()