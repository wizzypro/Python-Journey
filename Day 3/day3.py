print("Welcome to Number checker! \n")

number_input = int(input("Enter a Number of your choice: "))

if number_input % 2 == 0:
    print(f"{number_input} is an Even Number")
else:
    print(f"{number_input} is an Odd Number")
