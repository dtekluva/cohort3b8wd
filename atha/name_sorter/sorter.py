# filename = "C:/Users/kboys/OneDrive/Desktop/chort-3b8 week/atha/name_sorter/names.txt"

# names = open(filename, "r")
# data = names.readlines()

# number_of_names_in_file = len(data)

# while number_of_names_in_file > 0:

#     number_of_names_in_file -= 1

#     name = data[number_of_names_in_file]
#     first_char = name[0]
#     print(first_char)

#     sortfile = open(f"{first_char}.txt", "a")
#     sortfile.write(name)

# def myadduniversal(*args):
#     s = 0
#     for i in range(len(args)):
#         s += args[i]
#     return s
# print(myadduniversal(200,46,87,45,90))

def print_val(**cho):
    for i in cho:
        print("this is the variable name",i,"and this is the value",cho[i])
print_val(breZd = 23, game = "good", tea = "lame" )