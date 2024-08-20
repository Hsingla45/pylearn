from database_OOPS import Database
from object_patient import Patient
from consultation import Consultation
from tabulate import tabulate


def main():

    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO DOCTOR'S APP")
    print("~~~~~~~~~~~~~~~~~~~~~~~")

    db = Database()

    while True:

        print("1.Add new Patient : ")
        print("2.Update Patient Details: ")
        print("3.Delete Patient Details: ")
        print("4.View by Patient Phone: ")
        print("5.View by Patient Pid: ")
        print("6.View all")
        print("7.Add consultation for patient:")
        print("8.View all consultation:")
        print("9. View consultation for patient:")
        print("10.View followups")
        print("0. To Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
           patient = Patient()
           patient.add_patient_details()

           sql = "insert into Patient values(null, '{name}', '{phone}', {age}, '{gender}','{admitted_on}')".format_map(vars(patient))

           db.write(sql)

           print("patient added")
        
        elif choice == 2:
            pid = int(input("Enter pid where you want to update: "))
            sql = "select * from patient where pid ={}".format(pid)
            rows = db.read(sql)
            print(rows)

            patient = Patient(pid= rows[0][0], name = rows[0][1], phone= rows[0][2], age= rows[0][3], gender= rows[0][4])
            patient.show()
            patient.update_patient_details()

            sql = "update Patient set name = '{name}', phone= '{phone}', age= {age}, gender ='{gender}', admitted_on = '{admitted_on}'where pid = {pid}".format_map(vars(patient))

            db.write(sql)
            print("Patient details updated..")
            patient.show()



        elif choice == 3:
            pid =int(input("Enter PID which you want to delete:"))
            sql = "delete from patient where pid ={}".format(pid)
            ask= input("Are you sure you want to delete? (yes/no)")
            if ask == "yes":
                db.write(sql)
            else:
                print("Delete operation terminated.")


        elif choice == 4:
            phone = input("Enter Patient phone: ")
            sql = "select * from patient where phone= '{}'".format(phone)
            rows= db.read(sql)
            print(rows)

            columns = ["pid", "name", "phone", "age", "gender", "admitted_on"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))


        elif choice == 5:
            pid = int(input("Enter Patient ID:"))
            sql = "select * from patient where pid = {}".format(pid)
            rows= db.read(sql)
            print(rows)

            columns = ["pid", "name","phone", "age", "gender","admitted_on"]
            print(tabulate(rows, headers = columns, tablefmt="grid"))


        elif choice == 6:
            sql = "select * from patient"
            rows= db.read(sql)
            print(rows)

            columns = ["pid", "name","phone", "age", "gender","admitted_on"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 7:
            consultation = Consultation()
            consultation.add_consultation_details()
            sql = "insert into Consultation values (null, {pid}, '{remarks}', '{medicines}', '{next_followup}', '{created_on}')".format_map(vars(consultation))
            db.write(sql)
            
            print("Consultation added successfully")
        
        elif choice == 8:
            sql = "select * from consultation"
            rows= db.read(sql)

            columns = ["cid","pid", "remarks","medicines","next_followup","created_on"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))   

        elif choice == 9:
            pid = int(input("Enter Patient ID: "))
            sql = "select * from consultation where pid = {}".format(pid)
            rows = db.read(sql) 
            print(rows)

            columns = ["cid","pid", "remarks","medicines","next_followup","created_on"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 10:
            start_date= input("Enter start date time(yyyy-mm-dd hh:mm:ss)")
            end_date= input("Enter end date time(yyyy-mm-dd hh:mm:ss)")

            sql = "select * from consultation where next_followup >= '{}' and next_followup <= '{}'".format(start_date, end_date)
            rows= db.read(sql)

            columns = ["cid","pid", "remarks","medicines","next_followup","created_on"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break

        else:
            print("Invalid choice")    
    


if __name__ == "__main__":
    main()









