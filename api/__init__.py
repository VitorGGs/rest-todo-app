from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


basedir = os.path.abspath(os.path.dirname(__file__))

api = Flask(__name__)

api.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api.secret_key = os.environ.get('SECRET_KEY', 'macacos-me-mordam')

db = SQLAlchemy(api)
migrate = Migrate(api, db)

from api import models, routes