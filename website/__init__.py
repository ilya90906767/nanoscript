from flask import Flask,request, session
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo 
from .extensions import mongo
import os
#db = SQLAlchemy()
#DB_NAME = 'users.db'
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "20797fa400cf1b15deede7ae4262d2ebc32f025c"

    from .views import views
    #from .auth import auth

    #app.register_blueprint(auth, url_prefix='/auth/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nanoscript.db'
    app.register_blueprint(views, url_prefix='/')

    return app

