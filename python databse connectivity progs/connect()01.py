import cx_Oracle
obj_conn=None
try:
     obj_conn=cx_Oracle.connect("SYSTEM/oracle123@localhost/orcl")
     print("connected to database...")
     print("version:",obj_conn.version) 
     print("username:",obj_conn.username)
     cur_obj=obj_conn.cursor()
     print("cursor created")
     cur_obj.execute("CREATE TABLE student(name varchar(20),rollno number(4,0))" )
     print("table created!")

except (cx_Oracle.DatabaseError) as e:
     
     print(e)
finally:
    if obj_conn is not None:
        cur_obj.close()
        obj_conn.close()
        print("connection closed!")
