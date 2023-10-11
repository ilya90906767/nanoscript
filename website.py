import streamlit as st
import streamlit_authenticator as stauth
from get_db import *
import re
from nanoscript import *
import time
import subprocess
import os
import sqlite3
import datetime
import pymongo
from typing import Literal

st.header("Nanoscript")
#fastqfile = st.file_uploader(label = "Загрузите ваш FASTQ файл" )

#if fastqfile is not None:
    #file_details = {"filename":fastqfile.name, "filetype":fastqfile.type,
                              #"filesize":fastqfile.size}
    #st.write(file_details)

  
# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
db = get_database()
users = db.users 


def validate_email_in_db(email):
    if users.find_one({"email":email}) is None:
        return False
    else:
        return True
    
def insert_user(email,username,password):
    user = {
    "email": email,
    "username": username,
    "password": password }
    
    user_id = users.insert_one(user).inserted_id
    
    return



def sign_uo():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(":green[Регистрация]")
        email = st.text_input('Email', placeholder='Введите ваш email')
        username = st.text_input('Имя Пользователя', placeholder='Введите имя пользователя')
        password1 = st.text_input('Пароль', placeholder='Введите пароль')
        password2 = st.text_input('Подвердите пароль', placeholder='Введите пароль еще раз')

        btn1,btn2,btn3,btn4,btn5 = st.columns(5)
        with btn3: 
            st.form_submit_button('Регистрация')

sign_uo()