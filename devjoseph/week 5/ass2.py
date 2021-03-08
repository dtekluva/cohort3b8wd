# create a program that takes in numbers as a list comma seperated values from the terminal,then converts them into a literal python list and does the following.

# #     i. print the maximum, minumum, and average number of the bunch
# #     ii. print the numbers and their variances in a list i.e (x, x-xbar, x-xbar/squared) in a nicely formatted table.
# #     iii. write results into a csv file.



import csv
<<<<<<< HEAD
your_nums = list(input("enter list of numbers : "))
=======
your_nums = input("enter list of numbers : ").split(",")
>>>>>>> 475212f6bd6f24699cd0aba63db845583f89157e


my_nums = []



for i in your_nums:
    my_nums.append(int(i))

print(my_nums)

# mean
mean_numm = round(sum(my_nums) / len(my_nums))

print("The minumum value is", min(my_nums), "\nthe maximum value is ", max(my_nums), "\nthe average is ", mean_numm)


for i in range(1):
    
    for n in ["x","x-xbar","x-xbar**2"]:
<<<<<<< HEAD
        print(f"{n}".center(5), "|", end = "")
=======
        print(f"{n}".center(8), "|", end = "")
>>>>>>> 475212f6bd6f24699cd0aba63db845583f89157e

    print()
    if i == 0:
        print("-"*28)

    for s in my_nums:
<<<<<<< HEAD
        print(f"\n {s}".center(5), "|", f"{s-mean_numm}".center(5), "|", f"{(s-mean_numm) **2}".center(7), "|", end="")
=======
        print(f"\n {s}".center(8), "|", f"{s-mean_numm}".center(8), "|", f"{(s-mean_numm) **2}".center(8), "|", end="")
>>>>>>> 475212f6bd6f24699cd0aba63db845583f89157e



# Write in to csv file
<<<<<<< HEAD
with open('./devjoseph/week 5/your_file.csv', 'a') as my_file:
=======
with open('./devjoseph/week 5/your_file.csv', 'w') as my_file:
>>>>>>> 475212f6bd6f24699cd0aba63db845583f89157e
    file_writer = csv.writer(my_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    file_writer.writerow(["x","x-xbar","x-xbar**2"])
    for j in my_nums:
        file_writer.writerow([f"{j}",f"{j-mean_numm}", f"{(j-mean_numm) **2}"],)
    








        
    


