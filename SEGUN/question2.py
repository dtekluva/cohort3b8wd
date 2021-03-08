#program to check for calinbration
ent_text= input("enter your message: ")
ent_text.casefold()
if (ent_text==ent_text[::-1]):
    print("your message is palindrome")
else:
    print("your message is not palindrome")
