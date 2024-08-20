import mysql.connector as db

class Database:

    def __init__(self):
        self.connection = db.connect(user="root",
                                     password= "py2024",
                                     host= "127.0.0.1",
                                     database="Patient")
        
        print("[Database] connection created")

        self.cursor = self.connection.cursor()

        print("[Database] cursor created successfully")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

        print("SQL Statement Succesfully Executed...")


    def db_read(self):
        pass
