import unittest
from src.server.schemadb import Cliente, Embarque
from decimal import Decimal



def clear_test_data():
    Embarque.delete().execute()
    Cliente.delete().execute()


def create_test_data():
    clear_test_data()
    clientes = [
        {'id':'1', 'nome': 'Cliente-1'},
        {'id':'2', 'nome': 'Cliente-2'},
        {'id':'3', 'nome': 'Cliente-3'},
    ]
    Cliente.insert_many(clientes).execute()

    embarquesC1 = [
        {'id': '1', 'id_cliente':'1', 'descricao': 'embarque-1', 'embarcado': False},
        {'id': '2', 'id_cliente':'1', 'descricao': 'embarque-2', 'embarcado': True},
        {'id': '3', 'id_cliente':'1', 'descricao': 'embarque-3', 'embarcado': False}
    ]
    Embarque.insert_many(embarquesC1).execute()

    embarquesC2 = [
        {'id': '4', 'id_cliente':'2', 'descricao': 'embarque-4', 'embarcado': True}
    ]
    Embarque.insert_many(embarquesC2).execute()


    volumesEmb1 = [
        {'peso': '3.123', 'largura': '1', 'altura': '1', 'comprimento': '1'},
        {'peso': '1.245', 'largura': '1', 'altura': '1', 'comprimento': '1'},
        {'peso': '2.321', 'largura': '1', 'altura': '1', 'comprimento': '1'},
    ]


    emb1 = Embarque.get_by_id(1)
    emb1.volumes = volumesEmb1
    emb1.save()


    volumesEmb2 = [
        {'peso': '0.5', 'largura': '1', 'altura': '1', 'comprimento': '1'},
    ]
    emb2 = Embarque.get_by_id(2)
    emb2.volumes = volumesEmb2
    emb2.save()




class TestClienteMethods(unittest.TestCase):
    def setUp(self):
        create_test_data()
        self.c1 = Cliente.get_by_id(1)
        self.c2 = Cliente.get_by_id(2)
        self.c3 = Cliente.get_by_id(3)

    def test_quant_embarques(self):
        self.assertEqual(3, self.c1.quant_embarques)
        self.assertEqual(1, self.c2.quant_embarques)
        self.assertEqual(0, self.c3.quant_embarques)


    def test_quant_embarques_ativos(self):
        self.assertEqual(2, self.c1.quant_embarques_ativos)
        self.assertEqual(0, self.c2.quant_embarques_ativos)
        self.assertEqual(0, self.c3.quant_embarques_ativos)

    def tearDown(self):
        clear_test_data()



class TestEmbarquesMethods(unittest.TestCase):
    def setUp(self):
        create_test_data()
        self.emb1 = Embarque.get_by_id(1)
        self.emb2 = Embarque.get_by_id(2)
        self.emb3 = Embarque.get_by_id(3)
    
    def test_peso_total(self):
        self.assertEqual(Decimal('6.689'), self.emb1.peso_total)
        self.assertEqual(Decimal('0.5'),   self.emb2.peso_total)
        self.assertEqual(Decimal('0'),     self.emb3.peso_total)

    def test_quant_volumes(self):
        self.assertEqual(3, self.emb1.quant_volumes)
        self.assertEqual(1, self.emb2.quant_volumes)
        self.assertEqual(0, self.emb3.quant_volumes)
       
    def tearDown(self):
        clear_test_data()