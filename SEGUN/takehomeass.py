#write a simple program that can solve quadratic equation and pythagoras equation
#the program should ask to input a, b, c and give value for x1, x2, x3 
 

# print("This programs will solve quadratic problems")
# from math import sqrt
# a= int(input("enter the first coefficient : "))
# b= int(input("enter the second coefficient : "))
# c= int(input("enter the third coefficient : "))
# print()
# my_ex = b**2 -4*a*c  #b^2-4ac
# my_ex1 = sqrt(my_ex)
# positive =(-b + my_ex1)/(2*a)
# negative =(-b - my_ex1)/(2*a)
# print("the positive value of the quadratic equateion is {0}, and the negative value is {1}".format(positive,negative))

print("this is solving pythgoras theorem")
x= int(input(" enter the value of first side: "))
y= int(input(" enter the value of second side: "))
z_squared= x**2 + y**2 
z=z_squared**0.5
print(z_squared)
print("the lengnth of the hypotenus is ", z)