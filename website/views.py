from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Upload
import os
from . import db
import json
import paramiko
import time
#from .tasks import send_and_process_fastq

host = 'calc.cod.phystech.edu'
secret = 'Gq~#aCztH%6A}u'
username = 'kumondorova.a'
port = 22

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        uploaded_file = request.files['file_upload']
        if uploaded_file.filename != '':
            uploaded_file.save(f'./uploads/{uploaded_file.filename}')

            if 1==1:
                new_file = Upload(filename=uploaded_file.filename, user_id=current_user.id,status=0 )  #providing the schema for the note 
                db.session.add(new_file) #adding the note to the database 
                db.session.commit()
                flash('Файл загружен', category='success')

    return render_template("home.html", user=current_user)

@views.route('/send/<int:id>')
def send(id):
    file_to_cluster = Upload.query.get_or_404(id)
    dir = f"uploads/{file_to_cluster.filename}"
    abs_dir = os.path.abspath(dir)
    #send_and_process_fastq.apply_async(args = [host, username, secret, port, file_to_cluster], countdown=210)

    #flash(list(db.session.query(Upload).all()), category='success')
    #flash(list(db.session.query(Upload).filter(Upload.status == 0).all()),category='success')
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

@views.route('/ks.rsmu',methods=['GET', 'POST'] )
def find():
    
    return redirect('/')
