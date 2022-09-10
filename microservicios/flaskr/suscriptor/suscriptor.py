from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="alerta.boton_panico")
def boton_panico(mensaje):
     print("Se activo el boton de panico!!! :" +mensaje, file=sys.stderr)    
