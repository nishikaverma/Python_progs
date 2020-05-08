account={101:50000,102:45000,103:55000}
print("Account:",account)

accid=int(input("enter accouont id"))
accbal=int(input("enter balance"))

if accid in account.keys():
    
    account[accid]=accbal
    print("account updated")
else:
    print("new account created")
    account[accid]=accbal
print("after updation, Account:", account)    
