f = open("Python/I/O File/demo.txt", "r")

data = f.read()
print(data)
print(type(data))
f.close()