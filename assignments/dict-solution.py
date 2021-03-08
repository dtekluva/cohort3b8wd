input_value = (input('Enter a sentence: ').casefold()).split(" ")
print(input_value) 
dict_value ={}


vowels = ('a e i o u')

for item in input_value:
    count_number_vowels = 0
    for char in item:
        if char in vowels:
            count_number_vowels += 1
    dict_value[item] = {'len of value': len(item), "vowels in word":count_number_vowels}
    
print(dict_value)