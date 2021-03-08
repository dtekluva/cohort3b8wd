# RETURN STATEMENT

# def cube(number):
#     return number*number*number
# result = cube(4)
# print(result)

# WHILE LOOP
# from winsound import Beep
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
    
# print("Done with Loop")

print("(Hint -  It's a 3 letter name)")
secret_name = "bae"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_name and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Suggest a name - ")
        guess_count += 1
    
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Sorry, You are out of guess option!!!")

else:
    print("CONGRATS!!! You guessed rightly!")