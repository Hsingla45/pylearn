from mongodbhelper import MongoDBHelper
from mongodb_user_class import User
import datetime
from bson.objectid import ObjectId

def main():
    
    print("Welcome to MongoDb Test App")
    dbHelper = MongoDBHelper()
    
    query = {"email": "sia@ex.com"}
    document_to_update = {"name": "mia", "age": 32, "created_on": datetime.datetime.now()}
    
    #dbHelper.update(document = document_to_update, query= query)
    
    #user = User()
    #user.add_user_details()
    #document = vars(user)
    
    #dbHelper.insert(document)
    
    #query = {"_id"= ObjectId("gfhsgdjsfyjk")}
    
    #users = dbHelper.fetch()
    #for user in  users:
    #    print(user)
    
    
    query = {"email": "george@ex.com"}
    document_to_update = {"name": "georgeW", "age": 32, "created_on": datetime.datetime.now()}
    
    dbHelper.update(document=document_to_update, query=query)
    
    
if __name__ == "__main__":
    main()