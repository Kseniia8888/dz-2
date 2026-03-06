class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age}, Record book: {self.record_book}"


class Group:

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def __str__(self):
        result = f"Group: {self.name}\n"
        for student in self.students:
            result += str(student) + "\n"
        return result


st1 = Student("male", 20, "Ivan", "Petrov", "RB001")
st2 = Student("female", 19, "Anna", "Ivanova", "RB002")
st3 = Student("male", 21, "Oleg", "Sidorov", "RB003")

group = Group("Python")

group.add_student(st1)
group.add_student(st2)
group.add_student(st3)

print(group)

print(group.find_student("Ivanova"))

group.delete_student("Petrov")

print(group)