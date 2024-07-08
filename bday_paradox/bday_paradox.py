# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:43:03 2024

@author: Scott
"""

# This is a simple code to simulate the birthday paradox
# it imports two data to a text file, the first of which
# is the number of match and the second is the number of
# times that a  runthrough did not generate a match

# 23 gives a probability of about 50% that a match occurs
# 57 gives about 99%

from random import randint

x = 23; # number of people
a = {}

match = False

for i in range(x):
    a[i+1] = randint(1,365)
    # generates an array of x size with random numbers between 1 and 365

for i in range(len(a)):
    for j in range(len(a)):
        if a[j+1] == a[i+1] and (j+1) != (i+1):
            match = True
            # array elements checks every element if a match occurs except itself
            
try: # creates a file if there isn't one yet
    file = open("D:/Programming/bday.txt","r")
    f = file.read()
    mat, nop = f.split(' ')     # stores the current value from file to code

except FileNotFoundError:
    file = open("D:/Programming/bday.txt","w")
    mat = 0
    nop = 0

file.close()

if match == True:
    matf = int(mat) + 1
    nopf = int(nop)

elif match == False:
    nopf = int(nop) + 1
    matf = int(mat)

with open("D:/Programming/bday.txt","w") as file:
    file.write(str(matf) + " " + str(nopf))

# the code two values is separated by a column