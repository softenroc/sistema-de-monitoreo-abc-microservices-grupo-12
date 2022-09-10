import json
import logging
from flask import request
from ..colas import boton_panico 
from flask_restful import Resource
from ..modelos import Alerta

logging.basicConfig(level=logging.INFO,filename='../log.log', filemode='w', format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class VistaColaPublicar(Resource):

    def post(self):

        alerta = Alerta( request.json['tipo'], request.json['mensaje'], request.json['cliente_id']  )
        jsonStr = json.dumps(alerta.__dict__)
        print('Mensaje a enviar: '+jsonStr)
        logging.info(f'Mensaje a enviar: '+jsonStr)
        args = (jsonStr,)                                  
        boton_panico.apply_async(args)                  
        return jsonStr
    