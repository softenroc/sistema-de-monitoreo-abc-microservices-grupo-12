from flask import request
from ..colas import mensaje_microservicio 
from flask_restful import Resource

class VistaColaPublicar(Resource):

    def post(self):
            mensaje = request.json["mensaje"]            
            mensaje_microservicio.delay(mensaje)
            return {'mensaje':'Prueba de redis ok'}, 200
            

