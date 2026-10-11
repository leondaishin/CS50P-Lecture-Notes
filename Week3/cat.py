# saying while i is starting from 0 to 2 since i is smaller than 3 count meow so 0,1,2 so 3 times.
i = 0
while i < 3: 
    print("meow")
    i += 1

# when i is endless and not so much u can use this
for i in [0, 1, 2]: 
    print("meow")

# here we have a for range loop so for i in a range of thr numbers +...
for i in range(3): 
    print("meow")

# printing the thing n times also possible. 
print("meow\n" * 3, end="")

# here is more like asking and saying the amount to say meow.
while True: 
    n = int(input("What is n ? "))
# here it is saying when n is negative askt he question again until user says something positive
    if n < 0: 
        continue
#here the break means stop asking and do the execution
    else: 
        break
#here is the execution of the program. here the _ can be i or x or any variable and in range n means from 0 until n-1.
for _ in range(n): 
    print("meow")





#FUNCTIONS:
# here we defining a function for getting the meow
def main(): 
    #asking user for a number
    number = get_number()
    meow(3)

# since number = get_number() we dont have get number function in python so we difined it over here. 
def get_number(): 
    while True: 
        n = int(input("What is n ? "))
        if n < 0: 
            continue
        else: 
            return n


def meow(n):
    for _ in range(n): 
        print("meow")


main()



