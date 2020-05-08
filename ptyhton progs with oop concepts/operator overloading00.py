class distance:
    def __init__(self,feet ,inches):
        self.inches=inches
        self.feet=feet
    def __repr__(self):
        str=f"feet is ={self.feet} and inches is= {self.inches}"
        
        return str

    def __add__(self,other):
        inches=self.inches+other.inches
        feet=self.feet+other.feet

        while inches>=12:
            feet=feet+1
            inches=inches-12
        d=distance(feet,inches)
    
        return d

d1=distance(9,34)
d2=distance(10,59)
d3=d1+d2
print(d3)
