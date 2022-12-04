from decimal import Decimal
from testingPostgreDB import *

import unittest

def clear_test_data():
    Volume.delete().execute()
    Embarque.delete().execute()
    Cliente.delete().execute()

class TestEmbarquesMethods(unittest.TestCase):

    def create_test_data(self):
        clear_test_data()
        embarques = [
            {'id': '1', 'descricao': 'embarque-1'},
            {'id': '2', 'descricao': 'embarque-2'},
            {'id': '3', 'descricao': 'embarque-3'}
        ]
        Embarque.insert_many(embarques).execute()

        volumesEmb1 = [
            {'id_embarque': '1', 'peso': '3.123', 'largura': '1', 'altura': '1', 'comprimento': '1', 'id': '1'},
            {'id_embarque': '1', 'peso': '1.245', 'largura': '1', 'altura': '1', 'comprimento': '1', 'id': '2'},
            {'id_embarque': '1', 'peso': '2.321', 'largura': '1', 'altura': '1', 'comprimento': '1', 'id': '3'},
        ]
        Volume.insert_many(volumesEmb1).execute()
        
        volumesEmb2 = [
            {'id_embarque': '2', 'peso': '0.5', 'largura': '1', 'altura': '1', 'comprimento': '1', 'id': '4'},
        ]
        Volume.insert_many(volumesEmb2).execute()

        

    def test_peso_total(self):
        self.create_test_data()
        emb1 = Embarque.get_by_id(1)
        emb2 = Embarque.get_by_id(2)
        emb3 = Embarque.get_by_id(3)

        try:
            self.assertEqual(emb1.peso_total, Decimal('6.689'))
            self.assertEqual(emb2.peso_total, Decimal('0.5'))
            self.assertEqual(emb3.peso_total, Decimal('0'))
        except AssertionError:
            raise
        finally:
            clear_test_data()
        
    

    
    def test_quant_volumes(self):
        
        self.create_test_data()
        emb1 = Embarque.get_by_id(1)
        emb2 = Embarque.get_by_id(2)
        emb3 = Embarque.get_by_id(3)

        try:
            self.assertEqual(emb1.quant_volumes, 3)
            self.assertEqual(emb2.quant_volumes, 1)
            self.assertEqual(emb3.quant_volumes, 0)
        except AssertionError:
            raise
        finally:
            clear_test_data()
        
    


if __name__ == '__main__':
    unittest.main()
  
