# dic1 = {1:10,2:20}
# dic2 = {3:30,4:40}
# dic3 = {5:50,6:60}

# d = dict(dic1)

# d.update(dic2)
# d.update(dic3)
# print(d)


d = {1: "pp", 2:"pp",3:"des",4:"pol"}

uni = list(d)
result = []

for i in d.values():
    if i not in result:
        result.append(i)
print(result)

