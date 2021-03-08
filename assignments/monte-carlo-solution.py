# import random

# wins= 0

# for i in range(100):
#     cards = ["c", "g", "g"] # collection of game possibilities

#     random_pick = random.randint(0,len(cards)-1) # pick a number within the range of the cards length

#     selected_card = cards[random_pick] # use the randomly picked number to access the cards list and assign the selected card to a variable

#     cards.pop(random_pick) # remove user pick from collection

#     cards.remove("g") # remove one wrong answer

#     if selected_card == "c":
#         print("You win")
#         wins += 1

#     else:
#         print("Sorry here's your goat")

# print(wins)

# import random

# wins= 0

# for i in range(10000):
#     cards = ["c", "g", "g"] # collection of game possibilities

#     random_pick = random.randint(0,len(cards)-1) # pick a number within the range of the cards length

#     selected_card = cards[random_pick] # use the randomly picked number to access the cards list and assign the selected card to a variable

#     cards.pop(random_pick) # remove user pick from collection

#     cards.remove("g") # remove one wrong answer
    
#     selected_card = cards[0] # make the user switch his original selection with the remaining value.

#     if selected_card == "c":
#         # print("You win")
#         wins += 1

#     else:
#         # print("Sorry here's your goat")
#         pass

# print(wins/10000)




########################################
########### USING RANDOM.CHOICE  #######
########################################

# import random

# wins= 0

# for _ in range(100):
#     cards = ["c", "g", "g"] # collection of game possibilities


#     selected_card = random.choice(cards) # use the randomly picked number to access the cards list and assign the selected card to a variable

#     cards.remove(selected_card) # remove one wrong answer
#     cards.remove("g") # remove one wrong answer

#     if selected_card == "c":
#         print("You win")
#         wins += 1

#     else:
#         print("Sorry here's your goat")

# print(wins)