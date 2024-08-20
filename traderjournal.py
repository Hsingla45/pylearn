import hashlib
from flask import *
from datetime import datetime, timedelta
from TJ.check import MDBH
from bson.objectid import ObjectId 
from authlib.integrations.flask_client import OAuth


mdb = MDBH()
tweb_app = Flask("Trader Journal")


appconf = {
    "OAUTH2_CILENT_ID": "978137491809-7q5570kd6faoe3v9ujesp3k8lhdqkgpg.apps.googleusercontent.com",
    "OAUTH2_CILENT_SECRET": "",
    "OAUTH2_META_URL":"https://accounts.google.com/.well-known/openid-configuration",
    "FLASK_PORT": 5000
}

#creating oauth cilent
oauth= OAuth(tweb_app)
# registering oauth cilent
oauth.register("myApp",
               client_id=appconf.get("OAUTH2_CILENT_ID"),
               client_secret=appconf.get("OAUTH2_CILENT_SECRET"),
               server_metadata_url=appconf.get("OAUTH2_META_URL"),
               client_kwargs={ "scope": "openid profile email"}               
               ) 


# this route this redirecting me to page where we select google mail id for login
@tweb_app.route("/google-login")
def googlelogin():
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("googleCallback", _external= True))

@tweb_app.route("/signin-google")
def googleCallback():
    token = oauth.myApp.authorize_access_token() #token is storing all info in dict received from google account
    session["email"]=  token['userinfo']['email']
    session["fname"]= token['userinfo']['given_name']
    return redirect(url_for("home"))


@tweb_app.route("/")
def index():
    
    return render_template("try.html")



@tweb_app.route("/adding-trade")
def new_add_trade():
    
    return render_template("tryaddtrade.html", fname = session["fname"],  email = session['email'])



@tweb_app.route("/login")
def login():
    session.permanent = True
    return render_template("traderindex.html")




@tweb_app.route("/register")
def register():
    return render_template("traderregister.html")


@tweb_app.route("/home")
def home():
    if len(session["email"]) != 0:
        return render_template("tryhome.html", fname = session["fname"],  email = session['email'])
    else:
        return redirect("/")
    


@tweb_app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@tweb_app.route("/delete-trade/<id>")
def delete_trade(id):
    mdb.collection = mdb.db["trade_data"]
    query = {"_id": ObjectId(id)}
    
    result = mdb.delete(query)
    return render_template("trysuccess.html", message = "Trade Deleted Successfully.", fname = session["fname"],  email = session['email'])



@tweb_app.route("/search-trade")
def search_trade():
    
    return render_template("tradersearch.html", fname = session["fname"],  email = session['email'])

@tweb_app.route("/search-trade-from-db", methods = ["POST"])
def search_trade_from_db():
    
    trade_data = {
        "email": session['email'],
        "Symbol Name": request.form["Symbol Name"]  
    }
    
    mdb.collection= mdb.db["trade_data"]
    
    result = mdb.fetch(trade_data)
    
    print(result)
    
    if len(result)>0:
        
        return render_template("traderviewtrades.html", traderviewtrades= result, fname = session["fname"],  email = session['email'] )
    
    else:
        return render_template("tradererror.html", message = "No Trades Found", fname = session["fname"],  email = session['email'])
    
    


@tweb_app.route("/fetch-open-trades")
def fetch_open_trades_from_db():
    
    trade_data = {
        "email": session['email'],
        "Status": "Open" 
    }
    
    mdb.collection= mdb.db["trade_data"]
    
    result = mdb.fetch(trade_data)
    
    print(result)
    
    if len(result)>0:
        
        return render_template("tryviewopenposition.html", traderviewtrades= result, fname = session["fname"],  email = session['email'] )
    
    else:
        return render_template("tradererror.html", message = "No Trades", fname = session["fname"],  email = session['email'])



@tweb_app.route("/add-trade", methods =["POST"])
def add_trade():
    trade_data = {
        "Symbol Name": request.form['Symbol Name'].capitalize(),
        "Entry price": int(request.form['Entry Price']),
        "Exit Price": int(request.form['Exit Price']),
        "Quantity": int(request.form['Quantity']),
        "PNL": (int(request.form['Exit Price']) - int(request.form['Entry Price']))*int(request.form['Quantity']),
        "Status": request.form['Status'],
        "Remarks":request.form['Remarks'],
        "email": session['email'],
        "Created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    
    mdb.collection = mdb.db["trade_data"]
    
    result = mdb.insert(trade_data)
    
    return render_template("tradersuccess.html", message= "Trade added successfully" , fname = session["fname"], email = session['email'] )



@tweb_app.route("/fetch-trades")
def fetch_trades_from_db():
   
    trade_data = {
        "email": session['email'],  
    }

    mdb.collection= mdb.db["trade_data"]

    result = mdb.fetch(trade_data)

    print(result)

    if len(result)>0:
        
        return render_template("tryviewjournal.html", traderviewtrades= result, fname = session["fname"],  email = session['email'] )

    else:
        return render_template("tradererror.html", message = "No Trades", fname = session["fname"],  email = session['email'])





@tweb_app.route("/add-user", methods =["POST"])
def adding_user_in_db():
    
    user_data = {
        "fname": request.form['fname'].capitalize(),
        "lname": request.form['lname'],
        "DOBd": int(request.form['dd']),
        "DOBm": int(request.form['mm']),
        "DOBy": int(request.form['yyyy']),
        "email": request.form['email'],
        "password": request.form['password']
    }
    
    mdb.collection= mdb.db["user"]    
    result = mdb.insert(user_data)
    session['fname'] = user_data["fname"]
    session['email'] = user_data["email"]
    
    
    return render_template("try.html", fname = session["fname"], email = session['email'] )
    
    
@tweb_app.route("/fetch-user", methods =["POST"])
def fetch_user_from_db():
    
    user_data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    
    mdb.collection = mdb.db["user"]
    result = mdb.fetch(user_data)
    
    print(result)
    
    if len(result)>0:
        user_data =result[0]
        session['email'] = user_data["email"]
        session['fname'] = user_data["fname"]
        return render_template("tryhome.html", fname = session['fname'],  email = session['email'] )
    
    else:
        return render_template("tradererror.html", message = "User Not Found!", fname = session['fname'],  email = session['email'])
    
    
    



def main():
    
    tweb_app.secret_key= "traders-journal-v1"
    tweb_app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)
    
    tweb_app.run()
    
    
    
    
if __name__== "__main__":
    main()
    