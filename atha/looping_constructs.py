# from time import sleep
# from winsound import Beep
# import winsound

# ONLY SECONDS COUNT DOWN TIMER

# required_time = int(input("Enter time in seconds > "))

# while required_time > 0:

#     required_time -= 1
#     print(required_time, "seconds")
#     sleep(1)


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

#     seconds = 60
#     minutes -= 1

#     while seconds > 0:

#         seconds -= 1
#         print(f"{minutes}:{seconds}  ", sep="",  end = '')
#         sleep(1)
#         print("\r",end="")
    
#     Beep(1000, 200)


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


import random

while True:

    input("PRESS ENTER TO ROLL")

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print("DIE 1- ", die1)
    print("DIE 2- ", die2)


    if die1 == die2 == 6:
        print("CONGRATULATIONS YOU GOT SIKI 2..!!!")
        break
    else:
        print("Sorry Try again..!!!")
