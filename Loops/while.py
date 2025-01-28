# Loops are used to repeat instructions
# count = 1 #count -> iterator
# while count <= 5 :
#     print("Hello")
#     count += 1

# print(count)

# n = 1
# while n <= 50 :
#     if(n % 2 == 0):
#         print(n)
#     n += 1

# # Print numbers from 1 to 100
# n = 1
# while n <= 100:
#     print(n)
#     n += 1

# print numbers from 100 to 1
# n = 100
# while n >= 1 :
#     print(n)
#     n -= 1

# # Print the multiplication table of a number n.
# n = 3
# while n <= 30 :
#     print(n)
#     n += 3

# # Print the elements of the following list using a loop
# num = 1
# while num <= 10 :
#     print(num*num)
#     num += 1

# Search for a number x in this tuple using loop
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
idx = 0
x = 47
while idx < len(nums)  :
        if(nums[idx] == x) : 
            print("FOUND")
        else: print("NOT FOUND")
        idx += 1