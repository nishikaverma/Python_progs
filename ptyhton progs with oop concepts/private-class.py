class Emp:
    raise_amount=0
    @classmethod
    def set_raise_amt(cls):
        cls.raise_amount=float(input("enter yhe increment percentage"))
    def __init__(self,name ,age,sal):
        
        self.__name=name
        self.__age=age
        self.__sal=sal

    def increse(self):
        self.sal=self.__sal+(self.__sal*Emp.raise_amount/100)
    def display(self):
        
        print(self.__name,self.__age,self.__sal)


e1=Emp("ashish",34,50000.0)
e2=Emp("ishita",34,80000.0)
Emp.set_raise_amt()
print("Before incrementing:")
print("____________________")
e1.display()
e1.increse()
print("after incrementing by %f :"%Emp.raise_amount)
print("______________________________")
e1.display()
print("Before incrementing:")
print("____________________")
e2.display()
print("after incrementing by %f :"%Emp.raise_amount)
print("______________________________")
e2.increse()
e2.display()

    
