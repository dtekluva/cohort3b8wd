import csv

# Assign the file directory to a file variable
file = open("./devjoseph/week 6/filet.csv")

# made the csv file readable
file_re = csv.DictReader(file)

# An empty list that will hold the values of the csv
lor = []


for i in file_re:
    # if the value of the iteration is not an empty dictionary. Then append it to our empty list called ~> "lor"
    if i != {}:
        lor.append(i)

# if you print(lor) you'll get a dictionary inside a list


fina_resut = {
    k: [d.get(k) for d in lor]
    for k in set().union(*lor)
}

print(fina_resut)

file.close()