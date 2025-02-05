def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1) # Recurrance relation
    
print(5, "! =", fact(5))