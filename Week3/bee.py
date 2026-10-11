#Words dictionary
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main(): 
    #startinig introduction of the spelling game
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G") 

    #len words means the length of the amount of words in the dictionary of WORDS so 3. 
    while len(WORDS) > 0: 
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        # TODO: Check if guess is dictionary 
        #telling if user guessed graphic, the dictionary will be cleared totally because he guesed the most difficult name in the game
        if guess == "GRAPHIC": 
            WORDS.clear()
            print("You have won the game! ")
        if guess in WORDS.keys():
            points = WORDS.pop(guess) 
            print(f"Good job! You scored {points} points.")




    print("That is the game! ")




main()