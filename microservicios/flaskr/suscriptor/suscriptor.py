from celery import Celery
import os
import logging
import json
from modelos import Alerta
logging.basicConfig(level=logging.INFO,filename='../log.log', filemode='w', format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%d-%b-%y %H:%M:%S')

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="alerta.notificar")
def notificar(alerta_json):
     print(f'Nueva notificacion de alerta : '+json.dumps(alerta_json))
     logging.info(f'Nueva notificacion de alerta: '+alerta_json)  
     accionPorTipoAlerta(alerta_json)

def accionPorTipoAlerta(alerta_json):
    pass
