import sys

args = sys.argv
args.pop(0)

possibleArgs = ["--target", "--end", "--start"]

def get():
    argumentValues = {}
    x = 0
    for arg in args:
        if arg in possibleArgs:
            argumentValues[arg] = args[x + 1]
        x = x + 1
    return argumentValues
