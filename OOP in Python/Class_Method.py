# A class method is bound to the class & receives the class as an implicit first argument

# Note - static method can't access or modify class state & generally for utility.

class Student:
    total_students = 0

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        Student.total_students += 1

    @classmethod
    def get_total_students(cls):
        return cls.total_students
    
    @classmethod
    def reset_total_students(cls):
        cls.total_students = 0

student1 = Student("Rahul", "101", 90)
student2 = Student("Rohan", "102", 85)
student3 = Student("Raj", "103", 95)

print("Total Students : ", Student.get_total_students())

Student.reset_total_students()
print("Total students after reset: ", Student.get_total_students())