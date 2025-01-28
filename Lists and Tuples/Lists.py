# A built in datatype that can store set of values
# It can store elements of different types(integer, float, string, etc.)

marks = [43.2, 34.5, 56.6, 67.7, 78.9]
print(marks)
print(type(marks))
print(marks[1:4])  #ending index is not allowed

student = ["Karan", 85, 14, "Delhi"]
# strings -> immutable
# lists -> mutable 
student[0] = "Arjun" #mutable
print(student)
print(type(marks))
print(len(student)) # returns length

str = "Hello"
# str[1] = "y" #throws an error