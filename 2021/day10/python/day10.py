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

    scoreCorrupt = 0
    illegals = {")":3, "]":57, "}":1197, ">":25137}
    scoresIncomplete = []
    completion = {"(":1, "[":2, "{":3, "<":4}
    with open(inputFile, "r") as fileIn:
        for line in fileIn:
            current = navLine(line.rstrip("\n"))
            corrupt = current.findCorrupt()
            if corrupt != current.line: 
                scoreCorrupt += illegals[corrupt]

            if corrupt == current.line:
                scoreIncomplete = 0
                for char in reversed(list(current.line)):
                    scoreIncomplete = scoreIncomplete *5
                    scoreIncomplete += completion[char]

                scoresIncomplete.append(scoreIncomplete)

        scoresIncomplete = sorted(scoresIncomplete)

    print(scoreCorrupt)
    print(scoresIncomplete[int(np.floor(len(scoresIncomplete)/2))])
    

class navLine:
    def __init__(self, line):
        self.line = line
        self.pairs = {")":"(", "]":"[", "}":"{", ">":"<"}

    #recursive function
    def removeChunks(self):
        chunks = chunks = ["()", "[]", "{}", "<>"]
        if any(chunk in self.line for chunk in chunks):
            for chunk in chunks:
                self.line = self.line.replace(chunk, "")

            self.removeChunks()

        return(self.line)

    #wrapper to call recursive function, otherwise a mess
    def findCorrupt(self):
        self.removeChunks()
        for index, char in enumerate(list(self.line)):
            if char in self.pairs.keys():
                if list(self.line)[index-1] != self.pairs[char]:
                    return(char)

        #if its not corrupt, return the leftovers of the incomplete line.
        return(self.line)

if __name__ == "__main__":
    main(sys.argv[1:])