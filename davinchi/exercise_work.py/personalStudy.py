# from time import sleep
# from winsound import Beep
# import winsound

# minutes = int(input("Enter any number to countdown:- "))

# while minutes > 0:
    
#     seconds = 60
#     minutes -= 1
    
#     while seconds > 0:
#         seconds -= 1
#         print(f"{minutes}:{seconds} " , sep="",  end = '')   
#         sleep(1)
#         print("\r",end="" )


# staff_list = ['TAIWO',
#          'SEYE',
#          'IDRIS',
#          'JOHNSON',
#          'FAITH',
#          'ALABA',
#          'LOLU',
#          'MARVELOUS',
#          'MOBOLAJI'
#         ]
# name = input("Enter your name:  ")
# greet = ("How are you today and how's work activities progressing with you?")
# message = ("fine")

# if name == staff_list:
#     print(f"Hi {name}, {greet}")
#     ask = input("Your response-  ")
#     sleep(1)
#     print(ask)
    
#     if ask == message:
#         sleep(1)
#         print("Nice to know! Do have a safe trip back home.")
            
# else:
#     print("Sorry, you are not a registered staff of Liberty Assured!")


def seye_calc(num):
    return num**3
    

print(seye_calc(4))
