# WAP to find the sum of first n numbers.(using while)
n = int(input("Enter a number : "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("Total sum : ", sum)

# WAP to find the factorial of first n numbers.(using for)
num = int(input("Enter a number : "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial : ", fact)

# for i in range(1, n+1):
#     sum += i

# print("Total Sum : ", sum)