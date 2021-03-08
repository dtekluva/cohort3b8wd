#create a hangman game in python
import random
with open ('wordlist.txt','r') as f:
    word = f.readlines()

word = random.choice(word)[:-1]
allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower()in guesses:
            print(letter, end= " ")
        else:
            print("_", end =" ")

    print("")

    guess= input(f"you have {allowed_errors} entries left, next guess: ")
    guesses.append(guess.lower())
    if guess.lower()not in word.lower():
        allowed_errors -=1
        if allowed_errors == 0:
            break
done=True
for letter in word:
    if letter.lower()not in guesses:
        done=False
if done:
    print(f"you found the word it was {word}! ")
else:
    print(f"game over!!! word is {word}!!! ")


#create a program that takes in numbers as a list comma seperated values from the terminal,then converts them into a literal python list and does the following.

    #i. print the maximum, minumum, and average number of the bunch
    #ii. print the numbers and their variances in a list i.e (x, x-xbar, x-xbar/squared) in a nicely formatted table.
    #iii. write results into a csv file.

# list_string =input("Enter element of the list seperated by space: ")
# print("\n")
# user_list = list_string.split()
# #print list
# print('list:', user_list)

# #converting all item into int type
# for item in range(len(user_list)):
#     user_list[item] = int(user_list[item])
# print("sum = ", sum(user_list))
# average =sum(user_list)/len(user_list)
# print("avearage", average)
# print("maximum", max(user_list))
# print("manimum", min(user_list))
    

