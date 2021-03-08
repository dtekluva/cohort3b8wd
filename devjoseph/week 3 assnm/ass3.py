# write a program that takes an integer and print it as, such as 
# "a" + "axa" + "a**a"


enter_text = input("enter a number: ")

#conditional statement to check if my input is a number or string
if enter_text.isdigit():
    enter_textty = int(enter_text)
    print(f"{enter_textty}{enter_textty*enter_textty}{enter_textty**enter_textty}")
else:
    print("Please i need an integer")
