# Program to check if a string is palindrome or not

enter_text = input("please enter a word: ")
# casefold method removes all case distinctions present in a string.
enter_text.casefold()
if(enter_text == enter_text[::-1]):
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")