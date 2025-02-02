veggies = ["potato", "brinjal", "Ladyfinger", "Cucumber"]
for val in veggies:
    print(val)

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in tup:
    print(num)

str = "Apna College"
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END")
    
# Search for a number x in this tuple using loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
x = 49
idx = 0
for el in nums:
    if(el == 49):
        print("Number found at idx ", idx)
        break
    idx += 1