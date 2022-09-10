import string
from flask import request
from ..colas import boton_panico 
from flask_restful import Resource

class VistaColaPublicar(Resource):

    def post(self):
        mensaje = request.json['mensaje']                             
        args = (mensaje,)
        boton_panico.apply_async(args)                  
        return {'mensaje':'Prueba de redis ok'}, 200
    