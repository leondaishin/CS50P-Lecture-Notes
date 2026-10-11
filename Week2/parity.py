#Defining function of main: 
def main():
    x = int(input("What is x?"))
    if is_even(x):
        print("x is even")
    else: 
        print("x is odd")

# Defining function if any n is even or odd: 
def is_even(n):
    return True if n % 2 == 0 else False


#THE LONGER VERSION OF THE CODE. 
#    if n % 2 == 0:
#        return True  
#    else: 
#        return False

main()


# ONLY THE EASY VERSION.
#if x % 2 == 0: 
#    print("x is even ")
#elif x % 3 == 0:
#    print("x is divisible by 3")
#else: 
#    print("x is odd")

