import random
import string

print("Welcome to the PyPassword Generator")
nm_letters = int(input("How many letters would you like in your password? \n"))
nm_symbols = int(input("How many symbols would you like? \n"))
nm_numbers = int(input("How many numbers would you like? \n"))

# Easy Level
nm_letters_pass = ""
erm_letters_array = random.choices(string.ascii_letters, k=nm_letters)
erm_symbols_array = random.choices(string.punctuation, k=nm_symbols)
erm_numbers_array = random.choices(string.digits, k=nm_symbols)

epassword = ""
for letter in erm_letters_array:
    epassword += letter
for symbol in erm_symbols_array:
    epassword += symbol
for number in erm_numbers_array:
    epassword += number
print(f"Your Easy Password is: {epassword}")


# Hard Level

herm_letters_array = random.choices(string.ascii_letters, k=nm_letters)
herm_symbols_array = random.choices(string.punctuation, k=nm_symbols)
herm_numbers_array = random.choices(string.digits, k=nm_symbols)

hpassword = []

for letter in herm_letters_array:
    hpassword.append(letter)
for symbol in herm_symbols_array:
    hpassword.append(symbol)
for number in herm_numbers_array:
    hpassword.append(number)

total_chars = nm_letters + nm_symbols + nm_numbers
hard_password_array = random.choices(hpassword, k=total_chars)
hard_password = ""

for password in hard_password_array:
    hard_password += password

print(f"Your Hard Password is: {hard_password}")
