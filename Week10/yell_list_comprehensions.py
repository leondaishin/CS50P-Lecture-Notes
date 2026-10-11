def main(): 
    # yell(word1, word2, word3) == yell(words) 
    # since yell(words) not defined we need to define the thing. 
    yell("This", "is", "CS50P")

def yell(*words): 
    # make all capitalize for every word in words that is in yell
    uppercased = [word.upper() for word in words]
    # print the words uppercased (* for the whole list of words)
    print(*uppercased)

if __name__ == "__main__": 
    main()