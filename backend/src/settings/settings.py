import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASS = os.getenv("DATABASE_PASS")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")