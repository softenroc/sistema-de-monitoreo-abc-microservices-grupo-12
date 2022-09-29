import json
import logging
from flask import request
from ..colas import notificar 
from flask_restful import Resource
from ..modelos import Alerta
from flask_jwt_extended import jwt_required, create_access_token

logging.basicConfig(level=logging.INFO,filename='../log.log', filemode='w', format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class VistaColaPublicar(Resource):

    def post(self):

        alerta = Alerta(request.json['tipo'], request.json['mensaje'], request.json['cliente'])
        jsonStr = json.dumps(alerta.__dict__)
        print('Mensaje a enviar: '+jsonStr)
        logging.info(f'Mensaje a enviar: '+jsonStr)
        args = (jsonStr,)                                  
        notificar.apply_async(args)                  
        return jsonStr

class VistaLogin(Resource):

    def post(self):
        usuario = request.json['usuario']
        contrasena = request.json['contrasena']
        print(usuario,"------------------------------------------", contrasena)
        if (usuario == 'jj' and contrasena == "123"):
            print("------------------------------------------")
            token_de_acceso = create_access_token(identity = request.json["usuario"])
            return {"mensaje":"Usuario y contraseña correctos", "token de acceso":token_de_acceso}
        else:
            print("pppppppppppppppppppppppppppppppppp")
            return {"mensaje":"Usuario y contraseña incorrectos"}
