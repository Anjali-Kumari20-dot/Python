# WAF to print the length of a list.(list is the parameter)
cities = ["Delhi", "Gurgaon", "Noida", "Pune","Mumbai", "Chennai"]
heroes = ["Thor", "IRonman", "Captain America", "Shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

# WAF to print the list elements of a list in a single line. (list is the parameter)

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)

# WAF to find the factorial of n.(n is the parameter)

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

n = int(input("Enter a number : "))
print(n, "! = ", calc_fact(n))

# WAF to convert USD to INR

def USD_to_INR(n):
    print(n, "USD = ", n*83, "INR")

n = int(input("Enter a number : "))
USD_to_INR(n)

# WAF to display "ODD" if odd number otherwise "EVEN" if even number

def Odd_Even(num):
    if(num % 2 == 0):
        print("EVEN")
    else: print("ODD")

Odd_Even(70)