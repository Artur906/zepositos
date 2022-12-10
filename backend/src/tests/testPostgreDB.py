from peewee import PostgresqlDatabase
from esquemadb import *

databaseName = 'zepositosTEST'
user         = 'postgres'
password     = '1423'


test_database = PostgresqlDatabase(databaseName, host='localhost', port=5432, user=user, password=password)


tables = [Cliente, Embarque, Volume]
test_database.bind(tables)
test_database.connect()
test_database.create_tables(tables)
test_database.close()