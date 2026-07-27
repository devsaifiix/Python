# Many Values to Multiple Variables
x, y, z = "Saif", 45, 4.5
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
'''
If you have a collection of values in a list, tuple etc. Python allows you to extract the values
 into variables. This is called unpacking.
'''
fruites = ["Saif", "Tahir", "Fatima", 45]
x, y, z, a = fruites
print(x)
print(y)
print(z)
print(a)