#program that takesfirstname and lastname seperated with comma then 
# write the first name in a file name lastname 

First_name=input("enter your fisrt name : ")
Last_name =input("enter your last name : ")

file = open(f"{Last_name}.txt", "w")
file.write(First_name)
