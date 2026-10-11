def main(): 


#Boolian Expressions to short the Conditionals:
#Using if not = taking the not A values: 
#Returning means return the code on the process: 
    Difficulty = input("Difficult or Casual? ")
    if not (Difficulty == "Difficult" or Difficulty == "Casual"):
        print("Enter a valid Difficulty. ") 
        return

#Defining Players input
#If not ... same thing: 
#Using Return        
    Players = input("Multiplayer or Single-Player? ")
    if not (Players == "Multiplayer" or Players == "Single-Player"):
        print("Enter a valid number of Players. ") 
        return


# Asking if the player chose Multiplayer or Singleplayer
    if (Difficulty == "Difficult" and Players == "Multiplayer"):
        recommend("Poker")
    elif (Difficulty == "Difficult" and Players == "Single-Player"):
        recommend("Blackjack")
    elif (Difficulty == "Casual" and Players == "Multiplayer"):
        recommend("Hearts")
    else: 
        recommend("Clock")



# Defining the function Recommend: 
def recommend(game): 
    print("You might like", game)




main()