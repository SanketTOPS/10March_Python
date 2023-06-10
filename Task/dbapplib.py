import sqlite3

def dbconnection():
    global dbcon
    dbname=input("Enter your database name:")
    try:
        dbcon=sqlite3.connect(dbname+'.db')
        print("Database created/connected")
    except Exception as e:
        print(e)
    return dbcon


# Table Create
def createTABLE():
    global tblname
    dbcon=dbconnection()
    tblname=input("Enter your table name:")
    create_tbl=f"create table {tblname}(id integer primary key autoincrement, name text, sub text, city text)"
    try:
        dbcon.execute(create_tbl)
        print("Table Created successfully!")
    except Exception as e:
        print(e)
    return tblname

# Insert Operation
def insertUser():
    tbl=createTABLE()
    n=int(input("Enter number of records you want to insert:"))
    for i in range(n):
        name=input("Enter Name:")
        sub=input("Enter Subject:")
        city=input("Enter City:")
        insert_data=f"insert into {tblname}(name,sub,city)values('{name}','{sub}','{city}')"
        try:
            dbcon.execute(insert_data)
            dbcon.commit()
            print("Record Inserted!")
        except Exception as e:
            print(e)



