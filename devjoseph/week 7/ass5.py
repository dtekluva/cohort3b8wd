# Write a Python program to access a function inside a function

def main_func():
    def child_func(b,c):
        return b * c
    return child_func

func_instace = main_func()
print(func_instace(4,6))
