"""
    create table consultation(
         cid int primary key auto_increment,
         pid int,
         remarks varchar(256),
         medicines varchar(256),
         next_followup datetime,
         created_on datetime,
         FOREIGN KEY (pid) REFERENCES Patient(pid));

"""



import datetime


class Consultation:
     def __init__(self, cid = 0, pid =0,remarks="NA", medicines="NA", next_followup="NA", created_on=""):
        self.cid = cid
        self.pid = pid
        self.medicines = medicines
        self.next_followup = next_followup
        self.created_on = datetime.datetime.now()

     def add_consultation_details(self):
        self.pid = input("Enter patient ID: ")
        self.remarks = input("Enter consultation remarks: ")
        self.medicines = input("Enter medicines: ")
        self.next_followup = input("Enter next_followup(yyyy-mm-dd hh:mm:ss")

     def show(self):
         print('~~~~~~~consultation~~~~~~~')

         consultation= """
         {cid} | {pid}
         {remarks} | {medicines}
         {next_followup} | {created_on}""".format_map(vars(self))


         print(consultation)

         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
           


    

