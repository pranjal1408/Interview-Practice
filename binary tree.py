class Node():
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class binarytree():

    def __init__(self):
        self.root=None

    def getroot(self):
        return self.root

    def insert(self,value):
        if (self.root is None):
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value, node):

            if(value<node.value):
                if(node.left is None):
                    node.left=Node(value)
                else:
                    self._insert(value,node.left)
            if(value>=node.value):
                if(node.right is None):
                    node.right=Node(value)
                else:
                    self._insert(value,node.right)


    def printTree(self, node):
        if (node != None):
            print str(node.value) + ' '
            self.printTree(node.left)

            self.printTree(node.right)


tree=binarytree()
tree.insert(3)
tree.insert(1)
tree.insert(5)
tree.insert(7)
tree.insert(9)
tree.insert(2)
tree.insert(6)
tree.printTree(tree.root)