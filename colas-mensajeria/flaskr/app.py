from flaskr import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .vistas import VistaColaPublicar, VistaLogin
import logging

logging.basicConfig(filename='../log.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s : %(message)s')


app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaColaPublicar, '/publicar')
api.add_resource(VistaLogin, '/login')


jwt = JWTManager(app)
with app.app_context():
    print("experimento") 