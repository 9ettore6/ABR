import math
import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.padre = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def setp(self, p):
        self.padre = p

    def getp(self):
        return self.padre

    def getChildren(self):
        children = []
        if self.left != None:
            children.append(self.left)
        if self.right != None:
            children.append(self.right)
        return children


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def changeRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def insert(self, key):
        if self.root is None:
            self.setRoot(key)
            a = self.treesearch(key, self.root)
            a.padre = None  # self.previousnode(key, self.root)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if key <= currentNode.key:
            if currentNode.left:
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
                currentNode.left.setp(currentNode)
                return currentNode.left
        elif key > currentNode.key:
            if currentNode.right:
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)
                currentNode.right.setp(currentNode)
                return currentNode.right

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if currentNode is None:
            return False
        elif key == currentNode.key:
            return True
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def inorder(self):
        def _inorder(v):
            if v is None:
                return
            if v.left is not None:
                _inorder(v.left)
            print v.key
            if v.right is not None:
                _inorder(v.right)

        _inorder(self.root)

    def treesearch(self, k, currentNode):  # restituisce un ptr a un nodo con chiave k se esiste
        while currentNode and k != currentNode.key:
            if k < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        if currentNode:
            return currentNode
        print "Elemento non presente"

    '''def previousnode(self, k, currentNode):  # restituisce il ptr al nodo precendente
        while currentNode and k != currentNode.key:
            if k < currentNode.key:
                currentptr = currentNode
                currentNode = currentNode.left
            else:
                currentptr = currentNode
                currentNode = currentNode.right
        if currentNode:
            return currentptr
        print "Precedente non presente"
'''

def main():
    tree = ABR()
    tree.insert(4)
    tree.insert(8)
    tree.insert(15)
    tree.insert(7)
    tree.insert(5)
    print tree.treesearch(5, tree.root).padre.key
    print ""
    tree.inorder()
    a = tree.treesearch(7, tree.root)
    b = tree.previousnode(8, tree.root)
    print b.key


if __name__ == "__main__":
    main()
