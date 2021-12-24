#building a binary tree
#https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
#AoC example:
#https://gitlab.dataghost.com/dataghost/advent-of-code/-/snippets/25
import sys

class node:
    def __init__(self, value=None):
        #these selfs link to other class objects, creating the connection
        self._root = None
        self._depth = None
        self.parent = None
        self.left = None
        self.right = None

        self.value = value

    @classmethod
    def build(cls, tree, root = True):
        #to assign assign left and right, need to know whether they are values or 
        #further connections (i.e. is the item another list or a value)
        def connect(branch):
            if isinstance(branch, list):
                #the branch is a list, call recursion
                return node.build(branch, False)
            else:
                #the branch is not a list, thus a value
                #create a node object representing the value
                return node(branch)

        #first node is always a connection, create class object
        here = node()
        here.left = connect(tree[0])
        here.right = connect(tree[1])

        if root:
            #only active for the first call of this function
            #(executed after the rest, remember its serial)
            #this is automatically the root based on the list supplied
            #figure out all depths from here (inclusion in recursion is tricky)
            here._assemble(here)

        return here

    #turns single dimensional list into a tree
    #(upon creating we only have lefts and rights,
    #here the parent structure is created)
    def _assemble(self, root, depth=0):
        self._depth = depth
        self._root = root
        #recursively digging for values, if its a value max depth reached
        if self.isvalue:
            return
        for node in [self.left, self.right]:
            if node.parent is None:
                node.parent = self
            node._assemble(root, depth+1)

    #function for solving the three according to the snailfish math
    #always perform first operation that is encountered...
#    def solve(self):
#        for node in self._traverse():
#            #explode, triggers on top node
#            if max_depth == node._depth:



        
    #yield is similar to return but instead it "maintains" state
    #i.e. first returns this then returns that.
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    @property
    def isvalue(self):
        if self.left is None and self.right is None:
            return True
        assert self.left is not None and self.right is not None
        return False

    #below function is automatically called whenever trying to print object.
    def __str__(self):
        if self.value != None:
            return str(self.value)

        #formatted string output, find the connected objects
        return f"[{self.left},{self.right}]"

if __name__ == "__main__":
    #first read input into a single nested list
    with open(sys.argv[1], "r") as file:
        addition = eval(file.readline().rstrip("\n"))
        for line in file:
            addition = [addition, eval(line.rstrip("\n"))]

    tree = node.build(addition)
    print(tree)