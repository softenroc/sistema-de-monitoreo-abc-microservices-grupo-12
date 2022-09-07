
# Declarar el contructor con el nombre de la aplicación
from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    return app