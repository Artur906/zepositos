import unittest
from src.server.schemadb import Embarque
from decimal import Decimal


def create_test_data():
    volumesOfEmbarque1 = [
        {'peso': '3.123', 'largura': '1', 'altura': '1', 'comprimento': '1'},
        {'peso': '1.245', 'largura': '1', 'altura': '1', 'comprimento': '1'},
        {'peso': '2.321', 'largura': '1', 'altura': '1', 'comprimento': '1'},
    ]
    volumesOfEmbarque2 = [
        {'peso': '0.5', 'largura': '1', 'altura': '1', 'comprimento': '1'},
    ]

    embarques = [
        {'id': '1', 'descricao': 'embarque-1', 'volumes': volumesOfEmbarque1},
        {'id': '2', 'descricao': 'embarque-2', 'volumes': volumesOfEmbarque2},
        {'id': '3', 'descricao': 'embarque-3'}
    ]
    Embarque.insert_many(embarques).execute()


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
    