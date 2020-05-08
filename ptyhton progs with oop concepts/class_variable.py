class Emp:
    raiseit=7.5
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def increse(self):
        self.sal=self.sal+(self.sal*Emp.raiseit/100)
    def display(self):
        
        print(self.name,self.age,self.sal)
e1=Emp("ashish",34,50000.0)
e2=Emp("ishita",34,80000.0)
print("Before incrementing:")
print("____________________")
e1.display()
e1.increse()
print("after incrementing by 7.5 % :")
print("______________________________")
e1.display()
print("Before incrementing:")
print("____________________")
e2.display()
print("after incrementing by 7.5 % :")
print("______________________________")
e2.increse()
e2.display()
