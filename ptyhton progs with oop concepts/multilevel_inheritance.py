class person:
    def __init__(self,age ,name):
        self.age=age
        self.namee=name
        print("person's constructor called")
    def __repr__(self):
        return f"age is {self.age} and name is {self.name}"

class emp(person):
    def __init__(self,age,name,id,sal):
        super().__init__(age,name)
        self.id=id
        self.sal=sal
        print("employee's constructor called")
    def __repr__(self):
        return f"super().__repr__() id is{self.id} and salary is{self.sal}"


class manager(emp):
    def __int__(self,age, name,id,sal,bonous):
        super().__init__(age,name,id,sal)
        self.bonous=bonous
        print("manager's constructor called")
    def income(self):
        return f"increment is {self.sal +self.bonous}"
    def __repr__():
        return f"super().__repr__() bonous is {self.bonous}"


m=manager(23,'Nitin',101,39000.00,2000)
print(m)
print(m.income())
