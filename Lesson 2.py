class Student:
    amount_of_students = 0
    def __init__(self, name, height, age, group):
        self.age = age
        self.group = group
        self.height = height
        self.name = name
        Student.amount_of_students += 1

    def __str__(self):
        return (f"Студент {self.name} з групи {self.group}. Вік - {self.age}. Зріст - {self.height}.")
    def __del__(self):
        print(f"Студент {self.name} все...")
    def __bool__(self):
        return self.name !=None
    def __len__(self):
        return self.height

first_student = Student("Вася",167, 19, "8")
print(Student.amount_of_students)
second_student = Student("Петя",183, 20, "50")
print(Student.amount_of_students)
print(first_student)
print(second_student)