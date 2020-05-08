class Contact:
    def __init__(self,**kwargs):
        '''self.__dict__.update(kwargs)'''
        for x,y in kwargs.items():
            setattr(self,x,y)
            

    def display(self):
        print("contct details for object:")
        print("**************************")
        '''print(self.__dict__)'''
        for x in self.__dict__.keys():
            print(x,":",getattr(self,x))
    
c1=Contact(email="kschin@gmail.com",mob="9902873666")
c1.display()
c2=Contact(email='nishiakverma123@gmail.com',mob="878728627")
c2.display()
