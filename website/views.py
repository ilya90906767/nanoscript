from flask import Blueprint, render_template, request, flash
from .extensions import mongo


views = Blueprint('views', __name__)


@views.route('/sign_up/',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        db = SQLAlchemy(app)

        if len(email)<4:
            flash('Email должен быть длиннее чем 4 символа, перепроверьте его!',category='error') 
            pass 
        #elif mongo.db.count({"email":email}, { limit: 1 }) == 1:
            #flash('Данный email уже зарегестрирован', category='error')

        elif password1 != password2:
            flash('Пароли не совпадают, перепроверьте их!',category='error')
            pass
        elif len(password1)<6:
            flash('Пароль должен содержать больше 6-ти символов',category='error')
            pass
        else:
            flash('Аккаунт был зарегестрирован!',category='success')
        
        users_collection.insert_one({'username': username, 'email': email, 'password': password1})





    return render_template("sign_up.html") 

@views.route('/login/',methods=['GET','POST'])
def sign_in():
    login_data = request.form
    return render_template("sign_in.html") 


