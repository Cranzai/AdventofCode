import sys, getopt
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
    
    signalPatterns = []
    outputVals = []
    with open(inputFile, "r") as fileIn:
        for line in fileIn:
            signals, values = line.split(" | ")
            displaySignal.append(signals.split())
            displayVal.append(values.split())

    valLengthSort = lenSort(displayVal)
    
#print "answer" for part A, only need to manually add up occurences of length 2, 3, 4, 8    
    for key in valLengthSort:
        print(key, ":", len(valLengthSort[key]))

    decomp = decompose(sortedLengths)

#can only contain information from 1(2), 4(4), and 7(3)
    infoKeys = [2, 3, 4]
    
    digitMap = {8: ["a", "b", "c", "d", "e", "f", "g"]}
    for info in infoKeys:
        segments = []
        for i in range(info):

            maxKey = max(decomp[info], key=decomp[info].get)
            segments.append(maxKey)
            del decomp[info][maxKey]

        if info == 2: digitMap[1] = segments
        if info == 3: digitMap[7] = segments
        if info == 4: digitMap[4] = segments





#can deduce identity based on overlap with known digits
#using sorted lenghts again here which sorta makes decomp a bit redundant (only use it for 2, 3, 4)
    deductKeys = [5, 6]
    for deduct in deductKeys:
#using these if statements as crooked breaks
        if len(digitMap) != 9:
            for val in sortedLengths[deduct]:
                overlap147=0
                if len(digitMap) != 9:
                    for char in list(val):
                        if char in digitMap[1]: overlap147 += 1
                        if char in digitMap[4]: overlap147 += 1
                        if char in digitMap[7]: overlap147 += 1

                    if deduct == 5:
                        if not 2 in digitMap and overlap147 == 5:
                            print("2:", overlap147, val)
                            digitMap[2] = list(val)
                        if not 5 in digitMap and overlap147 == 8: 
                            print("5:", overlap147, val)
                            digitMap[5] = list(val)
                        if not 3 in digitMap and overlap147 == 6:  
                            print("3:", overlap147, val)
                            digitMap[3] = list(val)
                    if deduct == 6:
                        if not 0 in digitMap and overlap147 == 8:  
                            print("0:", overlap147, val)
                            digitMap[0] = list(val)                  
                        if not 6 in digitMap and overlap147 == 6:  
                            print("6:", overlap147, val)
                            digitMap[6] = list(val)
                        if not 9 in digitMap and overlap147 == 9:  
                            print("9:", overlap147, val)
                            digitMap[9] = list(val)

    print(digitMap)




# 0 = a b c   e f g - 6 segments
# 1 =     c     f   - 2    "
# 2 = a   c d e   g - 5    "
# 3 = a   c d   f g - 5    "
# 4 = b   c d   f   - 4    "
# 5 = a b   d   f g - 5    "
# 6 = a b   d e f g - 6    "
# 7 = a   c     f   - 3    "
# 8 = a b c d e f g - 7    "
# 9 = a b c d   f g - 6    "

#easy numbers (unique number of segments): 1(2), 4(4), 7(3), 8(7)

#part A
def lenSort(outVals):
    sortedLengths={}
    for entry in outVals:
        for val in entry:
            if not len(val) in sortedLengths:
                sortedLengths[len(val)]=[]

            sortedLengths[len(val)].append(val)

    return sortedLengths

#part B
#count occurences of all letters for each lenght:
#most occuring set of letters (e.g. most occuring 2 for 1) should be the number.
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