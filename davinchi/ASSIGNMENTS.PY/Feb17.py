1. # create a hangman game in python.

# 2. create a program that takes in numbers as a list comma seperated values from the terminal,then converts them into a literal python list and does the following.

#     i. print the maximum, minumum, and average number of the bunch
#     ii. print the numbers and their variances in a list i.e (x, x-xbar, x-xbar/squared) in a nicely formatted table.
#     iii. write results into a csv file.

# values = input("Input some comma seprated numbers: ")
# llist = values.split(",")
# d_lenght = len(values)
# my_list = llist()
# for i in range (llist):
#     my_list.append()
#     print(my_list)

    '''
# 1. create a hangman game in python.

# 2. create a program that takes in numbers as a list comma seperated values from the terminal,
# then converts them into a literal python list and does the following.

#     i. print the maximum, minumum, and average number of the bunch
#     ii. print the numbers and their variances in a list i.e (x, x-xbar, x-xbar/squared) in a nicely formatted table.
#     iii. write results into a csv file.
# '''

import csv
from statistics import mean

numbers = input('Enter numbers: ')
# numbers_list = [int(i) for i in numbers.split(',')]
numbers_list = []

for item in numbers.split(','):
    numbers_list.append(int(item))

print()

result = []

print('Maximum: ', max(numbers_list))
result.append(['Maximum', max(numbers_list)])

print('Minimum: ', min(numbers_list))
result.append(['Minimum', min(numbers_list)])

x_bar = mean(numbers_list)
print('Average (x-bar): ', x_bar)
result.append(['Average (x-bar)', x_bar])

print()
print('Table of values')
print()
print('x\tx-bar\tx - xbar/squared')
result.append(['x', 'x-bar', 'x - xbar/squared'])

sum_of_squares = 0

for num in numbers_list:
    num_minus_x_bar = num - x_bar
    num__minus_x_bar_squared = num_minus_x_bar**2

    sum_of_squares += num__minus_x_bar_squared
    
    result.append([num, num_minus_x_bar, num__minus_x_bar_squared])
    
    print(num, '\t', num_minus_x_bar, '\t', num__minus_x_bar_squared)

print()
print('Variance: ', sum_of_squares/(x_bar))
result.append(['Variance', sum_of_squares/(x_bar)])

with open('result.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    for row in result:
        csvwriter.writerow(row)
    

tuple = tuple(list)
final_list = 'List : ',list
# print('Tuple : ',tuple)
print(list)
print(max(list))
