from website import *
from flask_pymongo import PyMongo 

app = create_app()



if __name__ == "__main__":
    app.run(debug=True, port =5002)
    