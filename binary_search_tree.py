class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, newValue):
        # if binary search tree is empty, create a new node and declare it as root
        if self is None:
            self = BinaryTreeNode(newValue)
            return self
        # if newValue is less than value of data in root, add it to the left subtree and proceed recursively
        if newValue < self.data:
            if self.leftChild is None:
                self.leftChild = BinaryTreeNode(newValue)
            else:
                self.leftChild.insert(newValue)
        else:
            # if newValue is greater than value of data in root, add it to the right subtree and proceed recursively
            if self.rightChild is None:
                self.rightChild = BinaryTreeNode(newValue)
            else:
                self.rightChild.insert(newValue)

    def search(self, value):
        # node is empty
        if self is None:
            return False
        # if element is equal to the element to be searched
        elif self.data == value:
            return True
        # element to be searched is less than the current node
        elif self.data > value:
            return self.leftChild.search(value) if self.leftChild else False
        # element to be searched is greater than the current node
        else:
            return self.rightChild.search(value) if self.rightChild else False

    def inorder_traversal(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder_traversal()
            print(self.data, end=" ")
            if self.rightChild:
                self.rightChild.inorder_traversal()

    def preorder_traversal(self):
        if self:
            print(self.data, end=" ")
            if self.leftChild:
                self.leftChild.preorder_traversal()
            if self.rightChild:
                self.rightChild.preorder_traversal()

    def postorder_traversal(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder_traversal()
            if self.rightChild:
                self.rightChild.postorder_traversal()
            print(self.data, end=" ")
# Create a new binary search tree
root = BinaryTreeNode(5)

# Insert values into the tree
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(4)
root.insert(9)

# Perform inorder traversal
print("Inorder traversal:")
root.inorder_traversal()
print()

# Perform preorder traversal
print("Preorder traversal:")
root.preorder_traversal()
print()

# Perform postorder traversal
print("Postorder traversal:")
root.postorder_traversal()
print()
