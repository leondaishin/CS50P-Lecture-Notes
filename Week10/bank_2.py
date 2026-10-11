class Account: 
    def __init__(self): 
        self.balance = 0

    # getter 
    @property 
    def balance(self): 
        return self._balance

    def deposit(self, n): 
        self._balance += n 

    def withdraw(self, n): 
        self._balance -= n

def main(): 
    account = Account()
    print("Balance: ", account.balance)
    account.balance = 1000
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)

main()