delta = {"U":(+1, 0), "D":(-1,0), "L":(0,-1), "R":(0,+1)}

def movetail(head, tail):
  if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
    if head[1] > tail[1]:
      tail = (tail[0], tail[1] + 1)
    elif head[1] < tail[1]:
      tail = (tail[0], tail[1] - 1)
    if head[0] > tail[0]:
      tail = (tail[0] + 1, tail[1])
    elif head[0] < tail[0]:
      tail = (tail[0] - 1, tail[1])
  return tail

with open("day9.inp") as input:
    length = 2
    rope = [[0,0] for _ in range(length)]

    visited = set()
    visitedNew = set()
    
    for line in input.readlines():
        direction, step = line.strip().split(" ")
        dx, dy = delta[direction]

        for i in range(int(step)):
            rope[0][0] += dx
            rope[0][1] += dy

            for i in range(1, length):
                rope[i] = movetail(rope[i-1], rope[i])

            visited.add(tuple(rope[-1]))

    print(len(visited))

with open("day9.inp") as input:
    length = 10
    rope = [[0,0] for _ in range(length)]

    visited = set()
    visitedNew = set()
    
    for line in input.readlines():
        direction, step = line.strip().split(" ")
        dx, dy = delta[direction]

        for i in range(int(step)):
            rope[0][0] += dx
            rope[0][1] += dy

            for i in range(1, length):
                rope[i] = movetail(rope[i-1], rope[i])

            visited.add(tuple(rope[-1]))

    print(len(visited))

