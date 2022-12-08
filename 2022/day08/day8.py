with open("day8.inp") as input:
    #read grid
    grid = [list(map(int, row.strip())) for row in input.readlines()]

    height = len(grid)
    width = len(grid[0])

    #part A
    visible = 0
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            col = [r[c] for r in grid]
            if (r==0 or r==height-1) or (c==0 or c == height-1):
                visible +=1
            elif (max(row[:c]) < val or max(row[c+1:]) < val) or (max(col[:r]) < val or max(col[r+1:]) < val):
                visible +=1

    print(visible)

    #part B
    highscore = 0
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            col = [r[c] for r in grid]
            #look left
            left = 0
            if not c == 0:
                for neighbour in reversed(row[:c]):
                    if neighbour < val:
                        left +=1
                    elif neighbour >= val:
                        left +=1
                        break
            #look right
            right = 0
            if not c == width-1:
                for neighbour in row[c+1:]:
                    if neighbour < val:
                        right +=1
                    elif neighbour >= val:
                        right +=1
                        break
            #look up
            up = 0
            if not r == 0:
                for neighbour in reversed(col[:r]):
                    if neighbour < val:
                        up +=1
                    elif neighbour >= val:
                        up +=1
                        break
            #look down
            down = 0
            if not r == height-1:
                for neighbour in col[r+1:]:
                    if neighbour < val:
                        down +=1
                    elif neighbour >= val:
                        down +=1
                        break
            #score
            if left*right*up*down > highscore:
                highscore = left*right*up*down

    print(highscore)
