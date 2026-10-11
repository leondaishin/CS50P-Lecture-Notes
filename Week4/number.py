# Asking what x is.

# The reason why the program is not correct: 
# If someone inputs cat or dog it will be error.

# Try using to make alot of trials 

# While loop until user makes the integer for x 
# While the error is there excecute the quesiton the whole time 
# Else when error is not there anymore, break the loop and print the x

def main():
    #defining x as the function get int 
    x = get_int("What is x? ")
    print(f"x is {x}")


# defining a function get_int: 
# getting a integer function in short terms. 
def get_int(prompt):
    while True:  
        try: 
            x = int(input(prompt))

        # Making the cat or the dog incorrect. 
        except ValueError: 
            print("x is not an integer, please try again. ")
            # pass (passing the print in a way) (like a bypass in music)

        #else in conditionals but here for exceptions 
        # if try is succesful then else 
        # if try not successful then except and NOT else
        else: 
            return x 
    #after else needs to be break because if print is there, the what is x will always question eventhough if u inputted the number or an integer
    # so here is rather a while False kind of thing. 


main()