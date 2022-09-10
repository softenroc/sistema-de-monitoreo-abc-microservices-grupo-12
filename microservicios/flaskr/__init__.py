from flask import Flask
from celery import Celery

celery = Celery(__name__, broker='redis://localhost:6379/0')

def create_app(config_name):
    app = Flask(__name__)
    return app