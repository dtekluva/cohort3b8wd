# write a program that takes first name and last name seperated by comma and write the first name into a file and the lastname.


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print('\n')
print(first_name.title(), last_name.title(), sep = ', ')
print('\n')

file = open(f'{last_name}.txt', 'w')
file.write(first_name)
file.close()