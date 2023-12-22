#While loops are know as indefinite or conditional loops.
#THey will keep ite rating until certain conditions are met


"""
Syntax:

while experssion:
    statements
"""

count = 0

while count < 9:
    print("Number: ", count)
    count+=1
print("The end of count") 



import random
print(random.random())#It return a random num between 0 and 1 in float



#A little guessing game

import random

n = 20

to_be_gussed = int(n * random.random()) + 1

guess = 0

while guess != to_be_gussed:
    guess = int(input("New number: "))
    if guess > 0:
       if guess > to_be_gussed:
           print("Number is too large")
       elif guess < to_be_gussed: 
           print("Number is too small")
    else:
        print("sorry that you are giving up")
else:
    print("congratulation, you made it!")              

    