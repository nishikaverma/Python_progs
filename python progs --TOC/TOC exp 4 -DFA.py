###################################################
# A DFA accepting decimal numbers divisible by 2:-#
###################################################

class DFA:
    def __init__(self,s):
        self.s= s
        
    def validate(self):
        if len(self.s)>0:
            for x in self.s:
                if x not in range(0,10):
                    return "Invalid string! Only decimal numbers alloweded."
            self.q0()
    
    def q0(self):

        if int(self.s[len(self.s)-1]) % 2 == 0:
            self.q1()

        else:
            self.q2()
              
    
    def q1(self):
        print('Input accepted ,String divisible by 2 !')

    def q2(self):
        print('Input not accepted, String not divisible by 2 !')

s=input("Enter a string of decimal numbers :")
if not s: 
    print("Empty string not allowed!")
obj = DFA(s)
a = obj.validate()
if a!=None:
    print(a)


