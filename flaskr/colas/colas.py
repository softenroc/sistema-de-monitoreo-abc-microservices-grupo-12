from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="registrar_log")
def registrar_log(usuario):
    with open('cola_mensajes.txt','a') as file:
        file.write('{} - Prueba de cola:{}\n'.format(usuario))