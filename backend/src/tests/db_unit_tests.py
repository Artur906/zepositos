import unittest
from src.server.schemadb import Cliente, Embarque
from decimal import Decimal






def create_test_data():
    clientes = [
        {'id':'1', 'nome': 'Cliente-1'},
        {'id':'2', 'nome': 'Cliente-2'},
        {'id':'3', 'nome': 'Cliente-3'},
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


    volumesOfEmbarque1 = [
        {'peso': '3.123', 'largura': '1', 'altura': '1', 'comprimento': '1'},
        {'peso': '1.245', 'largura': '1', 'altura': '1', 'comprimento': '1'},
        {'peso': '2.321', 'largura': '1', 'altura': '1', 'comprimento': '1'},
    ]
    embarque1 = Embarque.get_by_id(1)
    embarque1.volumes = volumesOfEmbarque1
    embarque1.save()


    volumesOfEmbarque2 = [
        {'peso': '0.5', 'largura': '1', 'altura': '1', 'comprimento': '1'},
    ]
    embarque2 = Embarque.get_by_id(2)
    embarque2.volumes = volumesOfEmbarque2
    embarque2.save()




class TestClienteProperties(unittest.TestCase):
    def setUp(self):
        create_test_data()
        self.cliente1 = Cliente.get_by_id(1)
        self.cliente2 = Cliente.get_by_id(2)
        self.cliente3 = Cliente.get_by_id(3)

    def test_quant_embarques(self):
        self.assertEqual(3, self.cliente1.quant_embarques)
        self.assertEqual(1, self.cliente2.quant_embarques)
        self.assertEqual(0, self.cliente3.quant_embarques)

    def test_quant_embarques_ativos(self):
        self.assertEqual(2, self.cliente1.quant_embarques_ativos)
        self.assertEqual(0, self.cliente2.quant_embarques_ativos)
        self.assertEqual(0, self.cliente3.quant_embarques_ativos)

    def tearDown(self):
        clear_test_data()



class TestEmbarqueProperties(unittest.TestCase):
    def setUp(self):
        create_test_data()
        self.embarque1 = Embarque.get_by_id(1)
        self.embarque2 = Embarque.get_by_id(2)
        self.embarque3 = Embarque.get_by_id(3)
    

    def test_quant_volumes(self):
        self.assertEqual(3, self.embarque1.quant_volumes)
        self.assertEqual(1, self.embarque2.quant_volumes)
        self.assertEqual(0, self.embarque3.quant_volumes)

    def test_peso_total(self):
        self.assertEqual(Decimal('6.689'), self.embarque1.peso_total)
        self.assertEqual(Decimal('0.5'),   self.embarque2.peso_total)
        self.assertEqual(Decimal('0'),     self.embarque3.peso_total)
       
    def tearDown(self):
        clear_test_data()


def clear_test_data():
    Embarque.delete().execute()
    Cliente.delete().execute()