delta = {"U":(+1, 0), "D":(-1,0), "L":(0,-1), "R":(0,+1)}
#part A version 1
with open("day9demo.inp") as input:
    headpos = [0,0]
    tailpos = [0,0]
    visited = set()
        
    for line in input.readlines():
        direction, step = line.strip().split(" ")

        delx, dely = delta[direction]
        for i in range(int(step)):
            headpos = [headpos[0]+delx, headpos[1]+dely]
            vicinity = set([(headpos[0]-i, headpos[1]-j) for i in range(-1, 2) for j in range(-1, 2)])
            if not tuple(tailpos) in vicinity:
                tailpos = [headpos[0]-delx, headpos[1]-dely]

            visited.add(tuple(tailpos))

    print(len(visited))

#part A version 2
with open("day9.inp") as input:
    rope = [[0,0] for i in range(2)]
    visited = set()   

    for line in input.readlines():
        direction, step = line.strip().split(" ")

        for i in range(int(step)):
            delx, dely = delta[direction]
            rope[0] = [rope[0][0]+delx, rope[0][1]+dely]
            
            for i, part in enumerate(zip(rope, rope[1:])):
                lead, follow = part
                vicinity = set([(lead[0]-i, lead[1]-j) for i in range(-1, 2) for j in range(-1, 2)])
                if not tuple(follow) in vicinity:
                    rope[i+1] = [lead[0]-delx, lead[1]-dely]

            visited.add(tuple(rope[-1]))


    print(len(visited))
