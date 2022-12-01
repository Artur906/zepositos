nomeDatabase = 'zepositos'
usuario      = 'postgres'
senha        = '1234'

from peewee import PostgresqlDatabase
db = PostgresqlDatabase(nomeDatabase, host='localhost', port=5432, user=usuario, password=senha)
