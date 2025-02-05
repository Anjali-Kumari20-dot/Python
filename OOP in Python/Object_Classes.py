class Student:
    college_name = "ABC College"
    name = "Anonymous" # class attr

    # DEFAULT CONSTRUCTORS
    def __init__(self):
        pass

    # PARAMETERISED CONSTRUCTORS
    def __init__(self, name, marks):
        self.name = name  # obj attr > class attr
        self.marks = marks
        
    def welcome(self):
        print("Welcome student")

    def get_marks(self):
        return self.marks
    
s1 = Student("Karan", 97)
print(s1.name, s1.marks) #Karan
print(s1.get_marks())
s1.welcome()

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)
s2.welcome()