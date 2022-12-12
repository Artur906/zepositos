from peewee import PostgresqlDatabase
from server.esquemadb import *

from settings.settings import DATABASE_HOST, DATABASE_PASS, DATABASE_USER, DATABASE_PORT


#assegure que uma database com o nome abaixo exista
DATABASE_NAME = 'zepositosTEST'

test_database = PostgresqlDatabase(DATABASE_NAME, host=DATABASE_HOST, port=DATABASE_PORT, user=DATABASE_USER, password=DATABASE_PASS)



tables = [Cliente, Embarque, Volume]
test_database.bind(tables)
test_database.connect()
test_database.create_tables(tables)
test_database.close()