from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


from .models import db  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

api = Api(app)

from api import routes 
