import datetime

"""
creating table in database
     
     create table Customer(
         cid int primary key auto_increment,
         name varchar(256),
         phone varchar(256),
         email varchar(256),
         age int,
         gender varchar(256),
         created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP);


"""



#creating customer object with name phn etc as attributes
class Customer:
    def __init__(self, cid=0, name= "", phone= "", email= "", age = 0, gender= ""):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.created_on = datetime.datetime.now()


    def add_customer_details(self):
        self.name = input('enter customer name= ')
        self.phone = input('enter customer phone= ')
        self.email = input('enter customer email= ')
        self.age = int(input('enter customer age= '))
        self.gender = input('enter customer gender= ')

    def update_customer_details(self):
        name = input("Enter Customer Name: ")
        if len(name) != 0:
            self.name = name

        phone = input("Enter Customer Phone: ")
        if len(phone) != 0:
            self.phone = phone

        email = input("Enter Customer Email: ")
        if len(email) != 0:
            self.email = email
        
        age = input("Enter Customer Age: ")
        if len(age) != 0:
            self.age = int(age)

        gender = input("Enter Customer Gender: ")
        if len(gender) != 0:
            self.gender = gender


    def show(self):
        print("~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~")
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        print("{} | {} | {}".format(self.age, self.gender, self.created_on))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


"""
# Create Object : Python
customer1 = Customer(name="John", phone="+91 99999 11111", email="john@example.com",
                     age=20, gender="male")

print(vars(customer1))

customer1.show()
"""
