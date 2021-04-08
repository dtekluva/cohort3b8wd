# <<<<<<< HEAD
# <<<<<<< HEAD
# from time import sleep
# from winsound import Beep
# import winsound
#=======
from time import sleep
from winsound import Beep
import winsound
# >>>>>>> atha

# ONLY SECONDS COUNT DOWN TIMER

# required_time = int(input("Enter time in seconds > "))

# while required_time > 0:

#     required_time -= 1
#     print(required_time, "seconds", sep=" ",  end = '')
#     sleep(1)
#     print("\r",end="")
# =======
from time import sleep
from winsound import Beep
import winsound

#ONLY SECONDS COUNT DOWN TIMER

# required_time = int(input("Enter time in seconds > "))

# while required_time > 0:

#     required_time -= 1
#     print(required_time, "seconds")
#     sleep(1)
# >>>>>>> 121d033ab75b809b7d806bb7f067c62bb5e69727


# MINUTES AND SECONDS COUNTDOWN.

# minutes = int(input("Enter time in minutes > "))

# while minutes > 0:

#     seconds = 60
#     minutes -= 1

#     while seconds > 0:

#         seconds -= 1
#         print(f"{minutes}:{seconds}")
#         sleep(1)
        


# # MINUTES AND SECONDS COUNTDOWN PRINT ON SAME LINE.

# minutes = int(input("Enter time in minutes > "))

# while minutes > 0:

    # seconds = 60
    # minutes -= 1

    # while seconds > 0:

    #     seconds -= 1
    #     print(f"{minutes}:{seconds}  ", sep="",  end = '')
    #     sleep(1)
    #     print("\r",end="")
    
    # Beep(1000, 200)


# HOURS, MINUTES AND SECONDS COUNTDOWN PRINT ON SAME LINE.

# hours = int(input("Enter time in hours > "))


# while hours > 0:

#     hours -= 1
#     minutes = 60

#     while minutes > 0:

#         minutes -= 1
#         seconds = 60

#         while seconds > 0:

#             seconds -= 1
#             print(f"{hours}:{minutes}:{seconds}  ", sep="",  end = '')
#             sleep(1)
#             print("\r",end="")

# print("hello")


# n = 5

# while n > 0:
#     q= input("Please enter a word to test : ")
#     n -= 1

#     if q.startswith("a"):
#         print("Char with letter 'a' found.")
#         break
    
# else:
#     print(f"No char starting with a was inputed after 5 trials")

# dice_roll


# <<<<<<< HEAD
# <<<<<<< HEAD
# import random

# while True:

#     input("PRESS ENTER TO ROLL")

#     die1 = random.randint(1,6)
#     die2 = random.randint(1,6)

#     print("DIE 1- ", die1)
#     print("DIE 2- ", die2)


#     if die1 == die2 == 6:
#         print("CONGRATULATIONS YOU GOT SIKI 2..!!!")
#         break
#     else:
#         print("Sorry Try again..!!!")
# =======
# =======
# >>>>>>> 121d033ab75b809b7d806bb7f067c62bb5e69727
# import random

# while True:

#     input("PRESS ENTER TO ROLL")

#     die1 = random.randint(1,6)
#     die2 = random.randint(1,6)

#     print("DIE 1- ", die1)
#     print("DIE 2- ", die2)


#     if die1 == die2 == 6:
#         print("CONGRATULATIONS YOU GOT SIKI 2..!!!")
#         break
#     else:
#         print("Sorry Try again..!!!")


# <<<<<<< HEAD
# # Multiplication table 
# =======
# Multiplication table 
# >>>>>>> 121d033ab75b809b7d806bb7f067c62bb5e69727
# multiple = 2
# multiplier = 1
# max_multiplier = 13

# while multiplier < max_multiplier:

#      print(f"{multiple} x {multiplier}".ljust(6), "=", multiplier * multiple)
#      multiplier += 1
#      sleep(1)


# <<<<<<< HEAD
# long multiplication
# =======
 # long multiplication
# >>>>>>> 121d033ab75b809b7d806bb7f067c62bb5e69727

# for i in range(1,12):
#     for n in range(1,5):
#         print(f"{n*i}".center(5), "|", end = "")
#     print()
#     if i == 1:
#         print("-"*30)

# LOAN ARMOTIZATION SCHEDULE

# p = int(input("Please enter principal : "))
# r = int(input("Please enter rate : "))
# t = int(input("Please enter time : "))


# number_of_payments = 0

# while number_of_payments < t: 
#     payment = (p + ((p*r*t)/100))/t
#     print(f"Month {number_of_payments+1} |", payment)
#     number_of_payments += 1


# FOR LOOPS

# <<<<<<< HEAD
# ODD AND EVEN NUMBERS.

# number = int(input("Enter a number : "))
# odd_count = 0
# even_count = 0

# for numbers in range(1,number+1):
#   remainder = numbers%2

#   if remainder == 0 :
#     even_count += 1
#     print(numbers)

#   elif remainder >0:
#     odd_count +=1

# print (f"{odd_count} odd numbers,\n{even_count} even numbers")

# name = "adesola"

# for character in name:
#     print(character)

# matric_number = 10088757 # fails because matric is a number and  numbers are not iterable
# for number in matric_number:
#     print(number)

# items = ["phone", "red marker", "blue marker", "nothing"]

# for _ in items:
#     print("Hello")
# x = 30
# y = 15

# print(f"x-{x} y-{y}")

# x, y = y, x # SWITCH VARIABLES

# print(f"x-{x} y-{y}")

# count the occurences of a char in a word

# word = input("Please enter word : ").upper()
# target_char = input("Please enter character : ").upper()

# number_of_occurences = 0

# for character in word:
    
#     if character == target_char:
#         print("found", character)
#         number_of_occurences += 1

# print(f"Number of {target_char} in {word} - ", number_of_occurences)


# word = input("Please enter word : ").upper()
# target_char = input("Please enter character : ").upper()

# count = 0

# for character in word:
    
#     if character == target_char:
#         print("found", character)
#         count += 1

# print(f"Number of {target_char} in {word} - ", count)

# word = input("Please enter word : ")
# target_char = input("Please enter character : ")

# print(word.count(target_char))
# >>>>>>> atha
# =======
# >>>>>>> 121d033ab75b809b7d806bb7f067c62bb5e69727
