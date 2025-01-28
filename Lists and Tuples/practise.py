# PRASHANN 1
movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))

print(movies)  

# PRASHANN 2
list = [1, 2, 3, 2, 1]
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("Palindrome")
else:
    print("NOT Palindrome")