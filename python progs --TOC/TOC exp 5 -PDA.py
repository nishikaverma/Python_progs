################################################################################################
# Program for creating a machine (PDA) which accepts string having equal no. of 1’s and 0’s.
#Language = { 1^n 0^n | n>=1} U {0^n 1^n | n>=1}
################################################################################################

class STACK:
    def __init__(self,stack,string):
        self.stack = stack
        self.string = string
        self.top = 0

    def push(self,item):
        self.stack.append(item)
        self.top += 1
        #return self.stack

    def pop(self):
        if self.stack == []:
            return "Stack Underflow! i.e. Stack is empty."
            
        self.stack.pop()
        self.top -= 1
        #return self.stack


class PDA(STACK):
    def __init__(self,stack,string):
        super().__init__(stack,string)
        self.count = 0
    
    def validate(self):
        if len(self.string)>0:
            for x in self.string:
                if x!='1' and x!='0':
                    
                    return "Invalid string! Only 0's and 1's alloweded."
            self.q0()

    def q0(self):
        if self.count<len(self.string):
            if self.string[self.count] == '1' and self.stack[self.top]== 'z':
                super().push(self.string[self.count])
                self.count+=1
                self.q0()

            elif self.string[self.count] == '1' and self.stack[self.top]== '1':
                super().push(self.string[self.count])
                self.count+=1
                self.q0()
            
            elif self.string[self.count] == '0' and self.stack[self.top]== '1':
                super().pop()
                self.count +=1
                self.q1()
            
            elif self.string[self.count] == '0' and self.stack[self.top]== 'z':
                super().push(self.string[self.count])
                self.count+=1
                self.q0()

            elif self.string[self.count] == '0' and self.stack[self.top]== '0':
                super().push(self.string[self.count])
                self.count+=1
                self.q0()

            elif self.string[self.count] == '1' and self.stack[self.top]== '0':
                super().pop()
                self.count +=1
                self.q1()

        else:
            print("Input Not Accepted ! --> the number of 1's in string is/are not equals to the number of 0's.")


    def q1(self):
        if self.count<len(self.string):
            if self.string[self.count] == '0' and self.stack[self.top]== '1':
                super().pop()
                self.count+=1
                self.q1()
            
            elif self.string[self.count] == '1' and self.stack[self.top]== '0':
                super().pop()
                self.count+=1
                self.q1()
            else:
                print("Input Not Accepted ! -> Only a String of 1's followed by 0's or vice versa is accepted")


        elif self.count==len(self.string) and self.stack[self.top]== 'z':
            self.q2()   

        else:
            print("Input Not Accepted ! -> the number of 1's in string is/are not equals to the number of 0's.")
    
    def q2(self):
        print("Input Accepted !  the number of 1's in string = number of 0's.")

stack =['z',]
string = input("Enter a String of 1's followed by 0's : ")
if not string:
    print("Empty string not allowed!")
obj = PDA(stack,string)
a=obj.validate()
if a!=None: # i.e if validate func. returns an error msg (string)
    print(a)


