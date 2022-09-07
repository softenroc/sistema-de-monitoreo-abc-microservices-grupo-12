from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="mensaje_microservicio")
def mensaje_microservicio(mensaje):
    respuesta = "Enviado a redis: "+mensaje
    print(respuesta)
    return respuesta