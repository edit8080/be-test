import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

from resources.person import *
from resources.visit import *
from resources.condition import *
from resources.drug import *


if __name__ == '__main__':
  db.init_app(app)
  app.run(port=5000, debug=True)
