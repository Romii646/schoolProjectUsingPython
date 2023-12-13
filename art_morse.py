#!/usr/bin/env python3

"""Morse Code"""

__author__ = 'Aaron Cortina'
__date__ = '01/25/2023'

morse = input("? ")
print()

# declared variables
counter = 0
symbole = ""
end = "exit"

# a sentinal while loop
while morse != end:
    if morse == "....":
        symbole += '@'
    elif morse == "...-":
        symbole += '>'
    elif morse == "..-.":
        symbole += '<'
    elif morse == "..--":
        symbole += '-'
    elif morse == ".-..":
        symbole += '('
    elif morse == ".-.-":
        symbole += ')'
    elif morse == ".--.":
        symbole += '^'
    elif morse == ".---":
        symbole += '_'
    elif morse == "-...":
        symbole += '\''
    elif morse == "-..-":
        symbole += '\"'
    elif morse == "-.-.":
        symbole += '|'
    elif morse == "-.--":
        symbole += '='
    else:
        print("invalid code")
        print()
    morse = input("? ")
    print()
    counter += 1
# end of while loop

# print function to ask user for copies to used in a for loop
copies = int(input("Copies? "))
print()

# while loop used if copies less than 0 or greater than 15
while copies <= 0 or copies >= 15:
    copies = int(input("Copies? "))
    print()

# variable used to concatenate in the for loop with symbols
tab = ""

for _i in range(0, copies):
    print(tab + symbole)
    tab += ' '
