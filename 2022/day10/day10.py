def signalstrength(feed, pos):
    x = 1
    strength = 0
    for cycle, instruct in enumerate(feed):
        x+=instruct
        if cycle+1 in pos:
            strength += x * (cycle+1)

    return(strength)

def crtscreen(feed, width):
    x=1
    crt = ["." for _ in range(len(feed))] 
    for cycle, instruct in enumerate(feed):
        x+=instruct
        if x-1 <= cycle % width <= x+1:
            crt[cycle]="#"

    for i in range(0, len(feed), width):
        print(''.join(crt[i-width:i]))


with open("day10.inp") as input:
    #build feed
    feed = [0]
    for line in input.readlines():
        if line[:4] == "noop":
            feed.append(0)
        elif line[:4] == "addx":
            feed.append(0)
            feed.append(int(line.strip()[4:]))

    #execute feed
    print("Part A: ", signalstrength(feed, [20, 60, 100, 140, 180, 220]))
    print("Part B: ")
    crtscreen(feed, 40)
