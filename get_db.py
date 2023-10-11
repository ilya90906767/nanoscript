from pymongo import MongoClient
import datetime

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://localhost:27017" 
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['nanoscript']

db = get_database()
users = db.users 

def insert_user(email,username,password):
    user = {
    "email": email,
    "username": username,
    "password": password }
    
    user_id = users.insert_one(user).inserted_id
    
    return

#insert_user('betyaev@gmail.com','ilya90906767','90906767')

def validate_email(email):
    if users.find_one({"email":email}) is None:
        return False
    else:
        return True


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
