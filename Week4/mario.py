# Making a pyramid for any i for the mario game
def main(): 
    #asking the height of the pyramid
    height = int(input("Height: "))
    #printing the pyramid but we need to define pyramid
    pyramid(height)



def pyramid(n):
    #for any pyramid height == n , for i in the range from 0 to n  
    for i in range(n):
        #we print the # for any i for each column(reihe) 
        print("#" * (i + 1))


# 
if __name__ == "__main__":
    main()