from calendar import c
import os
#First Page - Log-In Page -> Create Acct Page
from random import randint, randrange
from datetime import date
today = date.today()

def AcctNo(n=7): #Generate Account Number
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='banksystem',
                                         user='root',
                                         password='Srihari@007')
    
    if connection.is_connected():
        cursor = connection.cursor(buffered=True)

        
        def deposit(id):
            amt = float(input("Enter the amount to be deposited: "))
            cursor.execute("SELECT MAX(TransactionID) FROM banksystem.transactions")
            '''if(cursor.fetchone()[0]==None):
                TransID = 1
            else:'''
            TransID = cursor.fetchone()[0] + 1
            #print(TransID)
            cursor.execute("SELECT Balance FROM banksystem.cust WHERE Id = %s", (id,))
            Bal = cursor.fetchone()[0]
            Bal = int(Bal) + amt
            #print(Bal)
            #connection.commit()
            #ins_transaction = ("INSERT INTO banksystem.transactions (CustId, TransactionID, TransactionType, Amount, Date, Balance) VALUES (%s, %s, %s, %s, %s, %s)", (id, TransID, "Deposit", amt, "2021-01-01", Bal))
            d1 = today.strftime("%Y-%m-%d")
            cursor.execute("INSERT INTO banksystem.transactions (CustId, TransactionID, TransactionType, Amount, Date, Balance) VALUES (%s, %s, %s, %s, %s, %s)", (id, TransID, "Deposit", amt, d1, Bal))
            connection.commit()
            print("Amount has been deposited successfully!!")
            print("Thank you for using our bank services..!!")

        def withdraw(id):
            cursor.execute("SELECT MAX(TransactionID) FROM banksystem.transactions")
            TransID = int(cursor.fetchone()[0]) + 1
            #print(TransID)
            cursor.execute("SELECT Balance FROM banksystem.cust WHERE Id = %s", (id,))
            Bal = cursor.fetchone()[0]
            print("\nCurrent Balance: ",Bal)
            amt = float(input("\nEnter the amount to be withdrawn: "))
            if amt<100:
                print("Withdrawl amount should be greater than or equal to 100")
                os._exit(0)
            else:
                if amt<Bal:
                    Bal = int(Bal) - amt
                else:
                    print("Insufficient funds")
                    os._exit(0)
            d1 = today.strftime("%Y-%m-%d")
            print("\nRemaining Balance: ",Bal)
            cursor.execute("INSERT INTO banksystem.transactions (CustId, TransactionID, TransactionType, Amount, Date, Balance) VALUES (%s, %s, %s, %s, %s, %s)", (id, TransID, "Withdraw", amt, d1, Bal))
            connection.commit()
            print("Amount has been withdrawn successfully!!")
            print("Thank you for using our bank services..!!")
        
        '''def transfer():
            pass'''

        def checkBalance(id):
            cursor.execute("SELECT Balance FROM banksystem.cust WHERE Id = %s", (id,))
            balance = cursor.fetchone()[0]
            print("Your balance is: ", balance)
            print("\nThank you for using our bank services..!!")

        def printTransactions(id):
            cursor.execute("SELECT * FROM banksystem.transactions WHERE CustId = %s", (id,))
            transactions = cursor.fetchall()
            print("\n")
            print("[CustomerId , TransactionID , Transaction Type , Amount , Date , Balance]\n")
            for i in range(len(transactions)):
                print("[",transactions[i][0],",",transactions[i][1],",",transactions[i][1],",",transactions[i][3],",",transactions[i][4],",",transactions[i][5],"]")
            print("\nThank you for using our bank services..!!")


        def login(): #To DO: Add password, 
            id = int(input("Enter your ID: "))
            pw = (input("Enter your password: "))
            cursor.execute("SELECT * FROM banksystem.password WHERE Id = %s and Password = %s", (id,pw,))
            record = cursor.fetchone()
            if record is None:
                print("Invalid ID or Password! Try Again!")
                i = int(input("1. Try Again\n2. Exit\n"))
                if i == 1:
                    login()
                else:
                    exit()
            cursor.execute("SELECT * FROM banksystem.cust WHERE Id = %s", (id,))
            record = cursor.fetchone()
            print("Login Successful!!")
            print("Welcome", record[1])
            print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Print Transactions\n5. Log-Out")
            c = int(input("Enter your choice: "))
            if c == 1:
                deposit(record[0])
            elif c == 2:
                withdraw(record[0])
            elif c == 3:
                checkBalance(record[0])
            elif c == 4:
                printTransactions(record[0])
            else:
                os._exit(0)
    
        def createAcct():
            print("Enter the following details to create an account")
            name = input("Enter your name: ")
            aadhar = input("Enter your Aadhar Number: ")
            #cursor.execute("SELECT AadharNo from banksystem.cust")
            '''record = cursor.fetchall()
            while i in record:
                print("Account Linked to this Aadhar already exists! Login (1) or Try Again (2) : ")
                i = int(input())
                if i == 1:
                    login()
                if i == 2:
                    aadhar = input("Enter your Aadhar Number: ")
                else:
                    print("Invalid index! Try Again")
                    print("Redirecting you to the Create Account Page")
                    createAcct()'''
            age = int(input("Enter your age: "))
            balance = 0.0
            cursor.execute("SELECT MAX(Id) FROM cust")
            id = cursor.fetchone()[0] + 1
            acctNo = int(AcctNo())
            cursor.execute("SELECT AcctNo from banksystem.cust")
            record = cursor.fetchall()
            while acctNo in record:
                acctNo = AcctNo()
            cursor.execute("INSERT INTO banksystem.cust (Id, Name, AadharNo, Age, Balance, AcctNo) VALUES (%s, %s, %s, %s, %s, %s)", (id, name, aadhar, age, balance, acctNo))
            pw = input("Enter your password: ")
            cursor.execute("INSERT INTO banksystem.password (Id, Password) VALUES (%s, %s)", (id, pw, ))
            connection.commit()
            print("Account created successfully!")
            print("Your account number is: ", acctNo)
            print("Your customer_id is: ", id)
            print("Your password is: ", pw)
            print("Please remember your customer_id and password for future purpose")
            print("Press any key to continue")
            input()
            os.system('cls')
            print("Redirecting you to Login Page.....")
            login()
            
        print("Connected To Bank Database!!!")
        print("Welcome to CloBank..!!!")
        print("1. Log-In\n2. Create Account\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Log-In")
            #Log-In Page -> Main Page
            #Check if the user exists in the database
            #If yes, then go to Main Page
            #If no, then go to Create Acct Page
            #Check if the password is correct
            #If yes, then go to Main Page
            #If no, then go to Log-In Page
            login()
        if choice == 2:
            print("Create Account")
            #Create Acct Page -> Main Page
            #Check if the user exists in the database
            #If yes, then go to Log-In Page
            #If no, then go to Main Page
            #Create a new user in the database
            #Create a new password for the user in the database
            #Go to Main Page
            createAcct()
        if choice == 3:
            print("Thank you for using CloBank")
            #Exit
            os._exit(0)
        else:
            os._exit(0)
except Error as e:
    print("Error while connecting to Bank Database(MySQL)", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Thank you")