from esquema import *

lista_clientes = [
    {'nome': 'O Rocha'},
    {'nome': 'Keanu Jeeves'},
    {'nome': 'Morgan HomemLivre'}
]
Clientes.insert_many(lista_clientes).execute()