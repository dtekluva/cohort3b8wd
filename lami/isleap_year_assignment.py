# write a program that ask for a year and return if the year is a leap year or not.

year = int(input('Please enter Year: '))

if year % 4 == 0 and year % 400 == 0:
    print(f'{year} is a leap year')
elif year % 100 != 0:
    print(f'{year} is a leap year')
elif year % 100 == 0:
    print(f'{year} is not leap year')
else:
    print(f'{year} is not leap year')