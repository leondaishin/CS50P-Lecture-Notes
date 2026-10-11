def main():
    names = ["Mario", "Luigi", "Yoshi", "Daisy"]
    for name in names: 
        print(write_letter(name, "Princess Peach"))


    #len(names) giving the length of the list so 0,1,2,3 so i is 0,1,2,3
    #for i in range(len(names)):
        #printing not the "i" but the names given 0,1,2,3 so "i":  
    #    print(write_letter(names[i], "Princess Peach"))


#    print(write_letter("Mario", "Princess Peach"))
#    print(write_letter("Luigi", "Princess Peach"))
#    print(write_letter("Yoshi", "Princess Peach"))
#    print(write_letter("Daisy", "Princess Peach"))

#defining the letter function that writes letters
# we directed receiver and sender in print write letter
# forst the receiver and then the sender 
# the f string f""" """ tells to paste the inserted text into the terminal

def write_letter(receiver, sender): 
    return f"""
    ==============================================
        Dear {receiver}, 
        
        You are cordially invited to a ball at
        Peaches Castlle this evening, 7:00 PM. 
        
        Looking forward to seeing you!
        
        Yours Sincerely, 
        
        {sender}
    ==============================================
    """





main()