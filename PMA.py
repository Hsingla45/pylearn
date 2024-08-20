from patient_db_connection import Database
from object_patient import Patient
from tabulate import tabulate

def main():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO PATIENT MANAGEMENT APP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    db = Database

    while True:

        print("1.Enter Patient Details: ")
        print("2.Update Patient Details: ")
        print("3.Delete Patient Details: ")
        print("4.View by Patient PID: ")
        print("5.View by Patient Phone: ")
        print("6.View all")
        print("0.Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
           patient = Patient()
           patient.add_patient_details()

           sql = "insert into Patient values(null, '{name}, '{phone}', {age}, '{gender}','{admitted_on}')".format_map(vars(patient))

           db.write(sql)

           print("[PMA]", Patient.name, "Saved in Database")
        
        elif choice == 2:
            pass

        elif choice == 3:
            pass


        elif choice == 4:
            pass


        elif choice == 5:
            pass


        elif choice == 6:
            pass

        elif choice == 0:
            break

        else:
            print("Invalid choice")

          

        
          

            
    

    
    


if __name__ == "__main__":
    main()









