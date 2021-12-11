import sys, getopt
import numpy as np

def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:')
    except getopt.GetoptError:
        print('test.py -i <inputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt == '-i':
            inputFile = arg

    dumbos = octopi(inputFile)
    print(dumbos.step(1000))

class octopi:
    def __init__(self, inputFile):
        self.octomap = []

        with open(inputFile, "r") as fileIn:
            for line in fileIn:
                self.octomap.append(list(map(int, list(line.rstrip("\n")))))

        #only reason for using numpy array is the np.where function.
        self.octomap = np.asarray(self.octomap)
        self.flashes = 0
        self.stepFlashes = []

    def flash(self):
        if np.where(self.octomap>=9)[0].size > 0:
            x, y = np.where(self.octomap >= 9)
            coords = list(zip(x,y))
            totFlash = np.full_like(self.octomap, 0)

            for x0, y0 in coords:
                #need to reset to 1 for counting
                self.octomap[x0][y0] = -1
                self.flashes += 1
                for x in [x0-1, x0, x0+1]:
                    if 0 <= x < self.octomap.shape[0]:
                        for y in [y0-1, y0, y0+1]:
                            if 0 <= y < self.octomap.shape[1]:
                                totFlash[x][y]+=1

            self.stepFlashes.extend(coords)
            for x, y in self.stepFlashes:
                totFlash[x][y]=0

            self.octomap = self.octomap + totFlash
            self.flash()

    def step(self, steps):
        #print(self.octomap)
        for i in range(steps):
            if len(self.stepFlashes) == 100:
                message = "synchronized at: " + str(i)
                return message
            self.stepFlashes = []
            self.flash()
            incFlash = np.full_like(self.octomap, 1)
            self.octomap = self.octomap + incFlash

        return self.flashes



if __name__ == "__main__":
    main(sys.argv[1:])