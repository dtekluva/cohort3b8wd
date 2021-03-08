# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
def sqaured_Func():
    numers = []
    for n in range(1,30):
        numers.append(n ** 2)
    print(numers)
sqaured_Func()