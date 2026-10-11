# permutation is n fakultät 
# iteration == n fakultät == n mal n-1 fakultät 
def factorial(n): 
    # definiere 0 fakultät gleich 1 und 1 fakulät gleich 1 
    if n == 1: 
        return 1
    if n == 0: 
        return 1
    
    return n * factorial(n - 1)

result = factorial(3) 
