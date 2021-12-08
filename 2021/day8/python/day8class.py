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
    
    displaySum = 0
    simpleOccur = {}
    with open(inputFile, "r") as fileIn:
        for line in fileIn:
            current = display(line)

            # for part A, add to total
            current.simpleOccurSum(simpleOccur)

            #part B
            displaySum += current.displayValue()




    #print part A
    answerA = 0
    for length in simpleOccur:
        if length in [2,3,4,7]:
            answerA += simpleOccur[length]

    print("A: ", answerA)
    print("B: ", displaySum)

class display:
#general utils
    #upon creation of class/object split input line.
    def __init__(self, line):
        signalDum, valueDum = line.split(" | ")
        self.signals = signalDum.split()
        self.values = valueDum.split()
        self.digitMap = {}

    #sort single dimensional list of choice into a dictionary 
    #with keys length and then a list of corresponding elements.
    def lenSort(self, sortThis):
        lenSort={}
        for val in sortThis:
            if not len(val) in lenSort:
                lenSort[len(val)]=[]

            lenSort[len(val)].append(val)

        return lenSort

#for solving part A
    def simpleOccurSum(self, totals):
        for key in self.lenSort(self.values):
            if not key in totals:
                totals[key] = 0

            totals[key] += len(self.lenSort(self.values)[key])

        return totals

#for solving part B
    def mapDigits(self):
        self.digitMap = {}
        sigLenSort = self.lenSort(self.signals)
        #handle simple numbers (i.e. 1 of length 2, "7" (3), "4" (4), "8" (7))
        for digit, key in zip([1,7,4,8],[2,3,4,7]):
            self.digitMap[digit] = sorted(list(sigLenSort[key][0]))
       
        #lookup / dict for remaining digits
        digitOverlap = {10: 2, 11: 5, 12: 6, 13: 3, 14: 0, 15: 9}

        for key in [5, 6]:
            if key in sigLenSort:
                for signal in sigLenSort[key]:
                    overlap1478=0
                    for digit in [1,4,7,8]:
                        overlap1478 += len(set(self.digitMap[digit]).intersection(list(signal)))

                    if not digitOverlap[overlap1478] in self.digitMap:
                        self.digitMap[digitOverlap[overlap1478]] = sorted(list(signal))
                        
        return self.digitMap

    def displayValue(self):
        #check if digitMap present, if not do map.
        #empty dictionaries return as "False", if not false = if true
        if not self.digitMap:
            self.mapDigits()

        digits = []
        for value in self.values:
            for key in self.digitMap:
                if sorted(list(value)) == self.digitMap[key]:
                    digits.append(str(key))

        return int(("".join(digits)))


if __name__ == "__main__":
    main(sys.argv[1:])