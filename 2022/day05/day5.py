import re
import copy
from collections import deque

with open("day5.inp") as input:
    instructions = False
    stacksA = {}
    for line in input.readlines():
        if not instructions:
            if not "[" in line:
                instructions=True
                stacksB = copy.deepcopy(stacksA)
                continue 
            else:
                for i in range(int(len(line)/4)):
                    if i+1 in stacksA and line[4*i+1] != " ":
                        stacksA[i+1].append(line[4*i+1])
                    elif line[4*i+1] != " ":
                        stacksA[i+1] = deque(line[4*i+1])
        if instructions:
            if len(line)==1: continue
            count, origin, target = map(int, re.findall(r'\d+', line))
            moveB = []
            for i in range(count):
                stacksA[target].appendleft(stacksA[origin].popleft())
                moveB.insert(0,stacksB[origin].popleft())

            stacksB[target].extendleft(moveB)

    print("".join([stacksA[i+1][0] for i in range(len(stacksA))]))
    print("".join([stacksB[i+1][0] for i in range(len(stacksB))]))
