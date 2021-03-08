# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
user_input = input("Enter your word ~: ").split("-")
# print(user_input)
items = []
for i in user_input:
    items.append(i)
items.sort()
print("-".join(items))


