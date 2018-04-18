#!/usr/bin/python

import time
import math

import hash

targetHash = "986bd07786ae5e4b4800df7eb16a710de8b8dc2c3bfb29794d97941fc30cb7f9"

startingInt = 0;
targetInt = 1000000;

start = time.time() # Start execution timer

currentInt = startingInt;
while currentInt != targetInt:
    currentHash = hash.generate(currentInt)
    if (currentHash == targetHash):
        print("Match found! Integer value: {:,}".format(currentInt))
        break
    currentInt = currentInt + 1;

end = time.time() # Stop execution timer
executionTime = str(round(end - start, 2))

print("{:,} hashes computed within {} seconds.".format(currentInt, executionTime))
