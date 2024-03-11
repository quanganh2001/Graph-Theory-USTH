# Creates a TreeNode class to represent each node in the binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Inserts a new node into the tree
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(data, node.right)

    # Traverse the tree in prefix
    def traverse_prefix(self):
        self._traverse_prefix_recursive(self.root)

    def _traverse_prefix_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._traverse_prefix_recursive(node.left)
            self._traverse_prefix_recursive(node.right)

    # Traverse the tree in infix
    def traverse_infix(self):
        self._traverse_infix_recursive(self.root)

    def _traverse_infix_recursive(self, node):
        if node is not None:
            self._traverse_infix_recursive(node.left)
            print(node.data, end=" ")
            self._traverse_infix_recursive(node.right)

    # Traverse the tree in postfix
    def traverse_postfix(self):
        self._traverse_postfix_recursive(self.root)

    def _traverse_postfix_recursive(self, node):
        if node is not None:
            self._traverse_postfix_recursive(node.left)
            self._traverse_postfix_recursive(node.right)
            print(node.data, end=" ")

# Creating a binary tree with characters in my name
name = "phở"
name_without_diacritics = name.replace("ở", "o")  # Removing diacritics
tree = BinaryTree()
for char in name_without_diacritics:
    tree.insert(char)

# Printing the tree in prefix, infix, and postfix order
print("Prefix order:")
tree.traverse_prefix()
print("\n\nInfix order:")
tree.traverse_infix()
print("\n\nPostfix order:")
tree.traverse_postfix()