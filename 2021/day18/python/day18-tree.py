#https://gitlab.dataghost.com/dataghost/advent-of-code/-/snippets/25
import sys
import json

class Node:
    def __init__(self, value = None):
        self.parent = None
        self._root = None
        self._depth = None
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def build(cls, snail, root=True):
        def buildNode(subsnail):
            if isinstance(subsnail, list):
                return Node.build(subsnail, False)
            return Node(subsnail)

        node = Node()
        node.left = buildNode(snail[0])
        node.right = buildNode(snail[1])

        if root:
            # Fill the tree parents and depths, reduce it to maintain the invariant
            node._treeFix(node)
            node._doActions()
        return node

    def _treeFix(self, root, depth=0):
        self._depth = depth
        self._root = root
        if self.isvalue:
            return
        for node in [self.left, self.right]:
            if node.parent is None:
                node.parent = self
            node._treeFix(root, depth+1)





if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        trees = [Node.build(json.loads(line)) for line in file.readlines()]