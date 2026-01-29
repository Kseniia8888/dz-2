price = float(input("Enter price: "))
discount = float(input("Enter discount (%): "))

final_price = price - (price * discount / 100)
print("Price with discount:", final_price)