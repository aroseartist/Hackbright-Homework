"""This calculator takes the users input and gives an output.

    The input is split into tokens, which then used as arguments 
    into the arithmetic functions"""

from arithmetic-calc2 import *

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ") #we have tokenized on the spaces
    if len(tokens) == 2:
        tokens[1] = int(tokens[1]) #we make the first index an integer
    if len(tokens) == 3:
        tokens[1] = int(tokens[1]) #we make the first index an integer
        tokens[2] = int(tokens[2]) #we make the second index an integer
    if tokens[0] == "q": #an input of q will break the loop
        break
    elif tokens[0] == "+":
        print add(tokens[1],tokens[2])
    elif tokens[0] == "-":
        print subtract(tokens[1],tokens[2])
    elif tokens[0] == "*":
        print multiply(tokens[1],tokens[2])
    elif tokens[0] == "/": #we can utilize 'is' on a string with one index
        print divide(tokens[1],tokens[2])
    elif tokens[0] == "square": #we must utilize '==' on a string with >1 index
        print square(tokens[1])
    elif tokens[0] == "cube":
        print cube(tokens[1])
    elif tokens[0] == "^":
        print power(tokens[1],tokens[2])
    elif tokens[0] == "power":
        print power(tokens[1],tokens[2])
    elif tokens[0] == "pow":
        print power(tokens[1],tokens[2])
    elif tokens[0] == "**":
        print power(tokens[1],tokens[2])
    elif tokens[0] == "%":
        print mod(tokens[1],tokens[2])
    elif tokens[0] == "mod":
        print mod(tokens[1],tokens[2])
    else:
        break

