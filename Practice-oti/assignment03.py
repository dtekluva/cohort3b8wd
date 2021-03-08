from winsound import Beep
import random
computers_guess = random.randint ( 1, 20)
number_of_guess = 0
max_guess = 7


while number_of_guess<max_guess:
    guess = int(input("Enter your guess :"))
    number_of_guess +=1
    if guess == computers_guess:
        print(" you got the guess right")
        Beep ( 3000, 5000)
        break
    elif guess < computers_guess:
        print ("too low")
        Beep ( 3000, 2000)
    elif guess == computers_guess+1:
        print (" very close : too high by +1")
        Beep ( 4000, 2000)
    elif guess == computers_guess-1:
        print ( "very close - too little by -1 ")
        Beep ( 4000, 2000)
    elif guess > computers_guess:
        print ("too high")
        Beep ( 4000, 2000)
else:
    print (" you have used all your guesses : ")
    Beep ( 4000, 2000)
   
