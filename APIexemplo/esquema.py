from postgredb import *
from peewee import Model, TextField, ForeignKeyField, DateTimeField

class BaseModel(Model):
    class Meta:
        database = db

    @property
    def serialize(self):# to-do: make it abstract, so children classes MUST implement it.
        # MUST return self in dict format. ex: {'key1': self.value1, 'key2': self.value2, ...}
        pass
    

class Clientes(BaseModel):
    nome = TextField()

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'nome': self.nome
        }
        return data



lista_tabelas = [
    Clientes
]

db.connect()
db.create_tables(lista_tabelas)
db.close()

