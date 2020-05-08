import cx_Oracle
conn=None
try:
    conn=cx_Oracle.connect("SYSTEM/oracle123@localhost/orcl")
    print("connection established successfully!")
    print("the Oracle version is:" ,conn.version)
    print("the Oracle username is:" ,conn.username)
except (cx_Oracle.DatabaseError) as a:
    print("connection not established:", a)

finally:
    if conn is not None:
        conn.close()
        print("Connection to database is successfully closed!")
