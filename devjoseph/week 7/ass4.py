# Write a Python program to execute a string containing Python code.

# fisf = 'print("Python week 7 assignment")'

# eval(fisf)

bigco = """
def sqaured_Func():
    numers = []
    for n in range(1,30):
        numers.append(n ** 2)
    print(numers)
sqaured_Func()
"""

exec(bigco)