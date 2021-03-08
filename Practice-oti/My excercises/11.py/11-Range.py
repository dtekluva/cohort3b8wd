my_range = range ( 1,21)
my_list = []

for numbers in my_range:
    n= (numbers *10)
    my_list.append(n)
print( my_list)

#Another way to solve this is 
print ([10* numbers for numbers in my_range])