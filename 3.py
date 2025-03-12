class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привіт, мене звуть {self.name}"

class Student(Person):
    def is_student(self):
        return True

student = Student("Олександр")

print(student.greet())         # Метод greet з класу Person
print("Чи є студентом:", student.is_student())  # Метод is_student з класу Student
