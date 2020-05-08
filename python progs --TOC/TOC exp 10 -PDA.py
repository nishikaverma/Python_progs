#########################################################################################################################################
#Program to create PDA machine that accept the well-formed parenthesis, brackets, curley braces. {{[()][]}} 
#########################################################################################################################################

class STACK:
    def __init__(self,stack):
        self.stack = stack
        self.top = 0

    def push(self,item):
        self.stack.append(item)
        self.top += 1
        

    def pop(self):
        if self.stack == []:
            return "Stack Underflow! i.e. Stack is empty."
            
        self.stack.pop()
        self.top -= 1
        


class PDA(STACK):
    def __init__(self,stack,string):
        self.s = string
        super().__init__(stack)
        
        self.count = 0

    def validate(self):
        lst=['(',')','{','}','[',']']
        if len(self.s)>0:
            for x in self.s:
                if x not in lst:
                    return "Invalid string input!"
            self.q0()
    
    def q0(self):
        if self.count<len(self.s):
            
            if self.s[self.count]== '(':
                super().push(self.s[self.count])
                self.count+=1
                self.q0()
                                
            elif self.s[self.count]== '[':
                super().push(self.s[self.count])
                self.count+=1
                self.q0()

            elif self.s[self.count]== '{':
                super().push(self.s[self.count])
                self.count+=1
                self.q0()

            elif self.s[self.count]== ')' and self.stack[self.top]=='(' :
                super().pop()
                self.count+=1
                self.q1()

            elif self.s[self.count]== ']' and self.stack[self.top]=='[':
                super().pop()
                self.count+=1
                self.q1()
            
            elif self.s[self.count]== '}' and self.stack[self.top]=='{':
                super().pop()
                self.count+=1
                self.q1()

            else:
                print("Input not accceptable !")

    
    def q1(self):
        if self.count<len(self.s):
            if self.s[self.count]== ')' and self.stack[self.top]=='(' :
                super().pop()
                self.count+=1
                self.q1()

            elif self.s[self.count]== ']' and self.stack[self.top]=='[':
                super().pop()
                self.count+=1
                self.q1()
            
            elif self.s[self.count]== '}' and self.stack[self.top]=='{':
                super().pop()
                self.count+=1
                self.q1()
            
            elif self.s[self.count]== '(':
                super().push(self.s[self.count])
                self.count+=1
                self.q0()
                                
            elif self.s[self.count]== '[':
                super().push(self.s[self.count])
                self.count+=1
                self.q0()

            elif self.s[self.count]== '{':
                super().push(self.s[self.count])
                self.count+=1
                self.q0()

            else:
                print("Input not accceptable !")

        elif self.count>=len(self.s):
            self.q2()
        
    def q2(self):
        print("Input Accepted ! ;-)")


stack=['z',]
string = input("Enter a string of parenthesis : ")
if not string:
    print("Empty string not allowded!")
obj = PDA(stack,string)
error = obj.validate()
if error!= None:
    print(error)