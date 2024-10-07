import sqlite3
from datetime import datetime

conn = sqlite3.connect("interview.db")
cursor = conn.cursor()


# table Create
cursor.execute('''
    CREATE TABLE IF NOT EXISTS details
    (
        "candidate" TEXT,
        "company_name" TEXT,
        "company_address" TEXT,
        "contact_number" INTEGER,
        "interview_type" TEXT,
        "date" INTEGER,
        "time" INTEGER
    )
''')

conn.commit()

def insert_data(candidate, company_name, company_address, contact_number, interview_type, date, time):
    cursor.execute("INSERT INTO details('candidate', 'company_name', 'company_address', 'contact_number', 'interview_type', 'date', time) VALUES (?, ?, ?, ?, ?, ?, ?)", (candidate, company_name, company_address, contact_number, interview_type, date, time))
    conn.commit()


def all_input():
    while True:
        while True:
            candidate = input("enter the candidate name : ")
            if candidate.isalpha():
                break
            else:
                print("invalid input! please enter a valid company (alphabetic characters only).")


        while True:
            company_name = input("enter the company name : ")
            if candidate.isalpha():
                break
            else:
              print("invalid input! please enter a valid company (alphabetic characters only).")               
                
        while True:
            company_address = input("enter the company address : ")
            if candidate.isalpha():
                break
            else:
                print("invalid input! please enter a valid company (alphabetic characters only).")

                
        while True:        
            contact_number = input("enter the contact number for company : ")
            if len(contact_number) == 10:
                break
            else:
                print("please enter a valid 10 digit contect number")

                
        while True:            
            interview_choice = input("enter 'o' for online, 'p' for phone call, 'n' not use : ")
            if interview_choice == 'o':
                interview_type = 'online'
                break
            elif interview_choice == 'p':
                interview_type = 'phone call'
                break
            elif interview_choice == 'n':
                interview_type = 'not use'
                break
            else:
                print("invalid input please enter 'o', 'p', or 'n' ")

                
        date = datetime.now().date().isoformat() 
        time = datetime.now().strftime("%H:%M:%S")
        insert_for_data(candidate, company_name, company_address, contact_number, interview_type, date, time)
        
        exite = input("try again y/n : ")        
        if exite == "n":
            print("successful save")
            break
        
        

all_input()        
        
