def cave(traj):
    rocks = set()
    abyss = 0
    for line in traj.split("\n"):
        vertices = line.strip().split(" -> ")
        for a, b in zip(vertices, vertices[1:]):
            xa, ya = map(int, a.split(","))
            xb, yb = map(int, b.split(","))

            x = sorted([xa,xb])
            y = sorted([ya,yb])

            if y[1] > abyss: abyss = y[1]
            
            for d in range(x[0], x[1]+1, 1):
                if x[0]==xa:
                    rocks.add((d, ya))
                if x[0]==xb:
                    rocks.add((d, yb))

            for d in range(y[0], y[1]+1, 1):
                if y[0]==ya:
                    rocks.add((xa, d))
                if y[0]==yb:
                    rocks.add((xb, d))

    return rocks, abyss

def movegrain(spawn, abyss, rocks, sand):
    x, y = spawn
    #down
    if (not (x,y+1) in rocks) and (not (x,y+1) in sand) and (not y == abyss):
        return movegrain((x,y+1), abyss, rocks, sand)
    #left
    elif (not (x-1,y+1) in rocks) and (not (x-1,y+1) in sand) and (not y == abyss):
        return movegrain((x-1,y+1), abyss, rocks, sand)
    #right
    elif (not (x+1,y+1) in rocks) and (not (x+1,y+1) in sand) and (not y == abyss):
        return movegrain((x+1,y+1), abyss, rocks, sand)
    #stopped
    else:
        sand.add((x, y))
        return y, sand

def sandfill(rocks, abyss, xspawn):
    sand = set()
    y=0
    while y < abyss: 
        y, sand = movegrain([500,0], abyss, rocks, sand)

    return len(sand)-1

with open("day14.inp") as input:
    #build set of boundary coords
    file = input.read()
    rocks, abyss = cave(file)

    print(sandfill(rocks, abyss, 500))
    

