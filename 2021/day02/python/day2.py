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

    hor = 0
    dep = 0
    with open(inputFile, "r") as fileIn:
        for line in fileIn.readlines():
            split = line.split()
            if (split[0] == "forward"):
                hor = hor + int(split[1])

            if (split[0] == "up"):
                dep = dep - int(split[1])

            if (split[0] == "down"):
                dep = dep + int(split[1])

    print(dep, hor, dep*hor)

if __name__ == "__main__":
	main(sys.argv[1:])