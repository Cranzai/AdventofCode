import sys, getopt

def main(argv):
    inputFile = ''
    depthList = []

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
        for val in fileIn.readlines():
            depthList.append(float(val))

    incrs=0
    for i, depth in enumerate(depthList[1:]):
        if (depthList[i]>depthList[i-1]):
            incrs = incrs + 1

    print(incrs)

if __name__ == "__main__":
	main(sys.argv[1:])