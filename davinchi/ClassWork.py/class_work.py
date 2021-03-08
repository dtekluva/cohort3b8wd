# print("Hello World!!!")
# print ("Davinchy on pyhton")
# print ("Courtesy Liberty Assured's Oristetimeyin Igbene")

# print("WELCOME TO CLASS TODAY AND CHECK IF A WORD STARTS WITH (A).")
# word=input("What is your name: ")
# print(word.startswith("a"))

# print("WELCOME TO CLASS TODAY AND CHECK IF YOUR NAME ENDS WITH (U).")
# word=input("WHAT IS YOUR NAME: ")
# normalize = word.lower()

# print(normalize.endswith("u"))

# print("This exercise is Checking out for True or False")
# age = input("What is your age? ")
# month =input("month of birth: ")
# result = int(age) + int(month)
# message = "Is " + str(result) + " a even number?: " + str(not bool(result%2))
# print(message)

# print("A program to calculaye Simple Interest")
# Principal = input("What loan amount do you want? ")
# Rate = input("What is the rate? ")
# Duration = input("For what duration? ")
# result1 = int(Principal) * int(Rate) * int(Duration)
# result2 = (result1)/(100)
# message = "If you take a loan of " + Principal + " at the rate of " + Rate + " for " + Duration + " months, you will pay back " + str(result2) + " as interest."
# print(message)  


# print("A program to calculaye Simple Interest")
# P = input("What loan amount do you want? "))
# R = ((input("What is the rate? ")))
# D = ((input("For what duration? ")))
# r1 = (P) * (R) * (D)
# r2 = (r1)/(100)
# message = f"If you take a loan of {P:,} at the rate of {R}% for {D}months, you will pay back total of {r2:,} as monthly interest."
# print(message)

# bola = int(input("how many sweet does bola have? "))
# tolu = int(input("how many sweet does tolu have? "))
# obum = int(input("how many sweet does obum have? "))
# no_of_friends = 3
# total = (bola + tolu + obum)
# share = total // no_of_friends
# extra = total % no_of_friends
# message = (f"The three friends shared among themselves, {total}  sweets while each got  {share}  and  {extra}   was thrown away.")
# print(message)

# bola = int(input("how many sweet does bola have? "))
# tolu = int(input("how many sweet does tolu have? "))
# obum = int(input("how many sweet does obum have? "))
# no_of_friends = 3

# print("UnivelCity admission requirement")
# a = 26
# y = input("How old are you : ")
# # print(f"{a} is greater than {y} : {a} > {y}")

# mynames = ["1", "2", "3"] 

# print("-".join(mynames)) # join takes a delimiter and uses it to join up values in a list.

# import datetime

# second = datetime.datetime.now().second

# if second >= 30:
#     print("You are in the first half of the minute...!!!")
#     seconds_left = 60 - second
#     print(second, "seconds have passed since you entered this minute.")
# #     print(seconds_left, "seconds remain before the next minute.")

# # TENARY OPERATORS

# a = 24
# b = 15

# # if a > b:
# #     m = a
# # else:
# #     m = b

# # a = 14
# # b = 13
# # m = a if a > b else b
# # print(m)

# # a = input("enter 1st number - ")
# # b = input("enter 2nd number - ")
# # m = a if a > b else b
# # print(m)

# # a = input("enter 1st number - ")
# # b = input("enter 2nd number - ")
# # m = a if a < b else a
# # # print(m)

# # cp = int(input("enter cost price - "))
# # sp = int(input("enter selling price - "))
# # mrg = float((sp - cp)/cp) * 100
# # print(f"{abs(mrg)}% loss" if sp < cp else f"{mrg}% profit")

# # cp = int(input("enter cost price - "))
# # sp = int(input("enter selling price - "))
# # mrg = float((sp - cp)/cp) * 100

# # profit_msg = f"{mrg}% profit"
# # loss_msg = f"{abs(mrg)}% loss"
# # print(profit_msg if sp > cp else loss_msg)

# # cp = int(input("enter cost price - "))
# # sp = int(input("enter selling price - "))
# # mrg = float((sp - cp)/cp) * 100

# # profit_msg = f"{mrg}% profit"
# # loss_msg = f"{abs(mrg)}% loss"
# # # print(profit_msg if sp > cp else loss_msg)

# # print("Checking if number inputted is a prime number")
# # num = int(input("enter a number - "))

# # READ MORE ON REALPYTHON.COM/PYTHON-CONDITIONAL-STATEMENTS/

# # a = 100
# # b = 50
# # m = a if a < b else b
# # print(m)

# # d = {'a': 0, 'b': 1, 'c': 0}

# # if d['a'] > 0:
# #     print('ok')
# # elif d['b'] > 0:
# #     print('ok')
# # elif d['c'] > 0:
# #     print('ok')
# # elif d['d'] > 0:
# #     print('ok')
# # else:
# #     print('not ok')

# # LOOP

# # # seconds count down
# # import time
# # cdt = int(input("enter a minute -  "))
# # while cdt:
# #     cdt -= 1
# # #     time.sleep(1)
# # #     print(f"{cdt} going down")

# # # minutes and seconds countdown
# # import time
# # from winsound import Beep
# # # minutes = int(input("enter a minute -  "))
# # # while minutes > 0:
# # #     seconds = 60
# # #     minutes -=1

# # #     while seconds > 0:

# # #         seconds -= 1
# # #         print(f"{minutes}:{seconds}")
# # #         time.sleep(1)


# # minutes = int(input("enter a minute -  "))
# # while minutes > 0:
# #     seconds = 60
# #     minutes -=1
# #     Beep(500, 200)

# #     while seconds > 0:

# #         seconds -= 1
# #         print(f"{minutes}:{seconds} ", end = '', flush=True)
# #         time.sleep(1)
# #         print("\r",end="")

# import random

# while True:
#     input("Please enter keyboard - ")

#     dial1 = random.randint(1,6)
#     dail2 = random.randint(1,6)

#     print("1st dial - ", dial1)
#     print("2nd dial - ", dail2)

#     if dial1 == dail2 == 1:
#         print("CONGRATS, YOU WON!!!")
#         break
#     else:
#         print("sorry, try again")

# import time
# from winsound import Beep

# n = int(input("Enter a number to print - "))
# multiplier = 1
# max_multiplier = 13

# while multiplier < max_multiplier:
#     print(f"{n} x {multiplier}" .center(7), "|", multiplier * n)
#     multiplier += 1
#     Beep(200, 500)

# LONG MULTIPLICATION
# for i in range(1,13):
#     for n in range(1,6):
#         print(f"{n*i}".center(5), "|", end = "")
#     print()
#     if i == 1:
#         print()


# sel_nos =  int(input("Enter a number to search through - "))
# even_Nos = 0
# odd_Nos = 0
# for numbers in range(1, int(sel_nos) + 1):
#     remainder = numbers%2
    
#     if (numbers % 2) == 0:
#         even_Nos +=1
#         print(numbers)
#     elif remainder > 0:
#         odd_Nos +=1
#         print("odd_Nos", numbers)

# LIST SLICING - DATA STRUCTURES
# combs = [1,2,3,4,5,6,7,8,9] 
# combs [1:]
# # print(combs[2:7])
# combs[-len(combs):]
# print(combs[-len(combs):])

