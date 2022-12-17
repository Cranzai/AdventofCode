import re

def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def partA(beacons, occupied, coords, y):
    #sensor
    if coords[1]== y:
        occupied.add(tuple(coords[:2]))
    #beacon
    if coords[3]== y:
        beacons.add(tuple(coords[2:]))

    #1) manhattan distance = abs(xa-xb)+abs(ya-yb)
    dist = manhattan(coords[:2], coords[2:])
    #2) spawn "diamond" corresponding to distance
    #print(list(range(-dist, dist+1, 1)))
    if coords[1]-dist <= y <= coords[1]+dist:
        for x in range(coords[0]-dist, coords[0]+(dist+1), 1):
            if (manhattan([x,y], coords[:2]) <= dist):
                occupied.add((x,y))

    return beacons, occupied

def partB(beacons, occupied, coords, bounds):
    lower, upper = bounds
    dist = manhattan(coords[:2], coords[2:])

    #beacons need to be "1" outside of sensor range


    return beacons, occupied

with open("day15.inp") as file:
    occupiedA = set()
    occupiedB = set()
    beaconsA = set()
    beaconsB = set()
    bounds = [0,4000000]
    for line in file.readlines():
        coords = list(map(int, re.findall(r'-?\d+', line)))
        beaconsA, occupiedA = partA(beaconsA, occupiedA, coords, 10)
        beaconsB, occupiedB = partB(beaconsB, occupiedB, coords, bounds)

    #Part A: remove beacon coordinates
    for beacon in beaconsA:
        if beacon in occupiedA: occupiedA.remove(beacon)
    
    print("Part A: ", len(occupiedA))

    #Part B:
    #beacons within 0 <= x <= 4000000 
    #               0 <= y <= 4000000
    #tuning frequency: x*4000000+y
    lower, upper = bounds
    for x in range(lower,upper+1):
        for y in range(lower, upper+1):
            if not (x,y) in occupiedB:
                #print((x,y))
                print("Part B: ", x*4000000+y)
