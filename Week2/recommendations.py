def main(): 
    Difficulty = input("Difficult or Casual? ")
    Players = input("Multiplayer or Single-Player? ")

# Asking if Player chose Difficult or Casual
    if Difficulty == "Difficult":

# Asking if the player chose Multiplayer or Singleplayer
        if Players == "Multiplayer":
            recommend("Poker")
        elif Players == "Single-Player":
            recommend("Blackjack")
        else: 
            print("Enter a valid number of Players. ")
# When Difficulty == Casual is chosen. 
    elif Difficulty == "Casual":
        if Players == "Multiplayer": 
            recommend("Hearts")
        elif Players == "Single-Player": 
            recommend("Clock")
        else: 
            print("Enter a valid Difficulty. ")
    else: 
        print("Enter a valid Difficulty. ")


# Defining the function Recommend: 
def recommend(game): 
    print("You might like", game)




main()