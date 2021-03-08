# DICTIONARY
# MLB_team = dict(
#     Colorado='Rockies',
#     Boston='Red Sox',
#     Minnesota='Twins',
#     Milwaukee='Brewers',
#     Seattle='Mariners',
# )
# print(MLB_team)

# Python_class = dict(
#     davinchy='oldskool',
#     johnson_py='low_cut',
#     segun='2layers',
#     michael='punk',
#     oti='cool_punk',
#     odun='above_skin',
#     nerdu='low_hair',
#     joseph='light_low',
# )
# print(Python_class)
# print(Python_class['odun'])
# Python_class['Paul'] = 'Dreadlocks'
# print(Python_class)


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