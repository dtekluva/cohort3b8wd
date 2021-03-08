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



vowel = ["a", "e", "i" , "o" , "u" ]
Sentence = input ( "Enter Sentence here : ")
Split_Sentence = Sentence.split(' ')
output ={}

for words in Split_Sentence:
    
    
    output[words] = {
        "lenght"  : len(words),
        "Vowel"  : 0
         }
    for char in words :
        if char.casefold() in vowel:
            output[words][" Vowel"] += 1

        # print(char, "--> ", char.casefold() in vowel)
           
print (output)

   

   
  



    # for char in words :
    #     print (char)
    #     if char  in vowels:
    #         print ("true")

