import unittest
import src.tests.test_cliente_properties as test_cliente_properties
import src.tests.test_embarque_properties as test_embarque_properties
import src.tests.test_phone_validator as test_phone_validator
from src.server.postgredb import ApplicationPostgresqlDatabase


DATABASE_NAME = 'zepositosTEST'# (assegure que esta database exista no seu postgresql)
testdb = ApplicationPostgresqlDatabase(DATABASE_NAME)
testdb.start()


cliente_suite         = unittest.TestLoader().loadTestsFromModule(test_cliente_properties)
embarque_suite        = unittest.TestLoader().loadTestsFromModule(test_embarque_properties)
phone_validator_suite = unittest.TestLoader().loadTestsFromModule(test_phone_validator)

unittest.TextTestRunner(verbosity=2).run(cliente_suite)
unittest.TextTestRunner(verbosity=2).run(embarque_suite)
unittest.TextTestRunner(verbosity=2).run(phone_validator_suite)


