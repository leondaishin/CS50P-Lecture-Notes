def total(galleons, sickles, knuts): 
    return (galleons * 17 + sickles) * 29 + knuts 

coins = [100, 50, 25]
# coins[0] = 100
# coins[1] = 50 
# coins[2] = 25
print(total(*coins), "Knuts")

# coins[0], coins[1], coins[2] == *coins == galleons=100, sickles=50, knuts=25
# unpacking the list the whole list...


