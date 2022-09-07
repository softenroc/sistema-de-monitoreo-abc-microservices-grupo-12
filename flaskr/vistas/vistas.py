from flask import request
from ..colas import registrar_log 
from flask_restful import Resource

class VistaColaPublicar(Resource):

    def post(self):
            u_nombre = request.json["nombre"]            
            registrar_log.delay(u_nombre)
            return {'mensaje':'IPrueba de redis ok'}, 200
            

