"""
    create table patient(
         pid int primary key auto_increment,
         name varchar(256),
         phone varchar(256),
         age int,
         gender varchar(256),
         admitted_on datetime);

"""

import datetime



class Patient:

    def __init__(self, pid = 0, name="NA", phone="NA", age =0, gender="NA", admitted_on=""):
        self.pid = pid
        self.name = name
        self.phone = phone
        self.age = age
        self.gender = gender
        self.admitted_on = datetime.datetime.now()

    def add_patient_details(self):
        self.name = input("Enter patient name: ")
        self.phone = input("Enter patient phone: ")
        self.age = int(input("Enter patient age: "))
        self.gender = input("Enter patient gender: ")
        
    def update_patient_details(self):
        name = input("Enter patient name: ")
        if len(name) != 0:
            self.name = name
        
        phone = input("Enter patient phone: ")
        if len(phone) != 0:
            self.phone = phone

        age = input("Enter patient age: ")
        if len(age) != 0:
            self.age = age

        gender = input("Enter patient gender: ")
        if len(gender) != 0:
            self.gender = gender    
            


    def show(self):
        print("~~~~~~~~~~~PATIENT DETAILS~~~~~~~~~~~~~~~")
        print("{} | {} | {} |{} |{}".format(self.name, self.phone, self.age, self.gender, self.admitted_on))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#patient1 = Patient(name="jim",phone="454544554",age=25,gender= "male")

#patient1.show()

