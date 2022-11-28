import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost', database='banksystem', user='root', password='Srihari@007')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        mySql_Create_Table_Query = """CREATE TABLE Cust ( Id int(11) NOT NULL,Name varchar(250) NOT NULL,AadharNo varchar(12) NOT NULL, Age int NOT NULL,Balance float NOT NULL, AcctNo int NOT NULL, PRIMARY KEY (Id))"""
        cursor.execute(mySql_Create_Table_Query)
        mySql_Create_Table_Query2 = """CREATE TABLE Transactions (CustId int(11) NOT NULL, TransactionID int NOT NULL, TransactionType varchar(250) NOT NULL, Amount float NOT NULL, Date date NOT NULL, Balance float NOT NULL, PRIMARY KEY (TransactionID))"""
        cursor.execute(mySql_Create_Table_Query2)
        mySql_Create_Table_Query3 = """CREATE TABLE Password ( Id int(11) NOT NULL,Password varchar(250) NOT NULL, PRIMARY KEY (Id))"""
        cursor.execute(mySql_Create_Table_Query3)
        print("Table created successfully ")
        ins = "INSERT INTO Cust (Id, Name, AadharNo, Age, Balance, AcctNo) VALUES (0001, 'ADMIN', 123456780987, 20, 109909.0, 9999999)"
        cursor.execute(ins)
        ins2 = "INSERT INTO Password (Id, Password) VALUES (0001, 'admin')"
        cursor.execute(ins2)
        connection.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")