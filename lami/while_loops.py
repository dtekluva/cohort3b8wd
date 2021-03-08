# Definit(while_loop) and Indefinit loops(while_loop)
# definit loops has intrinsic end
# infinit loops has no intrinsic  end


# using while loop write a countdown time in seconds

# import time
# from winsound import Beep

# sec = int(input('kindly enter sec number: '))
# while sec > 0:
#     print(f'{sec} seconds countdown')
#     sec -= 1
#     time.sleep(1)

    
#writing a program that print in seconds and minutes

# mins = int(input('Enter time in minutes > '))

# while mins > 0:
#     seconds = 60
#     mins -= 1
#     while seconds > 0:
#         seconds -= 1
#         print(f'{min}:{seconds}')
#         time.sleep(1)


# write a program that print in seconds and minutes on the same line
# mins = int(input('Enter time in minutes > '))

# while mins > 0:
#     sec = 60
#     mins -= 1
#     while sec > 0:
#         sec -= 1
#         print(f'{min}:{sec}', sep = '', end= '')
#         time.sleep(1)
#         print('\r', end='')
#         Beep(500,2)

# dice_roll

import random

while True:
    input('Press enter to roll')
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print("Die 1-", die1)
    print("Die 2-", die1)

    if die1 == die2 == 6:
        print('Congratulations you won')
        break
    else:
        print('Please try again')
break