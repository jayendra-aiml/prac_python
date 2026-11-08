name = input("Enter your name: ")
age = int(input("Enter your age: "))
couch = int(input("Enter 1 for normal couch and 2 for AC couch: "))
if age>=60:
    if couch==1:
        fare=(500*25)/100
        print(f'''                  Name={name}
                  Catergory: Senior Citizon                  
                  Couch: Normal
                  Discount: 25%
                  Fare: {fare}''')
    else:
        fare=(750*25)/100
        print(f'''                  Name={name}
                  Catergory: Senior Citizon
                  Couch: AC
                  Discount: 25%
                  Fare: {fare}''')
if age>=25 and age<60:
    if couch==1:
        fare=(500*5)/100
        print(f'''                  Name={name}
                  Catergory: General
                  Couch: Normal
                  Discount: 5%
                  Fare: {fare}''')
    else:
        fare=(750*5)/100
        print(f'''                  Name={name}
                  Catergory: General
                  Couch: AC
                  Discount: 5%
                  Fare: {fare}''')
if age>5 and age<25:
    if couch==1:
        fare=(500*30)/100
        print(f'''                  Name={name}
                  Catergory: Student
                  Couch: Normal
                  Discount: 30%
                  Fare: {fare}''')
    else:
        fare=(750*30)/100
        print(f'''                  Name={name}
                  Catergory: Student
                  Couch: AC
                  Discount: 30%
                  Fare: {fare}''')
if age>0 and age<=5:
    if couch==1:
        print(f'''                  Name:{name}
                  Catergory: Infant
                  Couch: Normal
                  Fare: No Fare, Its free for you''')
    else:
        print(f'''                  Name:{name}
                  Catergory: Infant
                  Couch: AC
                  Fare: No Fare, Its free for you''')
else:
    print("Invalid age enter again")
