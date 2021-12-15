import sys
import numpy as np
from collections import defaultdict
from collections import deque
import copy

def main(inputFile):
    sys.setrecursionlimit(25)
    mapA = riskMap(inputFile)
    mapA.pathfinder((0,0), (mapA.mapx, mapA.mapy))
    print(mapA.paths)
    

class riskMap:
    def __init__(self, mapFile):
        #read in as nested list, then throw into numpy array
        self.map = []
        with open(mapFile, 'r') as file:
            self.map = [list(map(int, line.rstrip("\n"))) for line in file]

        self.map = np.array(self.map)
        self.mapx, self.mapy = self.map.shape

        self.paths = []

    def pathfinder(self, start, finish):
        myVisited = set()
        myVisited.add(start)
        myPath = []
        myPath.append(start)
        self.finish = finish

        self.recursiveFind(myPath, myVisited)

    #as it stands now this nicely prints all nodes in the correct order....
    def recursiveFind(self, path, visited):
        if self.paths:
            return

        newPath = copy.deepcopy(path)
        newVisited = copy.deepcopy(visited)
        point = newPath [-1]

        neighbours = [neighbour for neighbour in self.neighbours(point) if not neighbour in visited]

        #neighbourdict contains the coordinates of neighbours and their value.
        neighbourdict = defaultdict(int)
        for x, y in neighbours:
            neighbourdict[(x,y)]=self.map[x][y]

        for position, value in sorted(neighbourdict.items(),key=lambda x: x[1]):
            print(position)
            if position == self.finish:
                print(newPath)
                self.paths.append(newPath)
                return

            newPath.append(position)
            #add all current branches to visited...
            for neighbour in neighbours:
                newVisited.add(neighbour)

            self.recursiveFind(newPath, newVisited)

    def lowpath(self):
        sums = []
        for path in self.paths:
            pathsum = 0
            for x, y in path:
                pathsum += self.map[x,y]

            sums.append(pathsum)

        return sums
        
    def neighbours(self, point):
        x, y = point
        allNeighbours = [(x+dx, y+dy) for dx, dy in [(0, 1),  (-1, 0), (1, 0), (0, -1)]]
        validNeighbours = [(x,y) for x, y in allNeighbours if 0 <= x < self.mapx and 0 <= y < self.mapy]
        return validNeighbours

if __name__ == "__main__":
    #only pass through the first argument which should be the inputfile
    main(sys.argv[1])