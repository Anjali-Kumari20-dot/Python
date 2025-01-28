# Set is a collection of the unordered items
# Each element in the set must be unique and immutable
# set is mutable
# Duplicate values not allowed


# collection = {1, 2, 2, 4, "Hello", "World", "coding", "Python"}
# EmptySet = set() #Empty set syntax
# print(collection.pop())
# print(collection.pop())
# # collection.add(4)
# # collection.add("Anjali Kumari")
# # collection.remove(4)
# # print(type(EmptySet))
# print(collection)
# print(type(collection))
# print(len(collection))

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1.intersection(set2))

# Unhashable" refers to an object that cannot be hashed, meaning its hash value cannot be computed or used for operations like storing in a hash table or set.

# In programming, hashability is a property of an object that allows it to be used as a key in a hash-based data structure, such as a dictionary or set. For an object to be hashable, it must:

# 1. Be immutable (its state cannot change after creation)
# 2. Have a hash value that can be computed (using a hash function)
# 3. Have a hash value that is consistent across different executions of the program

# Examples of unhashable objects include:

# - Lists (because they are mutable)
# - Dictionaries (because they are mutable)
# - Sets (because they are mutable)
# - Custom objects that are mutable or do not implement the __hash__() method

# In contrast, examples of hashable objects include:

# - Integers
# - Floats
# - Strings
# - Tuples (if they contain only hashable objects)
# - Custom objects that are immutable and implement the __hash__() method