class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print(f"Student's Name: {self.name}")
        print(f"Student's Age: {self.age}")
        print(f"Student's Id: {self.student_id}")

student1 = Student("Enock", 24, 189)
student1.display_info()     