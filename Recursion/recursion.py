# recursive function
def show(n):
    if(n == 0): # base case
        return
    # show(n-1)
    print(n)
    show(n-1)

show(5)