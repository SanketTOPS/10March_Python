import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newdatabase')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

# Table Create
"""create_tbl="create table studinfo(id integer primary key auto_increment,name text,sub text)"
try:
    cr.execute(create_tbl)
    print("Table Created!")
except Exception as e:
    print(e)"""


# Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('mitesh','java'),('nirav','php'),('ashok','html'),('prasiddh','ruby'),('hitesh','iOS')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set sub='android' where id=6"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    #data=cr.fetchall()
    #data=cr.fetchmany(2)
    data=cr.fetchone()
    print(data)
except Exception as e:
    print(e)
    