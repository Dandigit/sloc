#!/usr/bin/python

import os
import sys

class Flags():
    def __init__(self, root, types):
        self.root = root
        self.types = types

def getFlags():
    root = "./"
    types = []
    
    index = 1
    while index < len(sys.argv):
        arg = sys.argv[index]

        if arg == "-d" and len(sys.argv) > index + 1:
            root = sys.argv[index + 1]
            index += 1
        else:
            types.append(arg)

        index += 1

    sys.stdout.write("Searching for types: ")
    for type in types:
        sys.stdout.write(type + " ")

    print("in directory tree %s."%(root))

    return Flags(root, types)

def countLinesInFile(fileName):
    i = -1
    with open(fileName) as file:
        for i, l in enumerate(file):
            pass
    print("Counted %d lines in file: %s"%(i+1, fileName))
    return i + 1

def getTotalLines(flags):
    def isCounted(name):
        for type in flags.types:
	    if name.endswith("." + type) or type == "all": return True
        return False

    totalLines = 0
    for root, dirs, files in os.walk(flags.root):
        for file in files:
            if isCounted(file):
                totalLines += countLinesInFile(os.path.join(root, file))

    return totalLines

totalLines = getTotalLines(getFlags())
print("\nTOTAL: Counted %d lines of code."%(totalLines))
