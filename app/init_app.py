import sys
sys.path.append('.')
sys.path.append('./app')

from flask import Flask
from flask_restful import Api
from AppSrc.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
ma = Marshmallow(app)
db = SQLAlchemy(app)
