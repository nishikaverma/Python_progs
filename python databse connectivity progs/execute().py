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
    cur_obj.execute("CREATE TABLE student2(name varchar(20),rollno number(4,0))" )
    print("table created!")
    i=0
    while i<5:
        
        n=str(input("enter the name of student"))
        roll=int(input("enter roll no. of student"))
        cur_obj.execute("INSERT INTO student2(name,rollno) values(n,roll)")
        print("values inserted!") 
    cur_obj.execute("SELET * FROM student2")
    
    print("selected!")

except (cx_Oracle.DatabaseError) as e:
     
    print(e)
