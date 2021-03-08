# # You are a tv gameshow player.

# # In this game show there is a car to be won, but there are also goats to be won, 
# # the game show host hides these goats and one car behind three doors and asks you to make a choice.

# # The second part of the process is a part where the game show host removes one 
# # goat/ wrong answer from the remainder and asks you if you would like to switch your selection or remain with the chosen option.

# # Q: Should you switch or should you hold on to your original choice. Write a 
# # small program to show the probability of winning for if you switch or if you hold.
# import random

# a = "Car"
# b = "Goat"
# c = "Goat"


# while True:
#     user_selection = input("Pick between A, B & C to will a car: ").casefold()
#     if user_selection == "a":
#         mylist = ["CAR", "Goat"]
#         a = random.choice(mylist)
#         ca = random.choice(mylist)
#         final_ask = input("Do you want to hold on your selection 'option: YES OR NO':    ").casefold()
#         if final_ask == "yes":
#             print(f"you won yourself a {a}")
#             break
#         elif final_ask == "no":
#             print(f"you won yourself a {a}")
#             break
#     elif user_selection == "b":
#         mylist = ["apple", "banana"]
#         b = random.choice(mylist)
#         final_ask = input("Do you want to hold on your selection, or you want to choose between A & B: >  Yes or No:  ").casefold()
#         if final_ask == "yes":
#             print(f"you won yourself a {ca}")
#             break
#         elif final_ask == "no":
#             continue
        
#     else:
#         print("none")


