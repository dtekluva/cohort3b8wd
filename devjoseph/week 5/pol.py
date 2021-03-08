# # 2. create a program that takes in numbers as a list comma seperated values from the terminal,then converts them into a literal python list and does the following.

# #     i. print the maximum, minumum, and average number of the bunch
# #     ii. print the numbers and their variances in a list i.e (x, x-xbar, x-xbar/squared) in a nicely formatted table.
# #     iii. write results into a csv file.

# your_nums = list(input("enter list of numbers : "))
# print(min(your_nums), max(your_nums))




# Multiplication table 
# multiple = 2
# multiplier = 1
# max_multiplier = 12

# while multiplier < max_multiplier:

#      print(f"{multiple} x {multiplier}".ljust(10), "|", multiplier * multiple)
#      multiplier += 1

# long multiplication


# for i in range(1,12):
#     for n in range(1,5):
#         print(f"{n*i}".center(5), "|", end = "")
#     print()
#     if i == 1:
#         print("-"*30)

# import csv

# myData = [["first_nrame", "second_name", "Grade"],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B'],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B']]

# myFile = open('exampl45e2.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)
    
# print("Writing complete")

