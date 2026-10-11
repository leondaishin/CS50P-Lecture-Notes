import sys

# Check for errors
# telling if the length of the words after rightlengthname.py is too short print...
if len(sys.argv) < 2: 
    print("too few arguments. ")

# telling print if the words are too long 
elif len(sys.argv) > 2: 
    print("Too many arguments. ")

# if perfectly 2, then print the right output. 
else: 
    print("hello, my name is", sys.argv[1])

# So the length of sys.argv is already 1 because by typing python of rightlengthname.py that will be one so by adding Leon will be 2 so good



# for exiting use this 
# if len(sys.argv) < 2: 
    # sys.exit("too few arguments. ")
# elif len(sys.argv) > 2: 
    # sys.exit("too many arguments. ")
# print("hello, my name is", sys.argv[1])



# import sys
# if len(sys.argv) < 2: 
    # sys.exit("Too few arguments. ")
# for arg in sys.argv[1:]:([a, b] starting from element a to b or u can write 1: to write 2nd element to last element) 
    #print("hello, my name is", arg)


