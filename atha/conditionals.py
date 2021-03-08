# import datetime

# second = datetime.datetime.now().second

# if second >= 30:
#     print("You are in the second half of the minute..!!!")
#     seconds_remaining = 60 - second
#     print(second, "seconds have passed since you entered this minute.")
#     print(seconds_remaining, "seconds remain before the next minute.")

# elif second < 30:
#     print("You are in the first half of the minute..!!!")
#     seconds_remaining = 60 - second
#     print(second, "seconds have passed since you entered this minute.")
#     print(seconds_remaining, "seconds remain before the next minute.")
# else:
#     print("Hold on you are still in the first half of the second.!!")

# print("I am not controlled by the if 'MWAHAHAHAHAH'!!!")

# # input("Define a noun ? > ")

# age = int(input("PLease enter your age : > "))

# answer= "Old enough" if age > 18 else "Still too young"
# print(answer)


# raining = False
# print("let's go", 'beach' if not raining else 'library')
# ######## P1 ######################  P2 ################

# print(1, 2, 4, 23 > 21, 12 if "ade" is "boy" else 100)

# a= int(input("A > "))
# b= int(input("B > "))

# m = a if a > b else b

# print(m)

### USING TENARY OPERATOR (PROFIT CALCULATOR)

# cost = int(input("Cost price > "))
# sale = int(input("Selling price > "))

# percent_differnce = ((sale - cost)/cost)*100

# profit_message = f"{percent_differnce}% profit" 
# loss_messsage = f"{abs(percent_differnce)}% loss"

# print(profit_message if cost < sale else loss_messsage)

#############################################
### USING CLASSIC IF-ELSE (PROFIT CALCULATOR)

# cost = int(input("Cost price > "))
# sale = int(input("Selling price > "))

# percent_differnce = ((sale - cost)/cost)*100

# if cost < sale:
#     print(f"{percent_differnce}% profit" )
# elif cost > sale:
#     print(f"{abs(percent_differnce)}% loss" )
# else:
#     print("No profit or loss recorded.!!")

<<<<<<< HEAD
# x = 3

# s = ('foo' if (x == 1) else
#       'bar' if (x == 2) else
#       'baz' if (x == 3) else
#       'qux' if (x == 4) else
#       'quux'
#  )
=======
x = 3

s = ('foo' if (x == 1) else
      'bar' if (x == 2) else
      'baz' if (x == 3) else
      'qux' if (x == 4) else
      'quux'
 )
>>>>>>> atha
