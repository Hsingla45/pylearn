import datetime
import hashlib

class User:
    
    def __init__(self, name="", phone="", email="", passowrd="", age="", gender=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.passowrd = passowrd
        self.age = age
        self.gender = gender
        self.created_on = datetime.datetime.now()
        
    def add_user_details(self):
        self.name= input("Enter user name:")
        self.phone= input("Enter user phone:")
        self.email= input("Enter user email:")
        self.passowrd= input("Enter user passowrd:").encode('utf-8')
        self.password = hashlib.sha256(self.passowrd).hexdigest() 
        self.age= int(input("Enter user age:"))
        self.gender= input("Enter user gender:")
        
#user = User()
#user.add_user_details()
#print(vars(user))