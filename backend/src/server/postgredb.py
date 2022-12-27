from peewee import PostgresqlDatabase
from src.server.schemadb import Cliente, Embarque
from src.settings.settings import DATABASE_HOST, DATABASE_PASS, DATABASE_USER, DATABASE_PORT


class ApplicationPostgresqlDatabase():
    def __init__(self, database_name):
        self.__database = PostgresqlDatabase(database_name, host=DATABASE_HOST, port=DATABASE_PORT, user=DATABASE_USER, password=DATABASE_PASS)
    
    def start(self):
        tables = [Cliente, Embarque]
        self.__database.bind(tables)
        self.__database.connect()
        self.__database.create_tables(tables)
        self.__database.close()
