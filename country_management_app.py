# COUNTRY MANAGEMENT APPLICATION:
def  view():
    print("country codes are :")
    for (co,cn) in dict1.items():
        print(co)
    toview=str(input("enter the county code you want to view :"))
    for x in dict1.keys():
        if x==toview:
            print("the country is ",dict1[toview])
            break
        else:
           print("there is no country for country code %s"%toview)
            
        
    

def add():
    co=str(input("enter country code"))
    cn=str(input("enter country name "))
    dict1.setdefault(co,cn)
    print("country %s added to the list"%cn)

def delete():
    co=str(input("ener the country code you want to remove from the list"))
    dict1.pop(co)
    print("country deleted from list!")

dict1={"IN":'India',"US":'America',"AU":'Australia','CA':'Canada'}
print('SELECT AN OPTION\n view: for viewing a country\n add: for adding a country \n del:for deleting a country from list\n exit- for exitting the program ')
choice=str(input("your choice? "))
if choice=="view":
    view()
    

if choice=="add":
    add()
if choice=="del":
    delete()
if choice=="exit":
    print("thankyou for using the app :-)")
           
