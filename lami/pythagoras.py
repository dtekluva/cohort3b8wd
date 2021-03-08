Import math
print("This program will calculate pythagorean theorem.")

side_A = float(input("Input side A: "))
side_B = float(input("Input side B: "))
side_C = math.sqrt(side_A * side_A + side_B * side_B)

print("")
print("Side C is: " + "%.2f" % round(side_C,2))
print("")
