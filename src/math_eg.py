#This is an example to include math functions

import math

#this is a function
def pythagoras(a,b):
    return math.sqrt(a*a + b*b)

#define some variables
side_a = 3.0 
side_b = 4.0

#define a string
OutputString = "A right-angle triangle with sides {} and {}".format(side_a, side_b)
print(OutputString)

hype = pythagoras(side_a, side_b)

print("Has an hypotenuse of {}".format(hype)) 

