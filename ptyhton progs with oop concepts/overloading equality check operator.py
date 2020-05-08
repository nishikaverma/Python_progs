class distance:
    def __init__(self,feet ,inches):
        self.inches=inches
        self.feet=feet
    def __repr__(self):
        str=f"feet is ={self.feet} and inches is= {self.inches}"
        
        return str

    def __eq__(self,other):
        a=self.feet*12+self.inches
        b=other.feet*12+other.inches
        if a==b :
             return True

        else:
            return False

        
    
        

d1=distance(10,1)
d2=distance(10,0)

print(d1==d2)
