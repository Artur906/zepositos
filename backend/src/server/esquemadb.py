from peewee import Model, TextField,ForeignKeyField, BooleanField, DateField, DecimalField, IntegerField
from datetime import datetime

'''
CLIENTE(id, nome, telefone)

EMBARQUE(id, id_cliente, data_chegada, com_nota_fiscal, registrado, pago, embarcado)

VOLUME(id, id_embarque, largura, comprimento, altura, peso)
'''

class BaseModel(Model):
    @property
    def serialize(self):# to-do: make it abstract, so children classes MUST implement it.
        # MUST return self in dict (json) format. ex: {'key1': self.value1, 'key2': self.value2, ...}
        pass
   

class Cliente(BaseModel):
    nome     = TextField(null=False)
    telefone = TextField(unique=True, null=True)

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'quant_embarques': self.quant_embarques
        }
        return data
    
    @property
    def quant_embarques(self):
        q = (
            Embarque
            .select()
            .where(Embarque.id_cliente == self.id)
            .count()
        )
        return q

class Embarque(BaseModel):
    id_cliente      = ForeignKeyField(Cliente, backref='embarque', null=True, on_delete='CASCADE')
    descricao       = TextField()
    data_chegada    = DateField(default = datetime.now)
    com_nota_fiscal = BooleanField(default = False)
    registrado      = BooleanField(default = False)
    pago            = BooleanField(default = False)
    urgente         = BooleanField(default = False)
    embarcado       = BooleanField(default = False)


    @property
    def serialize(self):
        try:
            #gambiarra para nao retornar o tipo <Model>
            int_id_cliente = (Cliente.select().where(Cliente.id == self.id_cliente).get()).id
        except:
            int_id_cliente = None
        data = {
            'id': self.id,
            'id_cliente': int_id_cliente,
            'descricao': self.descricao,
            'data_chegada': self.data_chegada,
            'quant_volumes': self.quant_volumes,
            'peso_total': self.peso_total,
            'com_nota_fiscal': self.com_nota_fiscal,
            'registrado': self.registrado,
            'pago': self.pago,
            'urgente': self.urgente,
            'embarcado': self.embarcado
        }
        return data
    
    @property
    def quant_volumes(self):
        q = (
            Volume
            .select()
            .where(Volume.id_embarque == self.id)
            .count()
        )
        return q

    @property
    def peso_total(self):
        q = (
            Volume
            .select(Volume.peso)
            .where(Volume.id_embarque == self.id)
        )
        total = 0
        for row in q:
            total += row.peso
        return total
    
    

class Volume(BaseModel):
    id_embarque = ForeignKeyField(Embarque, backref='volume', on_delete='CASCADE')
    largura     = DecimalField(null=False)#centimetros
    comprimento = DecimalField(null=False)#centimetros
    altura      = DecimalField(null=False)#centimetros
    peso        = DecimalField(null=False)#quilogramas

    @property
    def serialize(self):
        try:
            #gambiarra para nao retornar o tipo <Model>
            int_id_embarque = (Embarque.select().where(Embarque.id == self.id_embarque).get()).id
        except:
            int_id_embarque = None

        data = {
            'id': self.id,
            'id_embarque': int_id_embarque,
            'largura': self.largura,
            'comprimento': self.comprimento,
            'altura': self.altura,
            'peso': self.peso
        }
        return data
    

