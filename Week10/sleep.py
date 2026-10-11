# count sheeps until we sleep
def main(): 
    n = int(input("What is n? "))
    for s in sheep(n): 
        print(s)


def sheep(n): 
    flock = []
    for i in range(n): 
        flock.append("🐑" * i)
    return flock
    # return return ´s alllll the sheep 
    # yield returns ONE value so that RAM dont kill. 
    ### yield flock


if __name__ == "__main__": 
    main()
