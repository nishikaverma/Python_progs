import cx_Oracle
try:
    conn=cx_Oracle.connect("system/oracle123@localhost/orcl")   
    print("connection established")
    print("***********************")
    print("username is: ",conn.username)
    print("oracle version is: ",conn.version)
    cur=conn.cursor()
    print("cursor created!")
    print("***********************")
    
except(cx_Oracle.DatabaseError)as e:
    print("Error in connectin: ",e)
finally:
    if conn is not None:
        cur.close()
        print("curser closed!")
        conn.close()
        print("connection closed!")
