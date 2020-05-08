import random
num=random.randint(1,100)
guess=num+1
while guess!=num:
    guess=int(input("guess the no.!!!"))
    if(guess==num):
        print('you guesseed it correctly, congratulations!')
    elif(0<guess<num):
        print('wrong guessing. no. too small ')
    else:
        print('wrong guessing. no. too large ')
    if(guess<0):
        print('really sorry you :-( are quitting the game')
        break
    
