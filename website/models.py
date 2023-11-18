from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String())
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Status info: 
    # 0 - just uploaded 1 - sent to cluster 2 - processing 3 - sent to the server 4 - done 5 - error
    status = db.Column(db.Integer()) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    uploads = db.relationship('Upload')

 
