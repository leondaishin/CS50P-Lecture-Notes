def main():

    #defining miles and minutes  
    miles = float(input("How many Miles is the marathon?"))
    minutes = float(input("How many Minutes are there to finish the Marathon? "))

    pace = get_pace(miles, minutes)
    print(f"You need to run each mile in {round(pace, 2)} minutes. ")



def get_pace(miles, minutes): 
    if not minutes > 0:
        # using exceptions raise
        raise ValueError("Invalid Value for minutes. ")
    
        # print("Invalid answer")

    return minutes / miles


main()