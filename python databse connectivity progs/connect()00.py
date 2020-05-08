import cx_Oracle
obj=None
try:
    obj=cx_Oracle.connect("nishika/123@localhost/orcl")
    print("connection established successfully!")
    print("username is",obj.username)
    print("versoion is",obj.version)

except (cx_Oracle.DatabaseError) as a:
    print("connwction not established",a)
    
finally:
    if obj is not None:
        obj.close()
        print("disconnected to DBMS successfully")
