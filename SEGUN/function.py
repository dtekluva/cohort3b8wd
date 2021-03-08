
# def cu_time():
#     from datetime import datetime
#     print("hello your current time zone is", datetime.now())

# cu_time()

#
# interest_calculator(20,40,50)
 
# employees = ['adekunle', 'sam', 'amadi', 'yetunde', 'seyi', 'john', 'king', 'fyfy']
# salaries = [2000, 501210, 100000, 250000, 104000, 33000, 15000, 100000]

# def fit(name):
#         if name [0] == "a" or name [-1]=="i":
#             return name 
    
#print(list(filter(fit,employees)))


# staffs = list(zip(employees, salaries))

# # sort_key = lambda value: value[1]

# def sort_key(value):
#     return value[0]

# print(sorted(staffs, key = sort_key))

# def maxi(a,b,c,d):
#     return max(a,b,c,d)
# print(maxi(47,10,56,2,))


# def maxi(a,b,c,d):
#     return sum([a,b,c,d])
# print(maxi(47,10,56,2,))

#


# numbers1 = [10, 20, 30,40]
# div= numbers1[0]/2,
# numbers2 = []
# numbers2.append []
  
# result = map(lambda x, y: x + y, num //2 , numbers1) 
# print(list(result)) 

    


     

# filter_key_a = lambda name: name[0]
# filtered = filter(filter_key_a,employees)
# print(filtered)

def dent():
    world_print = 'print("hello world")'
    mult = """
    def mutiply(a,z):
    return a*z

    print('Multiply of 5 and 10 is: ',mutiply(5,10))
    """
    exec(world_print)
    exec(mult)



mycode = 'print("hello world")'
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""
exec(mycode)
exec(code)