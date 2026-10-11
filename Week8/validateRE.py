# importing the "re" library
import re 

email = input("What is your email? ").strip()

# THINGS FOR re.search(...)
# . = any character except a newline 
# * = 0 or more repetition 
# + = 1 or more repetition
# ? = 0 or 1 repetition 
# {m} = m repetitions
# {m, n} = m-n repetitions
# ^ matches the start of the string
# $ matches the end of the string
# [] = set of characters (A Menge)
# [^] = complementing the set (A complementäre Menge)

# BACKSLASH THINGS
# \d decimal digit 
# \D not a decimal digit
# \s whitespace characters 
# \S not Whitespace characters 
# \w word character (contains letters, numebrs and _)
# \W not a word character


# REGULAR EXPRESSION LIBRARY VARIABLES 
# re.IGNORECASE = ignore the case of the input 
# re.MULTILINE = paragraph ex. recognize characters with sentences in a row u know 
# re.DOTALL = All dots
# re.match()
# re.fullmatch()

# this only looks for @ and says valid 
# .+ == ..* (1 ore more characters)
# .*@.* == 0 or more characters then @ and then 0 or more characters
# \ making the . not any charater but literally end with the "."
# r is the raw string that makes the \.com make sense 
# it is kind of similar to the f string
# instead of the . (any character) write the list of characters that are available threw []

# r"^[^@]+@[^@]+\.com$" 
# [abcdefghijklmnopqrstuvwxyz] = [a-z]
# \w (word) (the list of characters are in [a-zA-Z0-9...])
if re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.(com|edu|gov|net|org|de|fr|nl|jp)$", email): 
    print("Valid")
else: 
    print("Invalid")
    