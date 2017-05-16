class Node:
    def __init__(self, key, nil):
        if not key:
            self.key = "nil"
            self.left = self
            self.right = self
            self.p = self
        else:
            self.key = key
            self.left = nil
            self.right = nil
            self.p = nil

    def setP(self, p):
        self.p = p

    def getP(self):
        return self.p

    def height(self, node):
        if node.key == "nil":
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1


class ABR:
    def __init__(self):
        self.nil = Node(None, None)
        self.root = self.nil

    def setRoot(self, key):
        self.root = Node(key, self.nil)

    def changeRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def treeminimum(self, x):
        while x.left.key is not "nil":
            x = x.left
        return x

    def treemaximum(self, x):
        while x.right.key is not "nil":
            x = x.right
        return x

    def insert(self, key):
        if self.root is self.nil:
            self.setRoot(key)
            self.root.setP(self.nil)
            return self.root
        else:
            return self.insertNode(key, self.root)

    def insertNode(self, key, currentNode):
        if key <= currentNode.key:
            if currentNode.left.key != "nil":
                self.insertNode(key, currentNode.left)
            else:
                currentNode.left = Node(key, self.nil)
                currentNode.left.setP(currentNode)
                return currentNode.left
        elif key > currentNode.key:
            if currentNode.right.key != "nil":
                self.insertNode(key, currentNode.right)
            else:
                currentNode.right = Node(key, self.nil)
                currentNode.right.setP(currentNode)
                return currentNode.right

    def inorder(self):
        def _inorder(v):
            if v.key == "nil":
                return
            if v.left.key != "nil":
                _inorder(v.left)
            print v.key
            if v.right.key != "nil":
                _inorder(v.right)

            _inorder(self.root)

    def treeSearch(self, k, currentNode):
        while currentNode and k != currentNode.key:
            if k < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        if currentNode:
            return currentNode
        print "Elemento non presente"

    def serialize(self, node):
        print "", node.key, "(",
        if node.left.key is not "nil":
            self.serialize(node.left)
        else:
            print "_",
        if node.right.key is not "nil":
            self.serialize(node.right)
        else:
            print" _ ) ,",


tre = ABR()
tre.insert(8)
tre.insert(7)
tre.insert(4)
tre.insert(3)
tre.insert(9)
a = tre.treemaximum(tre.getRoot())
print a.key
tre.serialize(tre.getRoot())
