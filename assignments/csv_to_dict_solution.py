file = open("C:/Users/kboys/OneDrive/Desktop/CLASSES/UNIVELCITY CLASSES/cohort3b8wd/assignments/people.csv", "r")
data = file.readlines()

# print(data)
table_head = data.pop(0) # remove and hold head of table
print(table_head)

final_dict = {}

for column in table_head.split(","): # split head and use values as dictionary keys

    final_dict[column] = []
    # print(column)

for line in data:

    splitted_data = line.split(",")

    for index, key in enumerate(final_dict.keys()):

        final_dict[key].append(splitted_data[index])


print(final_dict)