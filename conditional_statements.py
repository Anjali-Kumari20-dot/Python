# # TRAFFIC LIGHT
# color = input("Enter color: ")
# if(color == "red"):
#     print("stop")
# elif(color == "green"):
#     print("go")
# elif(color == "yellow"):
#     print("look")
# else:
#     print("Light is broken😁")

# # CRITEREA TO VOTE
# age = int(input("enter you age: "))
# if(age == 18):
#     print("can vote")
# elif(age == 16):
#     print("can't vote")
# else:
#     print("go to home 😘")    

# # IDENTIFY GRADE
# marks = int(input("marks : "))
# if(marks >= 90) :
#     print("A")
# elif(marks >= 80 and marks < 90):
#     print("B")
# elif(marks >= 70 and marks < 80):
#     print("C")
# else:
#     print("D")

# # PRACTISE QUESTION
# A = int(input("A : "))
# G = input("M/F : ")
# if((A == 1 or A ==2) and G == "M"):
#     print("fee is rupees 100")
# elif((A ==3 or A ==2) or G == "F"):
#     print("fee is ruoees 200")
# elif( A == 5 or G == "M"):
#     print("fee is rupees 300")
# else:
#     print("no fee")       

# PRACTISE QUESTION -> EVEN OR ODD
num1 = int(input("Enter a number : "))
if(num1 % 2 == 0):
    print("Even")
else :
    print("Odd")

# PRACTISE QUESTION -> GREATEST AMONG 3
val1 = int(input("Enter 1st number : "))
val2 = int(input("Enter 2nd number : "))
val3 = int(input("Enter 3rd number : "))
if(val1 > val2 and val1 > val3):
        print(val1, "is greatest")
elif(val2 > val3):
        print(val2, "is greatest")
else:
    print(val3, "is greatest")

# PRACTISE QUESTION -> IF MULTIPLE OF 7
num = int(input("Enter a number : "))
print("Multiple of 7 or not : ")
if(num % 7 == 0):
    print("yes")
else:
    print("No")