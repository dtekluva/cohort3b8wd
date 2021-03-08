word = input( " Enter a word here : ").casefold()
specific_Char = input ( " Enter the character to count here : ")
character_count = 0
for characters in word:
    rev_word = word[::-1]
    if characters == specific_Char: 
        character_count += 1
        if word  == rev_word:
            print ("is a pallidrome")
        else:
            print ( " not a pallidrome")
print( f"{characters} =  {character_count} \n {rev_word} " )
