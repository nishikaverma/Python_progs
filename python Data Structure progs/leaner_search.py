class Leaner_Search:
    def __init__(self):
        self.lst=[]
    
    def get_input(self):
        self.n=int(input("size of list? : "))
        print("enter ",self.n," numbers :")
        [self.lst.append(int(input())) for i in range(self.n) ] 
        num=int(input("Enter number to be searched : "))
        self.search(num)

    def search(self, num):
        pos=[]
        for x in range(self.n):
            if self.lst[x]==num:
                pos.append(x)
        if pos==[]:
            print("Element not found")
        else:
            print("Element found at ", pos ,"position")
        

obj=Leaner_Search()
obj.get_input()
