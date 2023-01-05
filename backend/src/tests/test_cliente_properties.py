import unittest
from src.server.schemadb import Cliente, Embarque


def create_test_data():
    clientes = [
        {'id':'1', 'nome': 'Cliente-1'},
        {'id':'2', 'nome': 'Cliente-2'},
        {'id':'3', 'nome': 'Cliente-3'}
    ]
    Cliente.insert_many(clientes).execute()

    embarquesOfCliente1 = [
        {'id': '1', 'id_cliente':'1', 'descricao': 'embarque-1', 'embarcado': False},
        {'id': '2', 'id_cliente':'1', 'descricao': 'embarque-2', 'embarcado': True},
        {'id': '3', 'id_cliente':'1', 'descricao': 'embarque-3', 'embarcado': False}
    ]
    Embarque.insert_many(embarquesOfCliente1).execute()

    embarquesOfCliente2 = [
        {'id': '4', 'id_cliente':'2', 'descricao': 'embarque-4', 'embarcado': True}
    ]
    Embarque.insert_many(embarquesOfCliente2).execute()


class TestClienteProperties(unittest.TestCase):
    def setUp(self):
        create_test_data()
        self.cliente1 = Cliente.get_by_id(1)
        self.cliente2 = Cliente.get_by_id(2)
        self.cliente3 = Cliente.get_by_id(3)

    def test_clienteComNenhumEmbarque(self):
        self.assertEqual(0, self.cliente3.quant_embarques)
        self.assertEqual(0, self.cliente3.quant_embarques_ativos)

    def test_clienteComDoisEmbarquesAtivosEUmEmbarcado(self):
        self.assertEqual(3, self.cliente1.quant_embarques)
        self.assertEqual(2, self.cliente1.quant_embarques_ativos)

    def test_clienteComUmEmbarqueEmbarcado(self):
        self.assertEqual(1, self.cliente2.quant_embarques)
        self.assertEqual(0, self.cliente2.quant_embarques_ativos)

    def tearDown(self):
        clear_test_data()


def clear_test_data():
    Embarque.delete().execute()
    Cliente.delete().execute()