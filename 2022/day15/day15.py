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

    return len(occupied)

def corners(sensor, beacon):
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
    
    return corners

def covered(sensors, beacons, chance):
    for sensor, beacon in zip(sensors, beacons):
        if manhattan(sensor, chance) <= manhattan(sensor, beacon):
            return True

    return False

def partB(sensors, beacons, bounds):
    candidates = set()
    
    #diagonals for each sensor
    diags1 = list()
    diags2 = list()
    for sensor, beacon in zip(sensors, beacons):
        top, right, bottom, left = corners(sensor, beacon)
        diags1.append((bottom, right))
        diags1.append((left, top))
        diags2.append((left, bottom))
        diags2.append((top, right))

    for a,b in diags1:
        for c,d in diags2:
            # calculate intersection point via x-axis intersection
            d1x1, d1y1 = a
            d1x2, d1y2 = b
            d2x1, d2y1 = c
            d2x2, d2y2 = d

            x1 = (d1x1 - d1y1)
            x2 = (d2x1 + d2y1)
            d = x2 - x1
            if d % 2 != 0: continue  # not on integer point
            y = d // 2
            x = x1 + y
            assert x == x2 - y
            if (max(bounds[0], d1x1, d2x1) <= x <= min(bounds[1], d1x2, d2x2) and
                max(bounds[0], d1y1, d2y2) <= y <= min(bounds[1], d1y2, d2y1)):
                candidates.add((x, y))
    
    # Find the only candidate that is not covered by any sensors:
    answer, =(4000000 * x + y for x, y in candidates if not covered(sensors, beacons, (x,y)))
    return answer

with open("day15.inp") as file:
    sensors = []
    beacons = []

    for line in file.readlines():
        coords = list(map(int, re.findall(r'-?\d+', line)))
        sensors.append(coords[:2])
        beacons.append(coords[2:])

    #print("Part B: ", partB(sensors, beacons, [0,20]))
    #print("Part A: ", partA(sensors, beacons, 2000000))
    print("Part B: ", partB(sensors, beacons, [0,4000000]))
