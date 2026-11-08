#Exam result and scholarship system
phy = float(input("Enter your marks in physics out of 100: "))
chem = float(input("Enter your marks in chemistry out of 100: "))
math = float(input("Enter your marks in mathematics out of 100: "))
bio = float(input("Enter your marks in biology out of 100: "))
comp = float(input("Enter your marks in computer out of 100: "))
att = float(input("Enter your attandance: "))
percent = 100*(phy+chem+math+bio+comp)/500
if phy>=0 and chem>=0 and math>=0 and comp>=0 and bio>=0 and att<=100 and att>=0 and percent>=0 and percent<=100:
    if percent>=90:
        if att>=95:
            print("You are passed! with 1st division and your percentage is:",percent)
            print("Congratulation! Your scholarship has been granted")
        elif att>=80:
            print("You are passed! with 1st division and your percentage is:",percent)
            print("Congratulation! Your scholarship has been granted")
        elif att>=75:
            print("You are passed! with 2st division and your percentage is:",percent)
            print("Congratulation! Your scholarship has been granted")
        else:
            print("You are passed! with 3st division and your percentage is:",percent)
            print("Your are not eligible for scholarship")
    elif percent>=80:
        if att>=95:
            print("You are passed! with 1st division and your percentage is:",percent)
            print("Congratulation! Your scholarship has been granted")
        elif att>=80:
            print("You are passed! with 2st division and your percentage is:",percent)
            print("Congratulation! Your scholarship has been granted")
        elif att>=75:
            print("You are passed! with 3st division and your percentage is:",percent)
            print("Congratulation! Your scholarship has been granted")
        else:
            print("You are passed! with 3st division and your percentage is:",percent)
            print("Your are not eligible for scholarship")
    elif percent>=33:
        if att>=95:
            print("You are passed! with 2st division and your percentage is:",percent)
            print("Congratulation! Your scholarship has been granted")
        elif att>=80:
            print("You are passed! with 3st division and your percentage is:",percent)
            print("Your are not eligible for scholarship")
        elif att>=75:
            print("You are passed! with 3st division and your percentage is:",percent)
            print("Your are not eligible for scholarship")
        else:
            print("You are passed! with 3st division and your percentage is:",percent)
            print("Your are not eligible for scholarship")
    else:
        print("You are fail and your percentage is:",percent)
        print("You are not eligible for scholarship")
else:
    print("You have entered invalid numbers:")