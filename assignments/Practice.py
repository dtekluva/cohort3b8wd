# # # x = 100
# # # x = x + 5
# # # print (x)
# # # x = y = z = "hello"
# # # print(x,y,z)
# # # from winsound import Beep
# # # print("what operator do you want to use")

# # # while True:
# # #     enter_number = (input ("enter either + - * / // **: "))
# # #     num1 = int (input ( "enter a number "))
# # #     num2 = int (input ("enter a number "))

# # #     if enter_number == "+":
# # #         print(num1, enter_number, num2, "=", num1 + num2)
# # #         Beep(2000, 200)
# # #     elif enter_number == "-":
# # #         print(num1, enter_number, num2, "=", num1 - num2)
# # #         Beep(2000, 200)
# # #     elif enter_number == "*":
# # #         print(num1, enter_number, num2, "=", num1  * num2)
# # #         Beep(2000, 200)
# # #         break
# # #     elif enter_number == "/":
# # #         print(num1, enter_number, num2, "=", num1 / num2)
# # #         Beep(2000, 200)
# # #     elif enter_number == "//":
# # #         print(num1, enter_number, num2, "=", num1 // num2)
# # #         Beep(2000, 200)
# # #     elif enter_number == "**":
# # #         print(num1, enter_number, num2, "=", num1 ** num2)
# # #         Beep(2000, 200)
# # #     else:
# # #         print ("invalid number")


# # # multiplication table 12

# # # n = 12
# # # i = 1
# # # while i <= 13:
# # #     print (n,"x",i,"=".center(6),n*i) 
# # #     i = i+1

 
# # # get the highest number 

# # # num1 = input ("enter your first number: ")
# # # num2 = input ("enter your first number: ")
# # # num3 = input ("enter your first number: ")
# # # if (num1 >= num2) and (num1 >= num3 ):
# # #     highest = num1
# # # elif (num2 >= num1) and (num2 >= num3):
# # #     highest = num2
# # # else:
# # #     highest = num3
# # # print ("the highest number is", highest)

# # # write a program that check for the highest Number 
# # # num1 = 90
# # # num2 = 7
# # # num3 = 89
# # # # num1 = input ("enter your first number: ")
# # # # num2 = input ("enter your first number: ")
# # # # num3 = input ("enter your first number: ")
# # # if (num1 >= num2) and (num1 >= num3 ):
# # #     highest = num1
# # # elif (num2 >= num1) and (num2 >= num3):
# # #     highest = num2
# # # else:
# # #     highest = num3
# # # print ("the highest number is", highest)
# # # write a program that chcek for leap year 
# # #  year = int (input( "enter year: "))

# # # if year % 4 == 0:
# # #     if year % 100 == 0:
# # #         if year % 400 == 0:
# # #             print ("this is a leap year")
# # #         else:
# # #             print ("this is not a leap year")
# # #     else:
# # #         print ("this is a leap year")
# # # else: 
# # #     print ("this is a not a leap year")

# # # Generate Fibonacci Sequence 
# # # the first two term are 0 and 1. all other term are obtained by addding the two preceding terms
# # # this means to say nth term is equal to (n-1)th + (n-2)th term 

# # # number = int (input ("enter a number: "))
# # # num1 = 0 
# # # num2 = 1
# # # count = 0
# # # print ("Fibonacci Sequence upto", number,":")
# # # while count < number:
# # #     print (num1, end= " ,")
# # #     nth = num1 + num2 
# # #     num1 = num2
# # #     num2 = nth
# # #     count += 1
# # # print ()

# # # check for prime number 

# # # num = int ( input ("enter a number:"))
# # # numbers1 = 1
# # # for i in range (2, num):
# # #     if (num % i) == 0:
# # #         print(num, "is not a prime number")
# # #         print (i, "times", num //i, "is", num)
# # #         numbers1 = 0 
# # #         break 
# # #     if numbers1 == 1:
# # #         print (num, "is a prime number" )


# # # num = 7
# # # numbers1 = 1
# # # for i in range (2, num):
# # #     if (num % i) == 0:
# # #         print(num, "is not a prime number")
# # #         print (i, "times", num //i, "is", num)
# # #         numbers1 = 0 
# # #         break 
# # #     if numbers1 == 1:
# # #         print (num, "is a prime number" )

# # # print (8 ** (1/3))
# # # num = (20 // 6 )
# # # print (num)
# # # num = (10 // 4)
# # # print (num)

# # # print(888 / 60)
# # # print ( 20 % 6 )
# # # print ( 1.25 % 0.5)
# # # print (7 %(5 // 2))

# # # num = 7425 / 550
# # # print (num)

# # # print ("spam" + "3")
# # # print ("spam" * 3) 
# # # print (4 * "2")

# # # x = 123.456
# # # print (x)

# # # x = "this is a string"
# # # print (x + "!")

# # x = 3
# # num = 17
# # print (num % x)


# # import random 
# # from time import sleep 
# # from winsound import Beep

# # cloth = [ "chinos", "pant", "jeans", "shirt","suit","roundneck","jacket"]
# # system_name =["dell","hp", "lenovo","acer","apple", "huawei","toshiba"]

# # user_guess_list = []
# # user_guesses= []
# # play_Game = True
# # word = ""
# # continue_game = "Yes"

# # name = input ("Enter your name: "). upper ()
# # print ("HELLO", name, "i will like to play Hangman Game!!!!")
# # sleep (3)
# # Beep (2000, 300)
# # print ("the purpose of this game is for the player to Guess the secret word")
# # sleep (3)
# # print ("player can guess only one letter at a time. PRESS ENTER after each guess")
# # sleep(3)
# # print ("let the Game Begin")
# # sleep(3)
# # Beep(1000,300)
# # while True:
# #     if word.upper == "C":
# #         secretword = random.choice(cloth)
# #         break
# #     elif word.upper == "S":
# #         secretword = random.choice(system_name)
# #         break
# #     else:
# #         word = input( "please select a valid word: C for cloth/ S for system_name: A to exit")
# #         if word.upper() == "A":
# #             print ("BYE")
# #             play_Game = False
# #             break




# import random
# # library that we use in order to choose 
# # on random words from a list of words
 
# name = input("What is your name? ")
# # Here the user is asked to enter the name first
 
# print("Good Luck ! ", name)
 
# words = ['rainbow', 'computer', 'science', 'programming', 
#          'python', 'mathematics', 'player', 'condition', 
#          'reverse', 'water', 'board', 'geeks'] 
 
# # Function will choose one random
# # word from this list of words
# word = random.choice(words)
 
 
# print("Guess the characters")
 
# guesses = ''
 
# # any number of turns can be used here
# turns = 12
 
 
# while turns > 0:
     
#     # counts the number of times a user fails
#     failed = 0
     
#     # all characters from the input
#     # word taking one at a time.
#     for char in word: 
         
#         # comparing that character with
#         # the character in guesses
#         if char in guesses: 
#             print(char)
             
#         else: 
#             print("_")
             
#             # for every failure 1 will be
#             # incremented in failure
#             failed += 1
             
 
#     if failed == 0:
#         # user will win the game if failure is 0
#         # and 'You Win' will be given as output
#         print("You Win") 
         
#         # this print the correct word
#         print("The word is: ", word) 
#         break
     
#     # if user has input the wrong alphabet then
#     # it will ask user to enter another alphabet
#     guess = input("guess a character:")
     
#     # every input character will be stored in guesses 
#     guesses += guess 
     
#     # check input with the character in word
#     if guess not in word:
         
#         turns -= 1
         
#         # if the character doesn’t match the word
#         # then “Wrong” will be given as output 
#         print("Wrong")
         
#         # this will print the number of
#         # turns left for the user
#         print("You have", + turns, 'more guesses')
         
         
#         if turns == 0:
#             print("You Loose")

# mlb_team = dict (
#     Colorado = "Rockies",
#     Boston = "Red Sox",
#     Minnesota = "Twins",
#     Milwaukee = "Brewers",
#     Seattle = "Mariners"
# )
# print (mlb_team)

# mlb_team = dict ([
#     ("Colorado", "Rockies"),
#     ("Boston ","Red Sox"),
#     ("Minnesota", "Twins"),
#     ("Milwaukee", "Brewers"),
#     ("Seattle" ,"Mariners")
# ])
# print (mlb_team)


name = dict ([
    ("Segun", "Fair"),
    ("Nedru", "Fair"),
    ("Lami", "Dark"),
    ("Joseph", "Fair"),
    ("Mr jonhson", "Dark"),
    ("Davinchi", "Dark"),
    ("Mr Oti", "Fair")
])
name ["john"] = "Dark"
print (name)

