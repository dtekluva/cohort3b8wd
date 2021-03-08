# write a program to test if a word is a palindrome

input_value = input('Please enter a word: ')
if input_value == input_value[::-1]:
    print(f'{input_value.title()} is a Palindrome')
else:
    print(f'{input_value.title()}, is not a Palindrome')
