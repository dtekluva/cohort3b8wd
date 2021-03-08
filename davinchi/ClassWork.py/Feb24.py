# write a python script that concatenate other dictionaries into 1 dictionary
# dictionary
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# dic4 = {7:70, 80:80}

# dic2.update(dic4)
# dic1.update(dic2)
# dic1.update(dic3)

# print(dic1)

####################### a program to get unique values out from a dictionary ######################

dic_list = {'joe':'guy2','nerdu':'fair++',
        'johnson' :'567asda'
        }

for u in (dic_list.value()):
    print(u.title())


 def bubbleSort( theSeq ):
     n = len(theSeq)

    for i in range(n - 1) :
        flag = 0

        for j in range(n - 1) :
            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return theSeq

el = [21,6,9,33,3] 

result = bubbleSort(el)

print (result)