###########################################################################################
# A DFA(with output i.e Miley Machine) that finds 2’s complement of a given binary number.:-
###########################################################################################

''' list_name.reverse() -- it reverses the original list and returns a reverse object 
    reversed(list_name)-- it returns an itrable object which is the reversed list, but the original list remains the same'''

class DFA:
    def __init__(self,s):
        self.s = s
        self.count = 0
        self.result = []
        
    def validate(self):
        if len(self.s)>0:
            for x in self.s:
                if x!='0' and x!='1':
                    return "Invalid string! Only 0's and 1's alloweded."
            self.q0()
    
    def q0(self):
        if self.count<len(self.s):
            if self.s[self.count]== '0':
                self.result.append('0')
                self.count+=1
                self.q0() 
                
            elif self.s[self.count]== '1':
                self.result.append('1')
                self.count+=1
                self.q1()

                
        elif self.count>=len(self.s):
            self.result.reverse()
            print(f"The 2's compliment of {s} is : {self.result}")

    def q1(self):
        if self.count<len(self.s):
            if self.s[self.count]=='0':
                self.result.append('1')
                self.count+=1
                self.q1()

            elif self.s[self.count]=='1':
                self.result.append('0')
                self.count+=1
                self.q1()
                
        elif self.count>=len(self.s):
            self.result.reverse()
            print(f"The 2's compliment of {s} is :{self.result}")


s = list(input("Enter a binary number :"))
if not s:
    print("Empty string not allowed!")

reversed_s =  [x for x in reversed(s)]

obj = DFA(reversed_s)
a = obj.validate()
if a!=None:
    print(a)


