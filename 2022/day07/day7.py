#same item for folders (dir=True) and files (dir=False)
class item:
    def __init__(self, size, name, parent=None, dir=True):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        self.dir = dir

#function to calculate dir sizes
def dfsadd(root):
    for child in root.children:
        dfsadd(child)
        root.size += child.size

def solve(root, eq, crit, sizes):
    if eq=="le":
       for child in root.children:
           solve(child, eq, crit, sizes)
           if child.dir and child.size <= crit:
               sizes.append(child.size)
    elif eq=="ge":
       for child in root.children:
           solve(child, eq, crit, sizes)
           if child.dir and child.size >= crit:
               sizes.append(child.size)
    else:
        return "unrecognized option"

    return sizes

with open("day7.inp") as input:
    #assume that the inputs always start with "$ cd /"
    root = item(0, "/")
    pwd = root
    
    #assume that new files are not entered before explored by "$ ls"
    for line in input.readlines()[1:]:
        line = line.strip()
        if line[0] != "$":
            if line[:4] == "dir ":
                name = line[4:]
                pwd.children.append(item(0, name, pwd))
            else:
                size, name = line.split(" ")
                pwd.children.append(item(int(size), name, pwd, False))
        elif line[:4] == "$ cd":
            if line[5:] == "/":
                pwd = root
            elif line[5:] == "..":
                pwd = pwd.parent
            else:
                for child in pwd.children:
                    if child.name == line[5:]:
                        pwd = child

    #calculate directory sizes
    dfsadd(root)

    #perform assignment
    print("part A", sum(solve(root, "le", 100000, [])))
    print("part B", min(solve(root, "ge", root.size-40000000, [])))
