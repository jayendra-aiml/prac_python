#Personal Loan Approval System:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
employ = input("Enter yes if you are employed, if not enter no: ")
if age>=21 and employ.lower()=='yes':
    income = float(input("Enter your income: "))
    loans = int(input("Enter the number of loans you already have, if not enter 0: "))
    credit_score = int(input("Enter your credit score: "))
    if loans>=2 or credit_score<650 or income<25000:
            print("Sorry we cannot provide you loan")
    else:
        if credit_score>=650 and credit_score<700 and income>=25000:
                print("Intrest rate= 10%")
                print("Congratulations!..Loan Apprroved")
        elif credit_score>=700 and credit_score<750 and income>=25000:
                print("Intrest rate= 7%")
                print("Congratulations!..Loan Apprroved")
        else:
                print("Intrest rate= 5%")
                print("Congratulations!..Loan Apprroved")
else:
    print("Sorry you are not eligible for loan")