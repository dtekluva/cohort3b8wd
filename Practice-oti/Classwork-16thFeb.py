# definite_number = 3
# highest_number = 1

# while highest_number<= 12 :
#     multiplication_table = definite_number * highest_number
#     print (f"{definite_number} x {highest_number}" .ljust(7),"|", multiplication_table)
   
#     highest_number +=1

# Loan_amount = int(input ("Enter Loan amount :"))
# interest_rate = int(input ("Enter interest :"))
# Duration = int (input ("Enter duration  :"))

# number_of_payment = 0

# while number_of_payment < Duration :
#     interest_amount = Loan_amount *  (interest_rate*Duration)
#     total_repayment = Loan_amount + interest_amount
#     monthly_repayment = total_repayment/Duration


#     print (f"month{number_of_payment+1} |", monthly_repayment)
#     number_of_payment +=1


# number = int(input("Enter a number : "))
# odd_count = 0
# even_count = 0
# odd = []
# even = []
# for numbers in range(1,number+1):
#   even_numbers = numbers%2

#   if even_numbers == 0 :
#     even_count += 1
#     even.append (numbers)
#   elif even_numbers >0:
#     odd_count +=1
#     odd.append(numbers)

# print (f"{odd_count} odd numbers {odd},\n{even_count} even numbers {even}")

combs = [1,2,3,4,5,6,7,8,9]

print (combs[1:])
print (combs[2:6])
print (combs[-len(combs)])
