from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="alerta.notificar")
def notificar(mensaje):
    pass