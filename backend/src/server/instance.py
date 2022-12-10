from flask import Flask
from flask_restx import Api
from flask_cors import CORS

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['JSON_SORT_KEYS'] = False
        CORS(self.app)
        self.api = Api(self.app,
            version='1.0',
            title='ZePositos API',
            description='API para o sistema de gerenciamento de embarques ZePositos',
            doc='/'
        )
    
    def run(self):
        self.app.run(
            debug=True# Por enquanto esta API só é usada para desenvolvimento.
        )

server = Server()