################################################################################################
# A PDA to accept WCW^R where W is any string and W^R is reverse of that string and C is a Special symbol
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
                if ord(x)<65 or (ord(x)>90 and ord(x)<97) or ord(x)>122:
                    
                    return "Invalid string! Only alphabets alloweded."
            self.q0()

    def q0(self):
        if self.count<len(self.string):
            if self.string[self.count] != 'c':
                super().push(self.string[self.count])
                self.count+=1
                self.q0()

            else:
                self.count+=1
                self.q1()
        else:
            print("Input Not Accepted ! ")


    def q1(self):
        if self.count<len(self.string):
            if self.string[self.count] == self.stack[self.top]:
                super().pop()
                self.count+=1
                self.q1()
            
            else:
                print("Input Not Accepted ! ")


        elif self.count==len(self.string) and self.stack[self.top]== 'z':
            self.q2()   

    def q2(self):
        print("Input Accepted ;-) ")

stack =['z',]
string = input("Enter a String (alphabetic, without spaces) of type WcW(R) : ")
if not string:
    print("Empty string not allowed!")
obj = PDA(stack,string)
a=obj.validate()
if a!=None: # i.e if validate func. returns an error msg (string)
    print(a)
