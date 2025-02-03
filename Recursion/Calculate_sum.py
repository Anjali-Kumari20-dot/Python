def cal_Sum(n):
    if(n == 0):
        return 0
    return n + cal_Sum(n-1)

print(cal_Sum(10))