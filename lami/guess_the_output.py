# write a program tha picks a random number, and makes a user guess if the input number is lower than the number picked, print the number too low, if it is greater pinrt number too large and if it is accurrate print "congrats"
# 5 trials

# write a program that reveal a value behind space or hidden

num = int(input('Enter a number'))
guessed_num = random.randint(1,6)

if num < guessed_num:
    print(f'{num} is smaller than the Guessed')
