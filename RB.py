from ABR import ABR


class RB(ABR):
    def __init__(self):
        ABR.__init__(self)
        self.color = "Black"

    def getcolor(self):
        return self.color

    def left_rotate(self, tree, x):  # si suppone che x.right != T.nil
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.padre = x
        y.padre = x.padre
        if x.padre == None:
            tree.root = y
        elif x == x.padre.left:
            x.padre.left = y
        else:
            x.padre.right = y
        y.left = x
        x.padre = y


d = ABR()
c = RB()
c.insert(6)
c.insert(4)
c.insert(5)
c.insert(7)
c.insert(8)
c.insert(3)
print c.getRoot().key
print ""
c.inorder()
print ""
c.left_rotate(c, c.getRoot().left)
print c.getRoot().key
print ""
c.inorder()
z=0
