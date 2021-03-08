######  NO 1.
###### Write a Python program that accepts a hyphen-separated sequence #########
###### of words as input and prints the words in a hyphen-separated sequence ###
###### after sorting them alphabetically #######################################

data = []
take_in = input("Enter a hyphen separated sequence of words:\n ")

def dont_touch_it():
    store = take_in.split('-')
    store.sort()
   
dont_touch_it()


# '-'.join(dont_touch_it)



####   NO 2
#### Write a Python function to create and print a list where the values ######
###  are square of numbers between 1 and 30 (both included). ##################

# num = []
# sqrd_num = []

# for i in range(1,30):
#     num.append(i)

    
# for number in num:
#     sqrd_num.append(number**2)

# num.extend(sqrd_num)

# print(num)



#####  NO 3.
#####      Write a Python program to detect the number of
#####      local variables declared in a function.

# def davinchy_sum():
#     x = 23
#     y = 10
#     z = 35
#     ans = (x + y + z)
#     print(f"The addition of {x} and {y} and {z} = {ans}")

# print(davinchy_sum.__code__.co_nlocals)



########  No 4.
# ####  Write a Python program to access a function inside a function

# def davinchy(x):
#        def vinchy(y):
#            return x+y
#        return vinchy
 
# print(davinchy(5))     