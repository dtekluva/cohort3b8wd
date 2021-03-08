# Write a program that takes a string and print the "reverse"

# I can't use the reverse function to reverse a string. so i used slice.  this [:: -1] to reverse a string
enter_text = input("Please enter your message: ")[:: -1]
print(f"the reverse words of your input above are this: {enter_text}")



