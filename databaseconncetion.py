import mysql.connector as db

from creatingclassfx import Customer

#creating connection with database
connection = db.connect(user="root",
                        password = "py2024",
                        host = "127.0.0.1",
                        database = "Customer")

print('connected')
print(connection)

#doing it to make dynamic inserting data in database by importing class Customer from creatingclassfx.py
customer = Customer()
customer.add_customer_details()

# create sql statement
#sql = "insert into Customer values(null, 'john', '99999 55555', 'john@ex.com', 20, 'male')"
sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}')".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)



#obtain cursor - cursor need to perform CRUD operations with mysql
cursor = connection.cursor()

#for executing sql command
cursor.execute(sql)

#commit write(insert, update, delete) operation & read operaiton(execute), commit means to perform transaction in real
connection.commit()
    

print('sql statement executed')

