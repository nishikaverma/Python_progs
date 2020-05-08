class employee:
    def __init__(self,age,name,salary):
        self.his_age=age
        self.his_name=name
        self.his_sal=salary
        print("init called")

        
E=employee(45,"sagar",39000.0)
print("age is",E.his_age,"name is",E.his_name,"salary is",E.his_sal)
F=employee(29,"amit",20000.0)
print("age is",F.his_age,"name is",F.his_name,"salary is",F.his_sal)
print("age name ans salary are local variables whereas his_age, his_nmae and his_sal are instance/object variables")

