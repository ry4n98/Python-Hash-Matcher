import hashlib
import time
import math

print(hashlib.algorithms)

startingInt = 0;
currentInt = startingInt;
targetInt = 10000000;

start = time.time()
while currentInt != targetInt:
    h = hashlib.sha256()
    h.update(str(currentInt))
    # print(h.hexdigest())
    h.hexdigest()
    currentInt = currentInt + 1;
end = time.time()

executionTime = str(round(end - start, 2))
print("{:,} hashes computed within {} seconds".format(currentInt, executionTime))
