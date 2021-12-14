#naive implementation is way to slow to solve this
#it won't ever reach step 40 realistically

#hence use an approach in which you moniter all pairs.

import sys
from collections import defaultdict, Counter
import time

def main(inputFile):
    polymerA = polymer(inputFile)
    print(polymerA.polymerize(10))

    polymerB = polymer(inputFile)
    print(polymerB.polymerize(40))

class polymer:
    def __init__(self, recipe):
        with open(recipe, "r") as fileIn:
            self.pairs = defaultdict(int)
            self.singles = defaultdict(int)
            self.react = {}

            lines = fileIn.readlines()
            #read polymer from first line
            polymer = lines[0].rstrip("\n")

            self.singles |= Counter(polymer)
            for i in range(1, len(polymer)):
                #use polymer as string, list is not hashable
                self.pairs[polymer[i-1:i+1]] += 1 

            #save rules/reactions
            for line in lines[2:]:
                pair, insert = line.rstrip("\n").split(" -> ")
                self.react[pair]=insert

    def polymerize(self, steps):
        self.startTime = time.time()

        for i in range(steps):
            newpairs = defaultdict(int)
            for pair, num in self.pairs.items():
                extra = self.react[pair]
                newpairs[pair[0]+extra] += num
                newpairs[extra+pair[1]] += num
                self.singles[extra] += num
            self.pairs = newpairs.copy()

        values = sorted(self.singles.values())
        return values[-1]-values[0]

if __name__ == "__main__":
    #only pass through the first argument which should be the inputfile
    main(sys.argv[1])