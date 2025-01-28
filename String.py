str = "this is a string. \nWe are creating it in python."
str1 = "Apna"
str2 = "College"
concate_Str = str1 + str2
Str_length = len(str1)
# str1[2] = "@" # not allowed X
print(concate_Str)
print(Str_length)
print(str1[2])
print(str)
# SLICING
print(str[ 4 : 13]) 
print(str[ : 13])   #[0 : 4]
print(str[4 : ])    #[4 : len(str)]
print(str[-12 : -3])

print(str.endswith("on."))
print(str.capitalize())
print(str.replace("o","a"))
print(str.replace("python", "Javascript"))
print("find :- ",str.find("o"))
print(str.count("is"))

str3 = input("Enter your first name : ")
print(len(str3))

str4 = "Complete $ your $ goal $ today."
print(str4.count("$"))