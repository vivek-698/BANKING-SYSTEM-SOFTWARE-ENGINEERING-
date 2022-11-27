#This is a Unit Test Case for Login Page
#Test Parameters: Username, Password
#Test Data: Username, Password
#Test Cases - 
#1. Login with valid username and password
#2. Login with invalid username and password
#3. Login with valid username and invalid password
#4. Login with invalid username and invalid password

#import unittest
import mysql.connector
from mysql.connector import Error
import os

try:
    connection = mysql.connector.connect(host='localhost', database='banksystem', user='root', password='root')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        print("No Error in Connecting to MySQL Server")
        cursor = connection.cursor(buffered=True)
        

        def login():
            print("Log-In")
            cid = int(input("Enter your ID: "))
            pw = (input("Enter your password: "))
            #login_counter += 1
            cursor.execute("SELECT * FROM banksystem.password WHERE Id = %s and Password = %s", (cid,pw,))
            record = cursor.fetchone()
            if record is None:
                cursor.execute("SELECT * FROM banksystem.password WHERE Id = %s", (cid,))
                record = cursor.fetchone()
                if record is None:
                    print("Invalid Username")
                else:
                    print("Invalid Password")
                    return 0
            else:
                print("Login Successful")
            cursor.execute("SELECT * FROM banksystem.cust WHERE Id = %s", (cid,))
            record = cursor.fetchone()
            if record is None:
                return 0
            print("Welcome", record[1])
            return 1

        def tc1():
            print("Test Case 1: Login with valid username and password")
            login()
            if login() == 1:
                print("Login Successful")
                print("Test Case 1 Passed")
            print("Test Case 1 Failed")

        def tc2():
            print("Test Case 2: Login with invalid username and password")
            login()
            if login() == 0:
                print("Login Unsuccessful")
                print("Test Case 2 Passed")
            print("Test Case 2 Failed")

        def tc3():
            print("Test Case 3: Login with valid username and invalid password")
            login()
            if login() == 0:
                print("Login Unsuccessful")
                print("Test Case 3 Passed")
            print("Test Case 3 Failed")

        def tc4():
            print("Test Case 4: Login with invalid username and invalid password")
            login()
            if login() == 0:
                print("Login Unsuccessful")
                print("Test Case 4 Passed")
            print("Test Case 4 Failed")
        
        tc1()
        tc2()
        tc3()
        tc4()
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")