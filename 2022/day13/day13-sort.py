from collections import deque

def checkPair(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, int) and isinstance(b, list):
        return checkPair([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return checkPair(a, [b])
    elif isinstance(a, list) and isinstance(b, list):
        for c, d in zip(a, b):
            if (check := checkPair(c, d)) != 0:
                    return check

        return len(a)-len(b)

def partA(inp):
    partA = 0
    index = 0

    for pair in inp:
        index += 1
        lista, listb = map(eval, pair.strip().split("\n"))
        if checkPair(lista, listb) < 0:
            partA += index

    return partA

def partB(inp):
    packets = [eval(line.strip()) for line in inp if line != ""]
    packets.extend([[[2]], [[6]]])
   
    #simple insertion sort
    for i in range(1, len(packets)):
        key = packets[i]
        j = i-1
        while j >= 0 and (checkPair(key, packets[j]) <= 0):
            packets[j+1] = packets[j]
            j -= 1
        packets[j+1] = key

    #find [[2]] and [[6]]
    ans = 1
    for i, packet in enumerate(packets):
        if packet == [[2]] or packet == [[6]]:
            ans *= (i+1)

    return ans

with open("day13.inp") as file:
    inp = file.read()
    print("part A: ", partA(inp.split("\n\n")))
    print("part B: ", partB(inp.split("\n")))
