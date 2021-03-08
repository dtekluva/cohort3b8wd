Q= int(input ("which question do you want to take : 1 or 2:"))

if Q==2:
    from winsound import Beep
    import random
    repeat ="Y"
    while True: 
            a= random.randint (1 , 9)
            a1 =a
            a2 = a1
            b = random.randint (0 , 9)
            b1 = b
            b2 = b1
            c = random.randint (1 , 9)
            c1 =c
            c2 = c1
            Matrix_1 = [ a ,b, c   ]
            Matrix_2 = [a1 ,b1 ,c1 ]
            Matrix_3 = [a2 , b2 ,c2]
            line_1 = ((a*100)+(b*10)+(c*1))
            Line_2 = ((a1*100)+(b1*10)+(c1*1))
            Line_3 = ((a2*100)+(b2*10)+(c2*1))
            determinant = ((c*100) + (c1*10) + (c2*1))
            summ= line_1+Line_2+Line_3
            print (Matrix_1)
            print (Matrix_2)
            print (Matrix_3)
            print(summ)
            print(determinant)
            
            if summ == determinant:
                print ( "Eureka- you found the numbers!!!")
                break
                Beep(2000, 1000)
                
            
if Q == 1:
    from winsound import Beep
    import random
computers_guess = random.randint ( 1, 20)
number_of_guess = 0
max_guess = 7


while number_of_guess<max_guess:
    guess = int(input("Enter your guess :"))
    number_of_guess +=1
    if guess == computers_guess:
        print(" you got the guess right")
        Beep ( 3000, 5000)
        break
    elif guess < computers_guess:
        print ("too low")
        Beep ( 3000, 500)
    elif guess == computers_guess+1:
        print (" very close : too high by +1")
        Beep ( 4000, 2000)
    elif guess == computers_guess-1:
        print ( "very close - too little by -1 ")
        Beep ( 4000, 2000)
    elif guess > computers_guess:
        print ("too high")
        Beep ( 4000, 2000)
else:
    print (" you have used all your guesses : ")
    Beep ( 4000, 2000)
   

