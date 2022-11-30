nomeDatabase = 'zepositos'
usuario      = 'postgres'
senha        = '1423'

from peewee import PostgresqlDatabase
db = PostgresqlDatabase(nomeDatabase, host='localhost', port=5432, user=usuario, password=senha)
