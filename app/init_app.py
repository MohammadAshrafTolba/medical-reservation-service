from flask import Flask
from flask_restful import Api
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

import routes