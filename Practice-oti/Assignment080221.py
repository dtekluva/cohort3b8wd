
# Question = input ("which question do you want to answer : ")
# if Question == "1" :
#     print ("Question 1 : Print a String in reverse  :")
#     name = input ("enter name here: ")
#     rev_name = str(name[::-1])
#     print (rev_name)
#     Repeat = input("Repeat question 1 ?: (Y) or (N)")
#     print(Repeat)

# elif Question == "2":
#     print ("Question 2: Test that a word is a pallidrome  :")
#     n1 = input("enter word to check Palidrome :")
#     n2 = str(n1[::-1])
#     if n1== n2 :
#         print (f"{n1} is a Palidrome")
#     else:
#         print (f"{n1} is not a palidrome")
#         Repeat1 = input("Repeat question 1 ?: (Y) or (N)")
#         print(Repeat1)


# elif Question == "3" :
#     print ("""Question 3: Write a programme that atake an integer and prints it as such
#     "a"+"a*a +a**a""")
#     base_num = int(input( "Enter base number : "))
#     pow_num = base_num
#     result_1 = base_num * pow_num
#     result_2 = result_1* pow_num
#     result_3 = result_2 * pow_num

#     print(result_1,result_2,result_3)

# # def raise_to_power ( base_num, pow_num):
# #     result = 1
# #     for index in range (pow_num):
# #         result = result * base_num
# #     return result
# a = int(input("Enter for a :"))
# b = int(input("Enter for b :"))

# m = a if a>b else b
# print(m)

# a = int( input("Enter number here : "))
# b = int( input("Enter number here : "))

# m = a if a<b else b
# print (m)

# 
number =int (input("enter number : "))
count = 0

for numbers in range(1,number+1):
    determinant = number/ numbers
    if int(determinant) ==  determinant:
        count += 1
if count == 2:
    print('is prime')
else:
    print("is not prime")