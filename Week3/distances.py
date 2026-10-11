#definition or dictionary of the distance fo the spacecrafts
distances = {
    "Voyager 1": 163, 
    "Voyager 2": 136, 
    "Pioneer 10": 80, 
    "New Horizons": 58, 
    "Pioneer 11": 44
}

def main(): 
    for distance in distances.values(): 
        print(f"{distance} AU is {convert(distance)} m")




    #will return the distances of all the keys in the dictionay of distances
    #.keys for making the keys ooutput that is in the d+ictionary
    
    #for name in distances.keys(): 
        #printing every distance associated with itds name
        #depending on the name that is therepython 
   
    #    print(f"{name} is {distances[name]} AU from Earth")




#au = astronomical units in meters converting function
def convert(au): 
    return au * 149597870700




main()