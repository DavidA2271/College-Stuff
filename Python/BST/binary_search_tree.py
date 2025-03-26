from node import Node


class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        ''' Insert element into binary search tree '''
        if self.root is None:
            n = Node()
            n.value = value
            self.root = n
            return n
        return self._insert(self.root, value)
    def _insert(self, curr_node, value):
        if curr_node.value > value:
            if curr_node.left is None:
                n = Node()
                n.value = value
                curr_node.left = n
                n.parent = curr_node
                return n
            else:
                return self._insert(curr_node.left, value)
        else:
            if curr_node.right is None:
                n = Node()
                n.value = value
                curr_node.right = n
                n.parent = curr_node
                return n
            else:
                return self._insert(curr_node.right, value)
        
    def find(self, value, curr_node=None):
        ''' Search for element in binary search tree '''
        if curr_node is None:
            curr_node = self.root
        if curr_node.value == value:
            return curr_node
        elif curr_node.value > value:
            if curr_node.left is None:
                return None
            else:
                # recurses to find value on left branch
                return self.find(value, curr_node.left)
        else:
            if curr_node.right is None:
                return None
            else:
                # recurses to find value on right branch
                return self.find(value, curr_node.right)
    def delete(self, value, curr_node):
        ''' Delete element from binary search tree, while keeping nodes attached '''
        if curr_node is None:
            return None
        if curr_node.value > value:
            # recurses to find value on left branch
            curr_node.left = self.delete(value, curr_node.left)
        elif curr_node.value <= value:
            # recurses to find value on right branch
            curr_node.right = self.delete(value, curr_node.right)
        else:
            # value found
            if curr_node.left is None:
                return curr_node.right
            elif curr_node.right is None:
                return curr_node.left
            else: # node has two children
                # go right one and all the way left to find closest value that is more than the current value
                n = curr_node.right
                while n.left is not None:
                    n = n.left
                # replace current value with above value
                curr_node.value = n.value
                # restructure bst so it doesnt loop on itself
                # this line will clear out the value we replaced the original with
                curr_node.right = self.delete(n.value, curr_node.right)
        return curr_node
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end = " ")
            self.inorder(node.right)
    def preorder(self, node):
        if node is None:
            return
        print(node.value, end = " ")
        self.preorder(node.left)
        self.preorder(node.right)
    def postorder(self, node):
        i = 0
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end = " ")
