from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_envvar('FLASK_CONFIG')

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Registration api
from md5_api.api import app
