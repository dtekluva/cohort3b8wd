# 1. Please write a bubble sorting algorithm in python to sort any 
# list given.
# reference - 
# https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

# 2. Please write a small script to create a dictionary out of a 
# given csv file e.g

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

# 4. Using the requests module, please make a request from the below URL and get the weather dictionary, on retrieving the data please print the data as such:

# Time            weather         temp (C)   wind-speed  feels-like
# 20-01-21 20:20  light showers   30C         2km/h       32C
# 20-01-21 16:20  light showers   30C         2km/h       32C
# 20-01-21 13:20  light showers   30C         2km/h       32C
# 20-01-21 10:20  light showers   30C         2km/h       32C
# 20-01-21 07:20  light showers   30C         2km/h       32C
# 20-01-21 04:20  light showers   30C         2km/h       32C

# API-KEY = "336b102582e7d317c464efd5e6ac86aa" 
# "http://api.openweathermap.org/data/2.5/forecast?id=7871736&APPID={API-KEY}"


#assignment 
def sort(nums):
    """this function sorts any given combination of numbers in an
    ascending order {from lowest to the highest"""

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                swap = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = swap

nums =[-12,3,4,54,6,1000,7,23,56,10,0,0,-6,]
sort(nums)
print(nums)


#Assignment2
