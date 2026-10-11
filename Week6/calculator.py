# Unit Tests for testing my code for my self. 
# Helps to see where my bug is etc.

def main(): 
    # input x 
    x = int(input("What is x? "))
    print("x squared is", square(x))


# defining the square function
def square(n): 
    return n * n



# when i import square function from a "library"
# main is not called itself that is why we do here. 
if __name__ == "__main__":
    main()