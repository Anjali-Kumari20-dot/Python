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
    