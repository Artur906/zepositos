from src.server.postgredb import ApplicationPostgresqlDatabase
from src.server.instance import server
from src.controllers.clientes import *
from src.controllers.embarques import *
from src.controllers.embarquesOfCliente import *

DATABASE_NAME = 'zepositos'
zepositos_database = ApplicationPostgresqlDatabase(DATABASE_NAME)

zepositos_database.start()
server.run()