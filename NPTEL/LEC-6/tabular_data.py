# dictionary : key-value pairs -> data structure
# dict is mutable, unordered, indexed, heterogeneous
maths = {
    'III' : 306,
    'V' : 284,
    'VIII' : 255,
    'X': 220
}

print(len(maths))  # number of key-value pairs
print('V' in maths)  # check if key exists
print (284 in maths)

print(id(maths))
maths['II'] = 'Not measured'  # adding new key-value pair
maths['III'] += 1  # updating value for existing key
print(maths)
print(id(maths))