import unittest
import src.tests.db_unit_tests as db_unit_tests
import src.tests.test_phone_validator as test_phone_validator
from src.server.postgredb import ApplicationPostgresqlDatabase


DATABASE_NAME = 'zepositosTEST'
testdb = ApplicationPostgresqlDatabase(DATABASE_NAME)
testdb.start()


db_suite              = unittest.TestLoader().loadTestsFromModule(db_unit_tests)
phone_validator_suite = unittest.TestLoader().loadTestsFromModule(test_phone_validator)
unittest.TextTestRunner(verbosity=2).run(db_suite)
unittest.TextTestRunner(verbosity=2).run(phone_validator_suite)


''' 
    Rode este arquivo para executar os testes.
    Antes certifique-se que seu postgre está rodando, e que nele há
    uma database chamada "zepositosTEST".
    Certifique-se que na pasta settings ha um .env configurado.
'''
