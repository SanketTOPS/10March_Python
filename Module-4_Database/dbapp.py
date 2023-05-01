import sqlite3

try:
    dbcon=sqlite3.connect('testdb.db')
    print("Database connected!")
except Exception as e:
    print(e)


# Table Create
"""create_tbl="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(create_tbl)
    print("Table Created!")
except Exception as e:
    print(e)"""


# Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('mitesh','java'),('nirav','php'),('ashok','html'),('prasiddh','ruby'),('hitesh','iOS')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""


# Update Data
"""update_data="update studinfo set sub='android' where id=6"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

cr=dbcon.cursor()

# Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)
    