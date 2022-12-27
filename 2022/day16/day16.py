import re
import math

pattern = re.compile('^Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z]{2}(, [A-Z]{2})*)\n$')

def findpaths(FW, flowing, start, n, time):
    if n == 0:
        return [[start]]
    elif time < 0:
        return [[start]]

    paths=[]

    for valve in flowing:
        for path in findpaths(FW, flowing, valve, n-1, (time-FW[(start, valve)])):
            if start not in path:
                paths.append([start]+path)

    return paths

with open("day16.inp") as file:
    valves = dict()
    for line in file.readlines():
        source, rate, connected, _ = pattern.match(line).groups()
        valves[source]=(int(rate), tuple(connected.split(", ")))

    #attempt at floyd warshall
    FW = dict()
    #initialize with only diagonal at 0 
    #off diagonal at inf
    #direct connections at distance of 1
    for origin in valves.keys():
        for destination in valves.keys():
            rate, connected = valves[origin]
            if origin == destination:
                FW[(origin, destination)] = 0
            elif destination in connected:
                FW[(origin, destination)] = 1
            else:
                FW[(origin, destination)] = float("inf")

    #further update distances
    #https://favtutor.com/blogs/floyd-warshall-algorithm
    for a in valves.keys():
        for b in valves.keys():
            for c in valves.keys():
                FW[(b,c)]=min(FW[(b,c)], FW[(b,a)] + FW[(a,c)])

    #print matrix
    #width=int(math.sqrt(len(FW.keys())))
    #for i in range(0, len(FW.keys()), width):
    #    row = [FW[key] for key in list(FW.keys())[i:i+width]]
    #    print(" ".join(map(str, row)))

    flowing = [valve for valve, (rate, _) in valves.items() if rate != 0]
    paths = findpaths(FW, flowing, "AA", len(flowing), 30)
    maxreleased = 0

    for path in paths:
        time = 30
        opened = []
        released = 0
        for one, two in zip(path, path[1:]):
            dist = FW[(one,two)] + 1
            if dist <= time:
                time -= dist
                rate, _ = valves[two]
                released += rate*(time)
            else:
                break

        if released > maxreleased:
            maxreleased = released

    print(maxreleased)
