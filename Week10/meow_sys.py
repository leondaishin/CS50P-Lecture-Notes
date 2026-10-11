import sys

if len(sys.argv) == 1: 
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "amount": 
    n = int(sys.argv[2])
    if n >= 0: 
        for i in range(n): 
            print("meow")
    else: 
        print("Invalid")
else: 
    print("usage: meows.py")