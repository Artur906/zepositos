from peewee import PostgresqlDatabase
from src.server.esquemadb import Cliente, Embarque
from src.settings.settings import DATABASE_HOST, DATABASE_PASS, DATABASE_USER, DATABASE_PORT


#assegure que uma database com o nome abaixo exista



class ApplicationPostgresqlDatabase():
    def __init__(self, database_name):
        self.__DATABASE_NAME = database_name
        self.__db = PostgresqlDatabase(self.__DATABASE_NAME, host=DATABASE_HOST, port=DATABASE_PORT, user=DATABASE_USER, password=DATABASE_PASS)
    
    def start(self):
        tables = [Cliente, Embarque]
        self.__db.bind(tables)
        self.__db.connect()
        self.__db.create_tables(tables)
        self.__db.close()



