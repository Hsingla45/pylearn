import datetime
from mongodbhelper import MongoDBHelper
from flask import *
import hashlib

web_app = Flask( "Doctor's App")
db_helper = MongoDBHelper()


    

@web_app.route("/") #Decorator 
# if / use this run index function 
def index():
    # can return plain text or HTML
    #message= "Welcome to Patient Management App. Its {}".format(datetime.datetime.now())
    message = """
    <html>
    <head>
        <title>Doctor's App</title>
    
    </head>
    <body>
        <center>
                <h3>Welcome to Doctor's App</h3>
        </center>
        
    </body>
    
    </html>    
    """
    #return message


    return render_template("index.html")


@web_app.route("/register") 
def register ():
    return render_template("register.html")

@web_app.route("/home")
def home():
    return render_template("home.html", name= session["name"], email= session["email"])

@web_app.route("/success")
def success():
    return render_template("success.html", name= session["name"], email= session["email"])

@web_app.route("/error")
def error():
    return render_template("error.html", name= session["name"], email= session["email"])


@web_app.route("/add-patient", methods =["post"])
def add_patient_in_db():
    # creating a dictionary for adding data from register html file
    patient_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "doctor_email": session['email'],
        "doctor_name": session['name'],
        "created_on": datetime.datetime.now()     
    }
    
    db_helper.collection = db_helper.db["patients"]
    result = db_helper.insert(patient_data)
   
    return render_template("success.html", message = "Patient added succesfully", name=session['name'], email=session['email'])

@web_app.route("/fetch-user", methods=["POST"])
def feth_user_from_db():

    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    db_helper.collection = db_helper.db["users"]
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=user_data)

    print("result:", result)
    
    if len(result)>0:
        user_data = result[0] # Get the dictionary from List 
        session['email'] = user_data["email"]
        session['name'] = user_data["name"]
        return render_template("home.html", name=session['name'], email=session['email'])
    else:
        return render_template("error.html", message="User Not Found. Please Try Again", name=session['name'], email=session['email'])



def main():
    # run infinitely, till user end 
    web_app.run()
    #web_app.run(port=200) syntax for giving specific port
    
if __name__ == "__main__":
    main()  