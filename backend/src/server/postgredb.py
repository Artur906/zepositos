from peewee import PostgresqlDatabase
from src.server.esquemadb import Cliente, Embarque
from src.settings.settings import DATABASE_HOST, DATABASE_PASS, DATABASE_USER, DATABASE_PORT


class ApplicationPostgresqlDatabase():
    def __init__(self, database_name):
        self.__db = PostgresqlDatabase(database_name, host=DATABASE_HOST, port=DATABASE_PORT, user=DATABASE_USER, password=DATABASE_PASS)
    
    def start(self):
        tables = [Cliente, Embarque]
        self.__db.bind(tables)
        self.__db.connect()
        self.__db.create_tables(tables)
        self.__db.close()
