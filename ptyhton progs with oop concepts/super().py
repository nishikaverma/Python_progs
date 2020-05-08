import math
class Circle:
    def __init__(self,radious):
        self.radious=radious
    def area(self):
        ar=math.pi*math.pow(self.radious,2)
        return ar
class Cylender(Circle):
    def __init__(self,radious,height):
        super().__init__(radious)
        self.height=height
    def area(self):
        return 2*(super().area()+math.pi*self.radious*self.height)
        
    def volume(self):
        vol=super().area()*self.height
        return f"volume of cylender is is{vol}"
c1=Cylender(34,23)
print("area of circle is",Circle.area(c1))
print("area of cylender is",c1.area())
print("volume of cylender is",c1.volume())
