from flaskr import create_app
from flask_restful import Api
from .vistas.vistas import VistaHealth

app = create_app('microservicio')
app_context = app.app_context()
app_context.push()

app_context.push()

api = Api(app)
api.add_resource(VistaHealth, '/health')

with app.app_context():
    print("microservicio") 