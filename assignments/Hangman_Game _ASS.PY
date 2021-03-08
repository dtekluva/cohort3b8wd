import random 
from time import sleep 
from winsound import Beep

name = input ("Enter your name: "). upper ()
print ("HELLO", name, "i will like to play Hangman Game!!!!")
sleep (3)
Beep (2000, 300)
words  = ["chinos", "pant", "jeans", "shirt","egg","suit","roundneck","jacket"]

word = random.choice(words)
print ("the purpose of this game is for the player to Guess the secret word")
sleep (3)
print ("player can guess only one letter at a time. PRESS ENTER after each guess")
sleep(3)
print ("let the Game Begin")
guesses = ""
time_to_play = 8


while time_to_play > 0:
    failed = 0 
    for char in word:
        if char in guesses:
            print (char)
        else:
            print ("_")
            failed += 1
    if failed == 0:
        print ("Yappi you win")
        print ("the word is ", word)
        break
    guess = input ("guess a word: ")
    guesses += guess
    if guess not in word:
        time_to_play -= 1
        print ("wrong guessing")
        print ("you have ", + time_to_play, "more guesses")
    if time_to_play == 0 :
        print ("you loose")

# 2. create a program that takes in numbers as a list comma seperated values from the terminal,then converts them into a literal python list and does the following.

#     i. print the maximum, minumum, and average number of the bunch
#     ii. print the numbers and their variances in a list i.e (x, x-xbar, x-xbar/squared) in a nicely formatted table.
#     iii. write results into a csv file.

# import csv
# import statistics
# number = input("enter a list seperated by comma: ")
# print ("\n")
# user_inputed = number.split()
# print ("list:", user_inputed)
# for item in range (len(user_inputed)):
#     user_inputed[item] = int (user_inputed[item])
# average = sum(user_inputed)/ len (user_inputed)
# print("average",average)
# print("maximum =",  max (user_inputed))
# print("minimum =",  min (user_inputed))
