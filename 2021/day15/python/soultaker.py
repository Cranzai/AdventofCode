#code courtesy of https://github.com/maksverver/AdventOfCode/blob/master/2021/15.py
from heapq import heappush, heappop
import sys

def main(inputfile):
    with open(inputfile, 'r') as file:
        danger = [[int(c) for c in line.strip()] for line in file]

    H = len(danger)
    W = len(danger[0])

    print(Search(danger, H, W))

    danger2 = [[(danger[r % H][c % W] - 1 + (r // H) + (c // W)) % 9 + 1 for c in range(5*W)] for r in range(5*H)]

    print(Search(danger2, 5*H, 5*W))

def Search(danger, H, W):
    '''Dijkstra's algorithm'''
    todo = []
    min_dist = [[float('inf')]*W for _ in range(H)]

    def TryPush(d, r, c):
        if min_dist[r][c] > d:
            min_dist[r][c] = d
            heappush(todo, (d, r, c))

    TryPush(0, 0, 0)
    while todo:
        d, r, c = heappop(todo)
        if min_dist[r][c] == d:
            for rr, cc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= rr < H and 0 <= cc < W:
                    TryPush(d + danger[rr][cc], rr, cc)
        if r == H - 1 and c == W - 1:
            return d

if __name__ == "__main__":
    inputfile = sys.argv[1]
    main(inputfile)