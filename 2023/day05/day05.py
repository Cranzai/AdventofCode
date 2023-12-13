def mapRange(ranges, map):
    newRanges = []

    for entry in map[1:]:
        dest, source, length = (int(val) for val in entry.split())

        count = len(ranges)
        for _ in range(count):
            first, last = ranges.pop(0)

            if source <= first and last <= source+length:
                newRanges.append((dest+first-source, dest+last-source))

            elif source <= first <= source+length:
                newRanges.append((dest+first-source, dest+length-1))
                ranges.append((source+length, last))

            elif source <= last <= source+length:
                newRanges.append((dest, dest+last-source))
                ranges.append((first, source))
            else:
                ranges.append((first, last))

    newRanges.extend(ranges)
    
    return newRanges

#read input
almanac = open("day05.inp", "r")
maps = almanac.read().split("\n\n")

#parse a little bit
seeds = list(map(int, maps.pop(0).split(": ")[1].split()))
maps = [map.split("\n") for map in maps]

#part A
ranges = [(seed, seed) for seed in seeds]
for map in maps:
    ranges = mapRange(ranges, map)

print("A: ", min(min(ranges)))

#part B
ranges = [(start, start+length-1) for start, length in list(zip(seeds[::2], seeds[1::2]))]

for map in maps:
    ranges = mapRange(ranges, map)

print("B: ", min(min(ranges)))