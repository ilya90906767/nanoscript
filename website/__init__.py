from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager
#from celery import Celery

db = SQLAlchemy()
DB_NAME = "database.db"
ALLOWED_EXTENSIONS = {'fastq'}




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjahdfgdsfdss kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    UPLOAD_FOLDER  ='./uploads' 
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
    db.init_app(app)


    #app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    #app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    #celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    #celery.conf.update(app.config)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Upload
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('База данных создана')
