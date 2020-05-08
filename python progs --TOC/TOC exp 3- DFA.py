###############
# A mod3 DFA :-
###############

class mod3:
    def __init__(self,s):
        self.s= s
        self.count=0
        
    def validate(self):
        if len(self.s)>0:
            for x in self.s:
                if x!='0' and x!='1':
                    return "Invalid string! Only 0's and 1's alloweded."
            self.q0()
    
    def q0(self):
        if self.count<len(self.s):
            if self.s[self.count]=='0':
                self.count+=1
                self.q0()
                
            elif self.s[self.count]=='1':
                self.count+=1
                self.q1()

                
        elif self.count>=len(self.s):
            print("Remainder = 00")

    def q1(self):
        if self.count<len(self.s):
            if self.s[self.count]=='0':
                self.count+=1
                self.q2()
            elif self.s[self.count]=='1':
                self.count+=1
                self.q0()
                
        elif self.count>=len(self.s):
            print( "Remainder = 01")


    def q2(self):
        if self.count<len(self.s):
            if self.s[self.count]=='0':
                self.count+=1
                self.q1()
            elif self.s[self.count]=='1':
                self.count+=1
                self.q2()
                
        elif self.count>=len(self.s):
            print( "Remainder = 2 i.e. 10")

s=input("Enter a string of 0's and 1's in mod3 DFA machine :")
if not s:
    print("Empty string not allowed!")
DFA=mod3(s)
a=DFA.validate()
if a!=None:
    print(a)

