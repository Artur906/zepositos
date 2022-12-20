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
    
    def test_quant_embarques(self):
        create_test_data()
        c1 = Cliente.get_by_id(1)
        c2 = Cliente.get_by_id(2)
        c3 = Cliente.get_by_id(3)
        try:
            self.assertEqual(c1.quant_embarques, 3)
            self.assertEqual(c2.quant_embarques, 1)
            self.assertEqual(c3.quant_embarques, 0)
        except AssertionError:
            raise
        finally:
            clear_test_data()
    

    def test_quant_embarques_ativos(self):
        create_test_data()
        c1 = Cliente.get_by_id(1)
        c2 = Cliente.get_by_id(2)
        c3 = Cliente.get_by_id(3)
        try:
            self.assertEqual(c1.quant_embarques_ativos, 2)
            self.assertEqual(c2.quant_embarques_ativos, 0)
            self.assertEqual(c3.quant_embarques_ativos, 0)
        except AssertionError:
            raise
        finally:
            clear_test_data()





class TestEmbarquesMethods(unittest.TestCase):

    
    def test_peso_total(self):
        create_test_data()
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
        create_test_data()
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