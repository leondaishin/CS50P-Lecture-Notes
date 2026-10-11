#list of distances 
distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58", 
    "Pioneer 11": "44 AU"
}


def main(): 
    spacecraft = input("Enter a spacecraft: ")
    try: 
        #here wenn float is looked for and the pioneer 10 is 80 AU it can not be converted into a float 
        # so it is an input error or a keyerror 
        au = float(distances[spacecraft])
    #exceptions that can occur: 
    # one is the keyerror so the input is the error
    # one is the valueerror so the output is the error 
    except KeyError: 
        print(f"'{spacecraft}' is not in the dictionary. ")
        return
    except ValueError: 
        print(f"Can not convert '{distances[spacecraft]}' to a float ")
        return
    
    #converting into meters 
    meters = convert(au)
    print(f"{meters} m away")

def convert(au): 
    # the big number represents one AU astronomical unit
    # approx. 150 milliion km 
    return au * 149597870700


main()

