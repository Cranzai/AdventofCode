import re

def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def partA(sensors, beacons, y):
    occupied = set()

    for sensor, beacon in zip(sensors, beacons):
        if sensor[1] == y:
            occupied.add(tuple(sensor))

        dist = manhattan(sensor, beacon)
        if sensor[1]-dist <= y <= sensor[1]+dist:
            for x in range(sensor[0]-dist, sensor[0]+(dist+1),1):
                if (manhattan(sensor, [x,y]) <= dist) and ([x,y] != beacon):
                    occupied.add((x,y))

    #for beacon in beacons:
    #    if beacon[1]==y:
    #        if tuple(beacon) in occupied:
    #            occupied.remove(tuple(beacon))

    return len(occupied)

with open("day15demo.inp") as file:
    sensors = []
    beacons = []

    for line in file.readlines():
        coords = list(map(int, re.findall(r'-?\d+', line)))
        sensors.append(coords[:2])
        beacons.append(coords[2:])

    print("Part A: ", partA(sensors, beacons, 10))
