import re

with open("day03.inp", "r") as file:
    schematic = [line.strip() for line in file.readlines()]
    partnumbers = []

    maxx = len(schematic[0])-1
    maxy = len(schematic)-1

    for y, line in enumerate(schematic):
        nums = list([(m.group(), m.start(0), m.end(0)) for m in re.finditer(r"\d+", line)])

        for num, start, end in nums:
            yx = []
            for x in range(start-1, end+1):
                for dy in (-1, 0, 1):
                    if not (dy == 0 and start <= x <=end-1):
                        if 0 <= x <= maxx and 0 <= y+dy <= maxy:
                            yx.append((y+dy, x))

            for ys, xs in yx:
                if schematic[ys][xs] != "." and not int(num) in partnumbers:
                    partnumbers.append(int(num))

    print(sum(partnumbers))