import sys
from collections import Counter
import time

def main(inputFile):
        polymerA = polymer(inputFile)
        polymerA.polymerize(10)
        print(polymerA.characterize())

        polymerB = polymer(inputFile)
        polymerB.polymerize(40)
        print(polymerB.characterize())

class polymer:
    def __init__(self, recipe):
        with open(recipe, "r") as fileIn:
            lines = fileIn.readlines()
            #read polymer from first line
            self.polymer = list(lines[0].rstrip("\n"))

            self.react = {}
            for line in lines[2:]:
                pair, insert = line.rstrip("\n").split(" -> ")
                self.react[pair]=insert

    def polymerize(self, steps):
        self.startTime = time.time()
        for i in range(steps):
            print(i, " : at ", time.time()-self.startTime)
            stepSites = {}

            for site, x in enumerate(self.polymer[:-1]):
                pair = x+self.polymer[site+1]
                try:
                    stepSites[site] = self.react[pair]
                except:
                    pass

            polymerNew = []
            for i in range(len(self.polymer)):
                polymerNew.append(self.polymer[i])
                try:
                    polymerNew.append(stepSites[i])
                except:
                    pass

            self.polymer = polymerNew


    def characterize(self):
        composition = Counter(self.polymer)
        maxComponent = max(composition, key = composition.get)
        minComponent = min(composition, key = composition.get)

        return composition[maxComponent]-composition[minComponent]

if __name__ == "__main__":
    #only pass through the first argument which should be the inputfile
    main(sys.argv[1])