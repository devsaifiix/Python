name = input("Enter your name: ")
print("Hello", name, "Welcom!")

# Printing Variables
s = "Brad"
print(s)

s = "Anjelina"
age = 25
city = "New York"
print(s, age, city)

# Take Multiple Input in Python
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

# Change the Type of Input in Python
'''By default input() function helps in taking user input as string. 
If any user wants to take input as int or float,
we just need to typecast it.'''

color = input("What color is rose?: ")
print(color)

n = int(input("How many roses?: "))
print(n)

price = float(input("Price of each rose?: "))
print(price)

# Find DataType of Input in Python
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))