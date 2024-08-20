import datetime
from mongodbhelper import MongoDBHelper
from flask import *
import hashlib
from bson.objectid import ObjectId 

web_app = Flask( "Doctor's App") #web app is a reference variable where we are storing flask object
db_helper = MongoDBHelper()

@web_app.route("/") #Decorator #as soon as web app works, the page first visible deconates /
# if / use this run index function 
def index():

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
    #render_template is a function in flask which runs the webpage
    return render_template("index.html")
    #return message
   
@web_app.route("/home")
def home():
    if len(session["email"]) != 0:
        return render_template("home.html", name=session["name"], email = session["email"])
    else:
        return redirect("/")


@web_app.route("/logout") 
def logout ():
    #session.clear()
    session["email"]= ""
    session["name"]= ""
    return redirect("/")


@web_app.route("/register") 
def register ():
    return render_template("register.html")


@web_app.route("/success")
def success():
    return render_template("success.html", name= session["name"], email= session["email"])

@web_app.route("/error")
def error():
    return render_template("error.html", name= session["name"], email= session["email"])


 
@web_app.route("/add-user", methods = ["POST"])
def add_user_in_db():
    
    user_data = {
        "name": request.form["name"].capitalize(),#add-user is the link b/w register.html form and py code
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
        }
    result = db_helper.insert(user_data) #saving user data in mongoDB db= mongodbhelper, insert is function of mongodb 
    
    #message = "Welcome to home page, user id is: {}".format(result.inserted_id)
        
    
     #session is a dict provided by flask, by storing in session we can use it anywhere in project
    session['user_id']= str(result.inserted_id) 
    session['name'] = user_data["name"]
    session['email'] = user_data["email"]
    
    return render_template("home.html", name= session['name'], email=session['email'])


@web_app.route("/update-patient/<id>")
def update_patient(id):
    print("patient to be udpated",id)
    
    session ["id"] = id

    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["patients"]
    
    result = db_helper.fetch(query)
    
    patient_doc =  result[0]
    
    return render_template("update-patient.html", name= session['name'], email=session['email'], patient = patient_doc  )
    


@web_app.route("/fetch-user", methods = ["POST"])
def fetch_user_from_db():
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest()        
    }
    
    db_helper.collection = db_helper.db["users"]
    result = db_helper.fetch(query = user_data ) # by using db. we are using mongodb helper funcitions like insert, delete, fetch
    
    print("result", result )
    
    if len(result)>0:
        user_data =result[0]
        session['email'] = user_data["email"]
        session['name'] = user_data["name"]
        return render_template("home.html", name= session['name'], email=session['email'])
    
    else:
        return render_template("error.html",message ="User Not Found. Please Try Again.",  name= session["name"], email=session["email"])
        

@web_app.route("/add-patient", methods = ["POST"])
def add_patient_in_db():
    
    patient_data = {
        "name": request.form["name"],#add-user is the link b/w register.html form and py code
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "doctor_email": session["email"],
        "doctor_name": session["name"],
        "created_on": datetime.datetime.now()
        }
    
    db_helper.collection = db_helper.db["patients"] #changing collection
    
    result = db_helper.insert(patient_data)  
          
    
    return render_template("success.html", message = "Patient added successfully", name= session['name'], email=session['email'])
    

@web_app.route("/fetch-patients")
def fetch_patients_from_db():
    
    if len(session["email"]) == 0:
        return redirect ("/")
    
    user_data = {
        "doctor_email": session["email"]}
    
    db_helper.collection = db_helper.db["patients"]
    
    result = db_helper.fetch(query = user_data ) 
    
    if len(result)>0:
        print(result)
        return render_template("patients.html", patients=result, name= session['name'], email=session['email'])
    
    else:
        return render_template("error.html", message= "Paitents Not Found. Please Try Again.", name= session['name'], email=session['email'])

@web_app.route("/update-patient-in-db", methods = ["POST"])
def update_patient_in_db():
    patient_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "doctor_email": session["email"],
        "doctor_name": session["name"],
        "created_on": datetime.datetime.now()
        }
    
    db_helper.collection = db_helper.db["patients"] #changing collection
    query = {"_id": ObjectId(session["id"])}
    
    result = db_helper.update(patient_data, query)  
          
    
    return render_template("success.html", message = "Patient updated successfully", name= session['name'], email=session['email'], patient = patient_data)

@web_app.route("/delete-patient/<id>")
def delete_patient(id):
    db_helper.collection = db_helper.db["patients"]
    query = {"_id": ObjectId(id)}
    
    result = db_helper.delete(query)
    
    return render_template("success.html", message = "Patient deleted successfully", name= session['name'], email=session['email'])
    

@web_app.route("/add-consultation/<id>")
def add_consultation(id):
    
    session["patient_id"]= id
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["patients"]
    
    result = db_helper.fetch(query)
    
    patient_doc =  result[0]
    session["patient_name"] = patient_doc["name"]    

    
    return render_template("add_consultation.html",  name= session['name'], email=session['email'], patient_name = session["patient_name"])    


@web_app.route("/add-consultation-in-db", methods = ["POST"])
def add_consultation_in_db():
    
    patient_consultation_data = {
        "Complaints": request.form["Complaints"],
        "bp": request.form["bp"],
        "Temperature": request.form["Temperature"],
        "Sugar": request.form["Sugar"],
        "Remarks": request.form["Remarks"],
        "followup": request.form["followup"],
        "patient_name": session["patient_name"],
        "patient_id": session["patient_id"],    
        "doctor_email": session["email"],
        "doctor_name": session["name"],
        "created_on": datetime.datetime.now()
        }
    
    db_helper.collection = db_helper.db["consultations"] #changing collection
    
    result = db_helper.insert(patient_consultation_data)  
          
    
    return render_template("success.html", message = "Consultation added successfully", name= session['name'], email=session['email'])


@web_app.route("/fetch-consultations")
def fetch_consultation_from_db():
    
    if len(session["email"]) == 0:
        return redirect ("/")
    
    user_data = {
        "doctor_email": session["email"]}
    
    db_helper.collection = db_helper.db["consultations"]
    
    result = db_helper.fetch(query = user_data ) 
    
    if len(result)>0:
        print(result)
        return render_template("consultation.html", consultations=result, name= session['name'], email=session['email'])
    
    else:
        return render_template("error.html", message= "No Consultations.", name= session['name'], email=session['email'])

@web_app.route("/fetch-consultations-of-patient/<id>")
def fetch_consultation_of_patient(id):
    
    if len(session["email"]) == 0:
        return redirect ("/")
    
    user_data = {
        "doctor_email": session["email"],
        "patient_id": id
        }
    
    db_helper.collection = db_helper.db["consultations"]
    
    result = db_helper.fetch(query = user_data ) 
    
    if len(result)>0:
        print(result)
        return render_template("consultation.html", consultations=result, name= session['name'], email=session['email'])
    
    else:
        return render_template("error.html", message= "Consultation Not Found. Please Try Again.", name= session['name'], email=session['email'])    


@web_app.route("/search-patient")
def search_patient():
    
    return render_template("search.html",  name= session['name'], email=session['email'] )



@web_app.route("/search-patient-from-db", methods = ["POST"])
def search_patient_from_db():
    
    patient_data = {
        "doctor_email": session["email"],
        "email": request.form["email"]
        }
    
    db_helper.collection = db_helper.db["patients"]
    
    result = db_helper.fetch(query = patient_data ) 
    
    if len(result)>0:
        print(result)
        return render_template("patient-card.html", patient=result[0], name= session['name'], email=session['email'])
    
    else:
        return render_template("error.html", message= "No Patient Found!.", name= session['name'], email=session['email'])    


def main():
    
    web_app.secret_key = "doctors-app-key-v1" # making secret key for running session tracking
    
    # run function will run app infinitely, till user end 
    web_app.run()
    #web_app.run(port=200) syntax for giving specific port
    
if __name__ == "__main__":
    main()  