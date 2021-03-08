#python program to solve quadratic equation
#the standard formula od quadratic equation is 
#ax2+bx-c=0
import cmath
a= float(input("Enter the value of a :"))
b= float(input("Enter the value of b :"))
c= float(input("Enter the value of c :"))
d = (b**2)-(4*a*c)
sol1= (-b-cmath.sqrt(d))/(2*a)
sol2= (-b+cmath.sqrt(d))/(2*a)
print("the solutions are {0} and {1}".format(sol1,sol2))