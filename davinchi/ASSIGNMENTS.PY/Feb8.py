# Write a program that takes a string and print the reverse
# Write a program to test if a word is a palidrome
# Write a program that takes an integer and print it as such 'a' + 'a*a' + 'a**a' (i.e a=5,5253125)
# Write aprogram that takes a first name and last name seperated by a comma and writes the first name into a file named the last name.

# print("Write a program that takes a string and print the reverse")
# word=input("enter your name: ")
# print("".join(reversed(word)))

# print("This program is to test if a word is a palidrome")
# check = input("enter a string: ")
# rev_check = "".join(reversed(check))
# print("reversed word: ", rev_check)
# if check == rev_check:
#     print(f"the word {rev_check} is Palindrome")
# else:
#     print(f"the word {rev_check} is not Palindrome")

# #Write a program that takes an integer and print it as such 'a' + 'a*a' + 'a**a' (i.e a=5,5253125)
# age = int(input("Enter your age: "))
# age1 = (age*age)
# age2 = (age**age)
# print(f"{age}{age1}{age2}")

# print("a program that takes a first name and last name seperated by a comma and writes the first name into a file named the last name"
# first_name = input("enter your first name: ")
# last_name = input("enter your last name: ")
# file = open(f"./cohort3b8wd (Git) - davinchy/{last_name.txt" , "w")
# file.write(first_name)

# name = str(input("Enter you name- "))
# age = input("Enter you age- ")
# message = (f"{name}, you are {age}yrs Old!")
# print(message)

# How to determine whether a year is a leap year
# To determine whether a year is a leap year, follow these steps:

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

year = int(input("enter a year: "))
ly1 = float(year % 4)
ly2 = float(year % 100)
ly3 = float(year % 400)
if ly1 == 0: 
    if ly2 == 0:
        if ly3 == 0:
    print(f"the {year} is a leap year, it has 366 days")
else:
    print(f"the {year} is not a leap year. It has 365 days")
