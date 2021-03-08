import random

sentence = "solarin was  boy of about twenty four years old he loved to dance and shake body music was what got him ecstatic even during dark moments"

word_list = sentence.split(" ")

com_pick = list(random.choice(word_list).lower())
correct_chars =["_"] * len(com_pick)

correct_chars[0], correct_chars[-1] = com_pick[0], com_pick[-1]
print(" ".join(correct_chars))

guesses, max_guesses = 0, 10

while guesses < max_guesses:

    user_letter = input("Please enter guess : ").lower()

    if user_letter in com_pick:

        letter_position = com_pick.index(user_letter)
        correct_chars[letter_position] = user_letter
        com_pick[letter_position] = "_"

    else:
        guesses += 1
        print(f"{guesses} guess(es) used out of {max_guesses}")
        pass

    print(" ".join(correct_chars))

    if "_" not in correct_chars:
            print(f"Weldone, you won with just {guesses} wrong tries")
            break