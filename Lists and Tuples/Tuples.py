# A built-in data type that lets us create immutable sequences of values

tup = (87, 64, 33, 64, 95, 76, 64)
# tup[0] = 43 -> not allowed (immutable)
tup1 = ()
tup2 = (1,)
tup3 = (1,2,3)
print(tup)
print(tup1)
print(tup2)
print(tup3)
print(tup.count(64))