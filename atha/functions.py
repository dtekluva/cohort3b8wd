# def f():
#     s = '-- Inside f()'
#     print(s)
#     print(10)
#     print(10)
#     print(10)
#     print(10)
#     print(10)
#     print(10)
#     import winsound
#     winsound.Beep(1000, 1000)
#     print("Done..!!!")



# print("hello")


# # f()
# # print("end")

# # import datetime

# # def tell_time():
# #     print(datetime.datetime.now())

# # tell_time()

# def interest(p,r,t):
#     print((p*r*t)/100)

# interest(2000, 5, 1)
# import requests
# 

# q = a2 + b(root) + area_of_circle

# def square(num):
#     """
#         This function solves the square of any number an returns it.
#     """
#     return num ** 2
#     print(num)

# def root(num):
#     return num ** 0.5

# def area_circle(radius):
#     return 2 * (22/7) * square(radius)

# a = 4
# b = 3
# circle_radius = 15

# q = square(a) + root(b) * area_circle(radius = circle_radius)
# print(q)

# employees = ['adekunle', 'sam', 'amadi', 'yetunde', 'seyi', 'john', 'king', 'fyfy']
# salaries = [2000, 501210, 100000, 250000, 104000, 33000, 15000, 100000]


# filter_key = lambda name: len(name)>3

# above_5_chars = filter(filter_key, employees)

# staffs = list(zip(employees, salaries))

# # sort_key = lambda value: value[1]

# def sort_key(value):
#     return value[1]

# print(sorted(staffs, key = sort_key))

#  BUBBLE SORT WITH KEYS

# import time
# string_numbers = input("Please enter a list of comma-separated numbers: ").split(",")
# numbers = [ (i) for i in string_numbers]
# print (numbers) 

# def jokes_on_you(haha):
#     return len(haha)

# for i in range (0 , len(numbers)-1):
		
#     for j in range (0, len(numbers)-1):

#         if jokes_on_you(numbers[j]) > jokes_on_you(numbers[j+1]):
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#             time.sleep(.3)
#             print (numbers)
                

# sort_by_first_char = lambda name: name[0]

# print(list(sorted(employees, key = sort_by_first_char)))

def max_of_three(x,y,z):
    return max(x,y,z)

# print(max_of_three(3,1,8))

def addup(x, y, z):
    return sum([x,y,z])

def multiply(*numbers):
    multiple = 1

    for i in numbers:
        multiple *= i

    return multiple

def reverse(string):
    return string[::-1]

def find(number, collection):
    """ range should look like 
        - "start-stop
    """

    x = collection.split("-")
    start_range = int(x[0])
    end_range = int(x[1])

    print(number in range(start_range, end_range))

# find(5, "3-10")

def get_unique(*values):
    print(set(values))

# get_unique(2,2,2,3,3,3,2,1,1,1,4,5,4,45,4,534,4,4,56,6,4,3,2)

import string

def panagram_check(text):

    contains_all = True

    for character in string.ascii_lowercase:
        if character in text:
            # print(character, True)
            pass
        else:
            contains_all =False
        
    print(text, "is panagram : ", contains_all)

# panagram_check("qwertyuiopasdfghjklzxcvbnm")

def divide_by_2(list_of_nums):

    def dividebytwo(num):
        return num//2
    # squared = map(lambda num: num // 2, numbers)
    squared = map(dividebytwo, numbers)
    
    print(list(squared))

numbers = [10, 20, 30, 40]
# divide_by_2(numbers)

# print(reverse("alamu"))
# print(addup(20,10,3))

import winsound

def beep(qty, delay = False):

    for i in range(qty):
        winsound.Beep(1000, 100)

        if delay:
            import time
            time.sleep(1)

beep(50, delay = True)