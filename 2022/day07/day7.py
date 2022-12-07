#same object for folders (size=0) and files (size!=0)
class item:
    def __init__(self, size, name, parent=None, dir=True):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        self.dir=dir

def dfsadd(root):
    for child in root.children:
        dfsadd(child)
        root.size += child.size

def partA(root, sizes):
    for child in root.children:
        partA(child, sizes)
        if child.dir and child.size <= 100000:
            sizes.append(child.size)

def partB(root, sizes, crit):
    for child in root.children:
        partB(child, sizes, crit)
        if child.dir and child.size >= crit:
            sizes[child.name]=child.size

with open("day7.inp") as input:
    #assume that the inputs always start with "$ cd /"
    root = item(0, "/")
    pwd = root
    #assume that new files are only explored using "$ ls" 
    for line in input.readlines()[1:]:
        line = line.strip()
        if line[0] != "$":
            if line[:4] == "dir ":
                #dir
                name = line[4:]
                pwd.children.append(item(0, name, pwd))
            else:
                #file
                size, name = line.split(" ")
                pwd.children.append(item(int(size), name, pwd, False))
        elif line[:4] == "$ cd":
            if line[5:] == "/":
                #$ cd /
                pwd = root
            elif line[5:] == "..":
                #$ cd ..
                pwd = pwd.parent
            else:
                #$ cd dir
                for child in pwd.children:
                    if child.name == line[5:]:
                        pwd = child                

    #calculate directory sizes
    dfsadd(root)

    #perform assignment
    sizes = []
    partA(root, sizes)
    print(len(sizes))
    print(sizes)
    print("part A: ", sum(sizes))

    sizes = {}
    crit = root.size-40000000
    partB(root, sizes, crit)
    print("part B: ", sizes[min(sizes, key=sizes.get)]) 
