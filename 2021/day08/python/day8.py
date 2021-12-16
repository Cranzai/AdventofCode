import sys, getopt
import collections

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
    
    displaySignals = []
    displayVals = []
    with open(inputFile, "r") as fileIn:
        for line in fileIn:
            signals, values = line.split(" | ")
            displaySignals.append(signals.split())
            displayVals.append(values.split())

#part 1: Considerd how many times the digits 1, 4, 7, 8 appear accros all displays
#part A
    valLengthSort = lenSort(displayVals)
    for key in valLengthSort:
        print(key, ":", len(valLengthSort[key]))

#part 2: (PER DISPLAY) create map...
    totalVals = []
    for signals, values in zip(displaySignals, displayVals):
        #sort by length
        signalLengthSort = {}
        for signal in signals:
            if not len(signal) in signalLengthSort:
                signalLengthSort[len(signal)]=[]

            signalLengthSort[len(signal)].append(signal)
        #only lengths 2 (=1), 3 (=7), and 4 (=4) are useful.
        infoKeys = [2, 3, 4]
        digitMap = {8: "abcdefg"}
        for info in infoKeys:
            if info in signalLengthSort:
                if info == 2:
                    digitMap[1] = signalLengthSort[info][0]
                if info == 3:
                    digitMap[7] = signalLengthSort[info][0]
                if info == 4:
                    digitMap[4] = signalLengthSort[info][0]
                

        deductKeys = [5,6]
        for deduct in deductKeys:
                for signal in signalLengthSort[deduct]:
                    overlap147 = 0
                    for char in list(signal):
                        if char in digitMap[1]: overlap147 += 1
                        if char in digitMap[4]: overlap147 += 1
                        if char in digitMap[7]: overlap147 += 1

                    overlap147 += deduct

                    if not 0 in digitMap and overlap147 == 14:
                        digitMap[0] = signal

                    if not 2 in digitMap and overlap147 == 10:
                        digitMap[2] = signal

                    if not 3 in digitMap and overlap147 == 13:
                        digitMap[3] = signal

                    if not 5 in digitMap and overlap147 == 11:
                        digitMap[5] = signal

                    if not 6 in digitMap and overlap147 == 12:
                        digitMap[6] = signal

                    if not 9 in digitMap and overlap147 == 15:
                        digitMap[9] = signal


        digits = []
        for value in values:
            for key in digitMap:
                if collections.Counter(value) == collections.Counter(digitMap[key]):
                    digits.append(str(key))
                       
        totalVals.append(int(("".join(digits))))

    print(totalVals)
    print(sum(totalVals))


def lenSort(outVals):
    sortedLengths={}
    for entry in outVals:
        for val in entry:
            if not len(val) in sortedLengths:
                sortedLengths[len(val)]=[]

            sortedLengths[len(val)].append(val)

    return sortedLengths

def decompose(sorted):
    decomposition={}
    for key in sorted:
        decomposition[key]={}
        for entry in sorted[key]:
            for char in list(entry):
                if not char in decomposition[key]:
                    decomposition[key][char]=0

                decomposition[key][char] += 1

    return decomposition

if __name__ == "__main__":
    main(sys.argv[1:])