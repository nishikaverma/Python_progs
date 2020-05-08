class Emp:
    raise_amount=0
    @classmethod
    def set_raise_amt(cls):
        cls.raise_amount=float(input("enter yhe increment percentage"))
    def __init__(self,name ,age,sal):
        
        self.name=name
        self.age=age
        self.sal=sal
    def __repr__(self):
        return f"name is{self.name} age is {self.age} sal is{self.sal}"
e1=Emp("ashish",34,50000.0)
e2=Emp("ishita",34,80000.0)
print(type(Emp.set_raise_amt()))
print(type(e1.__repr__))
print(dir(e1.__repr__))
print(Emp.__repr__)
print(e1)
print(object.__repr__)
