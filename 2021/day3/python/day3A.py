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
    
    with open(inputFile, "r") as fileIn:
        #read firstline to determine length of bit sequence
        bitLen = len(fileIn.readline())-1
        fileIn.seek(0)
        bitCount = np.zeros((bitLen,2))
        # .readlines() to get all lines as a list and iterate
        for line in fileIn.readlines():
            bits = list(line)
            for index, bit in enumerate(bits):
                if bit == "0":
                    bitCount[index,0] += 1
                if bit == "1":
                    bitCount[index,1] += 1

    print(bitCount)

    gamma = ""
    epsilon = ""

    for counts in bitCount:
        if counts[1]>counts[0]:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        
        if counts[1]<counts[0]:
            gamma = gamma + "0"
            epsilon = epsilon + "1"

    gammaRate = int(gamma, 2)
    epsilonRate= int(epsilon, 2)

    print(gammaRate*epsilonRate)
if __name__ == "__main__":
	main(sys.argv[1:])