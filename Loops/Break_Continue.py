# Search for a number x in this tuple using loop
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 0
# x = 47
# while idx < len(nums)  :
#         if(nums[idx] == x) : 
#             print("FOUND at idx ",idx)
#             break
#         else: 
#             print("FINDING.......")
#         idx += 1

# PRINT ODD
i = 1
while i <= 10 :
    if(i%2 == 0):
        i += 1
        continue #skip
    print(i)
    i += 1

    # 5:37:54 -> for loop