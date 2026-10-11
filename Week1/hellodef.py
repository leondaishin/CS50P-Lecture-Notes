#defining  function hello
#printing hello and direction to user with "to"
def main():
    hello()
    name = input("What is your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()


