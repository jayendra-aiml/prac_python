#Movie Ticket Pricing Sysytem
day = int(input('''Enter 1 to book movie tickets on weekend
Enter 2 book movie tickets on weekdays: '''))
time =  int(input('''Enter 1 for morning time  
Enter 2 for evening time 
Enter 3 for night time : '''))
type = int(input('''Enter 1 if you are a student 
If not enter 2:  ''')) # 20% discount for students
if type == 1: 
    if day == 1:
        if time == 1: #150 base prize for morning weekend
            print("Your ticket prize=","₹",(20*150)/100) 
        elif time == 2: #220 base prize for evening weekend
            print("Your ticket prize=","₹",(20*220)/100) 
        elif time == 3: #200 base prize for night weekend
            print("Your ticket prize=","₹",(20*200)/100)
        else:
            print("Invalid choice, please enter again") 
    elif day == 2:
        if time == 1: #120 base prize for morning weekday
            print("Your ticket prize=","₹",(20*120)/100) 
        elif time == 2: #180 base prize for evening weekday
            print("Your ticket prize=","₹",(20*180)/100) 
        elif time == 3: #150 base prize for night weekday
            print("Your ticket prize=","₹",(20*150)/100)
        else:
            print("Invalid choice, please enter again") 
    else:
        print("Invalid choice, please enter again")
elif type == 2: 
    if day == 1:
        if time == 1:
            print("Your ticket prize=","₹",150) 
        elif time == 2:
            print("Your ticket prize=","₹",220) 
        elif time == 3:
            print("Your ticket prize=","₹",200)
        else:
            print("Invalid choice, please enter again") 
    elif day == 2:
        if time == 1:
            print("Your ticket prize=","₹",120) 
        elif time == 2:
            print("Your ticket prize=","₹",180) 
        elif time == 3:
            print("Your ticket prize=","₹",150)
        else:
            print("Invalid choice, please enter again") 
    else:
       print("Invalid choice, please enter again")
else:
    print("Invalid choice, please enter again")