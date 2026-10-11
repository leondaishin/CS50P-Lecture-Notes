def main():
    #each colomn of the dictionary like this
    #dictionary in {} and list in []:
    
    spacecraft = {
        "name": "Voyager 1",
        "distance": 163
    }

    #updating new definitions to the dictionary. 
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    #here is another update to the information about the voyager 1:
    spacecraft.update({"distance": "Unknown", "orbit": "Jupiter"})
    #now that the distance is updated into 0.01 it is no longer 163
    print(create_report(spacecraft))


#.get lets us define distance/name when we also dont have it -> then it will output unknown as an answer: 

def create_report(spacecraft): 
    return f"""
    ======== REPORT ========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ========================
    """

main()


