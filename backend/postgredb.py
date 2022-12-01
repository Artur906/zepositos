nomeDatabase = 'zepositos'
usuario      = 'postgres'
senha        = 'senhasegura'

from peewee import PostgresqlDatabase
db = PostgresqlDatabase(nomeDatabase, host='localhost', port=5432, user=usuario, password=senha)
