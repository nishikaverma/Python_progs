##################################################################
#Program which will increment the given binary number by 1.
##################################################################

class TM:
    def __init__(self,lst):

        self.lst=lst
        self.head = -1
    
    def validate(self):

        if len(self.lst)>0:
            for x in self.lst:
                if x!='0' and x!='1':
                    return "Invalid input !"
            self.q0()

    def q0(self):

        if abs(self.head)<= len(self.lst):
            if self.lst[self.head]=='1':
                self.lst[self.head]='0'
                self.head -= 1
                self.q0()

            elif self.lst[self.head]=='0':
                self.lst[self.head]='1'
                self.head -= 1
                self.q1()

        elif abs(self.head)> len(self.lst):
            self.lst.insert(0,'1')
            self.q2()

    def q1(self):

        if abs(self.head)<= len(self.lst):
            if self.lst[self.head]=='0':
                self.head -= 1
                self.q1()
            
            elif self.lst[self.head]=='1':
                self.head -= 1
                self.q1()
        
        elif abs(self.head)> len(self.lst):
            self.q2()

    def q2(self):
        print("A Binary increment is :",''.join(lst))
        
string = input("Enter a binary number : ")
if not string:
    print("Empty string not allowded!")
lst = list(string)
obj = TM(lst)
error = obj.validate()
if error!= None:
    print(error)