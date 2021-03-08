# How to determine whether a year is a leap year
# To determine whether a year is a leap year, follow these steps:

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

# A leap year is exactly divisible by 4 except for century years (years ending with 00). 
# The century year is a leap year only if it is perfectly divisible by 400.

enter_year = int(input("Please enter a year: "))

if enter_year % 4 == 0:

    if enter_year % 100 == 0:
        if enter_year % 400 == 0:
            print("The year is a leap year (it has 366 days).")
        else:
            print("The year is not a leap year (it has 365 days).")
    else:
        print("The year is a leap year (it has 366 days).")
    

else:
    print("The year is not a leap year (it has 365 days)")