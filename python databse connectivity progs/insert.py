import cx_Oracle
try:
    conn=cx_Oracle.connect("system/oracle123@localhost/orcl")   
    print("connection established")
    cur=conn.cursor()
    print("cursor created!")
    print("***********************")
    cur.execute("select Book_name,Book_price  from Books")
    '''n=cur.rowcount()
    print("no. of rows inserted ",n)
    conn.commit()'''
    
    print("************************")
    
except(cx_Oracle.DatabaseError)as e:
    print("Error in connectin: ",e)

    
finally:
    if conn is not None:
        cur.close()
        print("curser closed!")
        conn.close()
        print("connection closed!")

