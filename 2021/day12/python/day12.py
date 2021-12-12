import sys, getopt
import numpy as np
from collections import defaultdict
import copy

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

    thisCave = caveSystem(inputFile)
    thisCave.findPaths(False)
    thisCave.findPaths(True)


class caveSystem:
    def __init__(self, file):
        #use of defaultdict makes for easy appending even when key is not yet present.
        self.caves = defaultdict(list)

        with open(file, "r") as input:
            for line in input:
                a, b = line.rstrip("\n").split("-")
                pairs = [[a,b],[b,a]]

                for one, two in pairs:
                    if one != "end" and two != "start":
                        self.caves[one].append(two)

    def pathfinder(self, point, stop, visited, exception):
        exceptionNew = copy.deepcopy(exception)
        visitedNew = visited.copy()
        if point == stop:
            self.paths += 1
            return

        if point.islower():
            visitedNew.append(point)

        for connected in self.caves[point]:
            if not connected in visitedNew:
                self.pathfinder(connected, stop, visitedNew, exception)

            if connected in visitedNew and exception:
                exceptionNew = False
                self.pathfinder(connected, stop, visitedNew, exceptionNew)

    def findPaths(self, exception):
        self.paths = 0
        self.pathfinder('start', 'end', [], exception)
        print(self.paths)

if __name__ == "__main__":
    main(sys.argv[1:])