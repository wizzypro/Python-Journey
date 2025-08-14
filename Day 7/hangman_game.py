import random
word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)
placeholder = ""
random_word_length = len(random_word)

for letter in range(random_word_length):
    placeholder += "_"
print(f"Mystery Word: {placeholder}")

game_over = False
correct_letters = []


def ask_user():

    global game_over
    blank_random_word_list = ""
    user_guess = input("Guess a letter in the mystery word: \n").lower()
    for letter in random_word:
        if user_guess == letter:
            blank_random_word_list += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            blank_random_word_list += letter
        else:
            blank_random_word_list += "_"
    if "_" not in blank_random_word_list:
        game_over = True
        print("You Win!!")
    print(blank_random_word_list)



print(f"Game over value: {game_over}")

while not game_over:
    ask_user()
    # print(f"Game over value: {game_over}")


