import re

with open("day4.inp") as input:
    countA = 0
    countB = 0
    for line in input.readlines():
        lowerOne, upperOne, lowerTwo, upperTwo = map(int, re.split(",|-", line.strip()))
        overlap = set(range(lowerOne, upperOne+1)).intersection(range(lowerTwo, upperTwo+1))
        if overlap == set(range(lowerOne, upperOne+1)) or overlap == set(range(lowerTwo, upperTwo+1)): countA += 1
        if overlap: countB += 1

    print(countA)
    print(countB)
