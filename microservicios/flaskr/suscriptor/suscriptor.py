from celery import Celery
import os

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="alerta.boton_panico")
def boton_panico(args):
     print("Se activo el boton de panico!!! :" +args[0], file=sys.stderr)    
