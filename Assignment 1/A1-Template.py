import math
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

    def calcHeight(self, num, height, data):
        # We will use the formula 2^i = total nodes, where i = height

        if num == (2 ** (height + 1)) - 1:
            return self.left.insert(data)
        if (num - (2 ** height) + 1) < (2 ** height) / 2:
            return self.left.insert(data)
        else:
            return self.right.insert(data)

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure the tree remains complete - every level is filled save for the last, and each node is as far left as possible
        # Return this node after data has been inserted

        if data == None:
            self.data = MyTree(data)
        else:
            if self.left == None:
                self.left = MyTree(data)
                self.left.descendents = self.descendents
                return self.descendents

            elif self.left and self.right == None:
                self.right = MyTree(data)
                self.right.descendents = self.descendents
                return self.descendents

        height = self.getHeight()
        num = self.getNodes() + 1

        return self.calcHeight(num, height, data)

    def getHeight(self):
        # Return the height of this node
        if self.left and self.right:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        elif self.left:
            return 1 + self.left.getHeight()
        elif self.right:
            return 1 + self.right.getHeight()
        else:
            return 0

    def getNodes(self):
        total = 0

        if self.left:
            total += 1 + self.left.getNodes()
        if self.right:
            total += 1 + self.right.getNodes()

        return total

class MyBST(MyTree):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)
        pass

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted
        pass

    def __contains__(self, data):
        # Returns true if data is in this node or a node descending from it
        pass

class MyAVL(MyBST):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)
        pass

    def getBalanceFactor(self):
        # Return the balance factor of this node
        pass

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid AVL tree
        # Return the node in this node's position after data has been inserted
        pass

    def leftRotate(self):
        # Perform a left rotation on this node and return the new node in its spot
        pass

    def rightRotate(self):
        # Perform a right rotation on this node and return the new node in its spot
        pass

a = MyTree(1)
print(a.getHeight()) #0
a.insert(2)
a.insert(3)
print(a.getLeft().getData()) #2
print(a.getRight().getData()) #3
print(f"The height is {a.getHeight()}")

a.insert(4)
print(f"The height is {a.getHeight()}")
a.insert(5)
a.insert(6)
print(f"The height is {a.getHeight()}")
a.insert(7)
a.insert(8)
print(f"The height is {a.getHeight()}")
