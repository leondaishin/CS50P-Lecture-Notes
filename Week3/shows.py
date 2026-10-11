#The list of Shows 
SHOWS = [
    " Avatar: The last Airbender", 
    "Ben 10", 
    "Arthur", 
    "Spiderman", 
    "The Amazing World of Gumball", 
    "SpongeBob SquarePants", 
    "Teen Titans Go!", 
    "The Loud House", 
]

def main():
    #defining the list starting from 0 
    cleaned_shows = [] 
    for show in SHOWS: 
        #defining that the list will be added "append" and each and every word on the new coming list will be stripped and titles so capitalized 
        cleaned_shows.append(show.strip().title())

    #printing the list of shows 
    #joining the list of shows with a comma and a space in between each show
    print(", ".join(cleaned_shows))

        #making only the first letter capitalized
        #print(show.capitalize())

        #making all the words capitalize 
        #print(show.title())
        
        #making all words capitalize and strip so that every word is seperated by a space
        #print(show.strip().title())

main()