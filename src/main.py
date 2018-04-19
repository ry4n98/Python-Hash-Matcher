#!/usr/bin/python

import time
import math
from progress.bar import Bar

import args
import hasher
import file_handler

arguments = args.get()
values = file_handler.get_file_contents()

targetHash = str(arguments['--target']).lower()

bar = Bar('Computing hashes', max=len(values), suffix='%(percent).2f%% - ETA %(eta)ds')

print("\n{:,} values contained within file(s)\n".format(len(values)))
computed_counter = 0
match_found = 0

start = time.time() # Start execution timer
for value in values:
    bar.next()
    hash_value = hasher.generate(value)
    computed_counter = computed_counter + 1
    if (hash_value == targetHash):
        match_found = 1
        bar.finish()
        print("Match found!\n")
        print("-- Hash --\n{}".format(targetHash))
        print("-- Value --\n{}\n".format(value))
        break
end = time.time() # Stop execution timer

if match_found == 0:
    print("\nNo matches found.")

executionTime = str(round(end - start, 2))
print("{:,} hashes computed within {} seconds.".format(computed_counter, executionTime))
