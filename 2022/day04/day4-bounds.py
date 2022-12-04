import re
    
with open("day4.inp") as input:
    countA = 0
    countB = 0
    for line in input.readlines():
        lowerOne, upperOne, lowerTwo, upperTwo = map(int, re.split(",|-", line.strip()))
        if (lowerOne <= lowerTwo and upperOne >= upperTwo) or (lowerTwo <= lowerOne and upperTwo >= upperOne): countA +=1
        if lowerOne <= upperTwo and lowerTwo <= upperOne: countB += 1

    print(countA)
    print(countB)
