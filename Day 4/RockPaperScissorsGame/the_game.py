import paper
import rock
import scissors
import random
win = "You Win!"
draw = "It's a Draw!"
lose = "You Lose!"

value1 = 0
value2 = 2
value3 = 1
choice = int(input("What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)
if choice == value1 and computer_choice == value1:
    print(f"\nYour choice: \n{rock.rock}\nComputer chose: {rock.rock}\n {draw}")
elif choice == value1 and computer_choice == value2:
    print(f"\nYour choice: \n{rock.rock}\nComputer chose: {scissors.scissors}\n {win}")
elif choice == value1 and computer_choice == value3:
    print(f"\nYour choice: \n{rock.rock}\nComputer chose: {paper.paper}\n {win}")
elif choice == value2 and computer_choice == value1:
    print(f"\nYour choice: \n{scissors.scissors}\nComputer chose: {rock.rock}\n {lose}")
elif choice == value2 and computer_choice == value2:
    print(f"\nYour choice: \n{scissors.scissors}\nComputer chose: {scissors.scissors}\n {draw}")
elif choice == value2 and computer_choice == value3:
    print(f"\nYour choice: \n{scissors.scissors}\nComputer chose: {paper.paper}\n {win}")
elif choice == value3 and computer_choice == value1:
    print(f"\nYour choice: \n{paper.paper}\nComputer chose: {rock.rock}\n {win}")
elif choice == value3 and computer_choice == value2:
    print(f"\nYour choice: \n{paper.paper}\nComputer chose: {scissors.scissors}\n {lose}")
elif choice == value3 and computer_choice == value3:
    print(f"\nYour choice: \n{paper.paper}\nComputer chose: {paper.paper}\n {draw}")
else:
    print("Invalid Input!!!\nTry Again!")