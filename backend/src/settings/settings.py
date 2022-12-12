import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_PASS = os.getenv("DATABASE_PASS")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")

'''
Assegure-se que exista um arquivo .env localizado na pasta settings, 
e que neste arquivo voce inseriu as informacoes referentes ao PostgreSQL rodando em sua máquina.

ex: (.env)
DATABASE_USER="postgres"
DATABASE_PASS="1234"
DATABASE_HOST="localhost"
DATABASE_PORT=5432
'''