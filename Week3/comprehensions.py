def main(): 
    counts = {}
    words = get_words("address.txt")

    for word in words: 
        #if the word is nounted in theh counts dictionary 
        if word in counts: 
            #then the amounts of words inthe counts dictionary increases by 1 
            #therefore the += 1 sign 
            counts[word] += 1
        #else if not it will stay at the same amount of words 
        else: 
            counts[word] = 1


    save_counts(counts)
main()