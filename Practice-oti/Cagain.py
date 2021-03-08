Year = int(input("Enter Year : "))
div4 = Year% 4
div100 = Year% 100
div400 = Year % 400
if div4 == 0:
    if div100== 0 :
        if div400 == 0:
            print("The year is a leap year (It has 365 days)")
else:
    print("The year is not a leap year (It has 365 days)")