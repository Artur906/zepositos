from peewee import PostgresqlDatabase
from src.server.esquemadb import *
from src.settings.settings import DATABASE_HOST, DATABASE_PASS, DATABASE_USER, DATABASE_PORT


#assegure que uma database com o nome abaixo exista
DATABASE_NAME = 'zepositos'

db = PostgresqlDatabase(DATABASE_NAME, host=DATABASE_HOST, port=DATABASE_PORT, user=DATABASE_USER, password=DATABASE_PASS)


tables = [Cliente, Embarque]
db.bind(tables)
db.connect()
db.create_tables(tables)
db.close()