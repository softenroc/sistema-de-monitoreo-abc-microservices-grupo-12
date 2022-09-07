from flaskr import create_app
from flask_restful import Api
from .vistas.vistas import VistaHealth
import logging


logging.basicConfig(filename='../log.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s : %(message)s')

app = create_app('microservicio')
app_context = app.app_context()
app_context.push()

app_context.push()

api = Api(app)
api.add_resource(VistaHealth, '/health')

with app.app_context():
    print("microservicio") 