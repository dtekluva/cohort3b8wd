upper_limit = 333 # maximum possible that the sum of the three numbers can reach
n = 100 # also our lower limit

while n < upper_limit:

    n_multiple = n * 3 
    string_n_multiple = str(n_multiple) # n converted to a string

    n_as_string = str(n)

    if n_as_string[2] * 3 == n_multiple:
        print(n, n_multiple)
        break
    
    n += 1
    