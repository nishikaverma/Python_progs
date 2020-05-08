class Book:
    def __init__(self, name,price):
        self.name=name
        self.price=price

    def __repr__(self):
        
        return f"name is {self.name} price is {self.price} "
    def __add__(self,other):
        Tprice=self.price+other.price
        return f"the total price of two books is {Tprice}"

b1=Book("naveen",256)
b2=Book("tanan bomb",450)

print(b1)
print(b2)
print(b1+b2)

        
