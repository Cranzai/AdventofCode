import sys
import copy

class homework:
    def __init__(self, file):
        with open(file, "r") as f:
            #first line to initiate addition
            addition = eval(f.readline().rstrip("\n"))
            for line in f:
                addition = [addition, eval(line.rstrip("\n"))]

                print(addition)
                deep = self.depth(addition, 0, [0], [])
                print(deep)

                if deep:
                    i, j, k, l = deep[0]
                    self.explode(addition, deep[0])
                    

                    



    #returns first element that reaches a depth of 4.
    def depth(self, this, level, myindices, deepest):
        for index, item in enumerate(this):
            if type(item) == list:
                myindices[-1] = index
                if not deepest:
                    newindices = copy.deepcopy(myindices)
                    newindices.append(index)
                    self.depth(item, level+1, newindices, deepest)
            else:
                if level == 4:
                    if not deepest:
                        deepest.append(myindices[:-1])

        return deepest

    def explode(self, this, site):
        print('explode:',site)
        max_index = len(this) -1
        #0 is always minimum index.
        neigbhours_left = []
        neighbours_right = []



        

if __name__ == "__main__":
    #first read input into a single nested list
    with open(sys.argv[1], "r") as file:
        addition = eval(f.readline().rstrip("\n"))
            for line in f:
                addition = [addition, eval(line.rstrip("\n"))]

    #process nested list into a tree.
