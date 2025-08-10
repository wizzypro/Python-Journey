print('''
+--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(
 `------'
''')
print("Welcome to Treasure Island!\nYour mission is to find the treasure gun.\n")

first_question = input("You're at a cross road. Where do you want to go?\n Type 'left' or 'right' ").lower()


if first_question == "left":
    second_question = input("You've come to a lake. There is an island in middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if second_question == "wait":
        third_question = input("Congratulations, you're at the treasure building. One of the doors in front of you contains the treasures you seek. \nWhich door? Type 'red' for the Red door, 'blue' for the Blue door and 'yellow' for the Yellow door. ").lower()
        if third_question == "yellow":
            print("You Win!!!")
        else:
            print("Game over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")