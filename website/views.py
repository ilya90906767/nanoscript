from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Upload
import os
from . import db
import json


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        uploaded_file = request.files['file_upload']
        if uploaded_file.filename != '':
            uploaded_file.save(f'./uploads/{uploaded_file.filename}')

            if 1==1:
                new_file = Upload(filename=uploaded_file.filename, user_id=current_user.id)  #providing the schema for the note 
                db.session.add(new_file) #adding the note to the database 
                db.session.commit()
                flash('Файл загружен', category='success')

    return render_template("home.html", user=current_user)

@views.route('/send/<int:id>')
def send(id):
    #file_to_cluster = Upload.query.get_or_404(id)
   # dir = f"uploads/{file_to_cluster.filename}"
    return redirect('/')

@views.route('/delete/<int:id>')
def delete(id):
    update_to_delete = Upload.query.get_or_404(id)

    try: 
        db.session.delete(update_to_delete)
        db.session.commit()
        #update_to_delete.filename Дает имя файла с расширением
        return redirect('/')
    
    except: 
        return "Возникла проблема в удалении загруженного файла"

