class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        p=Point(x,y)
        return p
    def __repr__(self):
        return f"addition of p1 and p2 is x={self.x} and y={self.y}"

p1=Point(10,20)
p2=Point(39,50)
p3=p1+p2  #convrted to: p3=p1.__add__(p2) => p3=Point.__add(p1,p2)
print(p3)
