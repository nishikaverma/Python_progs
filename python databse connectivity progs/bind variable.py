import cx_Oracle
try:
    conn=cx_Oracle.connect("system/oracle123@localhost/orcl")   
    print("connection established")
    cur=conn.cursor()
    print("cursor created!")
    print("***********************")
    cur.execute("Select Book_name,Book_price from Books")
    
    
    for x in cur:
        print(x)
    print("***********************")
    name=input("enter book name : ")
    price=int(input("enter book price"))

    cur.execute("Insert into Books (Book_name,Book_price)values(:1,:2)",(name,price))
    n=cur.rowcount
    print(n,'rows inserted')
    conn.commit()
    
    cur.execute("Select Book_name,Book_price from Books")
    
    
    for x in cur:
        print(x)
    print("************************")
       
except(cx_Oracle.DatabaseError)as e:
    print("Error in connectin: ",e)
finally:
    if conn is not None:
        cur.close()
        print("curser closed!")
        conn.close()
        print("connection closed!")

