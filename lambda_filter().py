vowel=['a','e','i','o','u']
char=input("enter your name  ")
seq=list(filter(lambda char: char in vowel,char))
if len(seq)==0:
    print("no vowels in your name!")
else:
    print("the vowels in your entered name are: ",seq)
