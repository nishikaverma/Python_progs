######################################################################################
# Design a Turing machine that accepts the following language a^n b^n c^n where n>0.
######################################################################################
class TM:
    def __init__(self,lst):
        self.lst=lst
        self.head = 0
    
    def validate(self):
        if len(self.lst)>0:
            for x in self.lst:
                if  ord(x)!=97 and ord(x)!=98 and ord(x)!=99:
                    
                    return "Invalid string! Only a string of abc is allowded."
            self.q0()

    def q0(self):
        if self.head<len(self.lst):
            if self.lst[self.head] == 'a':
                self.lst[self.head]='x'
                self.head+=1
                self.q1()
            
            elif self.lst[self.head] == 'y':
                self.head+=1
                self.q4()
            else:
                print("Invalid String! not accepted.")
        
    def q1(self):
        if self.head<len(self.lst):
            if self.lst[self.head] == 'a':
                self.head+=1
                self.q1()
            
            elif self.lst[self.head] == 'b':
                self.lst[self.head]='y'
                self.head+=1
                self.q2()
            
            elif self.lst[self.head] == 'y':
                self.head+=1
                self.q1()
            else:
                print("Invalid String! not accepted.")
        
        
    def q2(self):
        if self.head<len(self.lst):
        
            if self.lst[self.head] == 'b':
                self.head+=1
                self.q2()
            
            elif self.lst[self.head] == 'z':
                self.head+=1
                self.q2()
            
            elif self.lst[self.head] == 'c':
                self.lst[self.head]='z'
                self.head-=1
                self.q3()
            else:
                print("Invalid String! not accepted.")
        

    def q3(self):
        if self.head<len(self.lst):
            if self.lst[self.head] == 'z':
                self.head-=1
                self.q3()
            elif self.lst[self.head] == 'b':
                self.head-=1
                self.q3()
            elif self.lst[self.head] == 'y':
                self.head-=1
                self.q3()
            elif self.lst[self.head] == 'a':
                self.head-=1
                self.q3()

            elif self.lst[self.head] == 'x':
                self.head+=1
                self.q0()
    
    def q4(self):
        if self.head<len(self.lst):
            if self.lst[self.head] == 'y':
                self.head+=1
                self.q4()
            elif self.lst[self.head] == 'z':
                self.head+=1
                self.q4()
            else:
                print("Invalid String! not accepted.")
        
        if self.head>=len(self.lst):
            self.q5()

    def q5(self):
        print("Input Accepted ;-)")
        
string = input("Enter a String of 'abc' : ")
if not string:
    print("Empty string not allowed!")
lst= list(string)
obj = TM(lst)
a=obj.validate()
if a!=None: # i.e if validate func. returns an error msg (string)
    print(a)
