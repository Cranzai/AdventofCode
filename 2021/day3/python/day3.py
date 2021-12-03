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
        bitList = fileIn.read().splitlines()

    O2Rate = int(bitCritO2(bitLen, bitList)[0],2)
    print(O2Rate)


    CO2Rate = int(bitCritCO2(bitLen, bitList)[0],2)
    print(CO2Rate)

    print(O2Rate*CO2Rate)

def bitCounter(bitLen, bitList):
    bitCount = np.zeros((bitLen,2))
    for entry in bitList:
        bits=list(entry)
        for index, bit in enumerate(bits):
            if bit == "0":
                bitCount[index,0] += 1
            if bit == "1":
                bitCount[index,1] += 1

    return bitCount

#pay attention to reverse logic
#O2 keep most, when equal keep 1
def bitCritO2(bitLen, bitList):
    for i in range(0,bitLen):
        bitCount = bitCounter(bitLen, bitList)

        counts=bitCount[i]
        keepVal = counts.argmax()
        if counts[0]==counts[1]:
            keepVal=1

        bitListDummy = []

        for item in bitList:
            if item[i] == str(keepVal):
                bitListDummy.append(item)

        if bitListDummy != []:
            bitList = bitListDummy

    return bitList



#pay attention to reverse logic
#O2 keep least, when equal keep 0
def bitCritCO2(bitLen, bitList):
    for i in range(0,bitLen):
        bitCount = bitCounter(bitLen, bitList)

        counts=bitCount[i]
        keepVal = counts.argmin()
        if counts[0]==counts[1]:
            keepVal=0

        bitListDummy = []

        for item in bitList:
            if item[i] == str(keepVal):
                bitListDummy.append(item)

        if bitListDummy != []:
            bitList = bitListDummy

    return bitList

if __name__ == "__main__":
	main(sys.argv[1:])