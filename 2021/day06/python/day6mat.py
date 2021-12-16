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
    
# first class object/initialize    
    with open(inputFile, "r") as fileIn:
        #no loop today, only read one line.
        line = fileIn.readline()
        stateHistogram = np.zeros(9)
        for ent in list(map(int, list(line.split(','))))
            stateHistogram[ent] += 1

    growthMat = np.array([
        [0,1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0]
        ])

    days = 256
    finalState = np.linalg.matrix_power(growthMat, days).dot(stateHistogram)
    print(sum(finalState))
 

if __name__ == "__main__":
    main(sys.argv[1:])