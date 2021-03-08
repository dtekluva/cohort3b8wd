#Write a small program that takes in any sentence or 
#speech and breaks down all the word into a dictionary 
#containing the word as key and a 
#list/dictionary of the length of the word, 
#and number of vowels in the word

take_in= (input("enter your take_in:").casefold()).split(" ")
print(take_in)
takein_dic = {}
vowels = ("a","e","i","o","u")

for word in take_in:
    vowelscount = 0
    for char in word:
        if char in vowels:
            vowelscount +=1
    takein_dic[word] = {"lenght":len(word),"vowels":vowelscount}
print(takein_dic)