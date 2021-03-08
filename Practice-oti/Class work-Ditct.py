# A1 ={1:10, 2:20}
# A2 ={3:30, 4:40}
# A3 ={5:50, 6:60}


# A1.update(A2)
# A1.update(A3)

# print (A1)

# Dictionary = {1:"ada",2:"ada",3:"john",4:"john", 5:"Timothy",6: "Lilian"}
# y= Dictionary.values()
# previous = ""
# for value in y :
#     unique = 0
#     if value == previous:
#         unique +=1
#     previous = value
#     print ( value , unique)
# print (y)

Dictionary = {1:"ada",2:"ada",3:"john",4:"john", 5:"Timothy",6: "Lilian"}

unique = []

for value in Dictionary.values():
    if value in unique:
        pass
    else:
        unique.append(value)

print(unique)