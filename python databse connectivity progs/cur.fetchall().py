import cx_Oracle
try:
    conn=cx_Oracle.connect("system/oracle123@localhost/orcl")   
    print("connection established")
    cur=conn.cursor()
    print("cursor created!")
    print("***********************")
    cur.execute("Select Book_name,Book_price from Books")
    my_list=cur.fetchall()
    num=int(input(f"enter record no.you want to view:"))
    if num>len (my_list) or num<0:
        raise Exception("invalid record no.")
    else:
        print(my_list[num])
    print("************************")
       
except(cx_Oracle.DatabaseError)as e:
    print("Error in connectin: ",e)

except Exception as e:
    print(e)
    
finally:
    if conn is not None:
        cur.close()
        print("curser closed!")
        conn.close()
        print("connection closed!")
