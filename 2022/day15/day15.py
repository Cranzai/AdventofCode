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

def outsidediamond(sensor, beacon):
    x, y = sensor
    dist = manhattan(sensor, beacon)

    corners = list()
    #top
    corners.append((x, y+(dist+1)))
    #right
    corners.append((x+(dist+1), y))
    #down
    corners.append((x, y-(dist+1)))
    #left
    corners.append((x-(dist+1), y))
    #add another top for easier looping
    corners.append((x, y+(dist+1)))

    diags = list()
    for a, b in zip(corners, corners[1:]):
        xr = list(range(min(a[0],b[0]), max(a[0],b[0])+1))
        yr = list(range(min(a[1],b[1]), max(a[1],b[1])+1))
        diags.extend([(x,y) for x, y in zip(xr, yr)])

    return set(diags)

def partB(sensors, beacons, bounds):
    chances = set()
    
    #get set of diagonal intersects
    for sensorA, beaconA in zip(sensors, beacons):
        for sensorB, beaconB in zip(sensors, beacons):
            if sensorA != sensorB:
                ax, ay = sensorA
                bx, by = sensorB
                distA = manhattan(sensorA, beaconA)
                distB = manhattan(sensorB, beaconB)

                diagsA = outsidediamond(sensorA, beaconA)
                diagsB = outsidediamond(sensorB, beaconB)

                overlap = diagsA.intersection(diagsB)
                chances = chances.union(overlap)

    return chances

with open("day15demo.inp") as file:
    sensors = []
    beacons = []

    for line in file.readlines():
        coords = list(map(int, re.findall(r'-?\d+', line)))
        sensors.append(coords[:2])
        beacons.append(coords[2:])

    print("Part B: ", partB(sensors, beacons, [0,20]))
    #print("Part A: ", partA(sensors, beacons, 2000000))
    #print("Part B: ", partB(sensors, beacons, [0,4000000]))
