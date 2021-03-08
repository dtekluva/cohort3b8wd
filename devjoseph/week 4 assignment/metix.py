# range_Limit = 333
# n = 100

# while n < range_Limit:
#     n_multiple = n * 3

#     n_multiple_4_string = str(n_multiple)

#     n_as_string = str(n)

#     if n_as_string[2] * 3 == n_multiple:
#         print(n, n_multiple)
#         break
#     n += 1


# limit = 12
# n = 0

# while n < limit:
#     n += 1
#     n1 = 2 * n
    
#     print(f"2 X {n}".ljust(7), "|", f"{n1}")





#Simple interest
# pt = int(input("Enter the amount you want to borrow: "))
# pi = int(input("Enter your interest: "))
# pr = int(input("Enter the duration: "))

# n = 0

# while n < pr:
#     n += 1
    

#     intrstr = (pt * pi * pr) / 100

#     dd = (pt  + intrstr) / pr

#     print(f"month {n} you'll pay | {dd}")


# for i in range(1,12):
#     for n in range(1,6):
#         print(f"{n*1}".center(5), "|", end="")
        
#     print()
#     print("-"*33)

b = range(1,100)
c = []
f = []
for n in range(1,100+1):
    if n % 2 == 1:
        c.append(n)
    if n % 2 == 0:
        f.append(n)
print(c)
print(f"the total number of odd numbers are", len(c))
print(f)
print(f"the total number of odd numbers are", len(f))

    

    
    
    
    