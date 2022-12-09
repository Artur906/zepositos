from peewee import PostgresqlDatabase
from src.server.esquemadb import *

databaseName = 'zepositos'
user         = 'postgres'
password     = '1423'


db = PostgresqlDatabase(databaseName, host='localhost', port=5432, user=user, password=password)


tables = [Cliente, Embarque, Volume]
db.bind(tables)
db.connect()
db.create_tables(tables)
db.close()