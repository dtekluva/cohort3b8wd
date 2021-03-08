import os
# write a program that takes a name and last name seperated by comma and write the first name into
# a file named the last name

firstname = input("enter your first name: ")
lastname = input("enter your last name: ")

file = open(f"./devjoseph/week 3 assnm/{lastname}.txt", "w")
file.write(firstname)
file.close()

open_command = f"C:/WINDOWS/system32/notepad.exe C:/Users/son of benjamin/Desktop/2021/python/cohort3b8wd/devjoseph/week 3 assnm/{lastname}.txt"
os.system(open_command)
