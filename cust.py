from calendar import c
import os
#First Page - Log-In Page -> Create Acct Page
from random import randint, randrange


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
                                         password='Venomgt@123')
    
    if connection.is_connected():
        cursor = connection.cursor()
        
      

        def deposit(id):
            amt = float(input("Enter the amount to be deposited: "))
            cursor.execute("SELECT MAX(TransactionID) FROM bansystem.transactions")
            TransID = cursor.fetchone()[0] + 1
            # ins_cust = ("UPDATE banksystem.cust SET Balance = Balance + %s WHERE Id = %s", (amt, id))
            # cursor.execute(ins_cust)
            # ins_transaction = ("INSERT INTO banksystem.transactions (CustId, TransactionID, TransactionType, Amount, Date, Balance) VALUES (%s, %s, %s, %s, %s, %s)", (id, TransID, "Deposit", amt, "2021-01-01", 0))
            # cursor.execute(ins_transaction)
            connection.commit()

        def withdraw():
            pass
        
        def transfer():
            pass

        def checkBalance():
            pass

        def printTransactions():
            pass

        def login(): #To DO: Add password, 
            print("Log-In")
            id = int(input("Enter your ID: "))
            pw = (input("Enter your password: "))
            cursor.execute("SELECT * FROM banksystem.password WHERE Id = %s and Password = %s", (id,pw,))
            record = cursor.fetchone()
            if record is None:
                print("Invalid ID or Password! Try Again!")
                i = int(input("1. Try Again\n2. Exit"))
                if i == 1:
                    login()
                else:
                    exit()
            cursor.execute("SELECT * FROM banksystem.cust WHERE Id = '%s'", (id,))
            record = cursor.fetchone()
            print("Login Successful!!")
            print("Welcome", record[1])
            print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transfer\n5. Print Transactions\n6. Log-Out")
            c = int(input("Enter your choice: "))
            if c == 1:
                deposit(record[0])
            elif c == 2:
                withdraw(record[0])
            elif c == 3:
                checkBalance(record[0])
            elif c == 4:
                transfer(record[0])
            elif c == 5:
                printTransactions(record[0])
            else:
                os._exit(0)

        def createAcct():
            print("Enter the following details to create an account")
            name = input("Enter your name: ")
            aadhar = input("Enter your Aadhar Number: ")
            cursor.execute("SELECT AadharNo from banksystem.cust WHERE AadharNo= %s",(aadhar,))
            record = cursor.fetchone()
            if record!=None:
                print("Account Linked to this Aadhar already exists! Login (1) or Try Again (2) : ")
                i = int(input())
                if i == 1:
                    login()
                if i == 2:
                    aadhar = input("Enter your Aadhar Number: ")
                else:
                    print("Invalid index! Try Again")
                    print("Redirecting you to the Create Account Page")
                    createAcct()
            age = int(input("Enter your age: "))
            balance = 0.0
            cursor.execute("SELECT MAX(Id) FROM cust")
            id = cursor.fetchone()[0] + 1
            acctNo = AcctNo()
            cursor.execute("SELECT AcctNo from banksystem.cust")
            record = cursor.fetchall()
            while acctNo in record:
                acctNo = AcctNo()
            pw=input("Enter Password: ")
            #implement criteria Checking    
            if age>18:    
                cursor.execute("INSERT INTO banksystem.cust (Id, Name, AadharNo, Age, Balance, AcctNo) VALUES (%s, %s, %s, %s, %s, %s)", (id, name, aadhar, age, balance, acctNo))
                cursor.execute("INSERT INTO banksystem.password (Id, Password) VALUES (%s, %s)", (id, pw))
                connection.commit()
                print("Account created successfully!")
                    
                print("Your account number is: ", id)
                print("Your Password is: ",pw)
                
                
                print("Please remember your account number and password")
                print("Press any key to continue")
                input()
                os.system('cls')
                print("Redirecting you to Login Page.....")
                login()

            else :
                print("Age Criteria For creating account is not satisfied")
                print("For Further Information please visit clobanking.com")
                os._exit(0)
                    
            
         


        #main   
        print("Welcome to the Bank of Python")
        print("1. Log-In\n2. Create Account\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # print("Log-In")
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
            print("Thank you for using the Bank of Python")
            #Exit
            os._exit(0)
        else:
            print("Invalid Choice! Try Again!")
            os._exit(0)
except Error as e:
    print("Error while connecting to Bank Server(MySQL)", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Thank you")