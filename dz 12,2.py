class Item:

    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Item: {self.name}, Price: {self.price}, Description: {self.description}, Dimensions: {self.dimensions}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"User: {self.name} {self.surname}, Phone: {self.numberphone}"


class Order:

    def __init__(self, user):
        self.user = user
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def total_price(self):
        total = 0
        for item, quantity in self.items:
            total += item.price * quantity
        return total

    def __str__(self):
        result = f"Order for: {self.user}\n"
        result += "Items:\n"
        for item, quantity in self.items:
            result += f"{item.name} - {quantity} pcs (price {item.price})\n"
        result += f"Total price: {self.total_price()}"
        return result


item1 = Item("Phone", 500, "Smartphone", "15x7x1")
item2 = Item("Laptop", 1200, "Gaming laptop", "35x25x2")

user1 = User("Ivan", "Ivanov", "+49123456789")

order1 = Order(user1)
order1.add_item(item1, 2)
order1.add_item(item2, 1)

print(order1)