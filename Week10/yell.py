def main(): 
    yell("This", "is", "CS50P")

def yell(*words): 
    uppercased = []
    for word in words: 
        uppercased.append(word.upper())
        print(*uppercased)

if __name__ == "__main__": 
    main() 
    
