n = input()
count = 0

while len(n) > 1:
    product = 1
    for digit in n:
        product *= int(digit)
    n = str(product)
    count += 1

print(count)