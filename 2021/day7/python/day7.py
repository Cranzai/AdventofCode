import sys, getopt
from statistics import median
from statistics import mean
import math

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
      
    with open(inputFile, "r") as fileIn:
        #no loop today, only read one line.
        positions = list(map(int, list((fileIn.readline()).split(','))))

#part A is easy (L1-norm?)
    targetPos = median(positions)

    fuel = 0
    for pos in positions:
        fuel += abs(pos-targetPos)

    print(fuel) 


#part B is trickier (L2-norm?)
    targetPos = min(math.floor(mean(positions)),math.ceil(mean(positions)))

    fuel = 0
    for pos in positions:
        distance = abs(pos-targetPos)
        fuel += distance*(distance+1)/2

    print(fuel) 
    
 

if __name__ == "__main__":
    main(sys.argv[1:])