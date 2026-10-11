# defining balance to start from 0 
balance = 0 

def main(): 
    print("Initial Balance: ", balance)
    deposit(100) 
    withdraw(50)
    print("After Balance: ", balance)


def deposit(i):
    # clue that it is not a local variable 
    # it shows that it is a global variable
    global balance 
    balance += i


def withdraw(i): 
    # the same thing over here 
    global balance
    balance -= i



if __name__ == "__main__":
    main()