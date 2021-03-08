#####################################
### WRITE A PROGRAM THAT COUNTS THE NUMBER OF TIMES AN ALPHABET APPEARS IN A WORD!

# word = input("Enter an Automobile Manufacturer - ")
# choice_alphabet = input("Enter an alphabet to count - ")
# num = 0

# for character in word:
#     if character == choice_alphabet:
#         num += 1
#         #print("found", character) 

# print(f"the number of occurence of {choice_alphabet} in {word} is",  num)  

word = input("Enter an Automobile Manufacturer - ").upper()
choice_alphabet = input("Enter an alphabet to count - ").upper()

print(f"the word '{word}' appears", word.count(choice_alphabet) "times") 