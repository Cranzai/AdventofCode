#code inspired by https://github.com/maksverver/AdventOfCode/blob/master/2021/15.py
import sys
from collections import deque
from heapq import heappush, heappop


class riskTile:
    def __init__(self, mapFile):
        with open(mapFile, 'r') as file:
            self.danger = [[int(val) for val in line.strip("\n")] for line in file]

        self.H = len(self.danger)
        self.W = len(self.danger[0])

    def dijkstra(self):
        todo = []
        minDist = [[float('inf')]*self.W for _ in range(self.H)]

        def TryPush(d, r, c):
            if minDist[r][c] > d:
                minDist[r][c] = d
                heappush(todo, (d, r, c))

        TryPush(0, 0, 0)

        while todo:
            d, r, c = heappop(todo)
            if minDist[r][c] == d:
                #neighbours....
                for rr, cc, in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= rr < self.H and 0 <= cc < self.W:
                        TryPush(d + self.danger[rr][cc], rr, cc)

            if r == self.H -1 and c == self.W -1:
                return d

class riskMap(riskTile):
    def extend(self, factor):
        W = self.W
        H = self.H
        dangerNew = [[(self.danger[r % H][c % W] - 1 + (r // H) + (c // W)) % 9 + 1 for c in range(factor*W)] for r in range(factor*H)]
        
        self.danger = dangerNew
        self.H = len(self.danger)
        self.W = len(self.danger[0])

if __name__ == "__main__":
    inputfile = sys.argv[1]
    mapA = riskTile(inputfile)
    print(mapA.dijkstra())

    mapB = riskMap(inputfile)
    mapB.extend(5)
    print(mapB.dijkstra())