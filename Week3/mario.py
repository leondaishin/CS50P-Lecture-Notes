# n = int(input("What is n ? "))

#for _ in range(n): 
#    print("#")


def main():
    print_column(3)
    print_row(4)
    print_square(3)

# here we have print_colomn(3) and in the () we have height later so height == 3 defined.
# height means in lines top of another
def print_column(height):
    for _ in range(height): 
        print("#")
#a way to also do the # 3 times. 
#     print("#\n" * height, end = "")

# defining the print_row so that the ? will stay in a row: 
#width for the characters being nebeneinander. 
def print_row(width):
    print("?" * width)

#defining a square so width AND height: 
def print_square(size): 
    #for each row in square
    for i in range(size): 
        #for each brick in row 
        for j in range(size): 
            #print brick ending "" so that brick is nebeneinander
            print("#", end="")
        #printing the blank new line
        print()


main()