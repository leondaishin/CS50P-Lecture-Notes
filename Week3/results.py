#  store the results of the race for mario kart 
#list of the results 
results = ["Mario", "Luigi", "Yoshi", "Daisy"]




#append means ADDING new stuff to the list on top
results.append("Princess")
results.append("Toad")



#inserting the element of the list into some reihenfolge
results.append("Coopa")
results.remove("Coopa")
#insert(number, element) the number is the reihenfolge 
#it starts at 0, 1, 2, ...
results.insert(0, "Coopa")


#adding a list itself to another list 
results.append(["Bowser", "DK Junior"])
results.remove(["Bowser", "DK Junior"])
results.extend(["Bowser", "DK Junior"])




#reversing the reihenfolge so goign from 0,1,2,...,n to n, n-1, ... , 3, 2, 1
results.reverse()


print(results)