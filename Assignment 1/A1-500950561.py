def getName():
    return "Kainth, Mayank"
class MyTree():
    def __init__(self, data):
        # Initialize this node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.descendents = self

    def getLeft(self):
        # Return the left child of this node, or None
        return self.left

    def getRight(self):
        # Return the right child of this node, or None
        return self.right

    def getData(self):
        # Return the data contained in this node
        return self.data

    def cH(self, n, h , d):
        # We will use the formula 2^i = total nodes, where i = height
        if n == (2 ** (h + 1)) - 1:
            return self.left.insert(d)
        if (n - (2 ** h) + 1) < (2 ** h) / 2:
            return self.left.insert(d)
        else:
            return self.right.insert(d)

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure the tree remains complete - every level is filled save for the last, and each node is as far left as possible
        # Return this node after data has been inserted
        if data is None:
            self.data = MyTree(data)
        else:
            if self.left is None:
                self.left = MyTree(data)
                self.left.descendents = self.descendents
                return self.descendents
            elif self.left is not None and self.right is None:
                self.right = MyTree(data)
                self.right.descendents = self.descendents
                return self.descendents

        n= self.gN() + 1
        h = self.getHeight()
        return self.cH(n, h, data)

    def getHeight(self):
        # Return the height of this node
        if self.left is not None and self.right is not None:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        elif self.left is not None:
            return 1 + self.left.getHeight()
        elif self.right is not None:
            return 1 + self.right.getHeight()
        else:
            return 0

    def gN(self):
        total = 0
        if self.left:
            total += 1 + self.left.gN()
        if self.right:
            total += 1 + self.right.gN()
        return total

class MyBST(MyTree):

    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted
        if self.data > data:
            if self.left is None:
                self.left = MyBST(data)
            else:
                self.left.insert(data)

        elif data >= self.data:
            if self.right is None:
                self.right = MyBST(data)
            else:
                self.right.insert(data)

        return self

    def __contains__(self, data):
        # Returns true if data is in this node or a node descending from it

        if self.data is None:
            return False

        elif self.data == data:
            return True
        else:
            if data < self.data:
                if self.left is None:
                    return False
                else:
                    return self.left.__contains__(data)
            if data > self.data:
                if self.right is None:
                    return False
                else:
                    return self.right.__contains__(data)
        return False


class MyAVL(MyBST):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)
        self.parent = None #holds the parent

    def getBalanceFactor(self):
        # Return the balance factor of this node
        """print(f"getting balance factor for node with data {self.data}")
        print(f"left height {self.left.getHeight() + 1}")
        print(f"right height {self.right.getHeight() + 1}")"""

        if self.left is not None and self.right is not None:
            return (self.left.getHeight() + 1) - (self.right.getHeight() + 1)
        elif self.left:
            return (self.left.getHeight() + 1)
        elif self.right:
            return -1 * (self.right.getHeight() + 1)

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid AVL tree
        # Return the node in this node's position after data has been inserted
        if data < self.data:
            if self.left == None:
                self.left = MyBST(data)
            else:
                self.left.insert(data)

        elif data >= self.data:
            if self.right == None:
                self.right = MyBST(data)
            else:
                self.right.insert(data)

        return self

    def inspectTree(self):
        pass

    def leftRotate(self):
        # Perform a left rotation on this node and return the new node in its spot
        pass

    def rightRotate(self):
        # Perform a right rotation on this node and return the new node in its spot
        pass

