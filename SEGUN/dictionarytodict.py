#write a scrpt to concantinate the following dictionary 
#to crate a new one 

#sample dictionary



# dict1={'1':'10','2':'20'}
# dict2={'3':'30','4':'40'}
# dict3={'5':'50', '6':'60'}

# dict2.update(dict3)
# dict2.update(dict1)

# print(dict2)

A ={'segun':'28','nedu':'30','shola':'45' }
B ={'john':'30','reneta':'40','atha':'45'}
C ={'michael':'28', 'folarin':'40','king':'30'}

A.update(B)
A.update(C)
print(A)
number = []
for i in A.values():
    if i not in number:
        number.append(i)

print(f"uinque values are as follows \n{number}")
