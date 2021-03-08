# 1. create a hangman game in python.









# We need to import random(to randomly select a word) and time(to calculate time)
import random


#our list of words that computer will choose from
from words  import word_list

# We'll create some variables to store the games data

userGuesslist = []
userGuesses = []
playGame = True
continueGame = "Y"


while True:
    computer_code = random.choice(word_list)
    if playGame:
        # We'll convert our computer guess to a list
        com_list = list(computer_code)
        attempts = (len(computer_code) + 9)
    
        # we'll add "_" to our computer guess word to show the length of the word and allow the user to guess
        for n in com_list:
            userGuesslist.append('_')
        print("Computer selected code is : " + ''.join(userGuesslist))

        # Starting our game
        while True:
            # Your guess
            your_word = input("Guess computer selected word ~>: ")

            if your_word in userGuesses:
                print("You already guessed this letter, try something else.")
            else:
                # Reduce the players time by 1
                
                # if the user guess is not in the userGuess,then add the user guess to the userGuess list
                userGuesses.append(your_word)

                # check if the user guess is in the computer selected, if so run this code
                if your_word in com_list:
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    
                    # Now your guess is in the computer selected word, we need to iterate the words using the number of word length
                    for i in range(len(com_list)):
                        if your_word == com_list[i]:
                            word_index = i
                            userGuesslist[word_index] = your_word
                    print("computer word is: " + ''.join(userGuesslist))
                else:
                    attempts -= 1
                    print("You have ", attempts, 'guess left!')
                    print()
                    print("Oops! Try again.")
                    print()
                    print("computer word is: " + ''.join(userGuesslist))
            
            join_list = ''.join(userGuesslist)
            if join_list == computer_code:
                print("Yay! you won.")

                break
            elif attempts == 0:
                print()
                print("Too many Guesses!, Sorry better luck next time.")
                print()
                print("computer word was: "+ computer_code)
                print()
                break
            
        
        continueGame = input("Do you want to play again? Y to continue, any other key to quit ~>: ").casefold()
        if continueGame == "y":
            userGuesslist = []
            userGuesses = []
            playGame = True
        else:
            print("Thank You for playing. See you next time!")
            break
    else:
        break


    
