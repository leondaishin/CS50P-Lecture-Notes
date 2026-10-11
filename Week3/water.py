from random import sample


def main(): 
    moisture = sample(range(30, 80), 1)[0]
    days = 0
    print(f"Day {days}: The Moisture is {moisture}%")

    while moisture > 20: 
        #the -= means every iteration minusing the value 
        #range 1 to 11 means always minusing between -1 and -11 
        moisture -= sample(range(1, 11), 1)[0]
        #adding the days each time
        days += 1
        #printing out the days and moisture
        #{} standing for the taking of the element from the list of the days and the moisture variable 
        print(f"Day {days}: The Moisture is {moisture}%")

    print("Time to Water!")
    print(f"Total days until watered: {days}")



main()