class Circle:
    def __init__(self,radious):
        self.rad=radious
    def cal_area(self):
        ar=self.rad*self.rad*3.14
        print("the area is: ",ar)
    def cal_circ(self):
        circ=3.14*2*self.rad
        print("circumference is",circ)
r=int(input("enter the radious of circle"))
C=Circle(r)
C.cal_area()
C.cal_circ()
