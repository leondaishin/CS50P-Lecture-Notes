# importing the site of sys by python (see the site)
import sys
# importing the random for the "n"
import random

# sys.argv list 
# there are 13 elements in the list
sys.argv = ["Lucas", "David", "Leon", "Sarah", "Melodine", "Julia", "Margareta", "Coline", "Lena", "Maria", "Alex", "Felix", "Jacob"]

#sys.argv[] is a list so taking an element of the list randomly taking a name 
# n going until 12 since 0 is the first element
n = random.randint(0, 12)

# try: 
    print("hello, my name is", sys.argv[n])

# except Indexerror: 
#     print("Too few arguments. ")