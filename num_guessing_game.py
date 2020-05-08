a=10

i=int(input("guess the no.!!!!!!!\n..."))
if(i==a):
         print('congratulation! you have guessed it correctly.')
while i!=a :
    print('[FOR QUITTING THE GAME TYPE 0OR A NEGTAIVE NO.]')
    if(i!=a):
         if(i>a):

             print('sorry! wrong guessing. no. is too large.')
         elif(0<i<a):
             print('sorry! wrong guessing . no. is too small.')
         if(i<=0):
             inp=input('are you sue you want to quit,dont want to guess anymore?. (y/n)')
             if(inp=="n"):
                 
                 break
             else:
                 continue
                      
    i=int(input("guess the no.!!!!!!!\n..."))
    
            
    
