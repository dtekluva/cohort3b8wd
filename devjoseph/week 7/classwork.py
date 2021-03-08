# import requests
# response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=7871736&APPID=336b102582e7d317c464efd5e6ac86aa').json()['list']
# for i in response:
#     print(f"{i['wind']['speed']}")


###### CURRENT TIME IN PYTHON
# import time

# def time_detector():
#     time_now = time.localtime()
#     currnt = time.strftime("%H:%M", time_now)
#     print(currnt)
# time_detector()


# def goods(a,b):
#     print(a+b)

# goods(10,20)




# employees = ['adekunle', 'sam', 'amadi', 'yetunde', 'seyi', 'john', 'king', 'fyfy']
# salaries = [2000, 501210, 100000, 250000, 104000, 33000, 15000, 100000]


# filter_key = lambda name: len(name)>3

# above_5_chars = filter(filter_key, employees)

# staffs = list(zip(employees, salaries))

# # sort_key = lambda value: value[1]

# def sort_key(value):
#     return value[1]

# print(sorted(staffs, key = sort_key))

# employees = ['adekunle', 'sam', 'amadi', 'yetunde', 'seyi', 'john', 'king', 'fyfy']

# sog = lambda f: f[0] == 'a' or f[0] == 's'
# print(list(filter(sog,employees)))


# def sot(xj):
#     return xj[0]
# print(sorted(employees, key = sot))

# def my_func(a,b,c):
#     return max(a,b,c)

# print(my_func(10,20,5))

# def my_func(a,b,c,d,e,f):
#     return sum([a,b,c,d,e,f])
# print(my_func(8,2,3,0,7,6))

# def my_func(a,b,c,d,e,f):
#     return a*b*c*d*e*f
# print(my_func(8,2,3,-1,7,6))

# def my_func(name):
#     return name[::-1]
# print(my_func("Joseph"))

# def my_func(*n):
# num = input("Enter range of nubers: ").split(" ")
# def my_func(n):
#     numr = list(num)
#     print(numr)
#     n

#     if n in numr:
#         print(True)
#     else:
#         print(False)
# print(my_func(2))


# def my_function(*n):
    
#     return [n / 2]
# x = map(my_function,[10,20,10])
# print(list(x))0

