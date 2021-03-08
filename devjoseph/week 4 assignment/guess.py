import random
n = 5

while n > 0:
    n -= 1
    g = int(input("please enter a number not greater than 10: "))
    gueg = random.randint(1,10)

    if g == gueg:
        print("Congrats!! You just guess the computer number")
        break
    elif g > gueg:
        print("Your number is too high")
        t = n - 5
        y = abs(t)
        print(f"you've played {y} times")
        
    elif g < gueg:
        print("too low")
        t = n - 5
        y = abs(t)
        print(f"you've played {y} times")
else:
    print("Your time is up")
        
    


    

