import cowsay
import sys

# cowsay is a list of user friendly things we can use
# its sort of like plugins 
if len(sys.argv) == 2: 
    cowsay.trex("hello, " + sys.argv[1])
    cowsay.cow("hello, " + sys.argv[1]) 