import unittest
import src.tests.db_unit_tests as db_unit_tests

suite = unittest.TestLoader().loadTestsFromModule(db_unit_tests)
unittest.TextTestRunner(verbosity=2).run(suite)




''' 
    Rode este arquivo para executar os testes.
    Antes certifique-se que seu postgre está rodando, e que nele há
    uma database chamada "zepositosTEST".
    Certifique-se que na pasta settings ha um .env configurado.
'''
