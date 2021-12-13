import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def main(inputFile):
    with open(inputFile, "r") as fileIn:
        lines  = [line.rstrip("\n") for line in fileIn.readlines()]
        points = [list(map(int, line.split(","))) for line in lines[:lines.index('')]]
        #"fold along " has a length of 10...
        instructs = [line[11:].split("=") for line in lines[lines.index('')+1:]]

    transparency(points, instructs).visual(True)

class transparency:
    def __init__(self, points, instructions):
        self.pts = points
        self.instructs = instructions

    def fold(self, foldAll):
        folding = self.pts 
        folded = []

        axis, index = self.instructs[0]
        for x, y in folding:
            xNew = x
            yNew = y
            if axis == "x" and x > int(index):
                xNew = int(index) - (x - int(index))
                yNew = y

            if axis == "y" and y > int(index):
                yNew = int(index) - (y - int(index))
                xNew = x

            if not [xNew, yNew] in folded:
                folded.append([xNew, yNew])
        
        if foldAll:
            for axis, index in self.instructs[1:]:               
                folding = folded.copy()
                folded = []

                for x, y in folding:                   
                    xNew = x
                    yNew = y

                    if axis == "x" and x > int(index):
                        xNew = int(index) - (x - int(index))
                        yNew = y

                    if axis == "y" and y > int(index):
                        xNew = x
                        yNew = int(index) - (y - int(index))

                    if not [xNew, yNew] in folded:
                        folded.append([xNew, yNew])

        return(folded)

    def visual(self, foldAll):
        folded = self.fold(foldAll)

        maxX = max([pt[0] for pt in folded]) + 1
        maxY = max([pt[1] for pt in folded]) + 1

        grid = np.zeros((maxX, maxY))
        for x, y in folded:
            grid[x][y] = 1

        #quite overkill matplotlib visualization, very nice though
        fig = plt.figure()
        ax1 = fig.add_subplot()
        ax1.imshow(np.transpose(grid), interpolation = 'nearest', cmap=cm.Greys_r)
        plt.show()

if __name__ == "__main__":
    #only pass through the first argument which should be the inputfile
    main(sys.argv[1])