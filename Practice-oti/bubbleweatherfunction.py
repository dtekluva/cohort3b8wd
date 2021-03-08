# 1. Please write a bubble sorting algorithm in python to sort any list given.
# reference - https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

# 2. Please write a small script to create a dictionary out of a given csv file e.g

# input file : people.csv

# name    age     gender  
# ade     23      male
# john    21      male
# shade   24      female

# output:

# {
#     name: ["ade", "john","shade"],
#     ages: [23, 21, 24],
#     gender: ["male", "male", "Female"]
# }

# 3. Please read up on functions on real python and come up with a small summary that must describe at least but limited to the fillowing:

# i.   how functions work and their usefulness.
# ii.  keyword arguments
# iii. positional arguments
# iv.  variable positional arguments
# v.   function declaration
# vi.  function return statements

sorting_list = [ 45, 14, 33, 27 , 35 , 10 , 19 , 32 ]
index =0
for numbers in sorting_list:
    if sorting_list[0] > sorting_list[1]:
        sorting_list[0],sorting_list[1] = sorting_list[1] , sorting_list[0]
        print ( sorting_list)