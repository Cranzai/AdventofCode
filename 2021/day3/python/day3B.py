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

    with open(inputFile, "r") as fileIn:
        dummy=fileIn.read().splitlines()
        print(bitCount)
        O2Rate = bitMost(dummy, bitCount)
        print(O2Rate)

    with open(inputFile, "r") as fileIn:
        dummy=fileIn.read().splitlines()
        CO2Rate = bitLeast(dummy, bitCount)
        print(CO2Rate)

def bitMost(bitList, bitCount):
    for pos, counts in enumerate(bitCount):
        most=str(counts.argmax())
        least=str(counts.argmin())

        print(most)

        if most != least:        
            for index, item in enumerate(bitList):
                if len(bitList)==1:
                    break

                if item[pos] == most:
                    del bitList[index]
        
        if most == least:
            for index, item in enumerate(bitList):
                if len(bitList)==1:
                    break

                if item[pos] == "0":
                    del bitList[index]
    return bitList

def bitLeast(bitList, bitCount):
    for pos, counts in enumerate(bitCount):
        most=str(counts.argmax())
        least=str(counts.argmin())

        if most != least:        
            for index, item in enumerate(bitList):
                if len(bitList)==1:
                    break

                if item[pos] == least:
                    del bitList[index]
        
        if most == least:
            for index, item in enumerate(bitList):
                if len(bitList)==1:
                    break

                if item[pos] == "1":
                    del bitList[index]
    return bitList
            

if __name__ == "__main__":
	main(sys.argv[1:])
