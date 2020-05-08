#################################################
# counting number of 0's and 1's in the input string :-
#################################################

class DFA:
    def __init__(self,s):
        self.s= s
        self.count=0
        self.count0=[]
        self.count1=[]

        
    def validate(self):
        if len(self.s)>0:
            for x in self.s:
                if x!='0' and x!='1':
                    return "Invalid string! Only 0's and 1's alloweded."
            m=self.q0()
            
            
    def q0(self):
        if self.count<len(self.s):
            if self.s[self.count]=='0':
                self.count0.append(self.s[self.count])
                self.count+=1
                self.q0()
                
            elif self.s[self.count]=='1':
                self.count1.append(self.s[self.count])
                self.count+=1
                self.q1()

                
        elif self.count>=len(self.s):
            self.result()
            
    def q1(self):
        if self.count<len(self.s):
            if self.s[self.count]=='0':
                self.count0.append(self.s[self.count])
                self.count+=1
                self.q0()
            elif self.s[self.count]=='1':
                self.count1.append(self.s[self.count])
                self.count+=1
                self.q1()
                
        elif self.count>=len(self.s):
            
            self.result()

    def result(self):
        
        print("In te string you entered, number of 0's :" ,len(self.count0), "and number of 1's:", len(self.count1))

    
s=input("Enter a string of 0's and 1's :")
if not s:
    print("Empty string not allowed!")
obj = DFA(s)
output = obj.validate()
if output!=None:
    print(output)

