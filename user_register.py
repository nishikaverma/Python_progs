def askname():
    while True:
        name=input("enter your full name").strip()
        
        if name.find(" ")!=-1:
            return name
            break
        
        
        
            

def askpass():
    while True:
        passw=input("enter  password [should contain atleat 1 digit , atleast 1 uppercase letter. it should be of 8 charactors")
        if len(passw)>=8:
            if passw.isalnum==True:
                return passw
                break
            

def show():
    print("thank you", name,"for registering!")


askname()
askpass()
show()
