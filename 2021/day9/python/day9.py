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
    print(day9.sumValleyRisk())

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
        for pos in [x-1, x+1]:
            # "<" to compensate for indexing
            if pos >= 0 and pos < (self.mapX):
                if self.map[y, pos] < self.map[y,x]: return False

        for pos in [y-1, y+1]:
            if pos >= 0 and pos < (self.mapY):
                if self.map[pos, x] < self.map[y,x]: return False

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
            print(valley, self.map[valley[1],valley[0]])
            riskSum += self.map[valley[1],valley[0]] + 1

        return riskSum


if __name__ == "__main__":
    main(sys.argv[1:])