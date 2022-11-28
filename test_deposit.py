#Testing Deposit Function - Unit Test
#Testing Various Stages as Different Test Cases

import mysql.connector
from mysql.connector import Error
import os
from datetime import date
today = date.today()

try:
    connection = mysql.connector.connect(host='localhost', database='banksystem', user='root', password='root')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        print("No Error in Connecting to MySQL Server")
        cursor = connection.cursor(buffered=True)

        def deposit(id):
            amt = float(input("Enter the amount to be deposited: "))
            cursor.execute("SELECT MAX(TransactionID) FROM banksystem.transactions")
            TransID = cursor.fetchone()[0] + 1
            cursor.execute("SELECT Balance FROM banksystem.cust WHERE Id = %s", (id,))
            Bal = cursor.fetchone()[0]
            Bal = int(Bal) + amt
            d1 = today.strftime("%Y-%m-%d")
            cursor.execute("INSERT INTO banksystem.transactions (CustId, TransactionID, TransactionType, Amount, Date, Balance) VALUES (%s, %s, %s, %s, %s, %s)", (id, TransID, "Deposit", amt, d1, Bal))
            connection.commit()

        def tc1():
            print("Test Case 1: Check For Working Of Trigger")
            cursor.execute("SELECT Balance FROM banksystem.cust WHERE Id = %s", (1,))
            Bal1 = cursor.fetchone()[0]
            deposit(1)
            cursor.execute("SELECT Balance FROM banksystem.cust WHERE Id = %s", (1,))
            Bal2 = cursor.fetchone()[0]
            if Bal2>Bal1:
                print("Trigger Working")
                print("Test Case 1 Passed")
            else:   
                print("Trigger Not Working")
                print("Test Case 1 Failed")
        
        def tc2():
            print("Test Case 2: Check For Correct Adding to Transaction Table")
            cursor.execute("SELECT MAX(TransactionID) FROM banksystem.transactions")
            TransID1 = cursor.fetchone()[0]
            deposit(1)
            cursor.execute("SELECT MAX(TransactionID) FROM banksystem.transactions")
            TransID2 = cursor.fetchone()[0]
            if TransID2==(TransID1+1):
                print("Transaction Added")
                print("Test Case 2 Passed")
            else:
                print("Transaction Not Added")
                print("Test Case 2 Failed")


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")