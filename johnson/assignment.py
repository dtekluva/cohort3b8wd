# How to determine whether a year is a leap year
# To determine whether a year is a leap year, follow these steps:

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).



# print("How to determine whether a year isH a leap year :  ")
# year = int(input("please insert the year"))
# step1 = year % 4 
# step2 = year % 100
# step3 = year % 400
# if ("step1 is divisible by 4, go to step 2"):
#     print(step2)
# else:
#      print(step3)



#   n = 5
# >>> while n > 0:
#      n -= 1
#       print(n)

# n = 5
# while n > 0:
#     n -= 1
#     print(n)


# n = 5
# while n > 0:
#     n -= 1
#     print(n)


# print("write a count down timer that counts to seconds -")
# import time
# count_down = int(input("please inser your time - "))
# while count_down:
#     count_down -= 1
#     time.sleep(1)
#     print(f"{count_down} seconds left")
# import time
# required_Time = int(input("Enter time in seconds   >"))
# while required_Time >0:
#     required_Time -=1
#     print(required_Time,"seconds")
#     time.sleep(1)


# HOURS,MINUTES AND SECONDS COUNTDOWN PRINT ON SAME LINE
# import time
# from winsound import Beep
# hours = int(input("Enter time in hours  >"))
# while hours > 0:
#     hours -=1
#     minutes = 60
#     while minutes > 0:
#         minutes -=1
#         seconds = 60
#         while seconds > 0 :
#             seconds -=1
#             print(f"{hours}:{minutes}:{seconds} sep="", eend = ")
#             time.sleep(1)
#             print("\r",end="")
#             Beep(1000, 200)

# from winsound import Beep
# import time
# time_allowed = int(input("please enter the alloted time  "))
# while time_allowed > 0: 
#     seconds = 60
#     time_allowed -=1
#     print(f"{time_allowed}seconds")
#     time.sleep(1)
#     Beep(1000,200)


# from winsound import Beep
# import time
# minutes = int(input("please enter the alloted time  "))
# while minutes > 0: 
#     minutes =60
#     seconds -=1
#     print(f"{minutes}seconds")
#     time.sleep(1)
#     Beep(1000,200)


# print("Generates a random number between a given positive range")
# import random
# r1 = int(input("insert your number  "))
# while r1 > 0:
#     r1 -=1
# #     r1 = random.randint(1, 6) 
#     print("Random number between 1 and 6 is % s" % (r1)) 
    



# import random
# r1 = int(input("insert your number  "))
# while r1 > 0:
#     r1 -=1
#     r1 = random.randint(1, 6) 
#     print(r1)
# 
# while True :
#     input("PRESS ENTER TO DIAL")
#     die1 = random.randint(1,6)
#     die2 = random.randint(1,6)

#     print("DIE 1- ", die1)
#     print("DIE 2- ", die2)

#     if die1 == die2 == 6 :
#         print("CONGRATULATIONS YOU GOT SIKI 2...!!!")
#         break
#     else:
#         print("SORRY TRY AGAIN...")



# print("write a python program that picks a number and make you guess. ")
# from random import randint
# choose = 1
# number = randint (1,80)
# choose = int(input("choose a number.  :"))
# while choose != number :
#     if choose < number :
#         print("your number too low")
#         choose = int(input("choose again  :"))
#         choose = choose + 1
#     elif  choose > number:
#         print("your number too high")
#         choose = int(input("choose a number  :"))
#         choose = choose + 1
#         print("congratulations, you chose right")
#         print("it only took you", choose,"chooses!")



# a = 2
# b = 1
# while b > 0:
#     b =+1
#     result = (a*b)
#     print(result)


# Iterate 10 times from i = 1 to 10
# Multiplication table (from 1 to 12)

# num = 13


# num = int(input("Display multiplication table of? "))
# for i in range(1, 13):
#    print(num, 'x', i, '|', num*i)


#EVEN AND ODD NUMBERS
import random
number = int(input("please insert a number"))
even_number = 0
odd_number = 0
for i in range(1,number+1):
    remainder = number % 2
    if remainder == 0:
        even_number +=1
        print(number)
    
   
              
       
    
























