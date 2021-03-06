#!/usr/local/bin/python3
import random
import os
potA = []; potB = []
s = 0
l = [potA,potB]
pair_c = input ("How many pairs are there? ")
try: pair_c = int(pair_c)
except ValueError: print("Not a digit, please try again"); exit()
while pair_c < 2:
    print("Wrong amount of pairs");
    pair_c = int(input ("How many pairs are there? "))
for item in l:
    s += 1
    for i in range (1, pair_c+1):
        inp = input ("Please input %i team for the %i pot: " % (i,s))
        while inp=="": print("Blank input, try again"); inp = input ("Please input %i team for the %i pot: " % (i,s))
        if inp != '': item.append(inp)
    random.shuffle (potA); random.shuffle (potB)
while potB:
    for counter in range (1, pair_c+1):
        pop_a = potA.pop(); random.shuffle (potA)
        pop_b = potB.pop(); random.shuffle (potB)
        print("Pair",str(counter)+ ":", str(pop_a),"-",str(pop_b)) # print("Pair", str(counter)
print("")
input("Press <Enter> to exit the app\n")
