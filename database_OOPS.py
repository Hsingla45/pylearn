import mysql.connector as db

class Database:

    def __init__(self):
        self.connection = db.connect(user="root",
                        password = "py2024",
                        host = "127.0.0.1",
                        database = "Customer")
 
        print("[Database] Connection Created")

        self.cursor = self.connection.cursor()  
        print("[Database] Cursor Created")
     #using self with connection and cursor so that to make it a attribute of class Database


    #insert/update/delete in DB
    def write(self, sql):
        print("[Database] SQL Statement- ", sql)
        self.cursor.execute(sql)
        self.connection.commit()# commit ensure there is no error in operation, to write opeartion fully 
        print("[Database] SQL Statement successfully executed....")

    #fetch data from DB
    def read(self, sql):
        self.cursor.execute(sql) 
        result = self.cursor.fetchall()
        return result