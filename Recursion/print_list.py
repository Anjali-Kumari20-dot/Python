cities = ["Delhi", "Gurgaon", "Noida", "Pune","Mumbai", "Chennai"]

def print_ele(list, idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_ele(list, idx+1)
    
print_ele(cities, 0)
