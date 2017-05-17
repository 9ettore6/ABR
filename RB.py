import ABR


class RBNode(ABR.Node):
    def __init__(self, key, nil):
        ABR.Node.__init__(self, key, nil)
        self.color = "black"

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


class RBTree(ABR.ABR):
    def __init__(self):
        ABR.ABR.__init__(self)
        self.nil = RBNode(None, None)
        self.nil.setColor("black")
        self.root = self.nil

    def setRoot(self, key):
        self.root = RBNode(key, self.nil)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left.key != "nil":
            y.left.setP(x)
        y.setP(x.getP())
        if x.getP().key == "nil":
            self.changeRoot(y)
        elif x == x.getP().left:
            x.getP().left = y
        else:
            x.getP().right = y
        y.left = x
        x.setP(y)

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right.key != "nil":
            y.right.setP(x)
        y.setP(x.getP())
        if x.getP().key == "nil":
            self.changeRoot(y)
        elif x == x.getP().left:
            x.getP().left = y
        else:
            x.getP().right = y
        y.right = x
        x.setP(y)

    def insert(self, key):
        if self.root is self.nil:
            self.setRoot(key)
            self.root.setColor("red")
            self.fixup(self.root)
        else:
            self.insertNode(key, self.root)

    def insertNode(self, key, currentNode):
        if key <= currentNode.key:
            if currentNode.left.key != "nil":
                self.insertNode(key, currentNode.left)
            else:
                currentNode.left = RBNode(key, self.nil)
                currentNode.left.setP(currentNode)
                currentNode.left.setColor("red")
                self.fixup(currentNode.left)
                return currentNode.left
        elif key > currentNode.key:
            if currentNode.right.key != "nil":
                self.insertNode(key, currentNode.right)
            else:
                currentNode.right = RBNode(key, self.nil)
                currentNode.right.setP(currentNode)
                currentNode.right.setColor("red")
                self.fixup(currentNode.right)
                return currentNode.right

    def inorder(self):
        def _inorder(v):
            if v.key == "nil":
                return
            if v.left.key != "nil":
                _inorder(v.left)
            print v.key, " ", v.getColor()
            if v.right.key != "nil":
                _inorder(v.right)

        _inorder(self.root)

    def fixup(self, z):
        while z.getP().getColor() == "red":
            if z.getP() == z.getP().getP().left:
                y = z.getP().getP().right
                if y.getColor() == "red":
                    z.getP().setColor("black")
                    y.setColor("black")
                    z.getP().getP().setColor("red")
                    z = z.getP().getP()
                else:
                    if z == z.getP().right:
                        z = z.getP()
                        self.left_rotate(z)
                    z.getP().setColor("black")
                    z.getP().getP().setColor("red")
                    self.right_rotate(z.getP().getP())
            else:
                y = z.getP().getP().left
                if y.color == "red":
                    z.getP().setColor("black")
                    y.setColor("black")
                    z.getP().getP().setColor("red")
                    z = z.getP().getP()
                else:
                    if z == z.getP().left:
                        z = z.getP()
                        self.right_rotate(z)
                    z.getP().setColor("black")
                    z.getP().getP().setColor("red")
                    self.left_rotate(z.getP().getP())
        self.root.setColor("black")

