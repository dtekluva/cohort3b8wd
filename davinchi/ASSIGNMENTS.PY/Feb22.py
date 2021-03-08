# Write a small program that takes in any sentence or speech and breaks down all the word into a dictionary containing the word as key and a list/dictionary of the length of the word, and number of vowels in the word


# example:

# input : "statistics and probabilty have made for discoveries"

# output:

#     {
#         "statistics": {
#             "length":10,
#             "vowels": 4
#         },
#         "and": {
#             "length":3,
#             "vowels": 1
#         },
#         "probability": {
#             "length":11,
#             "vowels": 4
#         },
#         "have": {
#             "length":4,
#             "vowels": 2
#         }
#     }


#####################  specify the vowels  ##########################

id_vowel = ['a', 'e', 'i', 'o', 'u']
entry = input('Type something: ')
final = dict()

words_list = entry.split(' ')

for word in words_list:
    final[word] = {
        'length' : len(word),
        'vowel' : 0
    }

    for character in word:
        if character.casefold() in id_vowel:
            final[word]['vowel'] += 1
print(final)

