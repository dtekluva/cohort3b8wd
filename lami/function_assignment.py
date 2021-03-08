# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

# Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.

# Write a Python program to execute a string containing Python code.

# Write a Python program to access a function inside a function.

# Write a Python program to detect the number of local variables declared in a function.






# SOLUTION 1

# def sortAlpha (a) :
#     for i in range (len(a) + 1) :
#         for j in range (len(a) - 1) :
#             if a[ j ][ 0 ] > a[ j + 1][ 0 ] :
#                 a[ j ], a[ j + 1 ] = a[ j + 1 ], a[ j ]
                
#     string = ("-").join(a)
#     print("Sorted words: \n>", string)
# str = input ("Please enter hyphen-separated words: \n>")
# c = str.split("-")
# print('\n')
# sortAlpha(c)




# SOLUTION 2

# def squaredList():
# 	lst = list()
# 	for i in range(1,30+1):
# 		lst.append(i**2)
# 	print(lst)
# print('The squared sequence of the list is shown below:'.upper())	
# squaredList()


# SOLUTION 3

# def makeBold(fn):
#    def wrapped():
#        return "<b>" + fn() + "</b>"
#    return wrapped

# def makeItalic(fn):
#    def wrapped():
#        return "<i>" + fn() + "</i>"
#    return wrapped

# def makeUnderline(fn):
#    def wrapped():
#        return "<u>" + fn() + "</u>"
#    return wrapped
# @makeBold
# @makeItalic
# @makeUnderline
# def hello():
#    return "Welcome to Univelcity"
# print(hello())





# SOLUTION 4

# user_input = 'print("Data science cyber security".upper())'
# exec(user_input)





# SOLUTION 5

# def outerFunc(): # this is the outer function
#     print ("HELLO from the outer WORLD(Alien from Mars)")
#     def innerFunc(): # this is the inner function
#         print ("HELLO from the inner WORLD(Earth Citizen)")
#     innerFunc()
# outerFunc()





# SOLUTION 6

# def fun(): 
#     x, y, z = 45, 100, 6.89
#     str = 'Univelcity'
#     bool = True
#     char = 'c'
 
# print(fun.__code__.co_nlocals)
