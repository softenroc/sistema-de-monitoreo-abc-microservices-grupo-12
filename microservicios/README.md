# sistema-de-monitoreo-abc-microservices-grupo-12
CLINICA ABC Grupo 12 - Arquitecturas ágiles de software 202214

###  README
##### Pasos para configurar Flask

- python3 -m venv venv
- source venv/Scripts/activate
- pip install flask
- pip install celery
- pip install redis
- pip install flask_restful
- Crear carpeta flaskr
- Dentro creamos el archjivo __init__.py

- pip install flask_sqlalchemy
- pip install marshmallow-sqlalchemy

- Para lanzar el consumir de las colas: celery -A suscriptor  worker -l info