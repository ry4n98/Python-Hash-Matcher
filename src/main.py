#!/usr/bin/python

import time
import math

import args
import hasher

arguments = args.get()

targetHash = str(arguments['--target'])
startingInt = int(arguments['--start'])
targetInt = int(arguments['--end'])

start = time.time() # Start execution timer

currentInt = startingInt;
while currentInt != targetInt:
    currentHash = hasher.generate(currentInt)
    if (currentHash == targetHash):
        print("Match found! Integer value: {:,}".format(currentInt))
        break
    currentInt = currentInt + 1;

end = time.time() # Stop execution timer
executionTime = str(round(end - start, 2))

print("{:,} hashes computed within {} seconds.".format((currentInt - startingInt), executionTime))
