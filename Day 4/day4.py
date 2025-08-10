import random

random_number = random.randint(0, 10)
if random_number % 2 == 0:
    print("Heads")
else:
    print("Tails")