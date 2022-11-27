#This is a Unit Test Case for Withdrawal
#Test Parameters: Withdrawal Amount
#Test Data: Withdrawal Amount
#Test Cases - 
#1. Withdrawl with valid amount and sufficient funds
#2. Withdrawl with insufficient funds
#3. Withdrawl with less than minimum amount

from calendar import c
import os
from datetime import date
today = date.today()
#import unittest
import mysql.connector
from mysql.connector import Error
import os

try:
    connection = mysql.connector.connect(host='localhost', database='banksystem', user='root', password='Sammu6704()')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        print("No Error in Connecting to MySQL Server")
        cursor = connection.cursor(buffered=True)
        

        def withdraw():
            
            cursor.execute("SELECT MAX(TransactionID) FROM banksystem.transactions")
            TransID = int(cursor.fetchone()[0]) + 1
            #print(TransID)
            cursor.execute("SELECT Balance FROM banksystem.cust WHERE Id = %s", (100,))
            Bal = cursor.fetchone()[0]
            print("\nCurrent Balance: ",Bal)
            amt = float(input("\nEnter the amount to be withdrawn: "))
            if amt<100:
                print("Withdrawl amount should be greater than or equal to 100")
                return 0
            else:
                if amt<Bal:
                    Bal = int(Bal) - amt
                else:
                    print("Insufficient funds")
                    return 0
            d1 = today.strftime("%Y-%m-%d")
            print("\nRemaining Balance: ",Bal)
            cursor.execute("INSERT INTO banksystem.transactions (CustId, TransactionID, TransactionType, Amount, Date, Balance) VALUES (%s, %s, %s, %s, %s, %s)", (100, TransID, "Withdraw", amt, d1, Bal))
            connection.commit()
            return 1

        def tc1():
            print("Test Case 1: Withdrawl with valid amount and sufficient funds")
            if withdraw() == 1:
                print("Withdrawl Successful")
                print("Test Case 1 Passed\n\n")
            else:
                print("Test Case 1 Failed\n\n")

        def tc2():
            print("Test Case 2: Withdrawl with insufficient funds")
            if withdraw() == 0:
                print("Withdrawal Unsuccessful")
                print("Test Case 2 Passed\n\n")
            else:
                print("Test Case 2 Failed\n\n")

        def tc3():
            print("Test Case 3:  Withdrawl with less than minimum amount")
            if withdraw() == 0:
                 print("Withdrawal Unsuccessful")
                 print("Test Case 3 Passed\n\n")
            else:
                print("Test Case 3 Failed\n\n")
        
        tc1()
        tc2()
        tc3()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")