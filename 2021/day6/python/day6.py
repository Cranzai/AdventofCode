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
        initialState = list(map(int, list(line.split(','))))

# (second) class object to first hist (integrate with prev?)
    #process state into histogram
    #maximum internal timer = 8
    stateHistogram = np.zeros(9)
    for ent in initialState:
        stateHistogram[ent] += 1

    #range(80) represents 80 days total
    for day in range(256):
        if stateHistogram[0] != 0:
            stateHistogram[7] += stateHistogram[0]

        stateHistogram = np.roll(stateHistogram, -1)
        
    print(sum(stateHistogram))

if __name__ == "__main__":
    main(sys.argv[1:])