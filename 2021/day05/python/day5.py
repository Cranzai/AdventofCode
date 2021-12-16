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
    
    coordMap={}
    with open(inputFile, "r") as fileIn:
        for line in fileIn:
            #keep vectors as strings for now, for dictionary
            rawVector = [coord.split(',') for coord in (line.rstrip("\n")).split(' -> ')]
            vector = [list(map(int, coord)) for coord in rawVector]

            mapNoDiag(vector, coordMap)
            mapWithDiag(vector, coordMap)

    dangerSpots = 0
    for key, value in coordMap.items():
        if value > 1:
            dangerSpots += 1

    print(dangerSpots)


def mapNoDiag(vector, coordOccur):

    #vertical x1=x2
    if (vector[0][0]==vector[1][0]):
        x=vector[0][0]
        lower=min(vector[0][1],vector[1][1])
        upper=max(vector[0][1],vector[1][1])

        for y in range(lower,upper+1):
            prevVal = coordOccur.get((x,y), 0)
            coordOccur[(x,y)] = prevVal + 1

    #horizontal y1=y2
    if (vector[0][1]==vector[1][1]):
        y=vector[0][1]
        lower=min(vector[0][0],vector[1][0])
        upper=max(vector[0][0],vector[1][0])

        for x in range(lower, upper+1):
            prevVal = coordOccur.get((x,y), 0)
            coordOccur[(x,y)] = prevVal + 1

    return coordOccur

def mapWithDiag(vector, coordOccur):
    #only need to consider 45 deg, determine said angle
    #in such a case dx=dy
    dx = max(vector[1][0]-vector[0][0], vector[0][0]-vector[1][0])
    dy = max(vector[1][1]-vector[0][1], vector[0][1]-vector[1][1])
    if dx == dy:
        xStep=1
        yStep=1
        if vector[0][0] > vector[1][0]: xStep=-1
        if vector[0][1] > vector[1][1]: yStep=-1

        xRange = range(vector[0][0],vector[1][0]+xStep, xStep)
        yRange = range(vector[0][1],vector[1][1]+yStep, yStep)

        for x, y in zip(list(xRange), list(yRange)):
            prevVal = coordOccur.get((x,y), 0)
            coordOccur[(x,y)] = prevVal + 1

    return coordOccur


            

if __name__ == "__main__":
    main(sys.argv[1:])