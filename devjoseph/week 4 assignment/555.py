a = int(input("Enter value of a: ")) * 3
b = int(input("Enter value of B: ")) * 3
c = int(input("Enter value of C: ")) * 3


# Assigning the sum of c and b if c is not a 10th number



if c // 10 == 1 or c // 20 == 1 or c // 30 == 1 or c // 40 == 1 :
    # if c is a 10th number, we'll make c a list object
    cx = list(str(c))
    
    # minimum value of the list object
    c_min = cx[0]
    c_min1 = int(c_min)
    
    

    # and the maximum value of the list object
    
    c_max = cx[-1]

    # Final result for C
    fina_c = c_max
    
    
    
    
    # ------- for b -----

    # we'll add the remainder from c to our b
    b1 = c_min1 + b

    # let's check if our b is 10th or 20th number
    if b1 // 10 or b1 // 20 or b1 // 30 == 1 :

        # if it is. we'll convert it to a list
        bx = list(str(b1))
        # minimum value of the list object
        b_min = bx[0]
        bd = int(b_min)

        # minimum value of the list object
        b_max = bx[-1]

        fina_b = b_max
       

        # Final result for A
        fina_result_A = a + bd 

        # Final result for all
        print(f"{fina_result_A}{fina_b}{fina_c}")

    else:
        print(a+b+b)

elif b // 10 == 1 or b // 20 == 1 or b // 30 == 1 or b // 40 == 1:
    bxE = list(str(b))
    b_minE = bxE[0]
    bd = int(b_minE)
    b_maxE = bxE[-1]

    fina_bE = int(b_maxE)
    

    print(f"{bd + a}{b_maxE}{c}")
elif c < 10  and b < 10:
    print(f"{a}{b}{c}") 

else:
    print(a+b+c)