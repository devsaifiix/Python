# '''Data Types: Data types in Python are a way to classify data items. They represent the kind of value, which 
# determines what operations can be performed on that data. Since everything is an object in Python 
# programming, Python data types are classes and variables are instances (objects) of these classes.'''

# # 1. Numeric Data Types
# '''Python numbers represent data that has a numeric value. A numeric value can be an integer, a 
# floating number or even a complex number. These values are defined as int, float and complex classes.'''

# # a) Integers
# a = 5
# print(type(a))

# # b) Float
# b = 5.0
# print(type(b))

# # c) Complex Number
# c = 2 + 4j
# print(type(c))

# # 2. Sequence Data Types
# '''A sequence is an ordered collection of items, which can be of similar or different data types. 
# Sequences allow storing of multiple values in an organized and efficient fashion.'''

# # A) String Data Type
# s = 'Welcome to the Code With Saif'
# print(s)

# # check data type 
# print(type(s))

# # access string with index
# print(s[1])
# print(s[2])
# print(s[-1]) # -1 refers to the last character, -2 is second last, and so on

# # B) List Data Type (Mutable Data Type)
# # Empty list
# a = []

# # list with int values
# a = [1, 2, 3]
# print(a)

# # list with mixed values int and String
# b = ["Code", "With", "Saif", 4, 5]
# print(b)

# # Access List Items
# a = ["Code", "With", "Saif"]
# print("Accessing element from the list")
# print(a[0])
# print(a[2])

# print("Accessing element using negative indexing")
# print(a[-1])
# print(a[-3])

# # C) Tuple Data Type (Immutable Data Type)
# tup1 = ()

# tup2 = ('Saif', 'Tahir')
# print("Tuple with the use of String: ", tup2)

# # Access Tuple Items
# tup1 = (1, 2, 3, 4, 5)

# # access tuple items
# print(tup1[0])
# print(tup1[-1])
# print(tup1[-3])

# # 3. Boolean Data Type
# # Truthy and Falsy Values
# if 1:
#     print("1 is truthy")

# if not 0:
#     print("0 is falsy")

# # 4. Set Data Type (Mutable Data Type)
# s1 = set()

# s1 = set("CodeWithSaif")
# print("Set with the use of String", s1)

# s2 = set(["Code", "With", "Saif"])
# print("Set with the use of List:", s2)

# Access Set Items

# set1 = set(["Code", "With", "Saif", "Code"])   #Duplicates are removed automatically 
# print(set1)

# # loop through set
# for i in set1:
#     print(i, end=" ")   #prints elements one by one

# # check if item exist in set
# print("Code" in set1)

# # 5. Dictionary Data Type
# d = {}

# d = {1: "Code", 2: "With", 3: "Saif"}
# print(d)

# # creating dictionary using dict() constructor
# d1 = dict({1: "Code", 2: "With", 3: "Saif"})
# print(d1)

# Accessing Key-value in Dictionary
d1 = dict({1: "Code", 2: "With", 3: "Saif"})

# Accessing an element using key
print(d1[2])

# Accessing a element using get
print(d1.get(3))