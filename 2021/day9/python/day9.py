import sys, getopt
import numpy as np

def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:')
    except getopt.GetoptError:
        print('test.py -i <inputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt == '-i':
            inputFile = arg

    day9 = heightMap(inputFile)
    print("A: ", day9.sumValleyRisk())
    print("B: ", np.prod(day9.findBassins()))

class heightMap:
    def __init__(self,input):
        self.valleys=[]
        #first determine dimensinos of array prior to allocation
        with open(input, "r") as fileIn:
            self.mapX = len(fileIn.readline().rstrip("\n"))
            #plus one because we already read the first line.
            self.mapY = sum(1 for line in fileIn) + 1

        #map as numpy array (empty for now)
        #note order of y, x
        self.map = np.empty([self.mapY, self.mapX])

        #read data onto array
        with open(input, "r") as fileIn:
            for y in range(self.mapY):
                line = list(map(int, list(fileIn.readline().rstrip("\n"))))
                for x, val in zip(range(self.mapX), line):
                    self.map[y, x] = val

    def isValley(self, x, y):
    	#AoC assignment only works with valleys of 1 unit wide.
    	#hence self.map[y, pos] <= self.map[y,x]
        for pos in [x-1, x+1]:
            # "<" to compensate for indexing
            if pos >= 0 and pos < (self.mapX):
                if self.map[y, pos] <= self.map[y,x]: return False

        for pos in [y-1, y+1]:
            if pos >= 0 and pos < (self.mapY):
                if self.map[pos, x] <= self.map[y,x]: return False

        return True

    def findValleys(self):
        self.valleys=[]
        for y in range(self.mapY):
            for x in range(self.mapX):
                if self.isValley(x, y): self.valleys.append([x,y])

        return self.valleys

    def sumValleyRisk(self):
        if not self.valleys:
           self.findValleys()

        riskSum = 0
        for valley in self.valleys:
            riskSum += self.map[valley[1],valley[0]] + 1

        return riskSum

    def bassinInspect(self,x,y):
        newPoints = []
        for pos in [x-1, x+1]:
            # "<" to compensate for indexing
            if pos >= 0 and pos < (self.mapX):
                if self.map[y, pos] >= self.map[y,x] and self.map[y,pos] != 9:
                    newPoints.append([pos,y])

        for pos in [y-1, y+1]:
            if pos >= 0 and pos < (self.mapY):
                if self.map[pos, x] >= self.map[y,x] and self.map[pos,x] != 9: 
                    newPoints.append([x,pos])

        return newPoints

    def bassinSize(self, valley):
        bassin = [valley]
        elementsAdded = 1

        #unfortunate while true loop
        while True:
            #save the last element before adding the newpoints
            #reduces number of elements in each consecutive loop.
            if elementsAdded == 0: break
            prevLastElement = len(bassin) - elementsAdded
            elementsAdded = 0
            for pos in bassin[prevLastElement:]:
                newPoints = self.bassinInspect(pos[0],pos[1])
                for point in newPoints:
                    if not point in bassin:
                        bassin.append(point)
                        elementsAdded +=1

        return len(bassin)

    def findBassins(self):
        self.bassinSizes = []
        for valley in self.valleys:
            self.bassinSizes.append(self.bassinSize(valley))

        #return three highest values
        return sorted(self.bassinSizes)[-3:]


if __name__ == "__main__":
    main(sys.argv[1:])