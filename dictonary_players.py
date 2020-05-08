players={}
i=1
while i<=5:
    
    name=input("enter name  ")
    runs=int(input("enter the runs they made  "))
    players[name]=runs
    i+=1

print("list of players:rums is:" ,players)
hs=0
maxm=""
for playr,run in players.items():
    if run>hs:
        
        hs=run
        maxm=playr


print("highest score is:",hs," scored by", maxm) 





