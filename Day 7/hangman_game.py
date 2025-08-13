import random
word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)
placeholder = ""
random_word_length = len(random_word)

for letter in range(random_word_length):
    placeholder += "_"
print(f"Mystery Word: {placeholder}")


correct_letters = []

def ask_user():
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
    print(blank_random_word_list)


while random_word_length != len(correct_letters):
    ask_user()