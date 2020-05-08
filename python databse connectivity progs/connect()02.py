import cx_Oracle
obj_conn=None
cur_obj=None
try:
    

    
    obj_conn=cx_Oracle.connect("SYSTEM/oracle123@localhost/orcl")
    print("connected to database...")
    print("version:",obj_conn.version) 
    print("username:",obj_conn.username)
    cur_obj=obj_conn.cursor()
    print("cursor created")
    cur_obj.execute("select * from student" )
    print("table selected!")
    for name,roll in cur_obj:
        print(name,roll)
   

except (cx_Oracle.DatabaseError) as e:
    print(e)

finally:
    if cur_obj is not None:
        cur_obj.close()
        print("connection closed for cursor")
    if obj_conn is not None:
        obj_conn.close()
        print("connection closed from database")
