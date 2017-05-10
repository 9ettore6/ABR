from ABR import ABR


class RB(ABR):
    def __init__(self):
        ABR.__init__(self)
        self.color = "Black"

    def getcolor(self):
        return self.color

    def left_routate(self, tree, x):  # si suppone che x.right != T.nil
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.padre = x
        y.padre = x.padre
        if x.padre == None:
            tree.changeRoot(y)
        elif x == x.padre.left:
            x.padre.left = y
        else:
            x.padre.right = y
        y.left = x
        x.padre = y


MyRBTree = RB()
MyRBTree.insert(3)
MyRBTree.insert(1)
MyRBTree.insert(2)
MyRBTree.insert(7)
MyRBTree.insert(5)
MyRBTree.insert(9)
print MyRBTree.getRoot().key
print ""
test = MyRBTree.treesearch(3, MyRBTree.getRoot())
MyRBTree.left_routate(MyRBTree, test)
print "Radice: ", MyRBTree.getRoot().key
print MyRBTree.getRoot().right.key