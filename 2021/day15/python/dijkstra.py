import sys
from collections import defaultdict
from collections import deque
import math
import copy

def main(inputFile):
    #tile = riskTile(inputFile)
    #path = tile.dijkstra((0, 0), (tile.x, tile.y))

    #pathSum = 0
    #for point in path:
    #    pathSum += tile.map0[point]

    #print(pathSum)

    mapB = riskMap(inputFile)
    mapB.extend(5)
    path = mapB.dijkstra((0, 0), (mapB.x, mapB.y))
    print(path)

    pathSum = 0
    for point in path:
        pathSum += mapB.mapSave[point]

    print(pathSum)

class riskTile:
    def __init__(self, mapFile):
        #read in as nested list, then throw into numpy array
        with open(mapFile, 'r') as f:
            self.map = {(x, y): float(num) for (y, line) in enumerate(f.read().split("\n")) for (x, num) in enumerate(line)}

        self.map0 = copy.deepcopy(self.map)

        self.x = max(map(lambda x: x[0], self.map.keys()))
        self.y = max(map(lambda y: y[1], self.map.keys()))

    def dijkstra(self, start, goal):
        dist = defaultdict(float)
        prev = {}
        for key in self.map.keys():
            dist[key] = float('inf')

        dist[start] = 0

        while self.map:
            #get vertex in Q with min dist[u]
            minimum = list(self.map.keys())[0]
            for key in self.map.keys():
                if dist[key] < dist[minimum]:
                    minimum = key

            point = minimum
            x, y = point
            del self.map[point]

            allNeighbours = [(x+dx, y+dy) for dx, dy in [(0, 1),  (-1, 0), (1, 0), (0, -1)]]
            validNeighbours = [neighbour for neighbour in allNeighbours if neighbour in self.map]

            for neighbour in validNeighbours:
                alt = dist[point] + self.map[neighbour]
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    prev[neighbour] = point

        path = deque()
        if goal in prev.keys():
            while goal in prev.keys():
                path.appendleft(goal)
                goal = prev[goal]
        elif goal == start:
            path.appendleft(start)

        return path

class riskMap(riskTile):
    def extend(self, factor):
        newMap = {}
        for n in range(0, factor):
            for (x, y), v in self.map0.items():
                newMap[((self.x+1)*n+x, y)] = (v+n)-9 if (v + n) >= 10 else (v+n)

        for n in range(0, factor):
            for (x, y), v in self.map0.items():
                newMap[(x, (y_max+1)*n+y)]] = (v+n)-9 if (v + n) >= 10 else (v+n)

        self.map = newMap
        self.map0 = newMap
        self.x = max(map(lambda x: x[0], self.map.keys()))
        self.y = max(map(lambda y: y[1], self.map.keys()))


if __name__ == "__main__":
    #only pass through the first argument which should be the inputfile
    main(sys.argv[1])