import random

while True:
    input("Press enter to play dice: ")

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print(f"you rolled: {die1} : {die2}")

    if die1 == die2 == 6:
        print("Congratulations. you won")
        break
    else:
        print("Sorry, roll the dice again")