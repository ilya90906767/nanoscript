from website import create_app
# -*- coding: utf-8 -*-
import os,sys

#путь к проекту
#sys.path.append('/home/b/betyaevilj/public_html')
#путь к фреймворку
#sys.path.append('/home/b/betyaevilj/public_html')
#путь к виртуальному окружению
#sys.path.append('/home/b/betyaevilj/public_html/nanoscript/lib/python3.8/site-packages/')
#исключить системную директорию

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
