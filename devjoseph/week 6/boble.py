import time
string_numbers = input("Please enter a list of comma-separated numbers: ").split(",")
numbers = [int (i) for i in string_numbers]
print (numbers) 

for i in range (0 , len(numbers)-1):
		
    for j in range (0, len(numbers)-1):

        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            time.sleep(.3)
    print (numbers)
                