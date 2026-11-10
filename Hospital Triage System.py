# Hospital Triage System
name = input("Enter your name: ")
fever = float(input("Enter your fever level: "))
oxygen = float(input("Enter your oxygen level: "))
pulse = int(input("Enter your pulse level: "))
if fever>=36 and fever<=38:
    if oxygen>=95 and oxygen<=100:
        if pulse>=60 and pulse<=100:
            print(f"You are in stable condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in serious condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    elif oxygen>=90 and oxygen<=94:
        if pulse>=60 and pulse<=100:
            print(f"You are in serious condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in serious condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    elif oxygen<=90:
        if pulse>=60 and pulse<=100:
            print(f"You are in critical condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in critical condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    else:
        print("Invalid input, please correct it")
elif fever>=38 and fever<=40:
    if oxygen>=95 and oxygen<=100:
        if pulse>=60 and pulse<=100:
            print(f"You are in serious condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in serious condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    elif oxygen>=90 and oxygen<=94:
        if pulse>=60 and pulse<=100:
            print(f"You are in serious condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in serious condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    elif oxygen<=90:
        if pulse>=60 and pulse<=100:
            print(f"You are in critical condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in critical condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    else:
        print("Invalid input, please correct it")
elif fever>=40:
    if oxygen>=95 and oxygen<=100:
        if pulse>=60 and pulse<=100:
            print(f"You are in critical condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in critical condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    elif oxygen>=90 and oxygen<=94:
        if pulse>=60 and pulse<=100:
            print(f"You are in critical condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in critical condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    elif oxygen<=90:
        if pulse>=60 and pulse<=100:
            print(f"You are in critical condition {name}")
        elif pulse>=101 and pulse<=120:
            print(f"You are in critical condition {name}")
        elif pulse>120:
            print(f"You are in critical condition {name}")
        else:
            print("Invalid input, please correct it")
    else:
        print("Invalid input, please correct it")
else:
    print("Invalid input, please correct it")