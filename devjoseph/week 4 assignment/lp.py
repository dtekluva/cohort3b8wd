# We're going to get input from the user

enter_year = input("Please enter a year: ")

# We're going to check if the user input is == number. We all know that
# whatever that's returned from the input is automatically converted to string
# but with isdigit(), we're going to know if the user input is a number. 
# example: '123' will return true while 'ABC' will return false.

if enter_year.isdigit():
    # Our leap year code will run here
    # let's make our user input to an integer.

    lep_year = int(enter_year)
    if lep_year % 4 == 0:
        if lep_year % 100 == 0:
            if lep_year % 400 == 0:
                print("The year is a leap year (it has 366 days).")
            else:
                print("The year is not a leap year (it has 365 days)")

        else:
            print("The year is a leap year (it has 366 days).")

    else:
       print("The year is not a leap year (it has 365 days)")


else:
    print("i need a number not a string")
