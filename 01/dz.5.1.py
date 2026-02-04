import string
import keyword

name = input("Enter variable name: ")

# 1. Must not start with a digit
if name[0].isdigit():
    print(False)
    exit()

# 2. Must not contain uppercase letters
if any(char.isupper() for char in name):
    print(False)
    exit()

# 3. Must not contain spaces or punctuation (except underscore)
for char in name:
    if char in string.punctuation and char != "_":
        print(False)
        exit()
    if char == " ":
        print(False)
        exit()

# 4. Must not be a reserved keyword
if name in keyword.kwlist:
    print(False)
    exit()

# 5. Must contain no more than one underscore
if name.count("_") > 1:
    print(False)
    exit()

print(True)