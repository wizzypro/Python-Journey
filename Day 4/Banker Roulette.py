import random

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
print(f"One of these friends would pay the bill today >>> {friends}")

# Option 1
random_number = random.randint(0,4)
print(f"{friends[random_number]}, You've been chosen by the gods to pay today's bill. Goodluck!")

# Option 2
print(f"{random.choice(friends)}, You've been chosen by the gods to pay today's bill. Goodluck!")