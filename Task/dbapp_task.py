import dbapplib as db
import sqlite3

print("------1: Database Create/Connect-------")
print("------2: Table Create-------")
print("------3: Insert Records-------")
ch=input("Select your choice:")



if ch=='1':
    db.dbconnection()
elif ch=='2':
    db.createTABLE()
elif ch=='3':
    db.insertUser()