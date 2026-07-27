# # global variable
# x = "awesome"

# def myfunc():
#     print("Python is " + x)
# myfunc()

# # Create a variable inside a function, with the same name as the global variable
# x = "awesome" # gobal variable

# def myfunc():
#     x = "fantastic" # local variable
#     print("Python is " + x)
# myfunc()

# print("Python is " + x)

# The global Keyword
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
myfunc()

print("Python is " + x)