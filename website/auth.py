from flask import Blueprint, render_template

views = Blueprint('auth', __name__)

@auth.route('/')
def login():
    return render_template("sign_in.html") 