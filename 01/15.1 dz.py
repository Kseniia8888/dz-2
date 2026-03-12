class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __add__(self, other):
        new_area = self.get_square() + other.get_square()
        new_width = self.width
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_area = self.get_square() * n
        new_width = self.width
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __lt__(self, other):
        return self.get_square() < other.get_square()

    def __le__(self, other):
        return self.get_square() <= other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __ge__(self, other):
        return self.get_square() >= other.get_square()