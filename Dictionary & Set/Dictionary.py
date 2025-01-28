# Dictionaries are used to store data values in key:Value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys
student = {
    "key"  : "Value",
    "name" : "Anjali",
    "cgpa" : 9.4,
    "marks": [98, 97, 100],
    "Subjects" : {
        "Phy" : 97,
        "chem": 98,
        "math": 100
    },
    "is_Present" : True
}
new_dict = {"name" : "Anam", "age": 18}
student.update(new_dict)
print(student)
# print(type(student))
# print(student["name"])
# print(student["cgpa"])
# print(student["marks"])
# print(student["Subjects"])
# print(student["Subjects"]["Phy"])

# print("Keys of student: ",student.keys())
# print("Values of student: ",list(student.values()))
# print("Items of student: ",student.items())

# pairs = list(student.items())
# print(pairs[1])

# print(student["name2"]) # ERROR
print(student.get("name2")) # NO ERROR -> None 

# student["name"] = "Anamika" # Overwrite
# print(student["name"])

# null_student = {}
# null_student["name"] = "ApnaCollege"
# print(null_student)