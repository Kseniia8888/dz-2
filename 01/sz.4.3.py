import random

# create a list with random length from 3 to 10
length = random.randint(3, 10)
numbers = []

i = 0
while i < length:
    numbers.append(random.randint(1, 10))
    i = i + 1

# create a new list with 3 elements
new_list = [numbers[0], numbers[2], numbers[-2]]

print(numbers)