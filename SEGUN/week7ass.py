#Write a Python program that accepts a hyphen-separated sequence 
#of words as input and prints the words in a hyphen-separated 
#sequence after sorting them alphabetically.
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow


# def word_sort():
#     word = [input("enter your list of word seperated with -:").split("-")]
#     for item in word:
#         item.sort()
#         end = "-".join(item)
#         print(end)

# word_sort()


# Write a Python function to create and print a list 
# where the values are square of numbers between 1 and 30 
# (both included).

# def root_of_value():
#      root = list()
#      for i in range(1,31):
#          root.append(i**2)
#      print(root)

# root_of_value()


# Write a Python program to make a chain of function decorators 
# (bold, italic, underline etc.) in Python.

# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# def make_underline(fn):
#     def wrapped():
#         return "<u>" + fn() + "</u>"
#     return wrapped
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return "hello world" 
# print(hello())

#Write a Python program to execute a string containing Python code.

dent = 'print("hello world")'
code = """
def mutiply(a,b):
    return a*b

print('Multiply of 5 and 10 is: ',mutiply(5,10))
"""
exec(dent)
exec(code)

#Write a Python program to access a function inside a function.

# def test(a):
#         def add(b):
#                 nonlocal a
#                 a += 1
#                 return a+b
#         return add
# func= test(2)
# print(func(4))

#Write a Python program to detect the number  local variables declared in a function

# def abc():
#     x = 1
#     y = 2
#     str1= "w3resource"
#     d=32
#     print("Python")

# print(abc.__code__.co_nlocals)