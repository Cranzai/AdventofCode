import sys
import copy

class homework:
    def __init__(self, file):
        with open(file, "r") as f:
            addition = f.readline().rstrip("\n")
            for line in f:
                addition = '[' + addition + line.rstrip("\n") + ']'

                print(addition)
                #check if there is an element at depth 4.
                index = self.depth(addition)
                if index != None:
                    self.explode(addition, index)

    #returns first element that reaches a depth of 4.
    def depth(self, this):
        brackets = 0
        for index, char in enumerate(list(this)):
            if char == '[':
                brackets += 1
            elif char == ']':
                brackets -= 1

            if brackets == 5:
                return index


    def explode(self, this, start):
        print(start)
        delims = ['[', ']', ',']
        close = 0
        #find first closing bracket:
        for index, char in enumerate(list(this[start:])):
            if char == ']':
                close = index
                break

        print('end found at', start+close)
        start += close

        #find first number not in pair number on right:
        right = []
        for index, char in enumerate(list(this[start:])):
            if not char in delims:
                right = [start+index, this[start+index]]
                break

        #find any number on left:
        left = []
        for index, char in enumerate(list(this[:start])):
            if char == ']':
                left = [start-index, this[start-index]]
                break

        print(left, right)

        




        

if __name__ == "__main__":
    part_a = homework(sys.argv[1])
