class TooManyStudentsError(Exception):
    pass


class Group:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsError
        self.students.append(student)


group = Group()

try:
    for i in range(11):
        group.add_student(f"Student {i+1}")
except TooManyStudentsError:
    print("Too many students")
