import re

with open("day03.inp", "r") as file:
    schematic = [line.strip() for line in file.readlines()]
    partnumbers = []
    gears = {}

    maxx = len(schematic[0])-1
    maxy = len(schematic)-1

    #part A
    for y, line in enumerate(schematic):
        nums = list([(m.group(), m.start(0), m.end(0)) for m in re.finditer(r"\d+", line)])

        for num, start, end in nums:
            added = False

            yx = []
            for x in range(start-1, end+1):
                for dy in (-1, 0, 1):
                    if not (dy == 0 and start <= x <=end-1):
                        if 0 <= x <= maxx and 0 <= y+dy <= maxy:
                            yx.append((y+dy, x))

            for ys, xs in yx:
                if schematic[ys][xs] != ".":
                    if not added:
                        partnumbers.append(int(num))

                    #part B
                    if schematic[ys][xs] == "*":
                        key = str(ys)+","+str(xs)
                        if key in gears.keys():
                            gears[key].append(int(num))
                        else:
                            gears[key] = [int(num)]


    print("A: ", sum(partnumbers))
    print("B: ", sum([value[0]*value[1] for key, value in gears.items() if len(value)==2]))

    exit()
    #print B
    for y, line in enumerate(schematic):
        gears = [m.start(0) for m in re.finditer(r"\*", line)]
        
        for x in gears:
            yx = []
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if not dy == dx == 0:
                        yx.append(y+dy, x+dx)
                

