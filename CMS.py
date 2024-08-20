from creatingclassfx import Customer
from database_OOPS import Database
from tabulate import tabulate


def main():
    print("-------------------")
    print("WELCOME to CMS APP")
    print("-------------------")

    db = Database()

    while True:
        print("1. Add New Customer")
        print("2. Update Existing Customer")
        print("3. Delete Existing Customer")
        print("4. View Customer By Phone")
        print("5. View Customer By CID")
        print("6. View All Customer")
        print("0. To Quit App")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer = Customer()
            customer.add_customer_details()
            sql = "insert into Customer values(null , '{name}', '{phone}', '{email}', '{age}', '{gender}', '{created_on}')".format_map(vars(customer))


            db.write(sql)
            print("[CMS App]", customer.name, "Saved in Database")




        elif choice == 2:
            cid = int(input("Enter the cid where you want to update:"))
            sql = "select * from customer where cid = {}".format(cid)
            rows = db.read(sql)
            print(rows)

            customer = Customer(cid= rows[0][0], name= rows[0][1], phone= rows[0][2], email= rows[0][3], age= rows[0][4], gender= rows
            [0][5])
            print("Customer to update: ")
            customer.show()
            customer.update_customer_details()

            sql = "update Customer set name= '{name}', phone= '{phone}', email= '{email}', age= {age}, gender= '{gender}', created_on='{created_on}'where cid = {cid}".format_map(vars(customer))

            db.write(sql)
            customer.show()
    

           

        elif choice == 3:
            cid = int(input("Enter Customer ID To Be Deleted: "))
            sql = "delete from customer where cid = {}".format(cid)

            ask = input("Are you sure to want to delete: (yes/no)")
            if ask == "yes":
                db.write(sql)
                print("[CMS App]", cid, "Deleted From Database")
            else:
                print("delete operation skipped")


        elif choice == 4:
            phone = input("Enter the phone number:")
            sql = "select * from customer where phone = '{}'".format(phone)
            rows = db.read(sql)

            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 5:
            cid = input("Enter the cid:")
            sql = "select * from customer where cid = {}".format(cid)
            rows = db.read(sql)
            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))


        elif choice == 6:
            sql = "select * from Customer"
            rows= db.read(sql)
            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            #for row in rows:
            #    print(customer)

        elif choice == 0:   
            break


        else:
            print("[CMS App] Invalid Choice", choice)



if __name__ == "__main__":
    main()








   