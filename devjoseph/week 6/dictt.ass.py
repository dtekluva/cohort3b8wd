# Write a small program that takes in any sentence or speech and breaks down all the word into a dictionary containing the word as key and a list/dictionary of the length of the word, and number of vowels in the word


# example:

# input : "statistics and probabilty have made for discoveries"

# output:

#     {
#         "statistics": {
#             "length":10,
#             "vowels": 4
#         },
#         "and": {
#             "length":3,
#             "vowels": 1
#         },
#         "probability": {
#             "length":11,
#             "vowels": 4
#         },
#         "have": {
#             "length":4,
#             "vowels": 2
#         }
#     }


user_input = input("Enter your sentence. ~>: ").split(" ")

# convt = list(user_input)
# print(user_input)
# vowels = 0

result = {}


for i in user_input:

    #vowel
    
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for n in i:
        # ff = len(n)
       if(n in vowels):
           vowel_count += 1
           
    # letr_lent = len(i)
    
    result[i] = {"length": len(i), "vowels": vowel_count}

print(result)


